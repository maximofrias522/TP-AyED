import os
from rich.console import Console

console = Console()

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




    