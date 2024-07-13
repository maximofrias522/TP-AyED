import os
from random import randint
from datetime import datetime
from maskpass import askpass

CANT_MAX_ESTUDIANTES = 8
CANT_MAX_MODERADORES = 4

estudiantesLen = 4
estudiantes = [[''] * 6 for _ in range(CANT_MAX_ESTUDIANTES)] # A lo sumo 8 estudiantes con email, nombre, contraseña, fecha de nacimiento, biografía y hobbies como datos

moderadoresLen = 1
moderadores = [[''] * 3 for _ in range(CANT_MAX_MODERADORES)] # A lo sumo 4 moderadores con email, nombre y contraseña como datos

currentEstudiante = -1
currentModerador = -1

asciiart = '''
 █████  ████████████████ ██████   █████    ██████   ██████           █████            █████     ███
░░███  ░░███░█░░░███░░░█░░██████ ░░███    ░░██████ ██████           ░░███            ░░███     ░███
 ░███   ░███░   ░███  ░  ░███░███ ░███     ░███░█████░███   ██████  ███████    ██████ ░███████ ░███
 ░███   ░███    ░███     ░███░░███░███     ░███░░███ ░███  ░░░░░███░░░███░    ███░░███░███░░███░███
 ░███   ░███    ░███     ░███ ░░██████     ░███ ░░░  ░███   ███████  ░███    ░███ ░░░ ░███ ░███░███
 ░███   ░███    ░███     ░███  ░░█████     ░███      ░███  ███░░███  ░███ ███░███  ███░███ ░███░░░ 
 ░░████████     █████    █████  ░░█████    █████     █████░░████████ ░░█████ ░░██████ ████ ████████
  ░░░░░░░░     ░░░░░    ░░░░░    ░░░░░    ░░░░░     ░░░░░  ░░░░░░░░   ░░░░░   ░░░░░░ ░░░░ ░░░░░░░░ 
'''

def buscarEstudiante(email):
    index = -1
    for i in range(CANT_MAX_ESTUDIANTES):
        if estudiantes[i][0] == email:
            index = i

    return index

def buscarModerador(email):
    index = -1
    for i in range(CANT_MAX_MODERADORES):
        if moderadores[i][0] == email:
            index = i

    return index

def validarContrasenaEstudiante(index):
    global currentEstudiante
    intentos = 3

    while intentos > 0:
        contrasena = askpass(prompt='Introduzca la contraseña: ')
        if estudiantes[index][2] == contrasena:
            currentEstudiante = index
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')

    if intentos == 0:
        return False

def validarContrasenaModerador(index):
    global currentModerador
    intentos = 3

    while intentos > 0:
        contrasena = askpass(prompt='Introduzca la contraseña: ')
        if moderadores[index][1] == contrasena:
            currentModerador = index
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')

    if intentos == 0:
        return False

def iniciarSesion(): # MODULARIZAR ESTA FUNCIÓN
    email = input('Introduzca su email: ')
    estudiante = buscarEstudiante(email)
    moderador = buscarModerador(email)

    while estudiante == -1 and moderador == -1:
        print('Estudiante no encontrado, intente nuevamente: ')
        email = input('Introduzca su email: ')
        estudiante = buscarEstudiante(email)
        if estudiante == -1:
            moderador = buscarModerador(email)

    if estudiante != -1 and moderador != -1:
        aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')
        while aux != 0 and aux != 1:
            opcionInvalida()
            aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')

        if aux == 1:
            estudiante = -1

    if estudiante != -1:
        return validarContrasenaEstudiante(estudiante)
    else:
        return validarContrasenaModerador(moderador)

def utnMatch():
    if estudiantesLen < 4 or moderadoresLen < 1:
        print('El inicio de sesión no está disponible.')
        continuar()
        return
    
    sesion_iniciada = iniciarSesion()
    if not sesion_iniciada: # Si no se inició sesión exitosamente imprime el error y finaliza el programa
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
        continuar()

    else:
        menuPrincipal()

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(asciiart)

def continuar():
    input("Presione enter para continuar...")

def opcionInvalida():
    print("Error: la opcion ingresada no es valida.")
    continuar()

def enConstruccion():
    limpiarPantalla()
    print("En construcción.")
    continuar()

def obtenerEdad(fecha):
    fecha = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fecha.year
    if (fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day): # Si el cumpleaños aún no sucedió le resta 1 a la diferencia de años
        edad -= 1
    return str(edad)

