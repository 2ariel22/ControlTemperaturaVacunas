from tkinter import *
from PIL import Image, ImageTk
import time
import serial
import pyttsx3

def getTemperatura():
    data = Conexion.readline().decode()
    time.sleep(.2)
    return float(data)

def setTemperatura():
    temperatura = getTemperatura()
    Temperatura.set(f"Temperatura: {temperatura}")

    if temperatura < 28 or temperatura > 32:
        # Si la temperatura está fuera del rango, muestra un mensaje de advertencia en voz
        engine.say(f"Advertencia: La temperatura es {temperatura} y está fuera de rango")
        engine.runAndWait()
        canvas_ok.config(bg="red")  # Cambiar el color del cuadro a rojo
        textOK.set("Bad: ")
    else:
        # Si la temperatura está dentro del rango, muestra un mensaje de estado normal
        canvas_ok.config(bg="green")  # Cambiar el color del cuadro a verde
        textOK.set("Good: ")

    raiz.after(5000, setTemperatura)

Conexion = serial.Serial('COM12', 9600)
raiz = Tk()
raiz.title("Monitoreo De Cadena De Frio")
raiz.geometry("500x650")
raiz.resizable(0, 0)

ruta_imagen = "Logo.jpeg"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((470, 200))
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = Label(raiz, image=imagen_tk)
label_imagen.place(x=15, y=5)

fuente = ("Times New Roman", 33)
Temperatura = StringVar()
entryTemperatura = Entry(raiz, width=20, font=fuente, textvariable=Temperatura, justify=CENTER)
entryTemperatura.config(state='readonly')
entryTemperatura.place(x=29, y=220)

textOK=StringVar()
labelOk=Label(raiz,textvariable=textOK, font= fuente)
labelOk.place(x=100, y=300)
textOK.set("Good: ")
canvas_ok = Canvas(raiz, width=125, height=50, bg="green")  # Cuadro para mostrar estado
canvas_ok.place(x=250, y=300)

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

setTemperatura()

raiz.mainloop()

Conexion.close()
