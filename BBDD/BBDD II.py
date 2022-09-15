import sqlite3

conexion = sqlite3.connect("GestiónProductos")

cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE ARTICULO VARCHAR (50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR (20))
""")

# UNIQUE hace que no pueda haber 2 registros con el mismo nombre

productos = [
    ('Pelota', 20, 'Juguetería'),
    ('Pantalón', 15, 'Confección'),
    ('Destornillador', 25, 'Ferretería'),
    ('Jarrón', 45, 'Cerámica')
]

conexion.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

conexion.commit()

conexion.close()