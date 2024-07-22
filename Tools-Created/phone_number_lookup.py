import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_phone_number(phone_number):
    try:
        # Parsing du numéro de téléphone
        parsed_number = phonenumbers.parse(phone_number, None)

        # Vérification si le numéro est valide
        if not phonenumbers.is_valid_number(parsed_number):
            return "Numéro de téléphone invalide."

        # Récupération du pays et de la région géographique
        country = geocoder.description_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "fr")

        # Récupération de l'opérateur du numéro de téléphone
        carrier_name = carrier.name_for_number(parsed_number, "en")

        return f"Pays: {country}\nRégion: {region}\nOpérateur: {carrier_name}"
    
    except Exception as e:
        return f"Erreur lors de la recherche du numéro: {str(e)}"

# Demander à l'utilisateur de saisir un numéro de téléphone
phone_number = input("Entrez un numéro de téléphone (format international, par ex. +14158586273): ")

# Appeler la fonction de recherche et afficher les résultats
result = lookup_phone_number(phone_number)
print(result)
