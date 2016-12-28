# -*- coding: utf-8 -*-
import ntpath
import tempfile
import os


class Utilidades(object):

    def __init__(self):
        pass

    #Quita los espacios en blanco del contenido del archivo XML
    @staticmethod
    def borrarBlancosArchivo(archivo):
        clean_lines = []
        with open(archivo, "r", encoding="utf8") as f:
            lines = f.readlines()
            clean_lines = [l.strip() for l in lines if l.strip()]
        with open(archivo, "w", encoding="utf8") as f:
            f.writelines("\n".join(clean_lines))
        f.close

    #Extrae el nombre del archivo, eliminando la ruta
    @staticmethod
    def extraerNombre(rutaArchivo):
        head, tail = ntpath.split(rutaArchivo)
        return tail or ntpath.basename(head)

    #Crea un archivo temporal con la clave de acceso
    @staticmethod
    def mensajero(clave):
        with open(tempfile.gettempdir() + os.sep + "clave.ca", "w", encoding="utf8") as f:
            f.writelines(clave)
        f.close
        print(("Clave de Acceso:", clave, tempfile.gettempdir() + os.sep + "clave.ca"))

    #Verifica si la clave de acceso es de una Factura, Retención, Nota de Crédito, Nota de Débito
    #o Guía de Remisión
    @staticmethod
    def verificaTipoDocumento(clave):
        if (clave[8:8 + 2]) == "01":
            return "FACTURA"
        elif (clave[8:8 + 2]) == "04":
            return "NOTA DE CRÉDITO"
        elif (clave[8:8 + 2]) == "05":
            return "NOTA DE DÉBITO"
        elif (clave[8:8 + 2]) == "06":
            return "GUÍA DE REMISIÓN"
        elif (clave[8:8 + 2]) == "07":
            return "COMPROBANTE DE RETENCIÓN"

        return "NO DEFINIDO"