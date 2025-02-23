# Group Info Extractor
# Estrae informazioni da gruppi WhatsApp pubblici tramite web automation.
# Crediti: Jashin L.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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

def search_group(driver, group_name):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(group_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)  # Attendere il caricamento della chat

def get_group_info(driver):
    group_info = {}
    
    driver.find_element(By.XPATH, '//header//span[@title]').click()
    time.sleep(3)  # Attendere il caricamento delle informazioni del gruppo

    group_info['group_name'] = driver.find_element(By.XPATH, '//div[@class="_3XrHh"]/span').text
    group_info['group_description'] = driver.find_element(By.XPATH, '//div[@class="_2iq-U"]').text
    group_info['group_participants'] = [elem.text for elem in driver.find_elements(By.XPATH, '//div[@class="_3XrHh"]/span[@class="_3Whw5"]')]

    driver.find_element(By.XPATH, '//button[@title="Close"]').click()
    return group_info

def main(group_name):
    driver = setup_driver()
    login_whatsapp(driver)
    search_group(driver, group_name)
    group_info = get_group_info(driver)
    driver.quit()

    print(f"Informazioni raccolte per il gruppo {group_name}:")
    print(f"Nome del gruppo: {group_info['group_name']}")
    print(f"Descrizione del gruppo: {group_info['group_description']}")
    print(f"Partecipanti del gruppo: {', '.join(group_info['group_participants'])}")

if __name__ == '__main__':
    group_name = input("Inserisci il nome del gruppo: ")
    main(group_name)