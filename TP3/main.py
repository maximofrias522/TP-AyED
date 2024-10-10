import sys
from datos import *
from interfaz import *
from menuEstudiante import menuEstudiante
from maskpass import askpass
from common import *













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
                print('Contraseña incorrecta, intente nuevamente.')

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
        print('Usuario no encontrado, intente nuevamente: ')
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
        print('El inicio de sesión no está disponible.')
        continuar()
        return
    
    usuario = validarInicioSesion()
    if usuario == -1:
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
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
        print('El estudiante ya se encuentra registrado.')
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