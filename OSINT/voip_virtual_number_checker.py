# VoIP & Virtual Number Checker
# Identifica se un numero è un VoIP, virtuale o burner.
# Crediti: Jashin L.

import phonenumbers
from phonenumbers import carrier, number_type, PhoneNumberType

def check_number_type(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    num_type = number_type(parsed_number)
    service_provider = carrier.name_for_number(parsed_number, 'en')
    
    if num_type == PhoneNumberType.VOIP:
        return "VoIP"
    elif num_type == PhoneNumberType.MOBILE:
        return "Mobile"
    elif num_type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
        return "Fixed line or Mobile"
    elif num_type == PhoneNumberType.FIXED_LINE:
        return "Fixed line"
    elif num_type == PhoneNumberType.TOLL_FREE:
        return "Toll Free"
    elif num_type == PhoneNumberType.PREMIUM_RATE:
        return "Premium Rate"
    elif num_type == PhoneNumberType.SHARED_COST:
        return "Shared Cost"
    elif num_type == PhoneNumberType.VOICEMAIL:
        return "Voicemail"
    elif num_type == PhoneNumberType.UNKNOWN:
        return "Unknown"
    else:
        return "Other"

def main():
    phone_number = input("Inserisci il numero di telefono (con prefisso internazionale, es. +39 per l'Italia): ")
    try:
        number_type = check_number_type(phone_number)
        print(f"Il numero {phone_number} è di tipo: {number_type}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Numero di telefono non valido. Assicurati di includere il prefisso internazionale.")

if __name__ == '__main__':
    main()