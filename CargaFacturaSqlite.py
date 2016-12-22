# -*- coding: utf-8 -*-

from Comprobante import *
from Config import *
from BaseSqlite import *
import datetime


class CargaFacturaSqlite(object):

    def __init__(self):
        pass

    def carga(self, factura):
        cfg = Config()
        cfg.getConfig()
        sqlite = BaseSqlite(cfg.rutaDB)

        sqlite.ejecutar("delete from ele_documentos where clave_acceso = '" +
        factura.claveAcceso + "'")

        fecha = datetime.datetime.strptime(factura.fechaEmision, '%d/%m/%Y').date()

        sqlite.ejecutar("INSERT INTO ELE_DOCUMENTOS VALUES ('"
        + factura.claveAcceso + "','" + factura.documento + "','" + factura.razonSocial + "','"
        + factura.nombreComercial + "','" + factura.direccion + "','" + factura.establecimiento
        + "','"
        + factura.puntoEmision + "','" + factura.secuencial + "','"
        + str(fecha)
        + "','" + factura.autorizacion + "','" + factura.identificacionReceptor + "','"
        + factura.razonSocialReceptor + "','" + factura.tipo + "')")

        i = 1

        for det in factura.detalle:
            sqlite.ejecutar("INSERT INTO ELE_FACTURA_DETALLES"
            + "(CLAVE_ACCESO_ELE_DOCUMENTOS,NUMFILA,CODIGO_PRINCIPAL,DESCRIPCION,CANTIDAD,"
            + "PRECIO_UNITARIO,DESCUENTO,PRECIO_TOTAL_SIN_IMPUESTO)"
            + "VALUES ('" + factura.claveAcceso + "'," + str(i) + ",'" + det.codigoPrincipal + "',"
            + "%s" + "," + str(det.cantidad) + "," + str(det.precioUnitario) + ","
            + str(det.descuento) + ","
            + str(det.total) + ")", (det.descripcion))
            j = 1
            for imp in det.impuesto:
                sqlite.ejecutar("INSERT INTO ELE_FACTURA_IMPUESTOS(CLAVE_ACCESO_ELE_DOCUMENTOS,"
                + "NUM_FILA_ELE_FACTURA_DETALLES,NUM_FILA,CODIGO,CODIGO_PORCENTAJE,TARIFA,"
                + "BASE_IMPONIBLE,VALOR) VALUES ('" + factura.claveAcceso + "'," + str(i) + ","
                + str(j) + ",'" + imp.codigo + "','" + imp.codigoPorcentaje + "',"
                + imp.tarifa + "," + imp.baseImponible + "," + imp.valor + ")")
                j = j + 1
            i = i + 1

        sqlite.desconectar()