import sqlite3


# Establecer conexión con la base de datos (si no existe, se creará)
conexion = sqlite3.connect('Vacunas.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla con una columna autoincremental
cursor.execute('''
    CREATE TABLE Paciente (
        id INT PRIMARY KEY ,
        nombre VARCHAR(150),
        apellido VARCHAR(150),
        documento VARCHAR(50),
        alergias VARCHAR(150),
        fecha Date     
    )
''')

# Insertar datos en la tabla (no es necesario proporcionar un valor para 'id')
#cursor.execute("INSERT INTO Ejemplo (nombre, edad, correo_electronico) VALUES (?, ?, ?)", ('Ejemplo Usuario', 30, 'usuario@example.com'))

# Guardar los cambios
conexion.commit()

# Realizar una consulta

# Cerrar la conexión
conexion.close()
