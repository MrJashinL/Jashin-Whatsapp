# Toolkit CTF OffSec per Android

Questo toolkit è stato creato per aiutare nella partecipazione ai CTF (Capture The Flag) con un focus sulla sicurezza (offsec) in ambito Android. Contiene una serie di strumenti e script utili per l'analisi e la vulnerabilità delle applicazioni Android.

## Strumenti Inclusi

1. **WhatsApp OSINT Scraper**: Raccoglie foto profilo, stati, ultimo accesso di un numero di telefono.
2. **Numero Checker**: Verifica se un numero è registrato su WhatsApp, con API e fingerprinting.
3. **Group Info Extractor**: Estrae informazioni da gruppi WhatsApp pubblici tramite web automation.
4. **MetaData Extractor**: Estrae metadati EXIF da immagini e video ricevuti su WhatsApp.
5. **Phone Number Geolocator**: Usa OSINT per trovare la posizione approssimativa di un numero di telefono.
6. **VoIP & Virtual Number Checker**: Identifica se un numero è un VoIP, virtuale o burner.

## Installazione

Ogni strumento deve essere installato e configurato individualmente. Seguire le istruzioni specifiche per ciascun strumento nelle rispettive sezioni.

### Dipendenze Generali

Assicurati di avere Python installato sul tuo sistema. Puoi scaricarlo da [python.org](https://www.python.org/).

### Installazione delle Librerie

Alcuni strumenti richiedono librerie specifiche. Esegui i seguenti comandi per installarle:

```sh
pip install selenium webdriver-manager requests phonenumbers Pillow hachoir
```

## Uso

### WhatsApp OSINT Scraper

1. **Installazione delle dipendenze**:
   ```sh
   pip install selenium webdriver-manager
   ```
2. **Esecuzione**:
   ```sh
   python whatsapp_osint_scraper.py
   ```

### Numero Checker

1. **Installazione delle dipendenze**:
   ```sh
   pip install requests
   ```
2. **Esecuzione**:
   ```sh
   python numero_checker.py
   ```

### Group Info Extractor

1. **Installazione delle dipendenze**:
   ```sh
   pip install selenium webdriver-manager
   ```
2. **Esecuzione**:
   ```sh
   python group_info_extractor.py
   ```

### MetaData Extractor

1. **Installazione delle dipendenze**:
   ```sh
   pip install Pillow hachoir
   ```
2. **Esecuzione**:
   ```sh
   python metadata_extractor.py
   ```

### Phone Number Geolocator

1. **Installazione delle dipendenze**:
   ```sh
   pip install phonenumbers
   ```
2. **Esecuzione**:
   ```sh
   python phone_number_geolocator.py
   ```

### VoIP & Virtual Number Checker

1. **Installazione delle dipendenze**:
   ```sh
   pip install phonenumbers
   ```
2. **Esecuzione**:
   ```sh
   python voip_virtual_number_checker.py
   ```

## Contributi

I contributi sono benvenuti! Sentiti libero di fare fork del progetto e inviare pull request.

## Crediti

Tutti gli strumenti inclusi in questo toolkit sono stati creati da Jashin L.
