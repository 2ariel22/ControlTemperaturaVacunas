from tkinter import *
from PIL import Image, ImageTk
import time, serial

def getTemperatura():
    #Conexion = serial.Serial('COM13', 9600)
    #data = Conexion.readline().decode()
    #Conexion.close()
    data="25 C°"
    return data

def setTemperatura():
    pass

tiempo = time.time()
raiz = Tk()
raiz.title("Monitoreo De Cadena De Frio")
raiz.geometry("500x650")
raiz.resizable(0,0)

# Cargar la imagen
ruta_imagen = "Logo.jpeg" 
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((470, 200)) 
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = Label(raiz, image=imagen_tk)
label_imagen.place(x=15,y=5)

fuente = ("Times New Roman", 33)
Temperatura = StringVar()
entryTemperatura = Entry(raiz,width=20,font=fuente,textvariable=Temperatura)
entryTemperatura.config(state='readonly')
entryTemperatura.place(x=29,y=220)

tiempoAxiliar =time.time
if((tiempoAxiliar - tiempo )>= 5):
    print("getiando la temperatura")
    tiempo = tiempoAxiliar


raiz.mainloop()
