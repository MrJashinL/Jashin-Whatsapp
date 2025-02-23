# Phone Number Geolocator
# Usa OSINT per trovare la posizione approssimativa di un numero di telefono.
# Crediti: Jashin L.

import phonenumbers
from phonenumbers import geocoder, carrier

def geolocate_phone_number(phone_number):
    parsed_number = phonenumbers.parse(phone_number)

    location = geocoder.description_for_number(parsed_number, 'it')
    service_provider = carrier.name_for_number(parsed_number, 'it')

    return location, service_provider

def main():
    phone_number = input("Inserisci il numero di telefono (con prefisso internazionale, es. +39 per l'Italia): ")
    try:
        location, service_provider = geolocate_phone_number(phone_number)
        print(f"Posizione approssimativa: {location}")
        print(f"Operatore di servizio: {service_provider}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Numero di telefono non valido. Assicurati di includere il prefisso internazionale.")

if __name__ == '__main__':
    main()