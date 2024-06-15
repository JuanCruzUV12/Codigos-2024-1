# Proyecto-Parcial de Matematicas Basicas
# Integrantes: 
# 1. Juan Stevan Cruz - 202459437
# 2. Brayan Urquijo - 202459407
# 3. Jhoan Hurtado - 202459472

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
from PIL import Image
from tkinter import PhotoImage

# Se crea la ventana
ventana = Tk()

# Fondo de la ventana
fondo_cielo = PhotoImage(file="fondo_cielo.png")
fondo_cielo = fondo_cielo.subsample(1, 1)
fondo_cielo1 = Label(ventana, image=fondo_cielo)
fondo_cielo1.config(bg="Black")
fondo_cielo1.place(x=-150, y=-37)

# Funciones del juego

# Palabra aleatoria
def palabra_aleatoria():
    palabras = ["matematicas", "funciones", "conicas", "cuadratica", "hiperbola",
                "parabola", "elipse", "circunferencia", "geogebra", "exponencial",
                "logaritmo", "inversa", "valorabsoluto", "dominio", "rango", "geometria",
                "cubica", "constante", "lineal", "simetria", "inyectiva", "sobreyectiva", "biyectiva",]
    return random.choice(palabras)

# Lee el archivo de las preguntas
def leer_archivo():
    with open("PreguntasActualizadas.txt", "r") as archivo:
        palabras = archivo.read()
        palabras = palabras.split("\n")
        for i in range(len(palabras)):
            palabras[i] = palabras[i].split(";")
        return palabras

# Elige una pregunta del archivo
def elegir_palabra():
    palabras = leer_archivo()
    palabra = random.choice(palabras)
    return palabra

# Funcion para verificar la respuesta
def respuesta_correcta():
    respuesta = opciones_p.get()
    correcta = pregunta[-1]
    if respuesta == "":
        showwarning(title="Respuesta", message="Debes seleccionar una respuesta")
    else:
        if respuesta == correcta:
            showwarning(title="Respuesta", message="Respuesta Correcta")
        else:
            showwarning(title="Respuesta", message="Respuesta Incorrecta")
    
# Funcion para obtener la respuesta
def respuesta_opcion():
    respuesta_opci = opciones_p.get()
    return respuesta_opci
    
# Funcion que muestra la ventana de preguntas
def ventana_preguntas():
    global opciones_p
    global respuesta
    global ventana_preguntas_ventana
    ventana_preguntas_ventana = Tk()
    ventana_preguntas_ventana.title("Preguntas")
    ventana_preguntas_ventana.geometry("700x300")
    ventana_preguntas_ventana.config(bg="White")
    preguntal = Label(ventana_preguntas_ventana, text="Pregunta", font=("ITALIC", 20))
    preguntal.config(bg="White", fg="Black", justify="center")
    preguntal.place(x=10, y=10)
    global pregunta
    pregunta = elegir_palabra()
    pregunta1 = Label(ventana_preguntas_ventana, text=f"{pregunta[0]}", font=("ITALIC", 15))
    pregunta1.config(bg="White", fg="Black")
    pregunta1.place(x=10, y=50)
    opciones = Label(ventana_preguntas_ventana, text="Opciones", font=("ITALIC", 20))
    opciones.config(bg="White", fg="Black")
    opciones.place(x=10, y=100)
    opciones_p = ttk.Combobox(ventana_preguntas_ventana, values=pregunta[1:-1])
    opciones_p.config(width=50)
    opciones_p.place(x=10, y=150)
    respuesta = Button(ventana_preguntas_ventana, text="Responder", font=("ITALIC", 20), command = lambda : (respuesta_opcion(), verificar_respuesta(), respuesta_correcta(), ventana_preguntas_ventana.withdraw()))
    respuesta.config(bg="Red", fg="White")
    respuesta.place(x=10, y=200)

# Imagenes del ahorcado
imagenes = [PhotoImage(file="Ahorcado7.png"), PhotoImage(file="Ahorcado6.png"), PhotoImage(file="Ahorcado5.png"),
            PhotoImage(file="Ahorcado4.png"), PhotoImage(file="Ahorcado3.png"), PhotoImage(file="Ahorcado2.png"),
            PhotoImage(file="Ahorcado1.png")]

palabra_secreta = palabra_aleatoria()
intentos = 7
letras_adivinadas = 0
List_letras_encontradas = []
letras_usadas = []
bandera_Otrointento = False

