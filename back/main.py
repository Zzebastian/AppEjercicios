import sqlite3, os

text=[]
text.append('''CREATE TABLE IF NOT EXISTS grupoMuscular (
            idGrupoM PRIMARY KEY,
            grupoM
            )''')
text.append('''CREATE TABLE IF NOT EXISTS entrenamientos (
            idEntrenamiento INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreEntrenamiento,
            Repeticiones,
            IncrementoPeso,
            idGrupoM,
            FOREIGN KEY (idGrupoM) REFERENCES grupoMuscular (idGrupoM)
            )''')
text.append('''CREATE TABLE IF NOT EXISTS nombreRutinas (
            idRutina PRIMARY KEY,
            nombreRutina
            )''')
text.append('''CREATE TABLE IF NOT EXISTS rutinas (
            idRutina,
            idEjercicio,
            PRiMARY KEY (idRutina, idEjercicio)
            )''')
text.append('''CREATE TABLE IF NOT EXISTS diario (
            idDia,
            idRutina1,
            idRutina2,
            FOREIGN KEY (idRutina1) REFERENCES rutinas (idRutina)
            )''')

    
class Inicializacion:
    def __init__(self,text):
        self.dir = os.path.dirname(os.path.relpath(__file__))
        self.conexion = sqlite3.connect(f'{self.dir}/ENTRENAMIENTO.sqlite')
        self.cursor = self.conexion.cursor()
        self.text = text
        for elemento in self.text:
            self.cursor.execute(elemento)
        self.conexion.commit()        

    def cerrarConexion(self):
        self.conexion.close()

inicio = Inicializacion(text)