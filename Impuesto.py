# -*- coding: utf-8 -*-


class Impuesto(object):
    codigo = None
    codigoPorcentaje = None
    tarifa = None
    baseImponible = None
    valor = None

    def __init__(self, codigo="", codigoPorcentaje="", tarifa=0, baseImponible=0, valor=0):
        self.codigo = codigo
        self.codigoPorcentaje = codigoPorcentaje
        self.tarifa = tarifa
        self.baseImponible = baseImponible
        self.valor = valor