# Funcion para cuando te queda 1 intento
def otro_intento():
    global opcionOtroIntento
    global ventana_otrointento
    ventana_otrointento = Tk()
    ventana_otrointento.title("Ultima Oportunidad")
    ventana_otrointento.geometry("550x200")
    ventana_otrointento.config(bg="White")
    pregunta = Label(ventana_otrointento, text="Ultima Oportunidad", font=("ITALIC", 20))
    pregunta.config(bg="White", fg="Black")
    pregunta.place(x=10, y=10)
    pregunta1 = Label(ventana_otrointento, text="¿Quienes escribieron el libro: Algebra, Trigonometria y Geometria Analitica?", font=("ITALIC", 12))
    pregunta1.config(bg="White", fg="Black")
    pregunta1.place(x=10, y=50)
    opcionOtroIntento = ttk.Combobox(ventana_otrointento, values=["Grace C. Young y Alfred Young", "Julia Robinson y Reuben Herdh", "Dennis G. Zill y Jacqueline M. Dewar"])
    opcionOtroIntento.config(width=50)
    opcionOtroIntento.place(x=10, y=80)
    respuesta = Button(ventana_otrointento, text="Responder", font=("ITALIC", 20), command = funcionIntento)
    respuesta.config(bg="Red", fg="White")
    respuesta.place(x=10, y=120)

# Funcion para verificar la respuesta de la ultima oportunidad
def funcionIntento():
    global intentos
    global ventana_otrointento
    if opcionOtroIntento.get() == "Dennis G. Zill y Jacqueline M. Dewar":
        showinfo(message="La respuesta es correcta")
        intentos += 1 
        imagenes_ahorcado = Label(ventana, image=imagenes[intentos])
        imagenes_ahorcado.config(bg="White", fg="Black")
        imagenes_ahorcado.place(x=10, y=10)
        intentos_label = Label(ventana, text="Intentos: " + str(intentos), font=("ITALIC", 20))
        intentos_label.config(bg="White", fg="Black")
        intentos_label.place(x=600, y=10)
        ventana_otrointento.destroy()
    else: 
        showinfo(message="La respuesta es incorrecta")
        ventana_otrointento.destroy()
        
# Funcion para verificar la respuesta
def verificar_respuesta():
    global intentos
    global letras_adivinadas
    if respuesta_opcion() == pregunta[-1]:
        letras_adivinadas += palabra_secreta.count(letra.get())
        for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra.get():
                        intentos_label = Label(ventana, text="Intentos: " + str(intentos), font=("ITALIC", 20))
                        intentos_label.config(bg="White", fg="Black")
                        intentos_label.place(x=600, y=10)
                        guiones[i].config(text=""+letra.get())
                        List_letras_encontradas.append(letra.get())
        letra.delete(0, END)
    else:
        intentos -= 1
        imagenes_ahorcado = Label(ventana, image=imagenes[intentos])
        imagenes_ahorcado.config(bg="White", fg="Black")
        imagenes_ahorcado.place(x=10, y=10)
        intentos_label = Label(ventana, text="Intentos: " + str(intentos), font=("ITALIC", 20))
        intentos_label.config(bg="White", fg="Black")
        intentos_label.place(x=600, y=10)
    if letras_adivinadas == len(palabra_secreta):
        showwarning(title="Ganaste", message="Felicidades, ganaste el juego con la palabra: " + palabra_secreta)
        ventana.destroy()

# Funcion para validar la letra
def probarLetraFuncion():
    global intentos
    global letras_adivinadas
    global bandera_Otrointento
    if letra.get() == "":
        showwarning(title="Letra", message="Debes ingresar una letra")
    else:
        letras_usadas.append(letra.get())
        if letra.get() in palabra_secreta:
            if letra.get() in List_letras_encontradas:
                showwarning(title="Letra", message="Ya has usado esa letra")
            else:
                ventana_preguntas()
        else:
            intentos -= 1
            imagenes_ahorcado = Label(ventana, image=imagenes[intentos])
            imagenes_ahorcado.config(bg="White", fg="Black")
            imagenes_ahorcado.place(x=10, y=10)
            intentos_label = Label(ventana, text="Intentos: " + str(intentos), font=("ITALIC", 20))
            intentos_label.config(bg="White", fg="Black")
            intentos_label.place(x=600, y=10)
            if intentos == 1 and bandera_Otrointento == False:
                bandera_Otrointento = True
                boton = Button(ventana, text="Presioname", font=("ITALIC", 20), command=otro_intento)
                boton.config(bg="Red", fg="White", border=5, relief="groove")
                boton.place(x=560, y=80)
            if intentos == 0:
                showwarning(title="Perdiste", message="Se te acabaron los intentos, la palabra era: " + palabra_secreta)
                ventana.destroy()

