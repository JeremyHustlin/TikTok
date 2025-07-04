from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import logging

# === CONFIGURARE LOGGING ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# === SETĂRI DE LA TINE ===
PROXY = None  # Setează proxy-ul aici pentru IP din România: "IP_PROXY:PORT"
VIDEO_URL = "https://www.tiktok.com/@username/video/1234567890123456789"  # Înlocuiește cu URL real
COMMENT_TEXT = "Foarte tare! Super video!"
MIN_DELAY = 2  # delay minim între acțiuni
MAX_DELAY = 5  # delay maxim între acțiuni

# === SETĂRI LOGARE AUTOMATĂ ===
TIKTOK_USERNAME = ""  # Username/email pentru logare
TIKTOK_PASSWORD = ""  # Parola pentru logare
AUTO_LOGIN = True  # True pentru logare automată
LOGIN_METHOD = "email"  # "email" sau "phone"

# === OPȚIUNI AVANSATE ===
HEADLESS_MODE = False  # True pentru a rula fără interfață grafică
ENABLE_LOGGING = True  # True pentru a afișa mesaje detaliate
WAIT_TIMEOUT = 15  # timeout pentru așteptarea elementelor (secunde)
SCROLL_PAUSE_TIME = 2  # timp de pauză pentru scroll
SIMULATE_HUMAN_BEHAVIOR = True  # True pentru comportament mai natural

def random_delay(min_delay=MIN_DELAY, max_delay=MAX_DELAY):
    """Generează un delay aleator pentru a simula comportament uman"""
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    return delay

def setup_driver():
    """Configurează și returnează driver-ul Chrome"""
    chrome_options = webdriver.ChromeOptions()
    
    # Opțiuni pentru a evita detectarea
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # User agents pentru România (localizare)
    romanian_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]
    selected_user_agent = random.choice(romanian_user_agents)
    chrome_options.add_argument(f'--user-agent={selected_user_agent}')
    
    # Setări pentru România
    chrome_options.add_argument('--lang=ro-RO')
    chrome_options.add_argument('--accept-lang=ro-RO,ro;q=0.9,en;q=0.8')
    
    # Proxy dacă este setat (pentru IP din România)
    if PROXY:
        chrome_options.add_argument(f'--proxy-server={PROXY}')
        if ENABLE_LOGGING:
            logger.info(f"Folosesc proxy românesc: {PROXY}")
    
    # Headless mode
    if HEADLESS_MODE:
        chrome_options.add_argument('--headless')
        if ENABLE_LOGGING:
            logger.info("Rulare în modul headless")
    
    # Setări pentru performanță și anonimitate
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--disable-images')  # Încarcă mai rapid
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    
    # Setări timezone pentru România
    chrome_options.add_argument('--timezone=Europe/Bucharest')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        # Ascunde faptul că este automatizat
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # Setează timezone și localizare pentru România
        driver.execute_script("""
            Object.defineProperty(navigator, 'language', {get: () => 'ro-RO'});
            Object.defineProperty(navigator, 'languages', {get: () => ['ro-RO', 'ro', 'en-US', 'en']});
        """)
        
        # Setează dimensiunea ferestrei
        driver.set_window_size(1920, 1080)
        
        if ENABLE_LOGGING:
            logger.info("✅ Driver Chrome configurat cu succes pentru România")
        
        return driver
        
    except Exception as e:
        logger.error(f"⚠️ Eroare la configurarea driver-ului: {str(e)}")
        return None

def scroll_to_view_video(driver):
    """Scrollează pentru a vedea videoul (simulează view)"""
    try:
        if ENABLE_LOGGING:
            logger.info("Scrollez pentru a vedea videoul...")
        
        # Simulează comportament uman de vizualizare
        if SIMULATE_HUMAN_BEHAVIOR:
            # Scroll treptată în jos
            for i in range(3):
                scroll_position = (i + 1) * 200
                driver.execute_script(f"window.scrollTo(0, {scroll_position});")
                random_delay(0.5, 1.5)
            
            # Pauză pentru "vizualizare"
            random_delay(3, 6)
            
            # Scroll înapoi în sus
            driver.execute_script("window.scrollTo(0, 0);")
            random_delay(1, 2)
        else:
            # Scroll simplu
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            random_delay(2, 4)
            driver.execute_script("window.scrollTo(0, 0);")
            random_delay(1, 2)
        
        if ENABLE_LOGGING:
            logger.info("✅ Video vizualizat!")
        return True
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare la scroll: {str(e)}")
        return False

