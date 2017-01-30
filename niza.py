from flask import Flask
from flask import render_template
from flask import request, send_file
from Modelos import *
from Config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/niza'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template('home.html', ele_contribuyentes=ele_contribuyentes.query.all())


@app.route('/home')
def home():
    return render_template('home.html', ele_contribuyentes=ele_contribuyentes.query.all())


@app.route("/documento")
def documento():
    documento = request.args.get("documento")
    if documento and documento != "9999999999999":
        print("Documento", documento)

        existe = ele_documentos.query.filter_by(identificacionReceptor=documento).count()
        if existe > 0:
            nombreReceptor = ele_documentos.query.filter_by(identificacionReceptor=documento).first()
            nombre = nombreReceptor.razonSocialReceptor
            print("Nombre", nombre)

            return render_template('busca_documento.html',
            ele_documentos=ele_documentos.query.filter_by(identificacionReceptor=documento)
            .order_by(ele_documentos.fecha_emision.desc()).all(), 
            nombre=nombre, documento=documento)    


        return render_template('busca_documento.html')        
    return render_template('busca_documento.html')


@app.route("/fecha")
def fecha():
    fecha = request.args.get("fecha")
    establecimiento = request.args.get("establecimiento")
    punto_emision = request.args.get("punto_emision")
    secuencial = request.args.get("secuencial")    
    ultimo_digito = request.args.get("ultimo_digito")

    if fecha and establecimiento and punto_emision and secuencial and ultimo_digito:
        print("Datos de Factura", fecha, establecimiento, punto_emision, secuencial, ultimo_digito)

        establecimiento = "{0:0>3}".format(establecimiento)
        punto_emision = "{0:0>3}".format(punto_emision)
        secuencial = "{0:0>9}".format(secuencial)        

        existe = ele_documentos.query.filter_by(fecha_emision=fecha, establecimiento=establecimiento, 
        punto_emision=punto_emision, secuencial=secuencial).count()
        if existe > 0:
            nombreReceptor = ele_documentos.query.filter_by(fecha_emision=fecha, establecimiento=establecimiento, 
            punto_emision=punto_emision, secuencial=secuencial).first()
            nombre = nombreReceptor.razonSocialReceptor
            documento = nombreReceptor.identificacionReceptor
            fecha_emision = nombreReceptor.fecha_emision
            establecimiento = nombreReceptor.establecimiento
            punto_emision = nombreReceptor.punto_emision
            secuencial = nombreReceptor.secuencial
            clave_acceso = nombreReceptor.clave_acceso

            return render_template('busca_fecha.html',nombre=nombre, documento=documento, fecha_emision=fecha_emision,
            establecimiento=establecimiento, punto_emision=punto_emision, secuencial=secuencial, clave_acceso=clave_acceso)    
    return render_template('busca_fecha.html')


@app.route('/descargar_pdf/<pdf>')
def descargarPDF(pdf=None):
    if pdf is not None:
        print("Descargar archivo PDF",pdf)
        cfg = Config()
        cfg.getConfig()
        return send_file(cfg.rutaPDF + os.sep + pdf, as_attachment=True)


@app.route('/descargar_xml/<xml>')
def descargarXML(xml=None):
    if xml is not None:        
        print("Descargar archivo XML",xml)
        cfg = Config()
        cfg.getConfig()
        return send_file(cfg.rutaXML + os.sep + xml, as_attachment=True)


@app.route('/acerca')
def acerca():
    return render_template('acerca.html')
    

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)

