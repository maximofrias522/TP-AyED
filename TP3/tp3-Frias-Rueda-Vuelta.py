import random
from maskpass import askpass
from rich.console import Console
import sys

console = Console()

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


# # Crear un moderador y un administrador
# def crear_moderador(moderador_db):
#     moderador = Moderador()
#     moderador.id = 1  # Asigna un ID único
#     moderador.email = "moderador@example.com".ljust(50)
#     moderador.nombre = "Moderador".ljust(50)
#     moderador.contrasena = "contrasenaModerador".ljust(50)
#     moderador.estado = True

#     # Guardar el moderador en la base de datos
#     moderador_db.seek(0, os.SEEK_END)  # Ir al final del archivo
#     pickle.dump(moderador, moderador_db)
#     moderador_db.flush()  # Asegurarse de que los datos se guarden

# def crear_administrador(administrador_db):
#     administrador = Administrador()
#     administrador.id = 1  # Asigna un ID único
#     administrador.email = "admin@example.com".ljust(50)
#     administrador.nombre = "Administrador".ljust(50)
#     administrador.contrasena = "contrasenaAdmin".ljust(50)
#     administrador.estado = True

#     # Guardar el administrador en la base de datos
#     administrador_db.seek(0, os.SEEK_END)  # Ir al final del archivo
#     pickle.dump(administrador, administrador_db)
#     administrador_db.flush()  # Asegurarse de que los datos se guarden






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
    os.system('cls' if os.name == 'nt' else 'clear') # si el sistema es win usa el comando cls, en caso contrario asume que es unix y usa clear
    console.print(asciiart)

def continuar():
    input("Presione enter para continuar...")

def opcionInvalida():
    console.print("Error: la opcion ingresada no es valida.", style='red')
    continuar()

def enConstruccion():
    limpiarPantalla() 
    print("En construcción.")
    continuar()

# Menú inicial del programa
def mostrarMenuInicial():
    limpiarPantalla()
    console.print('[bold white]Bienvenido![/bold white]')
    console.print('1. Iniciar sesión')
    console.print('2. Registrarse')
    console.print('0. [red]Salir[/red]')

# Submenú de registrarse
def mostrarRegistrarse():
    limpiarPantalla()
    console.print('1. Registrarse como estudiante')
    console.print('2. Registrarse como moderador')
    console.print('0. Volver')

# Submenú de iniciar sesión
def mostrarIniciarSesion():
    limpiarPantalla()
    console.print('[bold white]Por favor ingrese los datos de su cuenta[/bold white]')

# Menú principal de estudiante
def mostrarMenuEst():
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN-MATCH![/bold white]')
    console.print('1. Gestionar mi perfil')
    console.print('2. Gestionar candidatos')
    console.print('3. Matcheos')
    console.print('4. Reportes estadisticos')
    console.print('0. [red]Salir[/red]')

# Submenú de gestionar perfil
def mostrarGestionarPerfil():
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tu perfil[/bold white]')
    console.print('1. Ver mi perfil')
    console.print('2. Editar mis datos personales')
    console.print('3. Eliminar mi perfil')
    console.print('0. Volver')

# Submenú de editar datos personales
def mostrarEditarDatos():
    limpiarPantalla()
    console.print('[bold white]Estas editando tus datos personales[/bold white]')
    console.print('[bold white]¿Qué datos deseas editar?[/bold white]')
    console.print('1. Fecha de nacimiento')
    console.print('2. Biografia')
    console.print('3. Hobbies')
    console.print('0. Volver')

# Submenú de matcheos
def mostrarMatcheos():
    limpiarPantalla()
    console.print('[bold white]Matcheos[/bold white]')
    console.print('1. Ver matcheos')
    console.print('2. Eliminar match')
    console.print('0. Volver')

# Menú moderador/administrador
def mostrarMenuMod():
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN-MATCH![/bold white]')  
    console.print('1. Gestionar usuarios')
    console.print('2. Gestionar reportes')
    console.print('3. Reportes estadisticos')
    console.print('0. [red]Salir[/red]')

# Submenú de gestionar usuarios (moderador)
def mostrarGestionarUsuariosMod():
    limpiarPantalla()
    console.print('[bold white]Gestionando usuarios[/bold white]')
    console.print('1. Desactivar usuario')
    console.print('0. Volver')

