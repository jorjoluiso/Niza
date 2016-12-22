# -*- coding: utf-8 -*-
from Comprobante import *
from Utilidades import *
import xml.etree.ElementTree as parsexml
import tempfile
import os


class ParseXMLFactura(object):
    factura = None

    def __init__(self):
        self.factura = Comprobante()

    def getFactura(self, archivo):
        Utilidades.borrarBlancosArchivo(archivo)

        tree = parsexml.parse(archivo)
        root = tree.getroot()

        for i in root.iter("numeroAutorizacion"):
            self.factura.autorizacion = i.text
            #print((self.factura.autorizacion))

        self.getFacturaFirmada(archivo)

        self.getFacturaCabeza(tempfile.gettempdir() + os.sep + Utilidades.extraerNombre(archivo))
        self.getFacturaDetalle(tempfile.gettempdir() + os.sep + Utilidades.extraerNombre(archivo))

        return self.factura

    def getFacturaFirmada(self, archivo):
        #Recupero el comprobante electrónico firmado
        tree = parsexml.parse(archivo)
        root = tree.getroot()

        for i in root.iter("comprobante"):
            #print((i.text))
            with open(tempfile.gettempdir() + os.sep + Utilidades.extraerNombre(archivo), "w",
            encoding='utf8') as f:
                f.writelines(i.text)
            f.close

    #Recupera el encabezado de la factura
    def getFacturaCabeza(self, archivo):
        tree = parsexml.parse(archivo)
        root = tree.getroot()

        for datosFactura in root.iter("ruc"):
            self.factura.documento = datosFactura.text

        for datosFactura in root.iter("razonSocial"):
            self.factura.razonSocial = datosFactura.text

        for datosFactura in root.iter("nombreComercial"):
            self.factura.nombreComercial = datosFactura.text

        for datosFactura in root.iter("dirMatriz"):
            self.factura.direccion = datosFactura.text

        for datosFactura in root.iter("estab"):
            self.factura.establecimiento = datosFactura.text

        for datosFactura in root.iter("ptoEmi"):
            self.factura.puntoEmision = datosFactura.text

        for datosFactura in root.iter("secuencial"):
            self.factura.secuencial = datosFactura.text

        for datosFactura in root.iter("fechaEmision"):
            self.factura.fechaEmision = datosFactura.text

        for datosFactura in root.iter("claveAcceso"):
            self.factura.claveAcceso = datosFactura.text

        for datosFactura in root.iter("identificacionComprador"):
            self.factura.identificacionReceptor = datosFactura.text

        for datosFactura in root.iter("razonSocialComprador"):
            self.factura.razonSocialReceptor = datosFactura.text

    #Recupera de detalle de la factura
    def getFacturaDetalle(self, archivo):
        tree = parsexml.parse(archivo)
        root = tree.getroot()

        detalleFactura = []

        detalles = root.iter("detalle")

        for detalle in detalles:
            detalle_children = detalle.getchildren()
            d = FacturaDetalle()

            for elementos in detalle_children:

                #print(elementos.tag, elementos.text)
                if (elementos.tag == "codigoPrincipal"):
                    d.codigoPrincipal = elementos.text
                elif (elementos.tag == "descripcion"):
                    d.descripcion = elementos.text
                elif (elementos.tag == "cantidad"):
                    d.cantidad = elementos.text
                elif (elementos.tag == "precioUnitario"):
                    d.precioUnitario = elementos.text
                elif (elementos.tag == "descuento"):
                    d.descuento = elementos.text
                elif (elementos.tag == "precioTotalSinImpuesto"):
                    d.total = elementos.text
                elif (elementos.tag == "impuestos"):
                    detalleImpuesto = []
                    for impuestos in elementos:
                        impuesto_children = impuestos.getchildren()
                        i = Impuesto()
                        for impuesto in impuesto_children:
                            #print(" ", impuesto.tag, impuesto.text)
                            if (impuesto.tag == "codigo"):
                                i.codigo = impuesto.text
                            elif (impuesto.tag == "codigoPorcentaje"):
                                i.codigoPorcentaje = impuesto.text
                            elif (impuesto.tag == "tarifa"):
                                i.tarifa = impuesto.text
                            elif (impuesto.tag == "baseImponible"):
                                i.baseImponible = impuesto.text
                            elif (impuesto.tag == "valor"):
                                i.valor = impuesto.text
                        detalleImpuesto.append(i)
                    d.impuesto = detalleImpuesto
            detalleFactura.append(d)
        self.factura.detalle = detalleFactura

    def imprimir(self):
        print("\n")
        print("Datos Factura")
        print(("Clave de Acceso:", self.factura.claveAcceso))
        print(("Docuemto:", self.factura.documento))
        print(("Nombre Comercial:", self.factura.nombreComercial))
        print(("Dirección:", self.factura.direccion))
        print(("Establecimiento:", self.factura.establecimiento))
        print(("Punto Emisión:", self.factura.puntoEmision))
        print(("Secuencial:", self.factura.secuencial))
        print(("Fecha Emisión:", self.factura.fechaEmision))
        print(("Autorización:", self.factura.autorizacion))
        print(("Identificación Cliente:", self.factura.identificacionReceptor))
        print(("Razón Social Cliente:", self.factura.razonSocialReceptor))
        print(("Tipo:", self.factura.tipo))

        print("\n")
        print("Detalle Factura")
        for df in self.factura.detalle:
            print("Código " + df.codigoPrincipal)
            print("Descripción " + df.descripcion)
            print("Cantidad " + str(df.cantidad))
            print("Precio Unitario " + str(df.precioUnitario))
            print("Descuento " + str(df.descuento))
            print("Total " + str(df.total))
            print(" Impuestos")
            for i in df.impuesto:
                print(" Código", i.codigo)
                print(" Código porcentaje", i.codigoPorcentaje)
                print(" Tarifa", i.tarifa)
                print(" Valor base", i.baseImponible)
                print(" Valor", i.valor)
                print("\n")