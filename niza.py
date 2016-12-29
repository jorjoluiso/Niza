from flask import Flask
from flask import render_template
from flask import request, send_file
from Modelos import *
from Config import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:horiz0ns@localhost/niza'
db = SQLAlchemy(app)



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
            ele_documentos=ele_documentos.query.filter_by(identificacionReceptor=documento).order_by(ele_documentos.fecha_emision.desc()).all(), 
            nombre=nombre, documento=documento)    


        return render_template('busca_documento.html')        
    return render_template('busca_documento.html')

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


@app.route("/fecha")
def fecha():
    return render_template('busca_fecha.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)

