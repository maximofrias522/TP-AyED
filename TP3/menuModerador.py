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
            if gestionarUsuarios():
                return
        elif opcion == '2':
            gestionarReportes()
        elif opcion == '3':
            reportesEstadisticos()
        else:
            opcionInvalida()

        mostrarMenuMod()
        opcion = input('Seleccione una opción: ')


def gestionarUsuarios():
    enConstruccion()

def gestionarReportes():
    enConstruccion()

def reportesEstadisticos():
    enConstruccion()