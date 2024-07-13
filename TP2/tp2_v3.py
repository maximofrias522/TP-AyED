from maskpass import askpass
from tp2_v2_aux import *


CANT_MAX_ESTUDIANTES = 8
CANT_MAX_MODERADORES = 4

# max 8 estudiantes con 6 datos asociados 
estudiantesLen = 0 # Cantidad de estudiantes ingresados
estudiantes = [[''] * 6 for _ in range(CANT_MAX_ESTUDIANTES)] # A lo sumo 8 usuarios con email, nombre, contraseña, fecha de nacimiento, biografía y hobbies como datos

# max 4 moderadores con 3 datos asociados 
moderadoresLen = 0 # cantidad de moderadores ingresados
moderadores = [[''] * 3 for _ in range(CANT_MAX_MODERADORES)] # A lo sumo 4 moderadores con email, nombre y contraseña como datos

# indices de estudiante y moderador iniciando en -1 para indicar que no hay nignuno activo
currentEstudiante = -1
currentModerador = -1


def buscarEstudiante(email):
    index = -1   # Inicializa el índice como -1 para indicar que no se ha encontrado el estudiante.
    for i in range(CANT_MAX_ESTUDIANTES):   # Itera a través de todos los posibles estudiantes.
        if estudiantes[i][0] == email:   # Comprueba si el correo electrónico del estudiante en la posición i es igual al email proporcionado.
            index = i   # Si encuentra el email, guarda el índice correspondiente.
    return index   # Devuelve el índice encontrado, o -1 si no se encuentra.


def buscarModerador(email):
    index = -1   # Inicializa el índice como -1 para indicar que no se ha encontrado el moderador.
    for i in range(CANT_MAX_MODERADORES):   # Itera a través de todos los posibles moderadores.
        if moderadores[i][0] == email:   # Comprueba si el correo electrónico del moderador en la posición i es igual al email proporcionado.
            index = i   # Si encuentra el email, guarda el índice correspondiente.
    return index   # Devuelve el índice encontrado, o -1 si no se encuentra.


def validarContrasenaEstudiante(index):
    global currentEstudiante   # Declara currentEstudiante como una variable global para poder modificarla
    intentos = 3   # Establece el número de intentos permitidos

    while intentos > 0:   # Mientras queden intentos
        contrasena = askpass(prompt='Introduzca la contraseña: ')   # Solicita la contraseña al usuario
        if estudiantes[index][2] == contrasena:   # Verifica si la contraseña ingresada coincide con la almacenada
            currentEstudiante = index   # Si la contraseña es correcta, actualiza currentEstudiante con el índice proporcionado
            return True   # Devuelve True indicando que la verificación fue exitosa
        else:
            intentos -= 1   # Si la contraseña es incorrecta, reduce el número de intentos en 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')   # Si quedan intentos, avisa al usuario que la contraseña es incorrecta

    if intentos == 0:   # Si se agotan los intentos
        return False   # Devuelve False indicando que la verificación falló
    

def validarContrasenaModerador(index):
    global currentModerador   # Declara currentModerador como una variable global para poder modificarla
    intentos = 3   # Establece el número de intentos permitidos

    while intentos > 0:   # Mientras queden intentos
        contrasena = askpass(prompt='Introduzca la contraseña: ')   # Solicita la contraseña al usuario
        if moderadores[index][1] == contrasena:   # Verifica si la contraseña ingresada coincide con la almacenada
            currentModerador = index   # Si la contraseña es correcta, actualiza currentModerador con el índice proporcionado
            return True   # Devuelve True indicando que la verificación fue exitosa
        else:
            intentos -= 1   # Si la contraseña es incorrecta, reduce el número de intentos en 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')   # Si quedan intentos, avisa al usuario que la contraseña es incorrecta

    if intentos == 0:   # Si se agotan los intentos
        return False   # Devuelve False indicando que la verificación falló

# Inicio de modularizacion (funcion original "IniciarSesion")
def solicitarEmail():
    # Solicita al usuario que introduzca su email y lo devuelve
    return input('Introduzca su email: ')

def buscarUsuario(email):
    # Busca si el email corresponde a un estudiante o a un moderador
    estudiante = buscarEstudiante(email)
    moderador = buscarModerador(email)
    return estudiante, moderador

def opcionUsuario(estudiante, moderador):
    # Si el email pertenece tanto a un estudiante como a un moderador,
    # permite al usuario elegir con qué rol iniciar sesión
    aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')
    # Verifica que la opción ingresada sea válida ('0' o '1')
    while aux not in ['0', '1']:
        opcionInvalida()  # Muestra mensaje de opción inválida
        aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')
    if aux == '1':
        estudiante = -1  # Si elige moderador, invalida la opción de estudiante
    return estudiante, moderador

def opcionInvalida():
    # Muestra un mensaje de opción inválida
    print('Opción inválida, intente nuevamente.')

def iniciarSesion():
    # Función principal para coordinar el flujo de inicio de sesión
    email = solicitarEmail()  # Solicita el email al usuario
    estudiante, moderador = buscarUsuario(email)  # Busca si el email corresponde a un estudiante o moderador

    # Mientras no se encuentre ni estudiante ni moderador, sigue solicitando el email
    while estudiante == -1 and moderador == -1:
        print('Usuario no encontrado, intente nuevamente.')
        email = solicitarEmail()  # Vuelve a solicitar el email
        estudiante, moderador = buscarUsuario(email)  # Busca nuevamente el email

    # Si se encuentra tanto un estudiante como un moderador, solicita elegir uno
    if estudiante != -1 and moderador != -1:
        estudiante, moderador = opcionUsuario(estudiante, moderador)

    # Si se eligió estudiante, valida la contraseña de estudiante
    if estudiante != -1:
        return validarContrasenaEstudiante(estudiante)
    else:
        # Si se eligió moderador, valida la contraseña de moderador
        return validarContrasenaModerador(moderador)
# Fin de modularizacion (funcion original "IniciarSesion")

def utnMatch():
    # Verifica si hay suficientes estudiantes y moderadores para iniciar sesión
    if estudiantesLen < 4 or moderadoresLen < 1:
        print('El inicio de sesión no está disponible.')
        continuar()  # Pausa o espera al usuario antes de continuar
        return  # Sale de la función si no se cumplen los requisitos

    # Intenta iniciar sesión
    sesion_iniciada = iniciarSesion()

    # Verifica si el inicio de sesión fue exitoso
    if not sesion_iniciada:
        # Si no se inició sesión exitosamente, informa al usuario y pausa/espera
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
        continuar()  # Pausa o espera al usuario antes de continuar

    else:
        # Si la sesión se inició correctamente, muestra el menú principal
        menuPrincipal()

