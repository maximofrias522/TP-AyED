import os
import pickle
from datetime import datetime

class Estudiante:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.nombre = ""
        self.contrasena = ""
        self.sexo = ""
        self.hobbies = ""
        self.biografia = ""
        self.fechaNacimiento = datetime.strptime('01/01/1900', '%d/%m/%Y')
        self.estado = True

class Moderador:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.nombre = ""
        self.contrasena = ""
        self.estado = True

class Administrador:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.nombre = ""
        self.contrasena = ""
        self.estado = True

def abrirDbLogica(dbFisica, constructor):
    if os.path.exists(dbFisica):
        return open(dbFisica, 'r+b')
    else:
        dbLogica = open(dbFisica, 'w+b')
        aux = constructor()
        aux.id = -1
        aux.estado = False
        pickle.dump(aux, dbLogica) # se agrega un usuario vacío para evitar errores
        return dbLogica

estudiantesDbFisica = '/home/mfrias/tp3/databases/estudiantes.dat'
estudiantesDbLogica = abrirDbLogica(estudiantesDbFisica, Estudiante)

moderadoresDbFisica = '/home/mfrias/tp3/databases/moderadores.dat'
moderadoresDbLogica = abrirDbLogica(moderadoresDbFisica, Moderador)

administradoresDbFisica = '/home/mfrias/tp3/databases/administradores.dat'
administradoresDbLogica = abrirDbLogica(administradoresDbFisica, Administrador)
