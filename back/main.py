import sqlite3

import os

text = os.path.dirname(os.path.relpath(__file__))


conexion = sqlite3.connect(f'{text}/ENTRENAMIENTO.sqlite')
cursor = conexion.cursor()
text = []
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

for elemento in text:
    cursor.execute(elemento)
    print('hecho')




conexion.commit()
conexion.close()