# Submenú de gestionar usuarios (administrador)
def mostrarGestionarUsuariosAdmin():
    limpiarPantalla()
    console.print('[bold white]Gestionando usuarios[/bold white]')
    console.print('1. Eliminar un estudiante')
    console.print('2. Eliminar un moderador')
    console.print('3. Dar de alta un moderador')
    console.print('0. Volver')

# Submenú de gestionar reportes (moderador y administrador)
def mostrarGestionarReportes():
    limpiarPantalla()
    console.print('[bold white]Gestionando reportes[/bold white]')
    console.print('1. Ver reportes')
    console.print('0. Volver')

def mostrarMenuAdmin():
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN-MATCH![/bold white]')  
    console.print('1. Gestionar usuarios')
    console.print('2. Gestionar reportes')
    console.print('3. Reportes estadísticos')
    console.print('0. [red]Salir[/red]')




adminActual = Administrador()

def menuAdmin(usuario): # menu principal
    global adminActual
    adminActual = usuario
    mostrarMenuAdmin()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarUsuarios()
        elif opcion == '2':
            gestionarReportes()
        elif opcion == '3':
            reportesEstadisticos()
        elif opcion == '4':
            puntuarCandidatos()
        else:
            opcionInvalida()

        mostrarMenuMod()
        opcion = input('Seleccione una opción: ')

def gestionarUsuarios():
    mostrarGestionarUsuariosAdmin()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            eliminarEstudiante()
        elif opcion == '2':
            eliminarModerador()
        elif opcion == '3':
            darDeAltaModerador()
        else:
            opcionInvalida()

def gestionarReportes():
    enConstruccion()

def reportesEstadisticos():
    enConstruccion()






def imprimirDatosDeModerador(moderador):
    print("ID: " + str(moderador.id) + "\n" +
          "Email: " + moderador.email + "\n" +
          "Nombre: " + moderador.nombre)

def mostrarTodosLosModeradores():
    limpiarPantalla()
    tam = os.path.getsize(moderadoresDbFisica)
    moderadoresDbLogica.seek(0)
    while moderadoresDbLogica.tell() < tam:
        moderador = pickle.load(moderadoresDbLogica)
        if moderador.estado == True:
            imprimirDatosDeModerador(moderador)
            print('\n_________________\n')

def eliminarAux(dbFisica, dbLogica):
    opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')
    while opcion != '-1':
        if esIdValida(dbFisica, dbLogica, opcion):
            eliminarUsuario(dbFisica, dbLogica, obtenerUsuario(dbFisica, dbLogica, opcion))
            console.print('El usuario se eliminó correctamente.', style='green')
            continuar()
        else:
            opcionInvalida()
        opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')

def eliminarEstudiante():
    mostrarTodosLosEstudiantes(-1)
    eliminarAux(estudiantesDbFisica, estudiantesDbLogica)
    

def eliminarModerador():
    mostrarTodosLosModeradores()
    eliminarAux(estudiantesDbFisica, estudiantesDbLogica)

def darDeAltaModerador():
    mostrarTodosLosEstudiantes(-1)
    opcion = input('Introduza el ID del estudiante para hacerlo moderador o -1 para volver: ')
    while opcion != '-1':
        if esIdValida(estudiantesDbFisica, estudiantesDbLogica, opcion):
            estudiante = obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, opcion)
            nuevoModerador = Moderador()
            moderadoresDbLogica.seek(0)
            while moderadoresDbLogica.tell() < os.path.getsize(moderadoresDbLogica): # obtiene el último usuario registrado
                ultimoModerador = pickle.load(moderadoresDbLogica)

            try:
                nuevoModerador.id = ultimoModerador.id + 1
            except:
                nuevoModerador.id = 0
            nuevoModerador.email = estudiante.email
            nuevoModerador.nombre = estudiante.nombre
            nuevoModerador. contrasena = estudiante.contrasena

            moderadoresDbLogica.seek(0, os.SEEK_END)
            pickle.dump(nuevoModerador, moderadoresDbLogica)
            moderadoresDbLogica.flush()

            eliminarUsuario(estudiantesDbFisica, estudiantesDbLogica, estudiante)
            print('El usuario ahora es un moderador.')
            continuar()
        else:
            opcionInvalida()
        opcion = input('Introduza el ID del estudiante para hacerlo moderador o -1 para volver: ')

def idxmax(lista):
    idx = -1
    max = -1
    for i in range(len(lista)):
        if lista[i] > max:
            idx = lista[i]
            max = i

    return idx

