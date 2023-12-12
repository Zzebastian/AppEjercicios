import sqlite3, os
from diccionario import *

class Conexion:
    def __init__(self):
        self.dir = os.path.dirname(os.path.relpath(__file__))
        self.conexion = sqlite3.connect(f'{self.dir}/ENTRENAMIENTO.sqlite')
        self.cursor = self.conexion.cursor()
        self.accion = False

    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        print('conexión cerrada')

    def ejecutar(self):
        if self.accion:
            self.cursor.execute(self.accion)
            self.conexion.commit()
        else:
            pass

    def imprimir(self):
        if self.accion:
            print(self.accion)
        else:
            pass

class Inicializacion(Conexion):
    def __init__(self,text):
        super().__init__()
        # Le traigo los argumentos del padre
        self.text = text
        for elemento in self.text:
            self.cursor.execute(elemento)
        self.conexion.commit()
   
class MostrarElementos(Conexion):
    def __init__(self,seleccion=False,tabla=False,where=False,orden=False,limit=False):
        super().__init__()
        self.tabla = tabla
        self.seleccion = seleccion
        self.where = where
        self.orden = orden
        self.limit = limit
        self.accion = "SELECT %s FROM %s" % (self.seleccion, self.tabla)
        
        if self.where:
            self.accion += " WHERE %s" % (self.where)
            
        if self.orden:
            self.accion += " ORDER BY %s" % (self.orden)
            
        if self.limit:
            self.accion += " LIMIT %s" % (self.limit)
            
    def verDatos(self):
        self.cursor.execute(self.accion)
        self.conexion.commit()
        resultados = self.cursor.fetchall()
        return resultados

class AgregarElementos(Conexion):
    def __init__(self,tabla,columnas,valores):
        super().__init__()
        self.tabla = tabla
        self.columnas = columnas
        self.valores = valores
        self.accion = "INSERT INTO %s (%s) VALUES (%s)" % (self.tabla, self.columnas, self.valores,)

class ModificarElementos(AgregarElementos):
    def __init__(self, tabla, columnas, valores, llave, id):
        super().__init__(tabla, columnas, valores)
        self.llave = llave
        self.id = id
        self.accion = "UPDATE %s SET (%s) = %s WHERE %s = %s" % (self.tabla, self.columnas, self.valores, self.llave, self.id)

class EliminarElementos(Conexion):
    def __init__(self,tabla, llave, id):
        super().__init__()
        self.tabla = tabla
        self.llave = llave
        self.id = id
        self.accion = "DELETE FORM %s WHERE %s = %s" % (self.tabla, self.llave, self.id)

class CRUD(MostrarElementos) :
    def __init__(self,accion):
        super().__init__()
        self.accion = accion

def imprimirElementos(tabla):
    for elemento in tabla:
        print(elemento)

def otro():
    pass
print("\033[32m","#"*20,"\033[0m")
inicio = Inicializacion(text)
data = MostrarElementos("*","ejercicios",False,"nombreEjercicio DESC",4)
data.imprimir()
data.ejecutar()
data.verDatos()
imprimirElementos(data.verDatos())
agregar = AgregarElementos("plan", "dia, idRutina, idEjercicio, repeticiones, peso","6, 1, 1, '12-10-8-6', 20")
agregar.imprimir()
agregar.ejecutar()
modificar = ModificarElementos("plan","peso",10, "(dia, idRutina, idEjercicio)", "(6, 1, 1)")
modificar.ejecutar()
modificar.imprimir()
data = MostrarElementos("*", "plan",False, "dia DESC", 5)
data.verDatos()

data.imprimir()
eliminar = EliminarElementos("plan", "(dia, idRutina, idEjercicio)", "(6, 1, 1)")


form ={}
form["dia"] = 1
subC  = {}
subC["ejercicio"] = ", (SELECT nombreEjercicio FROM ejercicios WHERE plan.idEjercicio = ejercicios.idEjercicio)"
subC["grupoMuscular"] = ""#", (SELECT grupoM FROM grupoMuscular WHERE ejercicios.idGrupoM = grupoMuscular.idGrupoM)"
subC["grupo"] =", (SELECT idGrupoM%s FROM ejercicios WHERE plan.idEjercicio = ejercicios.idEjercicio)" % (subC["grupoMuscular"])
texto ="""SELECT *%s%s FROM plan WHERE dia =%s""" % (subC["ejercicio"], subC["grupo"], form["dia"])
print(texto)

"""
SELECT *, 
(SELECT nombreEjercicio FROM ejercicios WHERE plan.idEjercicio = ejercicios.idEjercicio) as NombreEj, 
(SELECT idGrupoM FROM ejercicios WHERE plan.idEjercicio = ejercicios.idEjercicio) as idGrupo
FROM plan WHERE dia =1
"""
"""
SELECT idGrupoM,
(SELECT grupoM FROM grupomuscular WHERE grupomuscular.idGrupoM = ejercicios.idGrupoM)
FROM ejercicios
"""


# accion = CRUD(texto)
# accion.ejecutar()
# accion.imprimir()
# imprimirElementos(accion.verDatos())