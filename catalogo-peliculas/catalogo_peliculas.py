import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    # root.iconbitmap(
    #     '/home/zeta/Escritorio/proyectos/tkinter/catalogo-peliculas/img/linux_logo_icon_168243 (2).ico')
    root.resizable(0, 0)

    barra_menu(root)

    app = Frame(root=root)
    app.mainloop()


if __name__ == '__main__':
    main()
