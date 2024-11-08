### PHASE 3
Pour réaliser cette phase de création d'image et de déploiement d'application, voici un guide étape par étape pour mettre en place une application Flask simple dans un conteneur Docker avec des bibliothèques spécifiques, comme `pandas`.

### Étape 1 : Écrire le code de l'application Flask (`app.py`)

Créez un fichier `app.py` qui contient une application Flask simple avec une route de base.

```python
# app.py
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is a basic API!"

@app.route("/data")
def data():
    # Exemple d'utilisation de pandas pour créer un DataFrame simple
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Étape 2 : Créer un fichier `requirements.txt`

Le fichier `requirements.txt` va contenir les bibliothèques Python nécessaires pour cette application.

```cmd
pip freeze > requirements.txt
```

### Étape 3 : Rédiger le Dockerfile

Voici un Dockerfile qui configure une image Python avec Flask et pandas installés.

```dockerfile
# Utiliser une image Python de base
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python", "app.py"]
```

Pour ne pas s'embêter sur la rédaction du dockerfile. J'utiliser `docker init`
```cmd
docker init
```

Il y aura un ensemble de questions : 
- Choix : `y`
- type de projet : `python`
- port : `5000`
- commande pour lancer l'application : `python.app.py`

### Étape 4 : Construire l’image Docker

À partir du répertoire où se trouve votre `Dockerfile`, exécutez la commande suivante pour construire l'image Docker. Remplacez `my-flask-app` par le nom que vous souhaitez donner à votre image.

```bash
docker build -t my-flask-app .
```

### Étape 5 : Lancer le conteneur et tester l'application

Lancez un conteneur à partir de l'image Docker que vous avez construite.

```bash
docker run -p 5000:5000 my-flask-app
```

L'application Flask sera maintenant accessible via `http://localhost:5000` dans votre navigateur.

### Étape 6 : Tester l’API

Ouvrez un navigateur et accédez aux URL suivantes pour tester l'application :
- **Pour la route de base** : `http://localhost:5000/`
- **Pour la route avec pandas** : `http://localhost:5000/data`