# Funcion para validar la palabra completa
def validar_palabra():
    if palabra_resultado.get() == palabra_secreta:
        showwarning(title="Ganaste", message="Felicidades, ganaste el juego")
        ventana.destroy()
    else:
        showwarning(title="Perdiste", message="La palabra no es correcta, Se te acabaron los intentos, la palabra era: " + palabra_secreta)
        ventana.destroy()

# Muestra Los Guiones
guiones = [Label(ventana, text="_", font=("ITALIC", 20)) for _ in palabra_secreta]
inicialX = 20
for i in range(len(palabra_secreta)):
    guiones[i].place(x=inicialX, y=375)
    guiones[i].config(bg="White", fg="Black")
    inicialX += 50

# Imagen de icono
ventana.iconbitmap("Logo.ico")

# Caracteristicas de la ventana
ventana.title("Ahorcado with Functions")
ventana.geometry("1000x700")
ventana.resizable(0,0)
ventana.config(bg="White")

# Imagenes
fondo_univalle = PhotoImage(file="logo_uv.png")
fondo_univalle = fondo_univalle.subsample(5, 5)
fondo_univalle1 = Label(ventana, image=fondo_univalle)
fondo_univalle1.config(bg="White")
fondo_univalle1.place(x=763, y=10)

fondo_ladrillo = PhotoImage(file="fondo_ladrillo.png")
fondo_ladrillo = fondo_ladrillo.subsample(-1, 2)
fondo_ladrillo1 = Label(ventana, image=fondo_ladrillo)
fondo_ladrillo1.config(bg="Black")
fondo_ladrillo1.place(x=0, y=560)

linea_frame = Frame(ventana, width=10, height=700)
linea_frame.config(bg="Black")
linea_frame.place(x=750, y=0)

linea_frame1 = Frame(ventana, width=750, height=10)
linea_frame1.config(bg="Black")
linea_frame1.place(x=0, y=550)

#nombre del juego y de los integrantes
nombre_juego = Label(ventana, text="Ahorcado", font=("ITALIC", 25))
nombre_juego.config(bg="White", fg="Black")
nombre_juego.place(x=810, y=250)

nombre_juego1 = Label(ventana, text="With", font=("ITALIC", 25))
nombre_juego1.config(bg="White", fg="Black")
nombre_juego1.place(x=845, y=300)

nombre_juego2 = Label(ventana, text="Functions", font=("ITALIC", 25))
nombre_juego2.config(bg="White", fg="Black")
nombre_juego2.place(x=810, y=350)

integrantes = Label(ventana, text="Integrantes:", font=("ITALIC", 25))
integrantes.config(bg="White", fg="Red")
integrantes.place(x=800, y=450)

integrantes1 = Label(ventana, text="Juan Stevan Cruz", font=("ITALIC", 17))
integrantes1.config(bg="White", fg="Black")
integrantes1.place(x=790, y=500)

integrantes2 = Label(ventana, text="Brayan Urquijo", font=("ITALIC", 17))
integrantes2.config(bg="White", fg="Black")
integrantes2.place(x=800, y=550)

integrantes3 = Label(ventana, text="Jhoan Fabricio H", font=("ITALIC", 17))
integrantes3.config(bg="White", fg="Black")
integrantes3.place(x=790, y=600)

# Boton para cerrar
def cerrar():
    ventana.destroy()

boton_cerrar = Button(ventana, text="Cerrar", font=("ITALIC", 20), command=cerrar)
boton_cerrar.config(bg="Red", fg="White", border="5", relief="groove")
boton_cerrar.place(x=825, y=635)

# Entry para la palabra
palabra_resultado = Entry(ventana, font=("ITALIC", 20))
palabra_resultado.config(width=30, border=5, relief="groove", bg="Red", fg="White")
palabra_resultado.config(justify="center")
palabra_resultado.place(x=10, y=480)

boton_validar = Button(ventana, text="Validar", font=("ITALIC", 20), command=validar_palabra)
boton_validar.config(width=5, bg="Red", fg="White", border=5, relief="groove")
boton_validar.place(x=500, y=470)

# Entry para la letra
letra_resultado = Label(ventana, text="Introduce una Letra",font=("ITALIC", 20))
letra_resultado.config(width=20, border=5, relief="groove")
letra_resultado.config(bg="Red", fg="White")
letra_resultado.place(x=10, y=430)

letra = Entry(ventana, width=2, font=("ITALIC", 20))
letra.config(justify="center")
letra.config(border=5, relief="groove", bg="White", fg="Black")
letra.place(x=350, y=430)

probrar_letra = Button(ventana, text="Probar", font=("ITALIC", 12), command=probarLetraFuncion)
probrar_letra.config(width=5, bg="Red", fg="White", border=3, relief="groove")
probrar_letra.place(x=400, y=434)

# Se mantiene la ventana abierta
ventana.mainloop()