def give_like(driver, wait):
    """Dă like la video"""
    try:
        if ENABLE_LOGGING:
            logger.info("Încerc să dau like...")
        
        # Diferite selectori pentru butonul de like
        like_selectors = [
            '[data-e2e="like-button"]',
            '[data-e2e="browse-like-icon"]',
            'button[data-e2e="like-button"]',
            '.tiktok-1yoqbmj-Button.e1bm6kft0',
            '[data-e2e="video-like-button"]',
            'button[aria-label*="like"]',
            'button[title*="Like"]'
        ]
        
        like_button = None
        for selector in like_selectors:
            try:
                like_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                break
            except:
                continue
        
        if like_button:
            # Verifică dacă butonul a fost deja apăsat
            try:
                button_classes = like_button.get_attribute('class')
                if 'liked' in button_classes.lower() or 'active' in button_classes.lower():
                    if ENABLE_LOGGING:
                        logger.info("ℹ️ Videoul a fost deja apreciat")
                    return True
            except:
                pass
            
            # Scroll la buton dacă nu este vizibil
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", like_button)
            random_delay(1, 2)
            
            # Simulează comportament uman
            if SIMULATE_HUMAN_BEHAVIOR:
                # Mișcă mouse-ul la buton
                ActionChains(driver).move_to_element(like_button).pause(random.uniform(0.5, 1.5)).perform()
                random_delay(0.5, 1)
            
            # Click pe buton
            try:
                like_button.click()
            except:
                # Încearcă cu JavaScript dacă click-ul normal nu funcționează
                driver.execute_script("arguments[0].click();", like_button)
            
            random_delay(2, 3)
            
            if ENABLE_LOGGING:
                logger.info("✅ Like dat cu succes!")
            return True
        else:
            if ENABLE_LOGGING:
                logger.warning("⚠️ Nu am găsit butonul de like")
            return False
            
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare la like: {str(e)}")
        return False

def post_comment(driver, wait):
    """Postează un comentariu"""
    try:
        if ENABLE_LOGGING:
            logger.info("Încerc să postez comentariu...")
        
        # Selectori pentru comment box
        comment_selectors = [
            '[data-e2e="comment-input"]',
            'textarea[placeholder*="comment"]',
            'textarea[placeholder*="Add comment"]',
            '.public-DraftEditor-content',
            'div[contenteditable="true"]',
            'textarea[data-e2e="comment-input"]'
        ]
        
        comment_box = None
        for selector in comment_selectors:
            try:
                comment_box = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                break
            except:
                continue
        
        if comment_box:
            # Scroll la comment box
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", comment_box)
            random_delay(1, 2)
            
            # Simulează comportament uman
            if SIMULATE_HUMAN_BEHAVIOR:
                ActionChains(driver).move_to_element(comment_box).pause(random.uniform(0.5, 1)).perform()
                random_delay(0.5, 1)
            
            # Click și scrie comentariul
            comment_box.click()
            random_delay(1, 2)
            
            # Șterge conținutul existent
            try:
                comment_box.clear()
            except:
                # Pentru contenteditable div
                comment_box.send_keys(Keys.CONTROL + "a")
                comment_box.send_keys(Keys.DELETE)
            
            random_delay(0.5, 1)
            
            # Scrie comentariul caracter cu caracter pentru a simula tastarea umană
            if SIMULATE_HUMAN_BEHAVIOR:
                for char in COMMENT_TEXT:
                    comment_box.send_keys(char)
                    time.sleep(random.uniform(0.05, 0.15))  # Delay între caractere
            else:
                comment_box.send_keys(COMMENT_TEXT)
            
            random_delay(2, 3)
            
            # Caută butonul de post
            post_selectors = [
                '[data-e2e="comment-post"]',
                'button[data-e2e="comment-post"]',
                'div[data-e2e="comment-post"]',
                'button[type="submit"]',
                'button:contains("Post")',
                'div:contains("Post")'
            ]
            
            post_button = None
            for selector in post_selectors:
                try:
                    post_button = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    if post_button.is_enabled():
                        break
                except:
                    continue
            
            if post_button:
                try:
                    post_button.click()
                except:
                    driver.execute_script("arguments[0].click();", post_button)
                
                random_delay(2, 4)
                
                if ENABLE_LOGGING:
                    logger.info("✅ Comentariu postat cu succes!")
                return True
            else:
                # Încearcă cu Enter
                comment_box.send_keys(Keys.RETURN)
                random_delay(2, 3)
                
                if ENABLE_LOGGING:
                    logger.info("✅ Comentariu postat cu Enter!")
                return True
        else:
            if ENABLE_LOGGING:
                logger.warning("⚠️ Nu am găsit comment box-ul")
            return False
            
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare la comentariu: {str(e)}")
        return False

