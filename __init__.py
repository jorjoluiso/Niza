# -*- coding: utf-8 -*-
import sys
from Config import *
from ParseXMLFactura import *
from CargaFacturaMySql import *
from Utilidades import *
import os
from os import listdir
from os.path import isfile, join
import logging


if __name__ == "__main__":
    LOG_FILENAME = 'niza.log'
    logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-2s; %(levelname)-2s; %(message)s',
                    datefmt='%Y-%m-%d; %H:%M;',
                    )

    if len(sys.argv) == 1:

        cfg = Config()

        cfg.getConfig()
        cfg.imprimir()

        carga = CargaFacturaMySql()

        archivosXML = [f for f in listdir(cfg.rutaXML) if isfile(join(cfg.rutaXML, f))]

        for archivo in archivosXML:
            if archivo.lower().endswith(".xml"):
                if Utilidades.verificaTipoDocumento(str(archivo)) == "FACTURA":
                    claveArchivo = str(archivo).replace(".xml", "")

                    c = carga.verificaClaveAcceso(claveArchivo)

                    if (c == 0):
                        try:
                            print(("Archivo:", archivo, c))
                            parseFactura = ParseXMLFactura()
                            factura = parseFactura.getFactura(cfg.rutaXML + os.sep + archivo)
                            #parseFactura.imprimir()

                            carga.carga(factura)
                        except:
                            e1 = sys.exc_info()[0]
                            e2 = sys.exc_info()[1]
                            exc_tb = sys.exc_info()
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            logging.error("Error en el Archivo: " + archivo + ";" + str(e1)
                            + str(e2) + " " + str(fname) + " " + str(exc_tb.tb_lineno))
                            print(("Error en el Archivo:", archivo, e1, e2, fname,
                            exc_tb.tb_lineno))

        print("Proceso terminado")
    else:
        print((len(sys.argv)))
