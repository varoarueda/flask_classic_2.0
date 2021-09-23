import sqlite3

# Crear un objeto que nos permita hacer consultas
class DBManager():
    def __init__(self, ruta_basedatos):
        self.ruta_basedatos = ruta_basedatos

    def consultaSQL(self, consulta):
        conexion = sqlite3.connect(self.ruta_basedatos) # Conexión BBDD con la app

        cur = conexion.cursor() # Crear cursor
        cur.execute(consulta)
        
        # Lista de diccionarios
        keys = []
        for item in cur.description:
            keys.append(item[0])

        movimientos = []
        for registro in cur.fetchall():
            ix_clave = 0 
            d = {}
            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            movimientos.append(d)

        conexion.close()
        return movimientos
