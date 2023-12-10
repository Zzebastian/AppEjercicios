import sqlite3, os
from diccionario import *

class Conexion:
    def __init__(self):
        self.dir = os.path.dirname(os.path.relpath(__file__))
        self.conexion = sqlite3.connect(f'{self.dir}/ENTRENAMIENTO.sqlite')
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        print('conexión cerrada')

class Inicializacion(Conexion):
    def __init__(self,text):
        super().__init__()
        # Le traigo los argumentos del padre
        self.text = text
        for elemento in self.text:
            self.cursor.execute(elemento)
        self.conexion.commit()
            
        
class MostrarElementos(Conexion):
    def __init__(self,seleccion,tabla):
        super().__init__()
        self.tabla = tabla
        self.seleccion = seleccion

    def verDatos(self):
        self.cursor.execute("SELECT %s FROM %s" % (self. seleccion, self.tabla))
        self.conexion.commit()
        resultados = self.cursor.fetchall()
        return resultados
    
    def imprimir(self):
        print("SELECT %s FROM %s" % (self. seleccion, self.tabla))

class AgregarElementos(Conexion):
    def __init__(self,tabla,columnas,valores):
        super().__init__()
        self.tabla = tabla
        self.columnas = columnas
        self.valores = valores
    
    def cargaDatos(self):
        self.cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (self.tabla, self.columnas, self.valores,))
        self.conexion.commit()
        
    
    def imprimir(self):
        print("INSERT INTO %s (%s) VALUES (%s)" % (self.tabla, self.columnas, self.valores,))

def imprimirElementos(tabla):
    for elemento in tabla:
        print(elemento)

inicio = Inicializacion(text)
data = MostrarElementos("*","grupoMuscular")
data.verDatos()
imprimirElementos(data.verDatos())