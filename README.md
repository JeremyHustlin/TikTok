# 🤖 TikTok Bot - Automatizare Like, Comment & View

Un bot Python pentru automatizarea interacțiunilor pe TikTok (like, comment, view) folosind Selenium WebDriver.

## ✨ Funcționalități

- 📺 **Simulare View** - Scrollează și vizualizează videoul natural
- 👍 **Like Automat** - Dă like la videouri
- 💬 **Comment Automat** - Postează comentarii personalizate
- 🔄 **Comportament Uman** - Delays aleatorii și mișcări naturale
- 🛡️ **Anti-Detectare** - Configurări pentru a evita detectarea ca bot
- 📊 **Logging Detaliat** - Urmărește progresul și erorile
- 🌐 **Suport Proxy** - Opțional pentru anonimitate

## 🚀 Instalare

### 1. Instalează Python 3.7+
Descarcă de pe [python.org](https://www.python.org/downloads/)

### 2. Instalează dependențele
```bash
pip install -r requirements.txt
```

### 3. Instalează Chrome Driver
Descarcă ChromeDriver de pe [chromedriver.chromium.org](https://chromedriver.chromium.org/) și adaugă-l în PATH.

Sau folosește webdriver-manager (recomandat):
```bash
pip install webdriver-manager
```

## ⚙️ Configurare

### Setări Principale (în `main.py`)

```python
# === SETĂRI DE LA TINE ===
PROXY = None  # Setează proxy-ul aici: "IP:PORT"
VIDEO_URL = "https://www.tiktok.com/@username/video/1234567890123456789"
COMMENT_TEXT = "Foarte tare! Super video!"
MIN_DELAY = 2  # delay minim între acțiuni
MAX_DELAY = 5  # delay maxim între acțiuni

# === OPȚIUNI AVANSATE ===
HEADLESS_MODE = False  # True pentru rulare fără interfață
ENABLE_LOGGING = True  # True pentru mesaje detaliate
WAIT_TIMEOUT = 15  # timeout pentru așteptarea elementelor
SIMULATE_HUMAN_BEHAVIOR = True  # True pentru comportament natural
```

### Configurare Proxy (Opțional)
```python
PROXY = "123.456.789.10:8080"  # Înlocuiește cu proxy-ul tău
```

## 🎯 Utilizare

### 1. Setează URL-ul videului
```python
VIDEO_URL = "https://www.tiktok.com/@username/video/1234567890123456789"
```

### 2. Personalizează comentariul
```python
COMMENT_TEXT = "Mesajul tău aici!"
```

### 3. Rulează scriptul
```bash
python main.py
```

## 📋 Exemple de Utilizare

### Exemplu Simplu
```python
# Setări minime
VIDEO_URL = "https://www.tiktok.com/@example/video/123456789"
COMMENT_TEXT = "Foarte tare!"

# Rulează scriptul
python main.py
```

### Exemplu cu Proxy
```python
PROXY = "192.168.1.100:8080"
VIDEO_URL = "https://www.tiktok.com/@example/video/123456789"
COMMENT_TEXT = "Super video!"
```

### Exemplu Headless (fără interfață)
```python
HEADLESS_MODE = True
ENABLE_LOGGING = False
VIDEO_URL = "https://www.tiktok.com/@example/video/123456789"
```

## 🔧 Opțiuni Avansate

### Comportament Uman
```python
SIMULATE_HUMAN_BEHAVIOR = True  # Activează simularea comportamentului uman
MIN_DELAY = 2  # Delay minim între acțiuni
MAX_DELAY = 5  # Delay maxim între acțiuni
```

### Logging
```python
ENABLE_LOGGING = True   # Afișează mesaje detaliate
ENABLE_LOGGING = False  # Rulare silențioasă
```

### Timeout-uri
```python
WAIT_TIMEOUT = 15  # Timp de așteptare pentru elemente (secunde)
```

## 📊 Output-ul Scriptului

```
2024-01-01 12:00:00 - INFO - 🚀 Pornesc botul TikTok...
2024-01-01 12:00:01 - INFO - ✅ Driver Chrome configurat cu succes
2024-01-01 12:00:02 - INFO - Deschid video: https://www.tiktok.com/@example/video/123
2024-01-01 12:00:05 - INFO - ✅ Pagina TikTok s-a încărcat
2024-01-01 12:00:06 - INFO - 📺 Începe vizualizarea...
2024-01-01 12:00:10 - INFO - ✅ Vizualizare completată
2024-01-01 12:00:12 - INFO - 👍 Încerc să dau like...
2024-01-01 12:00:15 - INFO - ✅ Like completat
2024-01-01 12:00:17 - INFO - 💬 Încerc să postez comentariu...
2024-01-01 12:00:22 - INFO - ✅ Comentariu completat
2024-01-01 12:00:24 - INFO - 🎉 Finalizat! 3/3 acțiuni completate cu succes
2024-01-01 12:00:25 - INFO - 🏆 Toate acțiunile au fost completate cu succes!
2024-01-01 12:00:27 - INFO - 🔒 Browser închis. Finalizat.
```

## ⚠️ Considerații Importante

### Termeni de Utilizare
- **Respectă regulile TikTok** - Nu abuza de bot
- **Folosește cu moderație** - Evită spam-ul
- **Cont personal** - Folosește doar pe contul tău

### Securitate
- **Proxy recomandat** - Pentru anonimitate
- **VPN opțional** - Pentru protecție suplimentară
- **Rate limiting** - Nu rula prea des

### Limitări
- **Necesită login** - Trebuie să fii logat în TikTok
- **Schimbări UI** - TikTok poate schimba interfața
- **Detectare** - Riscul de detectare ca bot există

## 🛠️ Troubleshooting

### Probleme Comune

#### 1. ChromeDriver nu este găsit
```bash
# Soluție: Instalează webdriver-manager
pip install webdriver-manager
```

#### 2. Elementele nu sunt găsite
- Verifică dacă ești logat în TikTok
- Actualizează selectorii CSS
- Mărește `WAIT_TIMEOUT`

#### 3. Proxy nu funcționează
- Verifică formatul: `IP:PORT`
- Testează proxy-ul în browser
- Folosește proxy-uri HTTP/HTTPS

#### 4. Bot detectat
- Activează `SIMULATE_HUMAN_BEHAVIOR`
- Mărește delay-urile
- Folosește proxy diferit
- Schimbă user-agent-ul

### Debugging
```python
# Activează logging detaliat
ENABLE_LOGGING = True

# Dezactivează headless pentru a vedea ce se întâmplă
HEADLESS_MODE = False

# Mărește timeout-ul
WAIT_TIMEOUT = 30
```

## 📝 Changelog

### v2.0 (Actualizat)
- ✅ Comportament uman simulat
- ✅ Selectori CSS îmbunătățiți
- ✅ Logging detaliat
- ✅ Verificare status login
- ✅ Gestionare erori îmbunătățită
- ✅ Suport pentru multiple user-agents
- ✅ Opțiuni avansate configurabile

### v1.0 (Original)
- ✅ Funcționalitate de bază
- ✅ Like, comment, view
- ✅ Suport proxy

## 📞 Support

Pentru probleme sau întrebări:
1. Verifică secțiunea **Troubleshooting**
2. Activează logging-ul pentru debugging
3. Verifică dacă toate dependențele sunt instalate

## ⚖️ Disclaimer

Acest bot este pentru scopuri educaționale. Utilizatorul este responsabil pentru respectarea termenilor de utilizare TikTok și a legilor locale. Folosirea abuzivă poate duce la suspendarea contului.

---

**🚀 Succes cu automatizarea TikTok!** 