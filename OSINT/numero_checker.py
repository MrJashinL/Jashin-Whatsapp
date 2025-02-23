# Numero Checker
# Verifica se un numero è registrato su WhatsApp, con API e fingerprinting.
# Crediti: Jashin L.

import requests

def check_number(phone_number):
    url = "https://api.whatsapp.com/send"
    params = {
        'phone': phone_number,
        'text': 'Ciao'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print(f"Il numero {phone_number} è registrato su WhatsApp.")
    else:
        print(f"Il numero {phone_number} non è registrato su WhatsApp.")

def main():
    phone_number = input("Inserisci il numero di telefono (con prefisso internazionale, es. +39 per l'Italia): ")
    check_number(phone_number)

if __name__ == '__main__':
    main()