# -*- coding: utf-8 -*-
from ComprobanteElectronico import *
from FacturaDetalle import *


class Comprobante(ComprobanteElectronico):
    identificacionReceptor = None
    razonSocialReceptor = None
    detalle = None
    tipo = None

    def __init__(self):
        self.detalle = []
        self.tipo = "FACTURA"


if __name__ == "__main__":
    f = Comprobante()
    f.claveAcceso = "123"
    f.detalle.append(FacturaDetalle("1", "Test -1"))
    f.detalle.append(FacturaDetalle("2", "Test -2"))

    print("Clave", (f.claveAcceso))
    for d in f.detalle:
        print("\n")
        print("Código", (d.codigoPrincipal))
        print("Descripción", (d.descripcion))
        print("Cantidad", (d.cantidad))
