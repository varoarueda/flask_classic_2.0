from balance import app # Importar la aplicación
from flask import render_template
from balance.models import DBManager

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS") 
dbManager = DBManager(ruta_basedatos)

# Crear las rutas

@app.route("/")
def inicio():

    consulta = "SELECT * FROM movimientos order by fecha"
    movimientos = dbManager.consultaSQL(consulta)
    
    return render_template("inicio.html", items=movimientos)

@app.route("/nuevo", methods=["GET", "POST"]) # Los métodos aquí van en mayusc.
def nuevo():
    return "Pagina de alta de movimientos"

@app.route("/borrar/<int:id>", methods=["GET", "POST"]) # Ruta con parámetro "tipo:id", es especifico de flask para identificar lo que quiero borrar
def borrar(id):
    return f"Pagina de borrado de {id}"