def reportesEstadisticos():
    cantModeradores = obtenerCantUsuario(moderadoresDbFisica, moderadoresDbLogica)
    moderadoresTotal = [0] * cantModeradores
    moderadoresIgnorado = [0] * cantModeradores
    moderadoresAceptado = [0] * cantModeradores 
    reportesTotales = 0
    reportesIgnorados = 0
    reportesAceptados = 0
    tam = os.path.getsize(reportesDbFisica)
    reportesDbLogica.seek(0)
    while reportesDbLogica.tell() < tam:
        reporte = pickle.load(reportesDbLogica)
        reportesTotales += 1
        moderadoresTotal[reporte.idMod] += 1
        if reporte.estado == 1:
            reportesAceptados += 1
            moderadoresAceptado[reporte.idMod] += 1
        elif reporte.estado == 2:
            reportesIgnorados += 1
            moderadoresIgnorado[reporte.idMod] += 1

    print(f'Reportes totales: {reportesTotales}')
    print(f'Reportes ignorados: {reportesIgnorados * 100 / reportesTotales}%')
    print(f'Reportes aceptados: {reportesAceptados * 100 / reportesTotales}%')

    modIgnorado = obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, idxmax(moderadoresIgnorado))
    print(f'El moderador que más reportes ignoró fue: {modIgnorado.nombre}')

    modAceptado = obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, idxmax(moderadoresAceptado))
    print(f'El moderador que más reportes aceptó fue: {modAceptado.nombre}')

    modTotal = obtenerUsuario(moderadoresDbFisica, moderadoresDbLogica, idxmax(moderadoresTotal))
    print(f'El moderador que más reportes procesó fue: {modTotal.nombre}')
    continuar()

def obtenerPuntaje(id):
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == id and like.estado == True:
            likesRecibidos.append(like.idEmisor)

    puntaje = 0
    for id in likesDados:
        if id in likesRecibidos:
            puntaje += 1
        else:
            puntaje -= 1

    if puntaje >= 0:
        puntaje = puntaje + puntaje // 3
    
    return puntaje

def puntuarCandidatos():
    limpiarPantalla()
    tam = os.path.getsize(estudiantesDbFisica)
    estudiantesDbLogica.seek(0)
    while estudiantesDbLogica.tell() < tam:
        estudiante = pickle.load(estudiantesDbLogica)
        if estudiante.estado == True:
            imprimirDatosDeEstudiante(estudiante)
            print(f"Puntaje: {obtenerPuntaje(estudiante.id)}")
            print('\n_________________\n')







from datos import *
from interfaz import *
from common import *


estudianteActual = Estudiante()

def menuEstudiante(usuario): # menu principal
    global estudianteActual
    estudianteActual = usuario
    mostrarMenuEst()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            if gestionarPerfil():
                return
        elif opcion == '2':
            gestionarCandidatos()
        elif opcion == '3':
            matcheos()
        elif opcion == '4':
            reportesEstadisticos()
        else:
            opcionInvalida()

        mostrarMenuEst()
        opcion = input('Seleccione una opción: ')

# Aux S

def mostrarPerfil():
    limpiarPantalla()
    console.print("Estás viendo tu perfil", style='bold white')
    imprimirDatosDeEstudiante(estudianteActual)

    continuar()
# Aux F



# Gestion perfil S
def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            mostrarPerfil()  
        elif opcion == '2':
            editarDatosPersonales()
        elif opcion == '3':
            if eliminarPerfil():
                return True
        else:
            opcionInvalida() 

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

    return False

def editarDatosPersonales():
    mostrarEditarDatos()
    opcion = input('Seleccione una opcion: ')
    while opcion != '0':
        if opcion == '1':
            editarFechaNacimiento()
        elif opcion == '2':
            editarBiografia()
        elif opcion == '3':
            editarHobbies()
        else:
            opcionInvalida()
        mostrarEditarDatos()
        opcion = input('Seleccione una opcion: ')

def obtenerFecha(): # para edicion
    formato_correcto = False 
    while not formato_correcto: 
        fecha = input("Ingrese la nueva fecha de nacimiento (dd/mm/aaaa): ")
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

