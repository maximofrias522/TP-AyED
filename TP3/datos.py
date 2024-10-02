import os
import pickle
from datetime import datetime

class Estudiante:
    def __init__(self):
        self.id = 0
        self.email = "".ljust(50)
        self.nombre = "".ljust(50)
        self.contrasena = "".ljust(50)
        self.sexo = "".ljust(50)
        self.hobbies = "".ljust(50)
        self.biografia = "".ljust(50)
        self.fechaNacimiento = datetime.strptime('01/01/1900', '%d/%m/%Y')
        self.estado = True

class Moderador:
    def __init__(self):
        self.id = 0
        self.email = "".ljust(50)
        self.nombre = "".ljust(50)
        self.contrasena = "".ljust(50)
        self.estado = True

class Administrador:
    def __init__(self):
        self.id = 0
        self.email = "".ljust(50)
        self.nombre = "".ljust(50)
        self.contrasena = "".ljust(50)
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

estudiantesDbFisica = './tp3/databases/estudiantes.dat'
estudiantesDbLogica = abrirDbLogica(estudiantesDbFisica, Estudiante)

moderadoresDbFisica = './tp3/databases/moderadores.dat'
moderadoresDbLogica = abrirDbLogica(moderadoresDbFisica, Moderador)

administradoresDbFisica = './tp3/databases/administradores.dat'
administradoresDbLogica = abrirDbLogica(administradoresDbFisica, Administrador)