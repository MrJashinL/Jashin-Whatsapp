# WhatsApp OSINT Scraper
# Raccoglie foto profilo, stati, ultimo accesso di un numero di telefono.
# Crediti: Jashin L.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=./User_Data")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_whatsapp(driver):
    driver.get('https://web.whatsapp.com')
    print("Scan the QR code to log in.")
    time.sleep(15)  # Attendere il tempo necessario per la scansione del QR code e il login

def search_contact(driver, phone_number):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)  # Attendere il caricamento della chat

def get_profile_info(driver):
    profile_info = {}
    
    driver.find_element(By.XPATH, '//header//img').click()
    time.sleep(3)  # Attendere il caricamento del profilo

    profile_info['profile_picture'] = driver.find_element(By.XPATH, '//div[@class="_2-3g3 _1lF7t"]/img').get_attribute('src')
    profile_info['status'] = driver.find_element(By.XPATH, '//span[@class="_3-cMa _3Whw5"]').text
    profile_info['last_seen'] = driver.find_element(By.XPATH, '//span[@class="_3-cMa _3Whw5 _1VzZY"]').text

    driver.find_element(By.XPATH, '//button[@title="Close"]').click()
    return profile_info

def main(phone_number):
    driver = setup_driver()
    login_whatsapp(driver)
    search_contact(driver, phone_number)
    profile_info = get_profile_info(driver)
    driver.quit()

    print(f"Informazioni raccolte per il numero {phone_number}:")
    print(f"Foto profilo: {profile_info['profile_picture']}")
    print(f"Stato: {profile_info['status']}")
    print(f"Ultimo accesso: {profile_info['last_seen']}")

if __name__ == '__main__':
    phone_number = input("Inserisci il numero di telefono (con prefisso internazionale, es. +39 per l'Italia): ")
    main(phone_number)