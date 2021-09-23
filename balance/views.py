from balance import app # Importar la aplicación

# Crear las rutas

@app.route("/")
def inicio():
    return "Página de inicio"

@app.route("/nuevo", methods=["GET", "POST"]) # Los métodos aquí van en mayusc.
def nuevo():
    return "Pagina de alta de movimientos"

@app.route("/borrar/<int:id>", methods=["GET", "POST"]) # Ruta con parámetro "tipo:id", es especifico de flask para identificar lo que quiero borrar
def borrar(id):
    return f"Pagina de borrado de {id}"
    


