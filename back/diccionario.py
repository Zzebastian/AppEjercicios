text = []

# Todo elemento que se ingrese, DEBE ser al final, para evitar problemas en carga de datos.

tablas = ("plan", "rutinas",
          "ejercicios", "grupoMuscular")
for elemento in tablas:
    text.append(f'''DROP TABLE IF EXISTS {elemento}''')

text.append('''CREATE TABLE grupoMuscular (
            idGrupoM INTEGER PRIMARY KEY AUTOINCREMENT,
            grupoM VARCHAR(20)
            )''')
text.append('''CREATE TABLE ejercicios (
            idEjercicio INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreEjercicio VARCHAR(20), 
            idGrupoM INTEGER,
            FOREIGN KEY (idGrupoM) REFERENCES grupoMuscular (idGrupoM)
            )''')
text.append('''CREATE TABLE rutinas (
            idRutina INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreRutina VARCHAR(20)
            )''')
text.append('''CREATE TABLE plan (
            dia INTEGER,
            idRutina INTEGER,
            idEjercicio INTEGER,
            repeticiones INTEGER,
            peso INTEGER,
            PRiMARY KEY (dia, idRutina, idEjercicio)
            )''')

grupos = ("Pecho", "Espalda", "Hombros", "Biceps",
          "Triceps", "Piernas", "Abdominales")
for elemento in grupos:
    text.append(
        f'''INSERT INTO grupoMuscular (grupoM) VALUES ("{elemento}")''')

ejercicios = (('Press Banca Plano', 1),
                  ('Press Banca Inclinado', 1),
                  ('Aperturas Planas', 1),
                  ('Scot con barra W', 4),
                  ('Martillo', 4),
                  ('Concentrado', 4),
                  ('Despegue', 6),
                  ('Buen día', 6),
                  ('Gemelos', 6),
                  ('Laterales', 3),
                  ('Frontales', 3),
                  ('Posteriores', 3),
                  ('Jalón a la Nuca', 2),
                  ('Remo con Barra', 2),
                  ('Remo 1 Brazo', 2),
                  ('Polea con soga', 5),
                  ('Press Frances', 5),
                  ('Fondos paralelos', 5),
                  ('Silla', 6),
                  ('Camilla', 6),
                  ('Prensa', 6),
                  ('Sentadilla', 6),
                  ('Que me importa', 3),
                  ('Press Nuca', 3),
                  ('Aperturas Inclinadas', 1),
                  ('Press banca Declinado', 1),
                  ('Press C/M Inclinado', 1),
                  ('Jalón al Pecho', 2),
                  ('Remo al Pecho', 2),
                  ('Remo 90°', 2),
                  ('Pullover', 2),
                  ('Curl con mancuernas', 4),
                  ('De pie con barra', 4),
                  ('Encogimientos invertidos', 7),
                  ('Encogimientos', 7),
                  ('Encogimientos oblicuos', 7),
                  ('Elevaciones piernas', 7),
                  )
for elemento in ejercicios:
    text.append(
        f'''INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES {elemento}''')

rutinas = (('Pecho-Biceps'),
           ('Piernas-Hombros'),
           ('Espalda-Triceps'),
           ('Piernas-Hombros2'),
           ('Abdominales'),
           )
for elemento in rutinas:
    text.append(f'''INSERT INTO rutinas (nombreRutina) VALUES ("{elemento}")''')

plan = ((1, 1, 1, '12-10-8-6', 20),
        (1, 1, 2, '10-8-6-4', 20),
        (1, 1, 3, '3x8', 10),
        (1, 1, 4, '12-10-8-6', 10),
        (1, 1, 5, '3x8', 8.5),
        (1, 1, 6, '10-8-6-4', 8.5),
        (2, 2, 7, '10-8-6-0', 30),
        (2, 2, 8, '10-8-6-0', 20),
        (2, 2, 9, '3x8', 60),
        (2, 2, 10, '4x10*', 3),
        (2, 2, 11, '4x10*', 3),
        (2, 2, 12, '4x10*', 3),
        (3, 3, 13, '12-10-8-6', 30),
        (3, 3, 14, '10-8-6-4', 20),
        (3, 3, 15, '10-8-6-4', 14),
        (3, 3, 16, '10-8-6-4', 10),
        (3, 3, 17, '3x10', 10),
        (3, 3, 18, '10-10-8-0', 0),
        (4, 4, 19, '12-10-8-6', 15),
        (4, 4, 20, '12-10-8-6', 15),
        (4, 4, 21, '12-10-8-6', 30),
        (4, 4, 22, '12-10-8-6', 20),
        (4, 4, 23, '3x8', 30),
        (4, 4, 24, '12-10-8-6', 10),
        (5, 5, 34, '3x20', 0),
        (5, 6, 35, '3x21', 0),
        (5, 7, 36, '3x22', 0),
        )
for elemento in plan:
    text.append(
        f'''INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES {elemento}''')

import os
nombre = "Entrenamiento"
file = os.path.dirname(os.path.relpath(__file__))+"/"+nombre+".sql"
if not os.path.exists(file):
    inicializacion = f"""DROP DATABASE IF EXISTS `{nombre}`;
    CREATE DATABASE {nombre};
    USE {nombre};"""
    with open (file, "w") as archivo:
        archivo.write(f"{inicializacion}\n")
        for elemento in text:
            elemento = elemento.replace("AUTOINCREMENT","AUTO_INCREMENT")
            archivo.write(f"{elemento};\n")
        
        archivo.close()
