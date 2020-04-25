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

@app.route('/esprimo/<numero>')
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

@app.route('/multiplo/<numero1>/<numero2>')
def multiplo(numero1, numero2):
    num1 = int(numero1)
    num2 = int(numero2)
    if(num1%num2 == 0):
        return "Si es múltiplo"
    else:
        return "No es múltiplo"

@app.route('/palindrome/<palabra>')
def es_palidromo(palabra):
    for i in range(0,int(len(palabra)/2)):
        if palabra[i] != palabra[len(palabra)-1-i]:
            return "No es palindrome"
    return "Es palindrome"

@app.route('/create_user/<nombre>/<apellido>/<passwords>/<usernames>')
def create_user(nombre, apellido, passwords, usernames):
    user = entities.User(
        name = nombre,
        fullname = apellido,
        password = passwords,
        username = usernames
    )

    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()

    return "User created!"

@app.route('/read_users')
def read_users():
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User)
    users = respuesta[:]
    retornar = ""
    cont = 0
    for user in users:
        retornar += "<b>Usuario</b>: " + str(cont+1) + "<br>Nombre: " + str(user.name) + "<br>Apellido: " + str(user.fullname) + "<br>Contraseña: " + str(user.password) + "<br>Usuario: " + str(user.username) + "<br>********************************************************************************************************************<br>"
        cont += 1
    return retornar

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
