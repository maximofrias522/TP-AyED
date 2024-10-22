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
        self.superlike = True
        self.revelarCandidatos = True
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
    def __init__(self):
        self.idEmisor = 0
        self.idReceptor = 0
        self.motivo = "".ljust(100)
        self.estado = 0
        self.idMod = -1

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


# Crear un moderador y un administrador
def crear_moderador(moderador_db):
    moderador = Moderador()
    moderador.id = 1  # Asigna un ID único
    moderador.email = "moder@ayed.com".ljust(50)
    moderador.nombre = "Moderador".ljust(50)
    moderador.contrasena = "moder".ljust(50)
    moderador.estado = True

    # Guardar el moderador en la base de datos
    moderador_db.seek(0, os.SEEK_END)  # Ir al final del archivo
    pickle.dump(moderador, moderador_db)
    moderador_db.flush()  # Asegurarse de que los datos se guarden

def crear_administrador(administrador_db):
    administrador = Administrador()
    administrador.id = 1  # Asigna un ID único
    administrador.email = "admin@ayed.com".ljust(50)
    administrador.nombre = "Administrador".ljust(50)
    administrador.contrasena = "admin".ljust(50)
    administrador.estado = True

    # Guardar el administrador en la base de datos
    administrador_db.seek(0, os.SEEK_END)  # Ir al final del archivo
    pickle.dump(administrador, administrador_db)
    administrador_db.flush()  # Asegurarse de que los datos se guarden

crear_administrador(administradoresDbLogica)
crear_moderador(moderadoresDbLogica)