def editarFechaNacimiento():
    nueva_fecha = obtenerFecha() 
    estudianteActual.fechaNacimiento = nueva_fecha
    console.print(f"Fecha de nacimiento actualizada a {nueva_fecha.strftime('%d/%m/%Y')}", style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def editarBiografia():
    nueva_biografia = input("Ingrese la nueva biografía: ") 
    while nueva_biografia == '': 
        console.print('La biografía no puede estar vacía.', style='red')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudianteActual.biografia = nueva_biografia.ljust(50)
    console.print('Su nueva biografía es: ', nueva_biografia, style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def editarHobbies():
    nuevos_hobbies = input("Ingrese los nuevos hobbies: ")
    while nuevos_hobbies == '':
        console.print('Los hobbies no pueden estar vacíos', style='red')
        nuevos_hobbies = input("Ingrese los nuevos hobbies: ")

    estudianteActual.hobbies = nuevos_hobbies.ljust(50)
    console.print("Sus nuevos hobbies son: ", nuevos_hobbies, style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def eliminarPerfil():
    opcion = input('¿Está seguro de que desea eliminar su perfil? s/n: ').lower()
    while opcion != 'n':
        if opcion == 's':
            eliminarUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
            console.print('Su perfil se eliminó correctamente.', style='green')
            continuar()
            return True
        else:
            opcionInvalida()
        opcion = input('¿Está seguro de que desea eliminar su perfil? s/n: ').lower()

    return False
# Gestion perfil F


# Gestion candidatos S 

# Submenú de gestionar candidatos
def mostrarGestionarCandidatos():
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tus candidatos[/bold white]')
    console.print('1. Ver candidatos disponibles')
    console.print('2. Reportar a un candidato')
    if estudianteActual.revelarCandidatos == True:
        console.print('3. Revelar candidatos')
    console.print('0. Volver')


def gestionarCandidatos():
    mostrarGestionarCandidatos()
    opcion = input('Seleccione una opcion: ')
    while opcion != '0':
        if opcion == '1':
            verCandidatos()
        elif opcion == '2':
            reportarCandidato()
        elif opcion == '3' and estudianteActual.revelarCandidatos == True:
            revelarCandidatos()
        else:
            opcionInvalida()

        mostrarGestionarCandidatos()
        opcion = input('Seleccione una opcion: ')

def darLike():
    nuevoLike = Like()
    nuevoLike.idEmisor = estudianteActual.id

    try:
        nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle like: '))
        if nuevoLike.idEmisor == nuevoLike.idReceptor:
            idValida = False
        else:
            idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
    except:
        idValida = False

    while not idValida:
        print('ID de usuario no válida.')
        try:
            nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle like: '))
            if nuevoLike.idEmisor == nuevoLike.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
        except:
            idValida = False


    yaTeGusta = False
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if (like.idEmisor == nuevoLike.idEmisor) and (like.idReceptor == nuevoLike.idReceptor) and (like.estado == True):
            yaTeGusta = True


    if yaTeGusta:
        console.print(f'Ya le diste me gusta en el pasado a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
        continuar()

    else:
        likesDbLogica.seek(0, os.SEEK_END)
        pickle.dump(nuevoLike, likesDbLogica)
        likesDbLogica.flush()
        console.print(f'Le diste like a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
        continuar()

def darSuperLike():
    if estudianteActual.superlike == True:
        nuevoLike = Like()
        nuevoLike.idEmisor = estudianteActual.id

        try:
            nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle un super-like: '))
            if nuevoLike.idEmisor == nuevoLike.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
        except:
            idValida = False

        while not idValida:
            print('ID de usuario no válida.')
            try:
                nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle un super-like: '))
                if nuevoLike.idEmisor == nuevoLike.idReceptor:
                    idValida = False
                else:
                    idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
            except:
                idValida = False

        leDisteLike = False
        teDioLike = False
        tam = os.path.getsize(likesDbFisica)
        likesDbLogica.seek(0)
        while likesDbLogica.tell() < tam:
            like = pickle.load(likesDbLogica)
            if like.idEmisor == nuevoLike.idEmisor and like.idReceptor == nuevoLike.idReceptor and like.estado == True:
                leDisteLike = True
            if like.idReceptor == nuevoLike.idEmisor and like.idEmisor == nuevoLike.idReceptor and like.estado == True:
                teDioLike = True

        if teDioLike and leDisteLike:
            print('Ya hiciste match con este usuario')
        else:
            likesDbLogica.seek(0, os.SEEK_END)
            pickle.dump(nuevoLike, likesDbLogica)
            nuevoLike2 = Like()
            nuevoLike2.idEmisor = nuevoLike.idReceptor
            nuevoLike2.idReceptor = nuevoLike.idEmisor
            pickle.dump(nuevoLike2, likesDbLogica)
            likesDbLogica.flush()
            console.print(f'Le diste un super-like a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
            estudianteActual.superlike = False
            sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    else:
        print('Ya usaste tu super-like en el pasado.')
    continuar()

def verCandidatos():
    mostrarTodosLosEstudiantes(estudianteActual.id)

    opcion = input('¿Querés darle like a algún estudiante? s/n o "super" para dar un super-like: ').lower()
    while opcion != 'n':
        if opcion == 's':
            darLike()
        elif opcion == 'super':
            darSuperLike()
        else:
            opcionInvalida()
        
        mostrarTodosLosEstudiantes(estudianteActual.id)
        opcion = input('¿Querés darle like a algún estudiante? s/n: ').lower()


def reportar():
    nuevoReporte = Reporte()
    nuevoReporte.idEmisor = estudianteActual.id

    try:
        nuevoReporte.idReceptor = int(input('Ingrese el ID o email del usuario para reportarlo: '))
        if nuevoReporte.idEmisor == nuevoReporte.idReceptor:
            idValida = False
        else:
            idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor)
    except:
        idValida = False

    while not idValida:
        console.print('ID de usuario no válida.', style='red')
        try:
            nuevoReporte.idReceptor = int(input('Ingrese el ID o email del usuario para reportarlo: '))
            if nuevoReporte.idEmisor == nuevoReporte.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor)
        except:
            idValida = False


    yaLoReportaste = False
    tam = os.path.getsize(reportesDbFisica)
    reportesDbLogica.seek(0)
    while reportesDbLogica.tell() < tam:
        reporte = pickle.load(reportesDbLogica)
        if (reporte.idEmisor == nuevoReporte.idEmisor) and (reporte.idReceptor == nuevoReporte.idReceptor):
            yaLoReportaste = True


    if yaLoReportaste:
        console.print(f'Ya reportaste en el pasado a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor).nombre}', style='green')
        continuar()

    else:
        reportesDbLogica.seek(0, os.SEEK_END)
        pickle.dump(nuevoReporte, reportesDbLogica)
        reportesDbLogica.flush()
        console.print(f'Reportaste a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor).nombre}', style='green')
        continuar()
        

def reportarCandidato():
    mostrarTodosLosEstudiantes(estudianteActual.id)

    opcion = input('¿Querés reportar a algún estudiante? s/n: ').lower()
    while opcion != 'n':
        if opcion == 's':
            reportar()
        else:
            opcionInvalida()
        
        mostrarTodosLosEstudiantes(estudianteActual.id)
        opcion = input('¿Querés reportar a algún estudiante? s/n: ').lower()


def revelarCandidatos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)

    hayCandidatos = False
    limpiarPantalla()
    for id in likesRecibidos:
        if id not in likesDados:
            hayCandidatos = True
            imprimirDatosDeEstudiante(obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, id))

    if not hayCandidatos:
        print('No hay candidatos para mostrar')
    else:
        estudianteActual.revelarCandidatos = False
        sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)

    continuar()


def eliminarMatch(likesDados):
    valido = False
    while not valido:
        matchAEliminar = int(input('Ingrese el ID del usuario para eliminar el match: '))
        if matchAEliminar in likesDados:
            valido = True
            tam = os.path.getsize(likesDbFisica)
            likesDbLogica.seek(0)
            while likesDbLogica.tell() < tam:
                pos = likesDbLogica.tell()
                like = pickle.load(likesDbLogica)
                if like.idEmisor == estudianteActual.id and like.idReceptor == matchAEliminar and like.estado == True:
                    like.estado = False
                    likesDbLogica.seek(pos)
                    pickle.dump(like, likesDbLogica)
                    likesDbLogica.flush()
                    tam = 0

            console.print('Eliminaste el match', style='green')

def matcheos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)

    limpiarPantalla()
    hayMatchs = False
    for id in likesDados:
        if id in likesRecibidos:
            hayMatchs = True
            imprimirDatosDeEstudiante(obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, id))
            print('\n_________________\n')
    
    if not hayMatchs:
        console.print('No tenés matchs', style='blue')
    else:
        opcion = input('¿Querés eliminar algún match? s/n: ').lower()
        while opcion != 'n':
            if opcion == 's':
                eliminarMatch(likesDados)
                continuar()
            else:
                opcionInvalida()
            opcion = 'n'
            

