import sqlite3

conexion = sqlite3.connect("GestiónProductos")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM main.PRODUCTOS WHERE SECCION = 'Confección'")

print(cursor.fetchall())

cursor.execute("UPDATE main.PRODUCTOS SET PRECIO = 35 WHERE NOMBRE='Pelota'")

cursor.execute("DELETE FROM main.PRODUCTOS WHERE NOMBRE = 'Pantalones'")  # No borra nada porque no lo hay

conexion.commit()

conexion.close()