import sqlite3, datetime
conexion = sqlite3.connect('Vacunas.db')
cursor = conexion.cursor()

cursor.execute("SELECT id FROM vacunas")
filas = cursor.fetchall()

print(filas[-1][0])

conexion.commit()
conexion.close()