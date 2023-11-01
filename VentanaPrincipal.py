from tkinter import *
from PIL import Image, ImageTk
import time,serial, pyttsx3, sqlite3
from tkcalendar import Calendar
from tkinter import messagebox 

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


def Registrar():
    def Confimacion():
        conexion = sqlite3.connect('Vacunas.db')
        cursor = conexion.cursor()

        DateG = Date.get_date()
        BiologoG = BiologoVar.get()
        DosisG = int(DosisVar.get())
        LoteG = LoteVar.get()
        ISPG = ISPVar.get()
        TemperaturaG = Temperatura.get()
        cursor.execute("SELECT id FROM vacunas")
        filas = cursor.fetchall()

        id = (filas[-1][0]) + 1

        cursor.execute("INSERT INTO Vacunas (id, biologo, dosis, lote, ISP,fecha, temperatura)" +
                    "VALUES(?,?,?,?,?,?,?)",(id,BiologoG,DosisG,LoteG,ISPG,DateG,TemperaturaG))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Información", "Registo exitoso")
    def atras():
        raiz.deiconify()
        ventana2.withdraw()
    raiz.withdraw()
    ventana2 = Toplevel(raiz)
    ventana2.geometry("500x650")
    ventana2.title("Registro de Vacunas")
    ventana2.resizable(0,0)

    ventana2.config(background="lightblue")

    fuente = ("Times New Roman", 23)
    fuente2 = ("Times New Roman", 16)
    titulo = Label(ventana2,text="Registro de Vacunas", font=fuente,background="lightblue")
    titulo.place(x=120,y=40)


    AtrasBoton = Button(ventana2,text="<",font=fuente2, width=4,background="lightgreen",command=atras)
    AtrasBoton.place(x=10,y=10)

    BiologoLabel = Label(ventana2, text="Biologo: ",font=fuente2,background="lightblue")
    BiologoLabel.place(x=60,y=100)
    BiologoVar = StringVar()
    BiologoEntry = Entry(ventana2, width=25,font=fuente2,textvariable=BiologoVar) 
    BiologoEntry.place(x=160,y=100)

    DosisLabel = Label(ventana2, text="Dosis: ",font=fuente2,background="lightblue")
    DosisLabel.place(x=60,y=150)
    DosisVar= StringVar()
    DosisEntry = Entry(ventana2, width=25,font=fuente2,textvariable=DosisVar)
    DosisEntry.place(x=160,y=150)

    LoteLabel = Label(ventana2, text="Lote: ",font=fuente2,background="lightblue")
    LoteLabel.place(x=60,y=200)
    LoteVar = StringVar()
    LoteEntry = Entry(ventana2, width=25,font=fuente2,textvariable=LoteVar)
    LoteEntry.place(x=160,y=200)

    ISPLabel = Label(ventana2, text="ISP Vacuna: ",font=fuente2,background="lightblue")
    ISPLabel.place(x=50,y=250)
    ISPVar = StringVar()
    ISPEntry = Entry(ventana2, width=25,font=fuente2, textvariable=ISPVar)
    ISPEntry.place(x=160,y=250)

    DateLabel = Label(ventana2, text="Fecha: ",font=fuente2,background="lightblue")
    DateLabel.place(x=50,y=300)
    Date = Calendar(ventana2, selectmode='day', year=2023, month=10, day=31)
    Date.place(x=160,y=300)

    RegistrarBoton = Button(ventana2,text="Registrar vacuna", font=fuente2, command=Confimacion)
    RegistrarBoton.place(x=180,y=520)

