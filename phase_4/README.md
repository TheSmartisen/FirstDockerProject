# Phase 4 : Déploiement en Conditions Réelles

Déploiement d'un modèle de prédiction avec Docker, en exposant une API pour effectuer des prédictions. Cette configuration utilise un volume pour sauvegarder les données de requêtes.

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/)

## Installation et Démarrage

1. **Clonez le dépôt** contenant l'application Flask et le `Dockerfile` :
   ```bash
   git clone https://github.com/TheSmartisen/nutriscore-prediction
   cd nutriscore-prediction
   ```

2. **Démarrez l'application** :
   ```bash
   docker-compose up --build
   ```

3. **Accédez à l'API de prédiction** :
   L'API est accessible à `http://localhost:5000/api/v1/predict`.

## Configuration du Dockerfile

Le `Dockerfile` pour construire l'image de l'application se trouve dans le dépôt GitHub :  
[https://github.com/TheSmartisen/nutriscore-prediction](https://github.com/TheSmartisen/nutriscore-prediction).


## Bonus : Connexion avec une Base de Données Dockerisée

Dans cette étape bonus, nous allons connecter le conteneur Flask à une base de données PostgreSQL Dockerisée et tester la communication entre les deux conteneurs.

### Étape supplémentaire

1. **Changer de branche** :
   ```bash
   git checkout bascule-postgre
   ```

Pour plus d'informations, consultez la branche "bascule-postgre" du dépôt GitHub :  
[https://github.com/TheSmartisen/nutriscore-prediction/tree/bascule-postgre](https://github.com/TheSmartisen/nutriscore-prediction/tree/bascule-postgre).