from flask import Flask,render_template, request, session, Response, redirect, jsonify
from database import connector
from model import entities
import json
import time
import os

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/albergue', methods = ['POST'])
def create_albergue():
    create = json.loads(request.data)
    session = db.getSession(engine)
    usuario = entities.Usuario(
        nombre = create["admin"]["nombre"],
        apellidos = create["admin"]["apellidos"],
        representante = create["admin"]["representante"],
        celular = create["admin"]["celular"],
        correo = create["admin"]["correo"]
    )
    session.add(usuario)
    session.flush()
    albergue = entities.Albergue(
        admin_id = usuario.id,
        nombre = create["albergue"]["nombre"],
        anios = create["albergue"]["anios"],
        direccion = create["albergue"]["direccion"],
        urbanizacion = create["albergue"]["urbanizacion"],
        distrito = create["albergue"]["distrito"],
        ciudad = create["albergue"]["ciudad"],
        departamento = create["albergue"]["departamento"],
        tamanio = create["albergue"]["tamanio"],
        material = create["albergue"]["material"],
        gasto = create["albergue"]["gasto"],
        pertenencia = create["albergue"]["pertenencia"],
        voluntarios = create["albergue"]["voluntarios"],
        albergan = create["albergue"]["albergan"],
        num_gatos = create["albergue"]["num_gatos"],
        acep_donaciones = create["albergue"]["acep_donaciones"],
        acep_apoyo = create["albergue"]["acep_apoyo"],
        banco_name = create["albergue"]["banco_name"],
        banco_number = create["albergue"]["banco_number"],
        banco_cci = create["albergue"]["banco_cci"],
        facebook = create["albergue"]["facebook"],
        instagram = create["albergue"]["instagram"],
        correo = create["albergue"]["correo"],
        otro_contacto = create["albergue"]["otro_contacto"]
    )
    session.add(albergue)
    session.flush()
    for i in range(6):
        nombre = "gato" + str(i)
        if(create[nombre]["nombre"] != ""):
            gato = entities.Gato(
                albergue_id = albergue.id,
                nombre = create[nombre]["nombre"],
                img = create[nombre]["img"], #nombre de la imagen 
                edad = create[nombre]["edad"],
                adopcion = create[nombre]["adopcion"]
            )
            session.add(gato)
            session.flush()
            temp = gato.id
            path = os.getcwd()
            os.mkdir(path+"/gatos_imgs/"+str(gato.id))
            #TODO: guardar la imagen en el directorio creado
            session.commit()
            actualizar = session.query(entities.Gato).filter(entities.Gato.id == temp).first()
            setattr(actualizar, 'img', "cambiorealizado")
            session.commit()
    session.close()
    return "finalizado la inserción de datos :)"

@app.route('/get_gatos/<id>', methods = ['GET'])
def search_gatos(id):
    _id = int(id)
    db_session = db.getSession(engine)
    gatos_from_id = db_session.query(entities.Gato).filter(entities.Gato.albergue_id == _id)
    db_session.close()
    gatos = gatos_from_id[:]
    for gato in gatos:
        print(gato.id)
    msg = {'gatos':gatos}
    return Response(json.dumps(msg, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/borrar')
def borrar():
    db.destroyTables(engine)

@app.route('/delete_gato/<id>', methods=['DELETE'])
def delete_gato(id):
    _id = int(id)
    session = db.getSession(engine)
    msg = session.query(entities.Gato).filter(entities.Gato.id == _id).one()
    session.delete(msg)
    session.commit()
    session.close()
    return "Gato borrado"
    #crear gato, creo un file con el nombre de la carpeta 



'''
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
'''

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