def check_login_status(driver):
    """Verifică dacă utilizatorul este logat"""
    try:
        # Caută indicii că utilizatorul este logat
        login_indicators = [
            '[data-e2e="profile-icon"]',
            '.avatar',
            '[data-e2e="nav-profile"]'
        ]
        
        for indicator in login_indicators:
            try:
                element = driver.find_element(By.CSS_SELECTOR, indicator)
                if element:
                    if ENABLE_LOGGING:
                        logger.info("✅ Utilizator logat detectat")
                    return True
            except:
                continue
        
        if ENABLE_LOGGING:
            logger.warning("⚠️ Nu pare să fii logat în TikTok")
        return False
        
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare la verificarea statusului de login: {str(e)}")
        return False

def wait_for_page_load(driver, timeout=WAIT_TIMEOUT):
    """Așteaptă încărcarea completă a paginii"""
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return True
    except:
        return False

def auto_login(driver, wait):
    """Logare automată în TikTok"""
    try:
        if not AUTO_LOGIN or not TIKTOK_USERNAME or not TIKTOK_PASSWORD:
            if ENABLE_LOGGING:
                logger.info("ℹ️ Logarea automată este dezactivată sau lipsesc credențialele")
            return False
        
        if ENABLE_LOGGING:
            logger.info("🔐 Încep logarea automată în TikTok...")
        
        # Mergi la pagina de login
        driver.get("https://www.tiktok.com/login")
        wait_for_page_load(driver)
        random_delay(3, 5)
        
        # Caută butonul pentru logare cu email/telefon
        login_options = [
            'div[data-e2e="channel-item"]:contains("email")',
            'div[data-e2e="channel-item"]:contains("phone")',
            'a[href*="email"]',
            'a[href*="phone"]',
            '.login-container a',
            '[data-e2e="login-phone-email"]'
        ]
        
        login_button = None
        for selector in login_options:
            try:
                if "email" in selector and LOGIN_METHOD == "email":
                    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                    break
                elif "phone" in selector and LOGIN_METHOD == "phone":
                    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                    break
            except:
                continue
        
        # Dacă nu găsește butonul specific, încearcă să găsească oricare
        if not login_button:
            try:
                login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="login"]')))
            except:
                pass
        
        if login_button:
            login_button.click()
            random_delay(2, 4)
        
        # Caută câmpul pentru username/email
        username_selectors = [
            'input[name="username"]',
            'input[placeholder*="email"]',
            'input[placeholder*="Email"]',
            'input[placeholder*="telefon"]',
            'input[placeholder*="Phone"]',
            'input[type="email"]',
            'input[type="text"]',
            '[data-e2e="email-input"]',
            '[data-e2e="phone-input"]'
        ]
        
        username_field = None
        for selector in username_selectors:
            try:
                username_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                break
            except:
                continue
        
        if username_field:
            username_field.clear()
            random_delay(0.5, 1)
            
            # Tastează username/email caracter cu caracter
            if SIMULATE_HUMAN_BEHAVIOR:
                for char in TIKTOK_USERNAME:
                    username_field.send_keys(char)
                    time.sleep(random.uniform(0.1, 0.3))
            else:
                username_field.send_keys(TIKTOK_USERNAME)
            
            random_delay(1, 2)
            
            if ENABLE_LOGGING:
                logger.info("✅ Username/email introdus")
        else:
            if ENABLE_LOGGING:
                logger.error("⚠️ Nu am găsit câmpul pentru username/email")
            return False
        
        # Caută câmpul pentru parolă
        password_selectors = [
            'input[name="password"]',
            'input[type="password"]',
            'input[placeholder*="password"]',
            'input[placeholder*="Password"]',
            'input[placeholder*="parolă"]',
            '[data-e2e="password-input"]'
        ]
        
        password_field = None
        for selector in password_selectors:
            try:
                password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                break
            except:
                continue
        
        if password_field:
            password_field.clear()
            random_delay(0.5, 1)
            
            # Tastează parola caracter cu caracter
            if SIMULATE_HUMAN_BEHAVIOR:
                for char in TIKTOK_PASSWORD:
                    password_field.send_keys(char)
                    time.sleep(random.uniform(0.1, 0.3))
            else:
                password_field.send_keys(TIKTOK_PASSWORD)
            
            random_delay(1, 2)
            
            if ENABLE_LOGGING:
                logger.info("✅ Parola introdusă")
        else:
            if ENABLE_LOGGING:
                logger.error("⚠️ Nu am găsit câmpul pentru parolă")
            return False
        
        # Caută butonul de login
        submit_selectors = [
            'button[type="submit"]',
            'button[data-e2e="login-button"]',
            'button:contains("Log in")',
            'button:contains("Login")',
            'button:contains("Conectare")',
            'div[data-e2e="login-button"]',
            '.login-button'
        ]
        
        submit_button = None
        for selector in submit_selectors:
            try:
                submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                break
            except:
                continue
        
        if submit_button:
            submit_button.click()
            random_delay(3, 6)
            
            if ENABLE_LOGGING:
                logger.info("✅ Butonul de login apăsat")
        else:
            # Încearcă cu Enter
            password_field.send_keys(Keys.RETURN)
            random_delay(3, 6)
            
            if ENABLE_LOGGING:
                logger.info("✅ Login cu Enter")
        
        # Verifică dacă logarea a avut succes
        wait_for_page_load(driver)
        random_delay(2, 4)
        
        # Verifică dacă suntem pe pagina principală sau dacă avem indicii de login
        if check_login_status(driver):
            if ENABLE_LOGGING:
                logger.info("🎉 Logare automată reușită!")
            return True
        else:
            if ENABLE_LOGGING:
                logger.warning("⚠️ Logarea automată a eșuat sau necesită verificare suplimentară")
            return False
        
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare la logarea automată: {str(e)}")
        return False

