import requests
import time

# Paramètres pour la requête initiale
url_device_code = "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0"
url_token = "https://login.microsoftonline.com/common/oauth2/token"
payload_device_code = {
    "client_id": "d3590ed6-52b3-4102-aeff-aad2292ab01c",  # Votre client_id
    "resource": "https://graph.microsoft.com"  # La ressource cible
}

# Étape 1 : Obtenir le code de l'appareil et les informations d'authentification
response = requests.post(url_device_code, data=payload_device_code)

if response.status_code == 200:
    data = response.json()
    device_code = data["device_code"]
    interval = int(data["interval"])  # Convertir en entier ici
    print("=== Étape 1 : Informations pour l'utilisateur ===")
    print(f"User Code: {data['user_code']}")
    print(f"Verification URL: {data['verification_url']}")
    print(f"Message: {data['message']}")
else:
    print(f"Erreur lors de la requête Device Code: {response.status_code}, {response.text}")
    exit()

# Étape 2 : Attendre que l'utilisateur termine l'authentification
print("\n=== Étape 2 : Attente de l'authentification ===")
while True:
    # Préparer la requête pour interroger l'endpoint de token
    payload_token = {
        "client_id": "d3590ed6-52b3-4102-aeff-aad2292ab01c",
        "resource": "https://graph.microsoft.com",
        "grant_type": "device_code",
        "code": device_code
    }

    token_response = requests.post(url_token, data=payload_token)

    if token_response.status_code == 200:
        token_data = token_response.json()
        print("\n=== Étape 3 : Authentification réussie ===")
        print(f"Access Token: {token_data['access_token']}")
        print(f"Refresh Token: {token_data['refresh_token']}")
        break
    elif token_response.status_code == 400:
        # Code 400 : L'utilisateur n'a pas encore terminé
        error = token_response.json().get("error", "")
        if error == "authorization_pending":
            print("En attente que l'utilisateur termine l'authentification...")
            time.sleep(interval)  # Attendre avant de réessayer
        else:
            print(f"Erreur: {token_response.json()}")
            break
    else:
        print(f"Erreur lors de la requête Token: {token_response.status_code}, {token_response.text}")
        break