def imprimirDatosDeEstudiante(estudiante):
    print("Nombre: " + estudiantes[estudiante][1] + "\n" +
          "Fecha de nacimiento: " + estudiantes[estudiante][3] + "\n" +
          "Edad: " + obtenerEdad(estudiantes[estudiante][3]) + "\n" +
          "Biografía: " + estudiantes[estudiante][4] + "\n" +
          "Hobbies: " + estudiantes[estudiante][5])

def mostrarEditarDatosPersonales():
    limpiarPantalla()
    print("Estas editando tus datos personales")
    print("¿Qué datos deseas editar?")
    print("a. Fecha de nacimiento")
    print("b. Biografía")
    print("c. Hobbies")
    print("d. Volver")

def obtenerFecha():
    formato_correcto = False
    while not formato_correcto:
        fecha = input("Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ")
        try:
            dtfecha = datetime.strptime(fecha, "%d-%m-%Y")
            if dtfecha > datetime.today():
                print("La fecha introducida no es válida. Intente nuevamente.") # Si la fecha introducida es del futuro devuelve un mensaje de error
            else:
                formato_correcto = True

        except ValueError as ve:
            if "does not match format" in str(ve):
                print("El formato de fecha ingresado es incorrecto. Intente nuevamente.") # Si la fecha se introdujo en formato incorrecto devuelve un mensaje de error
            else:
                print("Fecha fuera de rango. Intente nuevamente.") # Si la fecha introducida está fuera de rango devuelve un mensaje de error

    return fecha

def editarFechaNacimiento():
    nueva_fecha = obtenerFecha()
    estudiantes[currentEstudiante][3] = nueva_fecha

    continuar()

def editarBiografia():
    nueva_biografia = input("Ingrese la nueva biografía: ")
    while nueva_biografia == '':
        print('La biografía no puede estar vacía.')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudiantes[currentEstudiante][4]
    print('Su nueva biografía es: ', nueva_biografia)

    continuar()

def editarHobbies():
    nuevo_hobbie = input("Ingrese los nuevos hobbies: ")
    while nuevo_hobbie == '':
        print('Los hobbies no pueden estar vacíos')
        nuevo_hobbie = input("Ingrese los nuevos hobbies: ")

    print("Sus nuevos hobbies son: ", nuevo_hobbie)

    continuar()

def editarDatosPersonales():
    mostrarEditarDatosPersonales()
    opcion = input("Seleccione una opción: ")

    while opcion != 'd':
        if opcion == 'a':
            editarFechaNacimiento()
        elif opcion == 'b':
            editarBiografia()
        elif opcion == 'c':
            editarHobbies()
        else:
            opcionInvalida()
        
        mostrarEditarDatosPersonales()
        opcion = input("Seleccione una opción: ")

def mostrarPerfil():
    limpiarPantalla()
    print("Estás viendo tu perfil")
    imprimirDatosDeEstudiante(currentEstudiante)

    continuar()

def eliminarPerfil():
    opcion = input('Presione 1 si está seguro de que desea eliminar su perfil o 0 para volver: ')
    while opcion != '0' and opcion != '1': 
        opcionInvalida()
        opcion = input('Presione 1 si está seguro de que desea eliminar su perfil o 0 para volver: ')

    if opcion == 0:
        for dato in estudiantes[currentEstudiante]:
            dato = []
        print('Sus datos han sido eliminados correctamente')

def mostrarGEestionarPerfil():
    limpiarPantalla()
    print("Estas gestionando tu perfil")
    print("a. Editar mis datos personales")
    print("b. Ver mi perfil")
    print("c. Eliminar mi perfil")
    print("d. Volver")

def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != 'd':
        if opcion == 'a':
            editarDatosPersonales()
        elif opcion == 'b':
            mostrarPerfil()  
        elif opcion == 'c':
            eliminarPerfil()
        else:
            opcionInvalida()

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

def mostrarGestionarCandidatos():
    limpiarPantalla()
    print("Gestionando candidatos")
    print("a. Ver candidatos disponibles")
    print("b. Contactar candidatos")
    print("c. Volver")

def gestionarCandidatos():
    mostrarGestionarCandidatos()
    opcion = input('Seleccione una opción: ')
    
    while opcion != 'c':
        if opcion == 'a':
            verCandidatos()
        elif opcion == 'b':
            enConstruccion()
        else:
            opcionInvalida()

        mostrarGestionarCandidatos()
        opcion = input('Seleccione una opción: ')

