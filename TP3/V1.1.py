import pickle
from datetime import datetime

from interfaz import *

estudiantesDb = './estudiantes.dat'
if os.path.exists(estudiantesDb):
    estudiantesDbLogica = open(estudiantesDb, 'r+b')
    try:
        db = pickle.load(estudiantesDbLogica)  # Intentamos cargar el contenido
    except EOFError:
        # Si el archivo está vacío, inicializamos con una lista vacía
        db = []
        estudiantesDbLogica.seek(0)
        pickle.dump(db, estudiantesDbLogica)
        estudiantesDbLogica.seek(0)
else:
    # Si no existe, creamos el archivo y lo inicializamos con una lista vacía
    estudiantesDbLogica = open(estudiantesDb, 'w+b')
    db = []
    pickle.dump(db, estudiantesDbLogica)
    estudiantesDbLogica.seek(0)

class Estudiante:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.nombre = ""
        self.contrasena = ""
        self.sexo = ""
        self.hobbies = ""
        self.biografia = ""
        self.pais = ""
        self.ciudad = ""
        self.fechaNacimiento = datetime.strptime('01/01/1900', '%d/%m/%Y')
        self.materiaFavorita = ""
        self.deporteFavorito = ""
        self.materiaFuerte = ""
        self.materiaDebil = ""
        self.estado = True


def buscarEstudiante(email, db):
    for i in range(0, len(db)):
        if db[i].email == email:
            return i
        
    return -1


def generarEstudiante(id, email):
    nuevoEstudiante = Estudiante()

    nuevoEstudiante.id = id
    nuevoEstudiante.email = email
    return nuevoEstudiante


def registrarse():
    db = pickle.load(estudiantesDbLogica)
    estudiantesDbLogica.seek(0)
    email = input('Introduzca su email: ')
    if buscarEstudiante(email, db) != -1:
        print('El estudiante ya se encuentra registrado.')
        continuar()
        return
    
    nuevoEstudiante = generarEstudiante(len(db), email)
    
    pickle.dump(nuevoEstudiante, estudiantesDbLogica)
    estudiantesDbLogica.seek(0)

    print('El estudiante se registró exitosamente.')
    continuar()

def menuInicial():
    mostrarMenuInicial()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            # utnMatch()
            None
        elif opcion == '2':
            registrarse()
        else:
            opcionInvalida()
        

        mostrarMenuInicial()
        opcion = input('Seleccione una opción: ')

menuInicial()