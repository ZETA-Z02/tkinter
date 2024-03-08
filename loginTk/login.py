import tkinter as tk

# Colores
fondo_entrar = "#004AAD"
fondo_salir = "#FF1616"
fondo_correcto = "#8C52FF"
fondo_incorrecto = "#FF5757"
fondo_entrada = "#D9D9D9"

ventana = tk.Tk()

ventana.title("Login")
ventana.geometry("500x500+500+50")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="./Entrar.png")
fondo1 = tk.Label(ventana, image=fondo).place(
    x=0, y=0, relwidth=1, relheight=1)

# Usuario and Password
usuario = tk.StringVar()
password = tk.StringVar()

# Entradas de texto
entrada = tk.Entry(ventana, textvar=usuario, width=22, relief="flat",
                   bg=fondo_entrada)
entrada.place(x=255, y=244)
entrada2 = tk.Entry(ventana, textvar=password, show="*", width=22, relief="flat",
                    bg=fondo_entrada)
entrada2.place(x=255, y=300)
# Funciones


def login():
    nombre = usuario.get()
    contrasena = password.get()
    if nombre == "zeta" and contrasena == "zeta123":
        correcta()
    else:
        incorrecta()


def correcta():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("Bienvenido")
    window.geometry("500x500+500+50")
    window.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="./correcto.png")
    fondo1 = tk.Label(window, image=fondo).place(
        x=0, y=0, relwidth=1, relheight=1)

    def regresar():
        window.withdraw()
        ventana.deiconify()
    # Boton
    boton3 = tk.Button(window, text="Regresar", command=regresar,
                       cursor="hand2", width=13, relief="flat", bg=fondo_correcto, font=("Comic Sans MS", 12, "bold"))
    boton3.place(x=180, y=400)
    window.mainloop()


def incorrecta():
    ventana.withdraw()
    root = tk.Toplevel()
    root.title("Error")
    root.geometry("500x500+500+50")
    root.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="./incorrecto.png")
    fondo1 = tk.Label(root, image=fondo).place(
        x=0, y=0, relwidth=1, relheight=1)

    def regresar():
        root.withdraw()
        ventana.deiconify()
    # boton
    boton4 = tk.Button(root, text="Intentar de nuevo", command=regresar, cursor="hand2",
                       width=19, relief="flat", bg=fondo_incorrecto, font=("Comic Sans MS", 12, "bold"))
    boton4.place(x=148, y=400)
    root.mainloop()


def salir():
    ventana.destroy()


# Botones
boton = tk.Button(ventana, text="Entrar", command=login, cursor="hand2", bg=fondo_entrar,
                  width=12, relief="flat", font=('Comic Sans MS', 12, "bold"))
boton1 = tk.Button(ventana, text="Salir", command=salir, cursor="hand2", bg=fondo_salir,
                   width=12, relief="flat", font=('Comic Sans MS', 12, "bold"))
boton.place(x=60, y=405)
boton1.place(x=310, y=405)


ventana.mainloop()
