# -*- coding: utf-8 -*-
import configparser
import os


class Config(object):
    rutaXML = None
    rutaPDF = None

    def __init__(self):
        self.rutaXML = ""
        self.rutaPDF = ""
        self.rutaDB = ""

    def setConfigDirectorios(self):
        config = configparser.ConfigParser()
        config["Directorios"] = {}
        param = config["Directorios"]
        param["rutaXML"] = "/home/jorgequiguango/Electronicas/Ferriacabados/autorizado"
        param["rutaPDF"] = "/home/jorgequiguango/Electronicas/Ferriacabados/pdf"

        config["Sqlite"] = {}
        param = config["Sqlite"]
        param["rutaDB"] = "niza.db"

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def getConfigDirectorios(self, config):
        self.rutaXML = config["Directorios"]["rutaXML"]
        self.rutaPDF = config["Directorios"]["rutaPDF"]
        self.rutaDB = config["Sqlite"]["rutaDB"]

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + os.sep + 'config.ini')
        #print("Archivo de configuración", (os.path.dirname(__file__) + os.sep + 'config.ini'))
        self.getConfigDirectorios(config)

    def imprimir(self):
        print(("Ruta XML", self.rutaXML))
        print(("Ruta PDF", self.rutaPDF))
        print(("Ruta Sqlite", self.rutaDB))