def reportesEstadisticos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)
    
    limpiarPantalla()
    matcheos = 0
    likesDadosYNoDevueltos = 0
    for id in likesDados:
        if id in likesRecibidos:
            matcheos += 1
        else:
            likesDadosYNoDevueltos += 1
    likesRecibidosYNoDevueltos = 2 * matcheos - likesDadosYNoDevueltos
    estudiantesDbLogica.seek(0)
    cantidadDeEstudiantes = obtenerCantUsuario(estudiantesDbFisica, estudiantesDbLogica)

    print(f'Matcheaste con el {matcheos * 100 / cantidadDeEstudiantes}% de los estudiantes')
    print(f'Likes dados y no devueltos: {likesDadosYNoDevueltos}')
    print(f'Likes recibidos y no devueltos: {likesRecibidosYNoDevueltos}')
    continuar()










from rich.table import Table

modderActual = Moderador()

def menuModerador(usuario): # menu principal
    global modderActual
    modderActual = usuario
    mostrarMenuMod()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarUsuarios()
        elif opcion == '2':
            gestionarReportes()
        elif opcion == '3':
            reportesEstadisticos()
        else:
            opcionInvalida()

        mostrarMenuMod()
        opcion = input('Seleccione una opción: ')


def gestionarUsuarios():
    mostrarGestionarUsuariosMod()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            eliminarUsuario()
        else:
            opcionInvalida()
        mostrarGestionarUsuariosMod()
        opcion = input('Seleccione una opción: ')