def mostrarMenuPrincipal():
    limpiarPantalla()
    print("Bienvenido, ", estudiantes[currentEstudiante][1])
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir del programa")

def menuPrincipal():
    mostrarMenuPrincipal()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarPerfil()
        elif opcion == '2':
            gestionarCandidatos()
        elif opcion == '3':
            enConstruccion()
        elif opcion == '4':
            enConstruccion()
        else:
            opcionInvalida()

        mostrarMenuPrincipal()
        opcion = input('Seleccione una opción: ')

def verCandidatos():
    enConstruccion()

def mostrarGestionarPerfil():
    enConstruccion()

def registrarEstudiante(): # MODULARIZAR ESTA FUNCIÓN
    global estudiantesLen, estudiantes
    if estudiantesLen == 8:
        print('El registro de estudiantes no está disponible')
        continuar()
        return
    
    datosEstudiante = [''] * 6
    datosEstudiante[0] = input('Introduzca su email: ')
    
    aux = 0
    while aux < estudiantesLen:
        if estudiantes[aux][0] == datosEstudiante[0]:
            aux = -1
            print('El estudiante ya está registrado.')
            continuar()
            return
        aux += 1

    datosEstudiante[1] = input('Introduzca su nombre: ')
    datosEstudiante[2] = input('Introduzca la contraseña: ')
    datosEstudiante[3] = input('Introduzca su fecha de nacimiento: ') # Añadir validación de fecha de nacimiento
    datosEstudiante[4] = input('Introduzca su biografía: ')
    datosEstudiante[5] = input('Introduzca sus hobbies: ')

    index = buscarEstudiante('')

    estudiantes[index] = datosEstudiante
    estudiantesLen += 1

    print('El estudiante se registró exitosamente.')
    continuar()

def registrarModerador(): # MODULARIZAR
    global moderadoresLen, moderadores
    datosModerador = [''] * 3
    datosModerador[0] = input('Introduzca su email: ')

    aux = 0
    while aux < moderadoresLen:
        if estudiantes[aux][0] == datosModerador[0]:
            print('El moderador ya está registrado.')
            continuar()
            return
        aux += 1

    datosModerador[1] = input('Introduzca su nombre: ')
    datosModerador[2] = input('Introduzca la contraseña: ')

    index = buscarModerador('')

    moderadores[index] = datosModerador
    moderadoresLen += 1

    print('El moderador se registró exitosamente.')
    continuar()

def mostrarRegistrarse():
    limpiarPantalla()
    print('a. Registrarse como estudiante')
    print('b. Registrarse como moderador')
    print('c. Volver')

def registrarse():
    mostrarRegistrarse()
    opcion = input('Seleccione una opción: ')

    while opcion != 'c':
        if opcion == 'a':
            registrarEstudiante()
        elif opcion == 'b':
            registrarModerador()
        else:
            opcionInvalida()
        

        mostrarRegistrarse()
        opcion = input('Seleccione una opción: ')








def mostrarMenuInicial():
    limpiarPantalla()
    print('1. Iniciar sesión')
    print('2. Registrarse')
    print('0. Salir')

def menuInicial():
    mostrarMenuInicial()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            utnMatch()
        elif opcion == '2':
            registrarse()
        else:
            opcionInvalida()
        

        mostrarMenuInicial()
        opcion = input('Seleccione una opción: ')


menuInicial()




def bonus_track_1():
    index = 0
    edades = [0] * estudiantesLen
    for est in estudiantes: # se obtienen todas las edades
        if est[0] != '':
            edades[index] = obtenerEdad(est[3])
            index += 1

    for i in range(estudiantesLen): # se ordena el arreglo
        for j in range(0, estudiantesLen-i-1):
            if edades[j] > edades[j+1]:
                aux = edades[j+1]
                edades[j+1] = edades[j]
                edades[j] = aux

    for i in range(estudiantesLen):
        if edades[i] + 1 != edades[i + 1]:
            print(f'Existe un hueco entre {edades[i]} y {edades[i+1]}')



def bonus_track_2(): # lógica: el primer estudiante puede matchear con estudiantesLen -1 estudiante (todos menos él mismo),
                     # el segundo también tiene estudiantesLen -1 matcheos disponibles pero no se cuenta el matcheo que se
                     # registró con el primer estudiante, se puede probar que la secuencia es
                     # e_n = estudiantesLen - n, estudiantesLen >= n >= 1
    acum = 0
    for i in range(estudiantesLen):
        acum += estudiantesLen - i

    print(f'Hay {acum} matcheos posibles')