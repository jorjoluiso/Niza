from flask import Flask
from flask import render_template

from flask import request, make_response
from Modelos import *


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

@app.route('/transform')
def transform_view():
    print("Descargar archivo")
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
"1985/01/21","Douglas Adams",0345391802,5.95
"1990/01/12","Douglas Hofstadter",0465026567,9.95
"1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
"1999/12/03","Richard Friedman",0060630353,5.95
"2004/10/04","Randel Helms",0879755725,4.50"""
    # We need to modify the response, so the first thing we 
    # need to do is create a response out of the CSV string
    response = make_response(csv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response


@app.route("/fecha")
def fecha():
    return render_template('busca_fecha.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)

