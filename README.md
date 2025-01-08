# Exemple d'authentification avec code d'appareil

Ce script illustre comment implémenter l'authentification avec code d'appareil en utilisant le point de terminaison OAuth2 de Microsoft. Il permet aux utilisateurs de s'authentifier auprès d'Azure Active Directory (AAD) pour obtenir des jetons d'accès et de rafraîchissement afin d'accéder à des ressources comme Microsoft Graph.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants :

1. **Client ID :** Un identifiant client valide pour votre application Azure AD.
2. **Ressource cible :** La ressource à laquelle vous souhaitez accéder (par exemple, Microsoft Graph).
3. **Environnement Python :** Assurez-vous d'avoir Python 3.x installé.
4. **Dépendances :** Installez la bibliothèque `requests` en exécutant :

   ```bash
   pip install requests
   ```

## Comment ça fonctionne

### Étape 1 : Obtenir le code de l'appareil
Le script envoie une requête au point de terminaison Azure Device Code pour obtenir un code d'appareil et des instructions pour l'utilisateur. L'utilisateur doit visiter l'URL de vérification fournie et entrer le code utilisateur.

### Étape 2 : Vérification de l'authentification utilisateur
Le script interroge à plusieurs reprises le point de terminaison des jetons pour vérifier si l'utilisateur a terminé l'authentification. Il utilise l'intervalle fourni dans la réponse pour éviter de surcharger le serveur.

### Étape 3 : Récupérer les jetons
Une fois l'authentification réussie, le script récupère un jeton d'accès et un jeton de rafraîchissement, qui peuvent être utilisés pour accéder à la ressource spécifiée.

## Utilisation

1. Clonez le dépôt ou copiez le script sur votre machine locale.
2. Mettez à jour les champs `client_id` et `resource` dans les dictionnaires `payload_device_code` et `payload_token` avec les informations de votre application.
3. Exécutez le script en utilisant :

   ```bash
   python script_name.py
   ```
4. Suivez les instructions à l'écran pour terminer l'authentification.

## Exemple de sortie

```plaintext
=== Étape 1 : Informations pour l'utilisateur ===
User Code: ABCD-EFGH
Verification URL: https://microsoft.com/devicelogin
Message: Pour vous connecter, utilisez un navigateur web pour ouvrir la page et entrez le code ABCD-EFGH.

=== Étape 2 : Attente de l'authentification ===
En attente que l'utilisateur termine l'authentification...
En attente que l'utilisateur termine l'authentification...

=== Étape 3 : Authentification réussie ===
Access Token: eyJ0eXAiOiJKV...
Refresh Token: MIIEvAIBADANBg...
```

## Notes

- Assurez-vous de gérer les informations sensibles comme les jetons d'accès de manière sécurisée. Ne les consignez pas dans des environnements de production.
- Ce script est conçu pour des fins éducatives. Pour une utilisation en production, envisagez d'ajouter une gestion des erreurs appropriée et des mesures de sécurité.
- Consultez la [documentation Microsoft Authentication](https://learn.microsoft.com/fr-fr/azure/active-directory/develop/) pour plus de détails sur l'authentification avec code d'appareil.

## Défi Pwned Labs

Ce script a été développé dans le cadre d'un challenge Pwned Labs, pour illustrer une méthode d'authentification et interagir avec des services protégés par OAuth2.
