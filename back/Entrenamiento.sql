DROP DATABASE IF EXISTS `Entrenamiento`;
    CREATE DATABASE Entrenamiento;
    USE Entrenamiento;
DROP TABLE IF EXISTS plan;
DROP TABLE IF EXISTS rutinas;
DROP TABLE IF EXISTS ejercicios;
DROP TABLE IF EXISTS grupoMuscular;
CREATE TABLE grupoMuscular (
            idGrupoM INTEGER PRIMARY KEY AUTO_INCREMENT,
            grupoM VARCHAR(20)
            );
CREATE TABLE ejercicios (
            idEjercicio INTEGER PRIMARY KEY AUTO_INCREMENT,
            nombreEjercicio VARCHAR(20), 
            idGrupoM INTEGER,
            FOREIGN KEY (idGrupoM) REFERENCES grupoMuscular (idGrupoM)
            );
CREATE TABLE rutinas (
            idRutina INTEGER PRIMARY KEY AUTO_INCREMENT,
            nombreRutina VARCHAR(20)
            );
CREATE TABLE plan (
            dia INTEGER,
            idRutina INTEGER,
            idEjercicio INTEGER,
            repeticiones INTEGER,
            peso INTEGER,
            PRiMARY KEY (dia, idRutina, idEjercicio)
            );
INSERT INTO grupoMuscular (grupoM) VALUES ("Pecho");
INSERT INTO grupoMuscular (grupoM) VALUES ("Espalda");
INSERT INTO grupoMuscular (grupoM) VALUES ("Hombros");
INSERT INTO grupoMuscular (grupoM) VALUES ("Biceps");
INSERT INTO grupoMuscular (grupoM) VALUES ("Triceps");
INSERT INTO grupoMuscular (grupoM) VALUES ("Piernas");
INSERT INTO grupoMuscular (grupoM) VALUES ("Abdominales");
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press Banca Plano', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press Banca Inclinado', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Aperturas Planas', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Scot con barra W', 4);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Martillo', 4);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Concentrado', 4);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Despegue', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Buen día', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Gemelos', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Laterales', 3);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Frontales', 3);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Posteriores', 3);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Jalón a la Nuca', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Remo con Barra', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Remo 1 Brazo', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Polea con soga', 5);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press Frances', 5);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Fondos paralelos', 5);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Silla', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Camilla', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Prensa', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Sentadilla', 6);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Que me importa', 3);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press Nuca', 3);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Aperturas Inclinadas', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press banca Declinado', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Press C/M Inclinado', 1);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Jalón al Pecho', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Remo al Pecho', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Remo 90°', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Pullover', 2);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Curl con mancuernas', 4);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('De pie con barra', 4);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Encogimientos invertidos', 7);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Encogimientos', 7);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Encogimientos oblicuos', 7);
INSERT INTO ejercicios (nombreEjercicio, idGrupoM) VALUES ('Elevaciones piernas', 7);
INSERT INTO rutinas (nombreRutina) VALUES ("Pecho-Biceps");
INSERT INTO rutinas (nombreRutina) VALUES ("Piernas-Hombros");
INSERT INTO rutinas (nombreRutina) VALUES ("Espalda-Triceps");
INSERT INTO rutinas (nombreRutina) VALUES ("Piernas-Hombros2");
INSERT INTO rutinas (nombreRutina) VALUES ("Abdominales");
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 1, '12-10-8-6', 20);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 2, '10-8-6-4', 20);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 3, '3x8', 10);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 4, '12-10-8-6', 10);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 5, '3x8', 8.5);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (1, 1, 6, '10-8-6-4', 8.5);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 7, '10-8-6-0', 30);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 8, '10-8-6-0', 20);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 9, '3x8', 60);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 10, '4x10*', 3);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 11, '4x10*', 3);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (2, 2, 12, '4x10*', 3);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 13, '12-10-8-6', 30);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 14, '10-8-6-4', 20);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 15, '10-8-6-4', 14);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 16, '10-8-6-4', 10);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 17, '3x10', 10);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (3, 3, 18, '10-10-8-0', 0);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 19, '12-10-8-6', 15);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 20, '12-10-8-6', 15);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 21, '12-10-8-6', 30);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 22, '12-10-8-6', 20);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 23, '3x8', 30);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (4, 4, 24, '12-10-8-6', 10);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (5, 5, 34, '3x20', 0);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (5, 6, 35, '3x21', 0);
INSERT INTO plan (dia, idRutina, idEjercicio, repeticiones, peso) VALUES (5, 7, 36, '3x22', 0);
