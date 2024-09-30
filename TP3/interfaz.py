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
    console.print(asciiart, justify='center')

def continuar():
    input("Presione enter para continuar...")

def opcionInvalida():
    print("Error: la opcion ingresada no es valida.")
    continuar()

def mostrarMenuInicial():
    limpiarPantalla()
    console.print('[bold white]Bienvenido![/bold white]', justify='center')
    console.print('1. Iniciar sesión', justify='center')
    console.print('2. Registrarse', justify='center')
    console.print('0. [red]Salir[/red]', justify='center')

def mostrarRegistrarse():
    limpiarPantalla()
    console.print('1. Registrarse como estudiante', justify='center')
    console.print('2. Registrarse como moderador', justify='center')
    console.print('0. Volver', justify='center')

def mostrarIniciarSesion():
    limpiarPantalla()
    console.print('[bold white]Por favor ingrese los datos de su cuenta[/bold white]', justify='center')

def mostrarMenuEst():
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN MATCH![/bold white]', justify='center')
    console.print('1. Gestionar mi perfil', justify='center')
    console.print('2. Gestionar candidatos', justify='center')
    console.print('3. Matcheos' , justify='center')
    console.print('4. Reportes estadisticos', justify='center')
    console.print('0. [red]Salir[/red]', justify='center')

def mostrarGestionarPerfil():
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tu perfil[/bold white]', justify='center')
    console.print('1. Editar mis datos personales', justify='center')
    console.print('2. Ver mi perfil', justify='center')
    console.print('3. Eliminar mi perfil', justify='center')
    console.print('0. Volver', justify='center')

def mostrarEditarDatos():
    console.print('[bold white]Estas editando tus datos personales[/bold white]', justify='center')
    console.print('[bold white]¿Qué datos deseas editar?[/bold white]', justify='center')
    console.print('1. Fecha de nacimiento', justify='center')
    console.print('2. Biografia', justify='center')
    console.print('3. Hobbies', justify='center')
    console.print('0. Volver')

# def                                                     
