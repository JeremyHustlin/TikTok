# === EXEMPLU DE CONFIGURARE PENTRU ROMÂNIA ===
# Copiază acest fișier ca 'config.py' și completează cu datele tale

# === PROXY ROMÂNIA ===
# Proxy-uri recomandate pentru IP din România:
# - Bright Data: rotating residential proxies
# - Smartproxy: residential proxies România
# - Oxylabs: datacenter proxies România
# - ProxyEmpire: residential proxies România

# Exemple de format proxy:
PROXY_EXAMPLES = [
    "185.232.14.52:8080",      # Exemplu IP România
    "31.13.195.146:3128",      # Exemplu IP România  
    "89.47.164.219:8080",      # Exemplu IP România
    "86.105.51.150:3128"       # Exemplu IP România
]

# === SETĂRI PENTRU MAIN.PY ===
# Copiază aceste setări în main.py:

"""
# === SETĂRI DE LA TINE ===
PROXY = "185.232.14.52:8080"  # Înlocuiește cu proxy-ul tău românesc
VIDEO_URL = "https://www.tiktok.com/@username/video/1234567890123456789"
COMMENT_TEXT = "Foarte tare! Super video!"
MIN_DELAY = 2
MAX_DELAY = 5

# === SETĂRI LOGARE AUTOMATĂ ===
TIKTOK_USERNAME = "email@exemplu.ro"  # Email-ul tău TikTok
TIKTOK_PASSWORD = "parola_ta_sigura"  # Parola ta TikTok
AUTO_LOGIN = True  # True pentru logare automată
LOGIN_METHOD = "email"  # "email" sau "phone"

# === OPȚIUNI AVANSATE ===
HEADLESS_MODE = False  # True pentru rulare fără interfață
ENABLE_LOGGING = True  # True pentru mesaje detaliate
WAIT_TIMEOUT = 15  # timeout pentru așteptarea elementelor
SIMULATE_HUMAN_BEHAVIOR = True  # True pentru comportament natural
"""

# === PROXY-URI GRATUITE ROMÂNIA (INSTABILE) ===
# ATENȚIE: Proxy-urile gratuite sunt adesea instabile și lente
FREE_PROXIES_RO = [
    "89.47.164.219:8080",
    "31.13.195.146:3128", 
    "185.232.14.52:8080",
    "86.105.51.150:3128"
]

# === PROXY-URI PREMIUM RECOMANDATE ===
# Pentru rezultate mai bune, folosește servicii premium:
PREMIUM_PROXY_SERVICES = {
    "Bright Data": "https://brightdata.com/",
    "Smartproxy": "https://smartproxy.com/",
    "Oxylabs": "https://oxylabs.io/",
    "ProxyEmpire": "https://proxyempire.io/"
}

# === INSTRUCȚIUNI CONFIGURARE ===
print("""
🇷🇴 CONFIGURARE PENTRU ROMÂNIA:

1. PROXY ROMÂNIA:
   - Caută un proxy cu IP din România
   - Testează proxy-ul în browser înainte
   - Format: "IP:PORT" (ex: "185.232.14.52:8080")

2. CREDENȚIALE TIKTOK:
   - Folosește un cont secundar pentru siguranță
   - Nu folosi contul principal
   - Activează 2FA pe contul principal

3. TESTARE:
   - Rulează cu HEADLESS_MODE = False prima dată
   - Verifică dacă proxy-ul funcționează
   - Testează logarea automată

4. SIGURANȚĂ:
   - Nu împărtăși credențialele cu nimeni
   - Folosește proxy-uri de încredere
   - Monitorizează activitatea contului

📝 Pentru a începe:
1. Copiază setările din acest fișier în main.py
2. Completează PROXY cu IP-ul românesc
3. Completează TIKTOK_USERNAME și TIKTOK_PASSWORD
4. Rulează: python main.py
""")

# === VERIFICARE PROXY ROMÂNIA ===
def check_romanian_ip():
    """Verifică dacă IP-ul este din România"""
    import requests
    
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        
        if data.get('country_code') == 'RO':
            print(f"✅ IP din România detectat: {data.get('ip')}")
            print(f"📍 Locație: {data.get('city')}, {data.get('region')}")
            return True
        else:
            print(f"⚠️ IP nu este din România: {data.get('country_name')}")
            return False
            
    except Exception as e:
        print(f"❌ Eroare la verificarea IP-ului: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Verificare IP curent...")
    check_romanian_ip() 