def main():
    """Funcția principală"""
    driver = None
    success_count = 0
    total_actions = 3  # view, like, comment
    
    try:
        if ENABLE_LOGGING:
            logger.info("🚀 Pornesc botul TikTok...")
        
        # Configurează driver-ul
        driver = setup_driver()
        if not driver:
            logger.error("⚠️ Nu am putut configura driver-ul Chrome")
            return
        
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        
        # Logare automată dacă este activată
        if AUTO_LOGIN:
            if ENABLE_LOGGING:
                logger.info("🔐 Încep procesul de logare automată...")
            
            login_success = auto_login(driver, wait)
            
            if login_success:
                if ENABLE_LOGGING:
                    logger.info("✅ Logare automată completată cu succes")
                random_delay(2, 4)
            else:
                if ENABLE_LOGGING:
                    logger.warning("⚠️ Logarea automată a eșuat, continui fără login")
                # Continuă oricum, poate utilizatorul este deja logat
        
        # Deschide videoul
        if ENABLE_LOGGING:
            logger.info(f"Deschid video: {VIDEO_URL}")
        
        driver.get(VIDEO_URL)
        
        # Așteaptă încărcarea paginii
        if not wait_for_page_load(driver):
            logger.error("⚠️ Timeout la încărcarea paginii")
            return
        
        random_delay(3, 5)  # Pauză suplimentară
        
        # Verifică dacă pagina s-a încărcat corect
        if "tiktok.com" not in driver.current_url:
            logger.error("⚠️ Nu am putut accesa TikTok")
            return
        
        if ENABLE_LOGGING:
            logger.info("✅ Pagina TikTok s-a încărcat")
        
        # Verifică statusul de login final
        is_logged_in = check_login_status(driver)
        
        if not is_logged_in:
            if ENABLE_LOGGING:
                logger.warning("⚠️ ATENȚIE: Nu ești logat în TikTok. Unele funcționalități pot să nu funcționeze.")
                logger.info("💡 Sugestie: Activează AUTO_LOGIN=True și completează credențialele")
        else:
            if ENABLE_LOGGING:
                logger.info("✅ Utilizator logat confirmat")
        
        # 1. Simulează vizualizarea (view)
        if ENABLE_LOGGING:
            logger.info("📺 Începe vizualizarea...")
        
        if scroll_to_view_video(driver):
            success_count += 1
            if ENABLE_LOGGING:
                logger.info("✅ Vizualizare completată")
        
        random_delay(2, 4)
        
        # 2. Dă like
        if ENABLE_LOGGING:
            logger.info("👍 Încerc să dau like...")
        
        if give_like(driver, wait):
            success_count += 1
            if ENABLE_LOGGING:
                logger.info("✅ Like completat")
        
        random_delay(2, 4)
        
        # 3. Postează comentariu
        if ENABLE_LOGGING:
            logger.info("💬 Încerc să postez comentariu...")
        
        if post_comment(driver, wait):
            success_count += 1
            if ENABLE_LOGGING:
                logger.info("✅ Comentariu completat")
        
        random_delay(2, 3)
        
        # Raport final
        if ENABLE_LOGGING:
            logger.info(f"🎉 Finalizat! {success_count}/{total_actions} acțiuni completate cu succes")
            
            if success_count == total_actions:
                logger.info("🏆 Toate acțiunile au fost completate cu succes!")
            elif success_count > 0:
                logger.info(f"⚠️ {total_actions - success_count} acțiuni au eșuat")
            else:
                logger.error("❌ Toate acțiunile au eșuat")
        
    except KeyboardInterrupt:
        if ENABLE_LOGGING:
            logger.info("⏹️ Scriptul a fost oprit manual")
    except Exception as e:
        if ENABLE_LOGGING:
            logger.error(f"⚠️ Eroare generală: {str(e)}")
    
    finally:
        # Închide browserul
        if driver:
            random_delay(2, 3)
            driver.quit()
            if ENABLE_LOGGING:
                logger.info("🔒 Browser închis. Finalizat.")

if __name__ == "__main__":
    main()