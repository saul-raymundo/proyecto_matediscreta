
import tkinter as tk
from tkinter import messagebox
from pruebas import *
from PIL import Image, ImageTk
from urllib.request import urlopen, Request
from io import BytesIO

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Programa de Conjuntos")
ventana.geometry("850x500")
ventana.configure(bg="white")
ventana.resizable(False, False)

# Colores del programa
color_azul = "#079BC8"
color_gris = "#414141"
color_blanco = "#FFFFFF"

# Integrantes del proyecto
integrantes = [
    ("Saul", "https://github.com/saul-raymundo/proyecto_matediscreta/blob/main/imag4.jpeg?raw=true"),
    ("Robin", "https://github.com/saul-raymundo/proyecto_matediscreta/blob/main/imag2.jpeg?raw=true"),
    ("Amilcar", "https://github.com/saul-raymundo/proyecto_matediscreta/blob/main/imag1.jpeg?raw=true"),
    ("Cristian", "https://github.com/saul-raymundo/proyecto_matediscreta/blob/main/IMAGEN2.jpeg?raw=true")
]

imagenes = []

# Funcion para limpiar la pantalla
def limpiar():
    for elemento in ventana.winfo_children():
        if elemento != barra_menu:
            elemento.destroy()


# Funcion para mostrar el inicio
def inicio():
    limpiar()

    tk.Label(ventana, text="BIENVENIDOS",
             font=("Arial", 25, "bold"),
             bg="white", fg=color_azul).pack(pady=70)

    tk.Label(ventana, text="Programa de operaciones de conjuntos",
             font=("Arial", 16), bg="white").pack(pady=10)

    tk.Label(ventana, text="Seleccione una opción del menú para comenzar",
             font=("Arial", 12), bg="white").pack(pady=10)


# Funcion para realizar las operaciones
def operaciones(opcion):
    limpiar()

    if opcion == "union":
        titulo = "UNION DE CONJUNTOS"
    elif opcion == "interseccion":
        titulo = "INTERSECCION DE CONJUNTOS"
    elif opcion == "diferencia":
        titulo = "DIFERENCIA DE CONJUNTOS"
    else:
        titulo = "COMPLEMENTO DE CONJUNTOS"

    tk.Label(ventana, text=titulo, font=("Arial", 20, "bold"),
             bg="white", fg=color_azul).pack(pady=25)

    tk.Label(ventana, text="Ingrese los valores separados por comas",
             font=("Arial", 12), bg="white").pack(pady=10)

    tk.Label(ventana, text="Conjunto 1:",
             font=("Arial", 12), bg="white").pack()

    entrada1 = tk.Entry(ventana, font=("Arial", 13), width=40)
    entrada1.pack(pady=8)

    tk.Label(ventana, text="Conjunto 2:",
             font=("Arial", 12), bg="white").pack()

    entrada2 = tk.Entry(ventana, font=("Arial", 13), width=40)
    entrada2.pack(pady=8)

    resultado = tk.Label(ventana, text="",
                         font=("Arial", 15, "bold"),
                         bg="white", fg=color_azul)
    resultado.pack(pady=20)

    # Funcion para calcular el resultado
    def calcular():
        conjunto1 = entrada1.get()
        conjunto2 = entrada2.get()

        if conjunto1.strip() == "" or conjunto2.strip() == "":
            messagebox.showwarning(
                "Datos vacíos",
                "Por favor, ingrese los datos de ambos conjuntos."
            )
            return

        try:
            valores1 = conjunto1.split(",")
            valores2 = conjunto2.split(",")

            if any(valor.strip() == "" for valor in valores1 + valores2):
                messagebox.showwarning(
                    "Datos incorrectos",
                    "No deje espacios vacíos entre las comas."
                )
                return

            for valor in valores1 + valores2:
                int(valor.strip())

            operacion = opreac_conjunt(
                conjunto1, opcion, conjunto2
            )

            resultado.config(
                text="Resultado: " + str(operacion)
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese solamente números separados por comas.\n"
                "Ejemplo: 1, 2, 3, 4"
            )

    # Boton para ejecutar la operacion
    tk.Button(ventana, text="CALCULAR",
              font=("Arial", 11, "bold"),
              bg=color_azul, fg=color_blanco,
              activebackground=color_azul,
              activeforeground=color_blanco,
              relief="flat", command=calcular).pack(pady=10)


