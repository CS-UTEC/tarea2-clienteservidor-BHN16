from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/esprimo/<numero>')#parametro por defecto es string
def es_primo(numero):
    numero = int(numero)
    if numero > 1:
        for i in range(2,numero):
            if (numero % i) == 0:
                return "No es un numero primo"        
            else:
                return "Si es un numero primo"
    else:
        return "No es un numero primo"


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
