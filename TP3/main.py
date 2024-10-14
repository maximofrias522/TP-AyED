import random
from datos import *
from interfaz import *
from menuEstudiante import menuEstudiante
from menuModerador import menuModerador
from menuAdmin import menuAdmin
from maskpass import askpass
from common import *
from rich.console import Console

console = Console()











# INICIO DE SESIÓN __________________________________________________________________________________________________________


def estaDisponibleIniciarSesion():
    MIN_ESTUDIANTES = 4
    MIN_MODERADORES = 1
    MIN_ADMINISTRADORES = 1
    if obtenerCantUsuario(estudiantesDbFisica, estudiantesDbLogica) < MIN_ESTUDIANTES:
        return False
    if obtenerCantUsuario(moderadoresDbFisica, moderadoresDbLogica) < MIN_MODERADORES:
        return False
    if obtenerCantUsuario(administradoresDbFisica, administradoresDbLogica) < MIN_ADMINISTRADORES:
        return False
    return True



def validarContrasena(usuario):
    intentos = 3

    while intentos > 0:
        contrasena = askpass(prompt='Introduzca la contraseña: ').ljust(50)
        if usuario.contrasena == contrasena:
            return True
        else:
            intentos -= 1
            if intentos > 0:
                console.print('Contraseña incorrecta, intente nuevamente.', style='red')

    if intentos == 0:
        return False



def validarInicioSesion():
    email = input('Introduzca su email: ').ljust(50)
    usuario = obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, email)
    if usuario == -1:
        usuario = obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, email)
    if usuario == -1:
        usuario = obtenerUsuario(administradoresDbFisica, administradoresDbLogica, email)
    
    while usuario == -1:
        console.print('Usuario no encontrado, intente nuevamente: ', style='red')
        email = input('Introduzca su email: ').ljust(50)
        usuario = obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, email)
        if usuario == -1:
            usuario = obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, email)
        if usuario == -1:
            usuario = obtenerUsuario(administradoresDbFisica, administradoresDbLogica, email)

    if validarContrasena(usuario):
        return usuario
    else:
        return -1

def cargarLikes():
    cantEstudiantes = obtenerCantUsuario(estudiantesDbFisica, estudiantesDbLogica)
    for idEmisor in range(cantEstudiantes):
        for idReceptor in range(cantEstudiantes):
            if idEmisor != idReceptor and random.random() <= 0.5: # 50% de probabilidad
                nuevoLike = Like()
                nuevoLike.idEmisor = idEmisor
                nuevoLike.idReceptor = idReceptor
                pickle.dump(nuevoLike, likesDbLogica)
                likesDbLogica.flush()

    
    

def iniciarSesion():
    if not estaDisponibleIniciarSesion():
        console.print('El inicio de sesión no está disponible.', style='red')
        continuar()
        return
    
    usuario = validarInicioSesion()
    if usuario == -1:
        console.print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.', style='red')
        continuar()
        return

    if os.path.getsize(likesDbFisica) == 0:
        cargarLikes()

    if isinstance(usuario, Estudiante):
        menuEstudiante(usuario)
    elif isinstance(usuario, Moderador):
        menuModerador(usuario)
    elif isinstance(usuario, Administrador):
        menuAdmin(usuario)

# FIN INICIO DE SESIÓN ______________________________________________________________________________________________________










# REGISTRO DE ESTUDIANTE ____________________________________________________________________________________________________
def generarEstudiante(): # retorna un Estudiante o -1 si ya está registrado
    nuevoEstudiante = Estudiante()
    nuevoEstudiante.email = input('Introduzca su email: ').ljust(50)
    if (obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoEstudiante.email) != -1 or
        obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, nuevoEstudiante.email) != -1 or
        obtenerUsuario(administradoresDbFisica, administradoresDbLogica, nuevoEstudiante.email) != -1):
        return -1
    
    estudiantesDbLogica.seek(0)
    while estudiantesDbLogica.tell() < os.path.getsize(estudiantesDbFisica): # obtiene el último usuario registrado
        ultimoEstudiante = pickle.load(estudiantesDbLogica)

    try:
        nuevoEstudiante.id = ultimoEstudiante.id + 1
    except:
        nuevoEstudiante.id = 0

    nuevoEstudiante.contrasena = input('Introduzca su contraseña: ').ljust(50)
    while nuevoEstudiante.contrasena == ''.ljust(50):
        console.print('La contraseña no puede estar vacía.', style='red')
        nuevoEstudiante.contrasena = input('Introduzca su contraseña: ').ljust(50)
    nuevoEstudiante.nombre = input('Introduzca su nombre: ').ljust(50)
    nuevoEstudiante.biografia = input('Introduzca su biografia: ').ljust(50)
    nuevoEstudiante.hobbies = input('Introduzca sus hobbies: ').ljust(50)
    nuevoEstudiante.fechaNacimiento = obtenerFecha()
    return nuevoEstudiante

def obtenerFecha(): 
    formato_correcto = False 
    while not formato_correcto: 
        fecha = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
        try:
            dtfecha = datetime.strptime(fecha, "%d/%m/%Y") 
            if dtfecha > datetime.today(): 
                console.print("La fecha introducida no es válida. Intente nuevamente.", style='red') 
            else:
                formato_correcto = True

        except ValueError as ve:
            if "does not match format" in str(ve):
                console.print("El formato de fecha ingresado es incorrecto. Intente nuevamente.", style='red') 
            else:
                console.print("Fecha fuera de rango. Intente nuevamente.", style='red') 

    return dtfecha


def registrarEstudiante():
    nuevoEstudiante = generarEstudiante()
    if nuevoEstudiante == -1:
        console.print('El estudiante ya se encuentra registrado.', style='green')
        continuar()
        return
    
    estudiantesDbLogica.seek(0, os.SEEK_END)
    pickle.dump(nuevoEstudiante, estudiantesDbLogica)
    estudiantesDbLogica.flush()

    print('El estudiante se registró exitosamente.')
    continuar()
# FIN REGISTRO DE ESTUDIANTE ________________________________________________________________________________________________






def menuInicial():
    mostrarMenuInicial()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            iniciarSesion()
        elif opcion == '2':
            registrarEstudiante()
        else:
            opcionInvalida()
        

        mostrarMenuInicial()
        opcion = input('Seleccione una opción: ')

    estudiantesDbLogica.close()
    moderadoresDbLogica.close()
    administradoresDbLogica.close()


if os.path.getsize(administradoresDbFisica) == 0:
    admin = Administrador()
    admin.email = 'admin@ayed.com'.ljust(50)
    admin.contrasena = 'admin'.ljust(50)
    admin.nombre = 'Administrador'.ljust(50)
    administradoresDbLogica.seek(0, os.SEEK_END)
    pickle.dump(admin, administradoresDbLogica)
    administradoresDbLogica.flush()

if os.path.getsize(moderadoresDbFisica) == 0:
    admin = Moderador()
    admin.email = 'mod@ayed.com'.ljust(50)
    admin.contrasena = 'mod'.ljust(50)
    admin.nombre = 'Moderador'.ljust(50)
    moderadoresDbLogica.seek(0, os.SEEK_END)
    pickle.dump(admin, moderadoresDbLogica)
    administradoresDbLogica.flush()

menuInicial()