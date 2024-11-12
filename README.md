# Projet Docker : Déploiement et Gestion de Conteneurs

Ce projet est structuré en quatre phases pour apprendre et appliquer les concepts de Docker, de la veille technique à la mise en conteneur d'une application en conditions réelles.

## Phase 1 : Veille et Installation

Effectuez une veille technique sur Docker en répondant aux questions suivantes :

1. **Qu'est-ce qu'une machine virtuelle ?**
2. **Quelle est la différence entre une machine virtuelle et un conteneur ?**
3. **Qu'est-ce que Docker et la conteneurisation ?**
4. **Quels sont les avantages de la conteneurisation ?**
5. **Qu'est-ce qu'une image Docker ? Quelles différences avec un conteneur ?**
6. **Qu'est-ce qu'un Dockerfile ?**

Consultez le fichier **"Veille technique.pdf"** dans `phase_1` pour les réponses.

Installez Docker Desktop (ou WSL2 avec Docker Engine) et familiarisez-vous avec les commandes Docker de base pour lancer et gérer des conteneurs.

## Phase 2 : Création et Gestion de Conteneurs

1. **Lancez un conteneur Ubuntu en mode interactif** et explorez les commandes Linux de base.
2. **Exécutez des commandes dans un conteneur en cours d’exécution** avec `docker exec`.
3. **Récupérez les logs d’un conteneur** avec `docker logs` et supprimez-le avec `docker rm`.
4. **Montez un volume dans un conteneur** et observez la persistance des données après l'arrêt du conteneur.
5. **Créez un réseau Docker** et connectez deux conteneurs pour tester la communication entre eux.

## Phase 3 : Création d’Images et Déploiement d’une Application

1. **Écrivez un Dockerfile** pour créer une image Python de base avec des bibliothèques spécifiques, comme `pandas`.
2. **Construisez l’image Docker** avec la commande `docker build`.
3. **Intégrez une application Flask simple** dans un conteneur, qui expose une API de base retournant un message.
4. **Testez l’application localement** en accédant à l’API via un navigateur.
5. Ajoutez un fichier **requirements.txt** pour gérer les dépendances Python et modifiez le Dockerfile pour installer ces dépendances automatiquement.

Vous trouverez le code Flask, le Dockerfile, et le fichier requirements.txt dans le dossier `phase_3`.

## Phase 4 : Déploiement en Conditions Réelles

1. **Mettez en conteneur un modèle de prédiction** et exposez une API pour effectuer des prédictions.
2. **Configurez un volume pour stocker les données de requêtes** (par exemple, sauvegarder les prédictions et les résultats).

Bonus : Connectez le conteneur Flask avec une base de données Dockerisée (comme PostgreSQL) et testez la communication entre les deux conteneurs.

### Fichiers Docker

Pour le déploiement du modèle de prédiction en conditions réelles, vous pouvez vous référer au dépôt GitHub suivant pour obtenir un exemple de `Dockerfile` : [https://github.com/TheSmartisen/nutriscore-prediction](https://github.com/TheSmartisen/nutriscore-prediction).
