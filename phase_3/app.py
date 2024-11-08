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
    df = pd.DataFrame({"Name": ["Patoche", "Khadija", "Yoyo", "Niels"], "Age": [33, 33, 32, 30]})
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)