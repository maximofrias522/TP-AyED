import sys
from datos import *
from interfaz import *
from common import *

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

def gestionarReportes():
    enConstruccion()

def reportesEstadisticos():
    enConstruccion()


def eliminarUsuario():
    opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')
    while opcion != '-1':
        try:
            if esIdValida(opcion):
                estudiante = obtenerUsuario(opcion)
                estudiante.estado = False
                sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudiante)
                console.print('El usuario se eliminó correctamente.', style='green')
                continuar()
            else:
                opcionInvalida()
        except:
            opcionInvalida()
        opcion = input('Introduza el ID del usuario a eliminar o -1 para volver: ')