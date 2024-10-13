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

class Like:
    def __init__(self):
        self.idEmisor = 0
        self.idReceptor = 0
        self.estado = True

class Reporte:
    def __init__(self, idEmisor=0, idReceptor=0, motivo="", estado=0, idMod=0):
        self.idEmisor = idEmisor
        self.idReceptor = idReceptor
        self.motivo = motivo.ljust(50)  
        self.estado = estado
        self.idMod = idMod


def abrirDbLogica(dbFisica):
    if os.path.exists(dbFisica):
        return open(dbFisica, 'r+b')
    else:
        return open(dbFisica, 'w+b')

estudiantesDbFisica = './databases/estudiantes.dat'
estudiantesDbLogica = abrirDbLogica(estudiantesDbFisica)

moderadoresDbFisica = './databases/moderadores.dat'
moderadoresDbLogica = abrirDbLogica(moderadoresDbFisica)

administradoresDbFisica = './databases/administradores.dat'
administradoresDbLogica = abrirDbLogica(administradoresDbFisica)

likesDbFisica = './databases/likes.dat'
likesDbLogica = abrirDbLogica(likesDbFisica)

reportesDbFisica = './databases/reportes.dat'
reportesDbLogica = abrirDbLogica(reportesDbFisica)