def RegistrarPaciente():
    def Confimacion():
        conexion = sqlite3.connect('Vacunas.db')
        cursor = conexion.cursor()

        DateG = Date.get_date()
        NombreG = NombreVar.get()
        ApellidoG = ApellidoVar.get()
        DocumetonG = DocumentoVar.get()
        AlergiasG = AlergiaVar.get()
        cursor.execute("SELECT id FROM paciente")
        filas = cursor.fetchall()

        id = (filas[-1][0]) + 1

        cursor.execute("INSERT INTO paciente (id, nombre, apellido, documento, alergias,fecha)" +
                    "VALUES(?,?,?,?,?,?)",(id,NombreG,ApellidoG,DocumetonG,AlergiasG,DateG))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Información", "Registo exitoso")
    def atras():
        raiz.deiconify()
        ventana2.withdraw()
    raiz.withdraw()
    ventana2 = Toplevel(raiz)
    ventana2.geometry("500x650")
    ventana2.title("Registro de Pacientes")
    ventana2.resizable(0,0)

    ventana2.config(background="lightblue")

    fuente = ("Times New Roman", 23)
    fuente2 = ("Times New Roman", 16)
    titulo = Label(ventana2,text="Registro de paciente", font=fuente,background="lightblue")
    titulo.place(x=120,y=40)


    AtrasBoton = Button(ventana2,text="<",font=fuente2, width=4,background="lightgreen",command=atras)
    AtrasBoton.place(x=10,y=10)

    NombreLabel = Label(ventana2, text="Nombre: ",font=fuente2,background="lightblue")
    NombreLabel.place(x=60,y=100)
    NombreVar = StringVar()
    NombreEntry = Entry(ventana2, width=25,font=fuente2,textvariable=NombreVar)
    NombreEntry.place(x=160,y=100)

    ApellidoLabel = Label(ventana2, text="Apellido: ",font=fuente2,background="lightblue")
    ApellidoLabel.place(x=60,y=150)
    ApellidoVar = StringVar()
    ApellidoEntry = Entry(ventana2, width=25,font=fuente2,textvariable=ApellidoVar)
    ApellidoEntry.place(x=160,y=150)



    DocumentoLabel = Label(ventana2, text="Documento: ",font=fuente2,background="lightblue")
    DocumentoLabel.place(x=50,y=200)
    DocumentoVar= StringVar()
    DocumentoEntry = Entry(ventana2, width=25,font=fuente2,textvariable=DocumentoVar)
    DocumentoEntry.place(x=160,y=200)

    AlergiasLabel = Label(ventana2, text="Alergias: ",font=fuente2,background="lightblue")
    AlergiasLabel.place(x=50,y=250)
    AlergiaVar = StringVar()
    AlergiasEntry = Entry(ventana2, width=25,font=fuente2,textvariable=AlergiaVar)
    AlergiasEntry.place(x=160,y=250)

    DateLabel = Label(ventana2, text="Fecha: ",font=fuente2,background="lightblue")
    DateLabel.place(x=50,y=300)
    Date = Calendar(ventana2, selectmode='day', year=2023, month=10, day=31)
    Date.place(x=160,y=300)

    RegistrarBoton = Button(ventana2,text="Registrar Paciente", font=fuente2,command=Confimacion)
    RegistrarBoton.place(x=180,y=520)
    
def Visualizar():
    messagebox.showinfo("Notificacion","Dirigete a la app DB Browser")

def Losiento():
    messagebox.showinfo("Lo sentimos :0", "Lamentablemente esta opcion aun no se encuentra disponible :C")

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
fuente2 = ("Times New Roman", 20)
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


botonRegistrar = Button(raiz,text="Registrar Vacuna",font=fuente2, background="lightblue", command=Registrar)
botonRegistrar.place(x=50,y=450)

botonRegistrarPaciente = Button(raiz,text="Registrar Paciente",font=fuente2, background="lightblue", command=RegistrarPaciente)
botonRegistrarPaciente.place(x=30,y=520)

botonVisualizar = Button(raiz,text="Visualizar",font=fuente2, background="lightblue",command=lambda:Visualizar)
botonVisualizar.place(x=330,y=450)

botonLector = Button(raiz,text="Codigo qr/barras",font=fuente2, background="lightblue",command=Losiento)
botonLector.place(x=290,y=520)


# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

setTemperatura()

raiz.mainloop()

Conexion.close()
