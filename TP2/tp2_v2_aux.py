import os
from random import randint
from datetime import datetime
from maskpass import advpass

CANT_MAX_ESTUDIANTES = 8
CANT_MAX_MODERADORES = 4

estudiantesLen = 0
estudiantes = [[''] * 6 for _ in range(CANT_MAX_ESTUDIANTES)] # A lo sumo 8 estudiantes con email, nombre, contraseña, fecha de nacimiento, biografía y hobbies como datos

moderadoresLen = 0
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