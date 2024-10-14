from datos import *
from interfaz import *
from common import *

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