from tkinter import *
from tkcalendar import Calendar

ventana2 = Tk()
ventana2.geometry("500x650")
ventana2.title("Registro de Pacientes")
ventana2.resizable(0,0)

ventana2.config(background="lightblue")

fuente = ("Times New Roman", 23)
fuente2 = ("Times New Roman", 16)
titulo = Label(text="Registro de paciente", font=fuente,background="lightblue")
titulo.place(x=120,y=40)


AtrasBoton = Button(ventana2,text="<",font=fuente2, width=4,background="lightgreen")
AtrasBoton.place(x=10,y=10)

NombreLabel = Label(ventana2, text="Nombre: ",font=fuente2,background="lightblue")
NombreLabel.place(x=60,y=100)
NombreEntry = Entry(ventana2, width=25,font=fuente2)
NombreEntry.place(x=160,y=100)

ApellidoLabel = Label(ventana2, text="Apellido: ",font=fuente2,background="lightblue")
ApellidoLabel.place(x=60,y=150)
ApellidoEntry = Entry(ventana2, width=25,font=fuente2)
ApellidoEntry.place(x=160,y=150)



DocumentoLabel = Label(ventana2, text="Documento: ",font=fuente2,background="lightblue")
DocumentoLabel.place(x=50,y=200)
DocumentoEntry = Entry(ventana2, width=25,font=fuente2)
DocumentoEntry.place(x=160,y=200)

AlergiasLabel = Label(ventana2, text="Alergias: ",font=fuente2,background="lightblue")
AlergiasLabel.place(x=50,y=250)
AlergiasEntry = Entry(ventana2, width=25,font=fuente2)
AlergiasEntry.place(x=160,y=250)

DateLabel = Label(ventana2, text="Fecha: ",font=fuente2,background="lightblue")
DateLabel.place(x=50,y=300)
Date = Calendar(ventana2, selectmode='day', year=2023, month=10, day=31)
Date.place(x=160,y=300)

RegistrarBoton = Button(ventana2,text="Registrar Paciente", font=fuente2)
RegistrarBoton.place(x=180,y=520)

ventana2.mainloop()