# -*- coding: utf-8 -*-

from Comprobante import *
from modelo import *
import datetime
from sqlalchemy.sql import select
from sqlalchemy.sql import func


class CargaFacturaMySql(object):

    def __init__(self):
        pass

    def carga(self, factura):
        connection = engine.connect()
        fecha = datetime.datetime.strptime(factura.fechaEmision, '%d/%m/%Y').date()

        ins = ele_documentos.insert().values(
            clave_acceso=factura.claveAcceso,
            establecimiento=factura.establecimiento,
            punto_emision=factura.puntoEmision,
            secuencial=factura.secuencial,
            fecha_emision=fecha,
            autorizacion=factura.autorizacion,
            identificacionReceptor=factura.identificacionReceptor,
            razonSocialReceptor=factura.razonSocialReceptor,
            tipo=factura.tipo
        )

        print((str(ins)))
        ins.compile().params
        result = connection.execute(ins)
        print((result.inserted_primary_key))

        i = 1

        for det in factura.detalle:
            insDetalle = ele_factura_detalles.insert().values(
                id_ele_documentos=result.inserted_primary_key,
                numfila=i,
                codigo_principal=det.codigoPrincipal,
                descripcion=det.descripcion,
                cantidad=det.cantidad,
                precio_unitario=det.precioUnitario,
                descuento=det.descuento,
                precio_total_sin_impuesto=det.total
            )

            print((str(insDetalle)))
            insDetalle.compile().params
            resultDetalle = connection.execute(insDetalle)
            print((resultDetalle.inserted_primary_key))

            j = 1
            for imp in det.impuesto:
                insImpuesto = ele_factura_impuestos.insert().values(
                    id_ele_factura_detalles=resultDetalle.inserted_primary_key,
                    numfila=j,
                    codigo=imp.codigo,
                    codigo_porcentaje=imp.codigoPorcentaje,
                    tarifa=imp.tarifa,
                    base_imponible=imp.baseImponible,
                    valor=imp.valor
                )
                print((str(insImpuesto)))
                insImpuesto.compile().params
                resultImpuesto = connection.execute(insImpuesto)
                print((resultImpuesto.inserted_primary_key))

                j = j + 1
            i = i + 1

    def verificaClaveAcceso(self, clave):
        connection = engine.connect()

        s = select([func.count(ele_documentos.c.clave_acceso)]).where(
            ele_documentos.c.clave_acceso == clave)
        rp = connection.execute(s)
        record = rp.first()

        return record.count_1

    def cargaContribuyente(self, factura):
        connection = engine.connect()
        ins = ele_contribuyentes.insert().values(
            documento="0400351631001",
            razon_social="VILLARREAL MAFLA HUGO IGNACIO",
            nombre_comercial="FERRIACABADOS",
            direccion="Av. Mariano Acosta y Luis Felipe Borja 2530"
        )
        print((str(ins)))
        ins.compile().params
        result = connection.execute(ins)
        print((result.inserted_primary_key))

if __name__ == "__main__":
    f = Comprobante()
    c = CargaFacturaMySql()
    print(c.verificaClaveAcceso("0102201601040035163100120060010000022181234567815"))