def gestionarReportes():
    mostrarGestionarReportes()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            verReportes()
        else:
            opcionInvalida()
        mostrarGestionarReportes()
        opcion = input('Seleccione una opción: ')

def verReportes():
    console = Console()

    print("Reportes de prueba agregados al archivo.")

    table = Table(title="Tabla de Reportes")

    table.add_column("ID Emisor", style="bold blue")
    table.add_column("ID Receptor", style="bold red", justify="right")
    table.add_column("Motivo", style="bold red", justify="right")
    table.add_column("Estado", style="bold yellow", justify='right')

    with open("estudiantesDbFisica", "rb") as estudiantesDbLogica:
        tames = os.path.getsize("estudiantesDbFisica")
        estudiantesDbLogica.seek(0)  

        with open("reportesDbFisica", "rb") as reportesDbLogica:
        
            tam = os.path.getsize("reportesDbFisica")
            reportesDbLogica.seek(0)  

            while reportesDbLogica.tell() < tam:
                try:
                
                    reporte = pickle.load(reportesDbLogica)
                    
    
                    estado_emisor = False
                    estado_receptor = False

                    estudiantesDbLogica.seek(0)

                    while estudiantesDbLogica.tell() < tames:
                        estudiante = pickle.load(estudiantesDbLogica)

                        if estudiante.id == reporte.idEmisor:
                            estado_emisor = estudiante.estado

                    
                        if estudiante.id == reporte.idReceptor:
                            estado_receptor = estudiante.estado

                        if estado_emisor and estado_receptor:
                            break

                    if estado_emisor and estado_receptor:
                        table.add_row(str(reporte.idEmisor), str(reporte.idReceptor), reporte.motivo, str(reporte.estado))

                except EOFError:
                    break

    console.print(table)
    continuar()
    gestionarReportes()

def reportesEstadisticos():
    enConstruccion()

def eliminarUsuario():
    opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')
    while opcion != '-1':
        try:
            if esIdValida(opcion):
                eliminarUsuario(estudiantesDbFisica, estudiantesDbLogica, obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, opcion))
                console.print('El usuario se eliminó correctamente.', style='green')
                continuar()

                actualizarReportesPorUsuario(opcion, modderActual.id)

                continuar()
            else:
                opcionInvalida()
        except Exception as e:
            console.print(f'Error: {e}', style='red')
            opcionInvalida()
        opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')

def actualizarReportesPorUsuario(userId, modderId): 
    with open(reportesDbFisica, "r+b") as archivo_reportes:
        tam = os.path.getsize(reportesDbFisica)
        archivo_reportes.seek(0)  

        while archivo_reportes.tell() < tam:
            try:
                reporte = pickle.load(archivo_reportes)

                if reporte.idReceptor == userId:
                    reporte.estado = 1  
                    reporte.idMod = modderId  

                    archivo_reportes.seek(archivo_reportes.tell() - pickle.dumps(reporte).size) 
                    pickle.dump(reporte, archivo_reportes)  
                    console.print(f'Reporte de ID {reporte.idEmisor} o {reporte.idReceptor} actualizado con ID del moderador: {modderId}.', style='yellow')

            except EOFError:
                break
            except Exception as e:
                console.print(f'Error al actualizar el reporte: {e}', style='red')












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