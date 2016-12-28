# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
metadata = MetaData()
from datetime import datetime
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:horiz0ns@127.0.0.1/niza", pool_recycle=3600)

ele_contribuyentes = Table('ele_contribuyentes', metadata,
    Column('documento', String(20), primary_key=True),
    Column('razon_social', String(500)),
    Column('nombre_comercial', String(500)),
    Column('direccion', String(500))
)

ele_documentos = Table('ele_documentos', metadata,
    Column('id', Integer(), primary_key=True),
    Column('clave_acceso', String(100), unique=True),
    Column('establecimiento', String(10)),
    Column('punto_emision', String(10)),
    Column('secuencial', String(20)),
    Column('fecha_emision', DateTime()),
    Column('autorizacion', String(100)),
    Column('identificacionReceptor', String(20), index=True),
    Column('razonSocialReceptor', String(500)),
    Column('tipo', String(10)),
    Column('fecha_creacion', DateTime(), default=datetime.now)
)

ele_factura_detalles = Table('ele_factura_detalles', metadata,
    Column('id', Integer(), primary_key=True),
    Column('id_ele_documentos', Integer(), ForeignKey('ele_documentos.id', ondelete='CASCADE')),
    Column('numfila', Integer()),
    Column('codigo_principal', String(50)),
    Column('descripcion', String(200)),
    Column('cantidad', Numeric(12, 2)),
    Column('precio_unitario', Numeric(12, 2)),
    Column('descuento', Numeric(12, 2)),
    Column('precio_total_sin_impuesto', Numeric(12, 2)),
    Column('estado', String(10))
)

ele_factura_impuestos = Table('ele_factura_impuestos', metadata,
    Column('id', Integer(), primary_key=True),
    Column('id_ele_factura_detalles', Integer(), ForeignKey('ele_factura_detalles.id',
    ondelete='CASCADE')),
    Column('numfila', Integer()),
    Column('codigo', String(10)),
    Column('codigo_porcentaje', String(10)),
    Column('tarifa', Numeric(12, 2)),
    Column('base_imponible', Numeric(12, 2)),
    Column('valor', Numeric(12, 2))
)

metadata.create_all(engine)