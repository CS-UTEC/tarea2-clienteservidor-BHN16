from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from database import connector
'''
class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    username = Column(String(12))

class Message(connector.Manager.Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)
    content = Column(String(500))
    sent_on = Column(DateTime(timezone=True))
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])
'''
class Usuario(connector.Manager.Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    nombre = Column(String(15))
    apellidos = Column(String(30))
    representante = Column(Boolean)
    celular = Column(String(13))
    correo = Column(String(24))  

class Albergue(connector.Manager.Base):
    __tablename__ = 'albergues'
    id = Column(Integer, Sequence('albergue_id_seq'), primary_key=True)
    admin_id = Column(Integer, ForeignKey('usuarios.id'))
    nombre = Column(String(20))
    anios = Column(Integer)
    direccion = Column(String(100))
    urbanizacion = Column(String(30))
    distrito = Column(String(15))
    ciudad = Column(String(20))
    departamento = Column(String(15))
    tamanio = Column(Float)
    material = Column(String(40))
    gasto = Column(Float)
    pertenencia = Column(Boolean)
    voluntarios = Column(Integer)
    albergan = Column(String(25))
    num_gatos = Column(Integer)
    acep_donaciones = Column(Boolean)
    acep_apoyo = Column(Boolean)
    banco_name = Column(String(15))
    banco_number = Column(String(15))
    banco_cci = Column(String(15))
    facebook = Column(String(20))
    instagram = Column(String(20))
    correo = Column(String(24))
    otro_contacto = Column(String(20))
    admin = relationship(Usuario, foreign_keys=[admin_id])

class Gato(connector.Manager.Base):
    __tablename__ = 'gatos'
    id = Column(Integer, Sequence('gato_id_seq'), primary_key=True)
    albergue_id = Column(Integer, ForeignKey('albergues.id'))
    nombre = Column(String(15))
    img = Column(String(30))
    edad = Column(Integer)
    adopcion = Column(Boolean)
    albergues_from = relationship(Albergue, foreign_keys=[albergue_id])

class Recomendacion(connector.Manager.Base):
    __tablename__ = 'recomendaciones'
    id = Column(Integer, Sequence('recomendacion_id_seq'), primary_key=True)
    albergue_id = Column(Integer, ForeignKey('albergues.id'))    
    reco = Column(String(420))
    comentarios = Column(String(420))
    albergues_from = relationship(Albergue, foreign_keys=[albergue_id])

class Contacto(connector.Manager.Base):
    __tablename__ = 'contactos'
    id = Column(Integer, Sequence('contacto_id_seq'), primary_key=True)
    nombre = Column(String(15))
    apellidos = Column(String(30))
    celular = Column(String(13))
    correo = Column(String(24))
    mensaje = Column(String(420))

