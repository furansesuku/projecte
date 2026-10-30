from flask import Flask, render_template

app = Flask(__name__)

# Per afegir un projecte nou, copia un bloc i canvia els camps.
PROJECTES = [
    {
        "nom": "Somriures",
        "descripcio": "Joc per a la campanya solidària #RiuadadeNassos",
        "url": "../somriures/",
    },
    {
        "nom": "Benzineres",
        "descripcio": "Web per veure les benzineres més econòmiques de Catalunya",
        "url": "../benzineres/",
    },
]


@app.route("/")
def inici():
    return render_template("index.html", projectes=PROJECTES)