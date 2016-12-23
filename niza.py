from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:horiz0ns@localhost/niza'
db = SQLAlchemy(app)

class ele_contribuyentes(db.Model):
    documento = db.Column('documento', db.String(20), primary_key=True)
    razon_social = db.Column('razon_social', db.String(500))
    nombre_comercial = db.Column('nombre_comercial', db.String(500))
    direccion = db.Column('direccion', db.String(500))

    def __init__(self, documento, razon_social, nombre_comercial, direccion):
        self.documento = documento
        self.razon_social = razon_social
        self.nombre_comercial = nombre_comercial
        self.direccion = direccion

@app.route('/')
def show_all():
   return render_template('show_all.html', ele_contribuyentes = ele_contribuyentes.query.all())

if __name__ == "__main__":
    app.run(port=5000, debug=True)

