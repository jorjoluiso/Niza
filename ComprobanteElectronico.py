# -*- coding: utf-8 -*-


class ComprobanteElectronico(object):
    claveAcceso = None
    documento = None
    razonSocial = None
    nombreComercial = None
    direccion = None
    establecimiento = None
    puntoEmision = None
    secuencial = None
    fechaEmision = None
    autorizacion = None
    tipo = None

    def __init__(self, tipo=""):
        self.claveAcceso = ""
        self.documento = ""
        self.razonSocial = ""
        self.nombreComercial = ""
        self.direccion = ""
        self.establecimiento = ""
        self.puntoEmision = ""
        self.secuencial = ""
        self.fechaEmision = ""
        self.autorizacion = ""
        self.tipo = tipo
