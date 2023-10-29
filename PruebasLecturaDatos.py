
import serial
import time as tm

Conexion= serial.Serial('COM13', 9600)
data = Conexion.readline().decode()

Conexion.close()

print(data)