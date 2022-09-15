"""---Pasos A Seguir Para Conectar con BBDD---"""

import sqlite3

""" 
1 Abrir/Crear Conexión
2 Crear Puntero para poder Ejercutar y Manejar Querys/Consultas
3 Ejecutar Query/Consulta SQL
4 Manejar los resultados de la Query/Consulta (Insertar 'Create', Leer 'Read', Actualizar y Borrar info de la tabla)
5 Cerrar Puntero
6 Cerrar Conexión
"""


conexion = sqlite3.connect("PrimeraBase")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR (20))")

# Lo ponemos en comentarios para poder seguir ejecutando, si no dará error de que la tabla ya existe
# Al ser varchar/string 50, la longitud de caracteres máxima que puede tener es de 50

# cursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', 15, 'DEPORTES')")

varios_productos = [
    ('Camiseta', 10, 'Deportes'),
    ('Jarrón', 90, 'Cerámica'),
    ('Camión', 20, 'Jugetería')
]

# cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", varios_productos)
# Método para insertar varias filas a la vez, se ponen los 3 campos como interrogante para indicar que son 3 elementos

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()  # fetchall() devuelve una lista con los registros que devuelve la instrucción anterior
print(productos)

for producto in productos:
    print('Nombre Artículo:\n', producto[0], '\nSección:\n', producto[2])

conexion.commit()  # Para ejecutar los cambios

conexion.close()
