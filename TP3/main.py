import sys
from datos import *
from interfaz import *
from menuEstudiante import menuEstudiante
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

    if isinstance(usuario, Estudiante):
        menuEstudiante(usuario)
    """ elif usuario is Moderador:
        menuModerador()
    elif usuario is Administrador:
        menuAdministrador() """

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
    return nuevoEstudiante



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


def generarModder():
    enConstruccion()
    nuevoModder = Moderador()
    nuevoModder.email = input('Introduzca su email: ').ljust(50)
    if (obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoModder.email) != -1 or
        obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, nuevoModder.email) != -1 or
        obtenerUsuario(administradoresDbFisica, administradoresDbLogica, nuevoModder.email) != -1):
        return -1
    
    moderadoresDbLogica.seek(0)
    while moderadoresDbLogica.tell() < os.path.getsize(moderadoresDbFisica): # obtiene el último usuario registrado
        ultimoModder = pickle.load(moderadoresDbLogica)

    try:
        nuevoModder.id = ultimoModder.id + 1
    except:
        nuevoModder.id = 0

    nuevoModder.contrasena = input('Introduzca su contraseña: ').ljust(50)
    while nuevoModder.contrasena == ''.ljust(50):
        console.print('La contraseña no puede estar vacía.', style='red')
        nuevoModder.contrasena = input('Introduzca su contraseña: ').ljust(50)
    nuevoModder.nombre = input('Introduzca su nombre: ').ljust(50)
    return nuevoModder

def registrarModder():
    enConstruccion()
    nuevoModder = generarModder()
    if nuevoModder == -1:
        console.print('El moderador ya se encuentra registrado.', style='green')
        continuar()
        return

    moderadoresDbLogica.seek(0, os.SEEK_END)
    pickle.dump(nuevoModder, moderadoresDbLogica)
    moderadoresDbLogica.flush()

    print('El moderador se registró exitosamente. Para iniciar sesion debe esperar a que un admin lo valide.')
    continuar()





def menuInicial():
    mostrarMenuInicial()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            iniciarSesion()
        elif opcion == '2':
            des = input('Desea registrarse como estudiante o moderador? (E/M): ').lower()
            if des == 'e':
                registrarEstudiante()
            elif des == 'm':
                registrarModder()
            else:
                opcionInvalida()
        else:
            opcionInvalida()
        

        mostrarMenuInicial()
        opcion = input('Seleccione una opción: ')

    estudiantesDbLogica.close()
    moderadoresDbLogica.close()
    administradoresDbLogica.close()

admin = Administrador()
admin.email = 'e'.ljust(50)
admin.contrasena = 'e'.ljust(50)
admin.nombre = 'e'.ljust(50)
administradoresDbLogica.seek(0, os.SEEK_END)
pickle.dump(admin, administradoresDbLogica)
administradoresDbLogica.flush()

admin = Moderador()
admin.email = 'f'.ljust(50)
admin.contrasena = 'f'.ljust(50)
admin.nombre = 'f'.ljust(50)
moderadoresDbLogica.seek(0, os.SEEK_END)
pickle.dump(admin, moderadoresDbLogica)
administradoresDbLogica.flush()

menuInicial()