# Funcion para mostrar los integrantes
def sobre_nosotros():
    limpiar()
    imagenes.clear()

    tk.Label(ventana, text="SOBRE NOSOTROS",
             font=("Arial", 22, "bold"),
             bg="white", fg=color_azul).pack(pady=25)

    tk.Label(ventana, text="Integrantes del proyecto",
             font=("Arial", 14), bg="white").pack(pady=10)

    # Crear espacio para mostrar las fotografias
    marco = tk.Frame(ventana, bg="white")
    marco.pack(pady=15)

    # Mostrar los cuatro integrantes
    for i, integrante in enumerate(integrantes):
        tarjeta = tk.Frame(marco, bg="#F0F0F0",
                           width=180, height=230,
                           relief="ridge", bd=2)
        tarjeta.grid(row=0, column=i, padx=8)
        tarjeta.pack_propagate(False)

        tk.Label(tarjeta, text=integrante[0],
                 font=("Arial", 11, "bold"),
                 bg="#F0F0F0", fg=color_gris).pack(pady=12)

        try:
            # Cargar la fotografia desde el enlace
            peticion = Request(
                integrante[1],
                headers={'User-Agent': 'Mozilla/5.0'}
            )

            respuesta = urlopen(peticion, timeout=10).read()
            foto = Image.open(BytesIO(respuesta))
            foto.thumbnail((140, 150))

            imagen = ImageTk.PhotoImage(foto)
            imagenes.append(imagen)

            tk.Label(tarjeta, image=imagen,
                     bg="#F0F0F0").pack(pady=5)

        except Exception:
            tk.Label(tarjeta, text="Fotografia no disponible",
                     font=("Arial", 9), bg="#F0F0F0",
                     fg="red").pack(pady=40)

    tk.Label(ventana, text="Proyecto de Matemática Discreta",
             font=("Arial", 11, "italic"),
             bg="white").pack(pady=15)


# Crear barra de menu
barra_menu = tk.Frame(ventana, bg=color_azul, height=55)
barra_menu.pack(fill="x")
barra_menu.pack_propagate(False)

# Boton de inicio
tk.Button(barra_menu, text="INICIO",
          font=("Arial", 11, "bold"),
          bg=color_azul, fg=color_blanco,
          activebackground=color_azul,
          activeforeground=color_blanco,
          relief="flat", command=inicio).pack(
              side="left", padx=15, pady=8
          )

# Crear menu desplegable de conjuntos
menu_conjuntos = tk.Menubutton(
    barra_menu, text="CONJUNTOS ▼",
    font=("Arial", 11, "bold"),
    bg=color_azul, fg=color_blanco,
    activebackground=color_azul,
    activeforeground=color_blanco,
    relief="flat"
)
menu_conjuntos.pack(side="left", padx=15, pady=8)

opciones = tk.Menu(
    menu_conjuntos, tearoff=0,
    bg=color_gris, fg=color_blanco,
    activebackground=color_azul,
    activeforeground=color_blanco
)

opciones.add_command(label="Union",
                     command=lambda: operaciones("union"))
opciones.add_command(label="Interseccion",
                     command=lambda: operaciones("interseccion"))
opciones.add_command(label="Diferencia",
                     command=lambda: operaciones("diferencia"))
opciones.add_command(label="Complemento",
                     command=lambda: operaciones("complemento"))

menu_conjuntos.config(menu=opciones)

# Boton sobre nosotros
tk.Button(barra_menu, text="SOBRE NOSOTROS",
          font=("Arial", 11, "bold"),
          bg=color_azul, fg=color_blanco,
          activebackground=color_azul,
          activeforeground=color_blanco,
          relief="flat", command=sobre_nosotros).pack(
              side="left", padx=15, pady=8
          )

# Mostrar pantalla inicial
inicio()

# Ejecutar programa
ventana.mainloop()
