import tkinter as tk
import sqlite3


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda App")

        self.create_db_connection()
        self.create_table()

        self.create_widgets()

    def create_db_connection(self):
        self.conn = sqlite3.connect('agenda.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS contactos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            telefono TEXT NOT NULL)''')
        self.conn.commit()

    def create_widgets(self):
        self.label_nombre = tk.Label(self.root, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_telefono = tk.Label(self.root, text="Teléfono:")
        self.label_telefono.grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefono = tk.Entry(self.root)
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)

        self.button_agregar = tk.Button(
            self.root, text="Agregar contacto", command=self.agregar_contacto)
        self.button_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_contactos = tk.Listbox(self.root)
        self.listbox_contactos.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5)
        self.show_contacts()

    def agregar_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        self.cur.execute(
            "INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
        self.conn.commit()
        self.show_contacts()
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

    def show_contacts(self):
        self.listbox_contactos.delete(0, tk.END)
        self.cur.execute("SELECT * FROM contactos")
        rows = self.cur.fetchall()
        for row in rows:
            self.listbox_contactos.insert(
                tk.END, f"{row[0]} - {row[1]} - {row[2]}")


root = tk.Tk()
app = AgendaApp(root)
root.mainloop()
