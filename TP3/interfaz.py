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

### menu inicial

def mostrarMenuInicial():# menu inicial e programa 
    limpiarPantalla()
    console.print('[bold white]Bienvenido![/bold white]', justify='center')
    console.print('1. Iniciar sesión', justify='center')
    console.print('2. Registrarse', justify='center')
    console.print('0. [red]Salir[/red]', justify='center')

def mostrarRegistrarse(): # sub menu de mostrarMenuInicial
    limpiarPantalla()
    console.print('1. Registrarse como estudiante', justify='center')
    console.print('2. Registrarse como moderador', justify='center')
    console.print('0. Volver', justify='center')

def mostrarIniciarSesion():# sub menu de mostrarMenuInicial
    limpiarPantalla()
    console.print('[bold white]Por favor ingrese los datos de su cuenta[/bold white]', justify='center')

# menu estudiante

def mostrarMenuEst():# menu principal de estudiante 
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN-MATCH![/bold white]', justify='center')
    console.print('1. Gestionar mi perfil', justify='center')
    console.print('2. Gestionar candidatos', justify='center')
    console.print('3. Matcheos' , justify='center')
    console.print('4. Reportes estadisticos', justify='center')
    console.print('0. [red]Salir[/red]', justify='center')

def mostrarGestionarPerfil():# sub menu de mostrarMenuEst
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tu perfil[/bold white]', justify='center')
    console.print('1. Editar mis datos personales', justify='center')
    console.print('2. Ver mi perfil', justify='center')
    console.print('3. Eliminar mi perfil', justify='center')
    console.print('0. Volver', justify='center')

def mostrarEditarDatos():# sub menu de mostrarGestionarPerfil
    console.print('[bold white]Estas editando tus datos personales[/bold white]', justify='center')
    console.print('[bold white]¿Qué datos deseas editar?[/bold white]', justify='center')
    console.print('1. Fecha de nacimiento', justify='center')
    console.print('2. Biografia', justify='center')
    console.print('3. Hobbies', justify='center')
    console.print('0. Volver')

def mostrarGestionarCandidatos():# sub menu de mostrarMenuEst
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tus candidatos[/bold white]', justify='center')
    console.print('1. Ver candidatos disponibles', justify='center')
    console.print('2. Reportar a un candidato', justify='center')
    console.print('3. Volver', justify='center')

def mostrarMatcheos():
    limpiarPantalla()
    console.print('[bold white]Matcheos[/bold white]', justify='center')
    console.print('1. Ver matcheos', justify='center')
    console.print('2. Eliminar match', justify='center')
    console.print('3. Volver', justify='center')
    
# menu moderador y administrador 
    
def mostrarMenuMod(): # menu aplicable en ambos
    limpiarPantalla()
    console.print('[bold white]Bienvenido a UTN-MATCH![/bold white]')  
    console.print('1. Gestionar usuarios', justify='center')
    console.print('2. Gestionar reportes', justify='center')
    console.print('3. Reportes estadisticos', justify='center')
    console.print('0. [red]Salir[/red]', justify='center')

def mostrarGestionarUsuariosMod(): # menu para moderador
    limpiarPantalla()
    console.print('[bold white]Gestionando usuarios[/bold white]', justify='center')
    console.print('1. Desactivar usuario', justify='center')
    console.print('0. Volver', justify='center')

def mostrarGestionarUsuariosAdmin(): # menu para admin
    limpiarPantalla()
    console.print('[bold white]Gestionando usuarios[/bold white]', justify='center')
    console.print('1. Eliminar usuarios(user o modder)', justify='center')
    console.print('2. Dar de alta un moderador', justify='center')
    console.print('3. Desactivar usuario', justify='center')
    console.print('0. Volver', justify='center')
    
def mostrarGestionarReportes(): # menu aplicable para ambos
    limpiarPantalla()
    console.print('[bold white]Gestionando reportes[/bold white]', justify='center')
    console.print('1. Ver reportes', justify='center' )
    console.print('0. Volver', justify='center')


    








    
