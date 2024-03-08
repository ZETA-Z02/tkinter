import sqlite3
import os


class ConexionDB:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_datos = os.path.join(script_dir, '../database/peliculas.db')
        # print(self.base_datos)
        # self.base_datos = './database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
