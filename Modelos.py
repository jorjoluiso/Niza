from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class ele_contribuyentes(db.Model):
    documento = db.Column('documento', db.String(20), primary_key=True)
    razon_social = db.Column('razon_social', db.String(500))
    nombre_comercial = db.Column('nombre_comercial', db.String(500))
    direccion = db.Column('direccion', db.String(500))

    def __init__(self, documento, razon_social, nombre_comercial, direccion):
        self.documento = documento
        self.razon_social = razon_social
        self.nombre_comercial = nombre_comercial
        self.direccion = direccion


class ele_documentos(db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    clave_acceso = db.Column('clave_acceso', db.String(100), unique=True)
    establecimiento = db.Column('establecimiento', db.String(10))
    punto_emision = db.Column('punto_emision', db.String(10))
    secuencial = db.Column('secuencial', db.String(20))
    fecha_emision = db.Column('fecha_emision', db.DateTime())
    autorizacion = db.Column('autorizacion', db.String(100))
    identificacionReceptor = db.Column('identificacionReceptor', db.String(20), index=True)
    razonSocialReceptor = db.Column('razonSocialReceptor', db.String(500))
    tipo = db.Column('tipo', db.String(10))
    fecha_creacion = db.Column('fecha_creacion', db.DateTime(), default=datetime.now)

    def __init__(self, clave_acceso, establecimiento, punto_emision, secuencial, fecha_emision,
         autorizacion, identificacionReceptor, razonSocialReceptor, tipo):
        self.clave_acceso = clave_acceso
        self.establecimiento = establecimiento
        self.punto_emision = punto_emision
        self.secuencial = secuencial
        self.fecha_emision = fecha_emision
        self.autorizacion = autorizacion
        self.identificacionReceptor = identificacionReceptor
        self.razonSocialReceptor = razonSocialReceptor
        self.tipo = tipo