from tkinter import *
from tkcalendar import Calendar

ventana2 = Tk()
ventana2.geometry("500x650")
ventana2.title("Registro de Vacunas")
ventana2.resizable(0,0)

ventana2.config(background="lightblue")

fuente = ("Times New Roman", 23)
fuente2 = ("Times New Roman", 16)
titulo = Label(text="Registro de Vacunas", font=fuente,background="lightblue")
titulo.place(x=120,y=40)


AtrasBoton = Button(ventana2,text="<",font=fuente2, width=4,background="lightgreen")
AtrasBoton.place(x=10,y=10)

BiologoLabel = Label(ventana2, text="Biologo: ",font=fuente2,background="lightblue")
BiologoLabel.place(x=60,y=100)
BiologoEntry = Entry(ventana2, width=25,font=fuente2)
BiologoEntry.place(x=160,y=100)

DosisLabel = Label(ventana2, text="Dosis: ",font=fuente2,background="lightblue")
DosisLabel.place(x=60,y=150)
DosisEntry = Entry(ventana2, width=25,font=fuente2)
DosisEntry.place(x=160,y=150)



LoteLabel = Label(ventana2, text="Lote: ",font=fuente2,background="lightblue")
LoteLabel.place(x=60,y=200)
LoteEntry = Entry(ventana2, width=25,font=fuente2)
LoteEntry.place(x=160,y=200)

ISPLabel = Label(ventana2, text="ISP Vacuna: ",font=fuente2,background="lightblue")
ISPLabel.place(x=50,y=250)
ISPEntry = Entry(ventana2, width=25,font=fuente2)
ISPEntry.place(x=160,y=250)

ISPLabel = Label(ventana2, text="Fecha: ",font=fuente2,background="lightblue")
ISPLabel.place(x=50,y=300)
Date = Calendar(ventana2, selectmode='day', year=2023, month=10, day=31)
Date.place(x=160,y=300)

RegistrarBoton = Button(ventana2,text="Registrar vacuna", font=fuente2)
RegistrarBoton.place(x=180,y=520)

ventana2.mainloop()