import os
import getpass as gp

estudiante1_nombre = 'Estudiante 1'
estudiante1_email = 'estudiante1@ayed.com'
estudiante1_contrasena = '111222'
estudiante1_fechaNacimiento = '24-11-2002'
estudiante1_biografia = 'Estudia ingeniería en sistemas, su materia favorita es análisis matemático, es de Rosario.'
estudiante1_hobbies = 'Pescar, jugar al fútbol.'

estudiante2_nombre = 'Estudiante 2'
estudiante2_email = 'estudiante2@ayed.com'
estudiante2_contrasena = '222333'
estudiante2_fechaNacimiento = '08-10-2003'
estudiante2_biografia = 'Estudia ingeniería en sistemas, su materia favorita es algoritmos, es de Rosario.'
estudiante2_hobbies = 'Salir a correr, cocinar.'

estudiante3_nombre = 'Estudiante 3'
estudiante3_email = 'estudiante3@ayed.com'
estudiante3_contrasena = '333444'
estudiante3_fechaNacimiento = '06-12-2004'
estudiante3_biografia = 'Estudia ingeniería en sistemas, su materia favorita es física, es de Rosario.'
estudiante3_hobbies = 'Leer libros de ficción, salir a remar.'

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtenerEmail():
    email = input('Introduzca su email: ')
    while email != estudiante1_email and email != estudiante2_email and email != estudiante3_email:
        print('Usuario no encontrado')
        email = input('Introduzca su email: ')

    return email

def obtenerContrasena(email):
    intentos = 3

    if email == 'estudiante1@ayed.com':
        while intentos > 0:
            if gp.getpass("Introduzca la contraseña: ") != estudiante1_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False
        
    elif email == 'estudiante2@ayed.com':
        while intentos > 0:
            if gp.getpass("Introduzca la contraseña: ") != estudiante2_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False
        
    elif email == 'estudiante1@ayed.com':
        while intentos > 0:
            if gp.getpass("Introduzca la contraseña: ") != estudiante1_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False
        
def iniciarSesion():
    email = obtenerEmail()
    logged = obtenerContrasena(email)
    if logged:
        return email
    else:
        return False

def mostrarMenuPrincipal():
    limpiarPantalla()
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir")

def gestionarPerfil():
    return

def gestionarCandidatos():
    return

def enConstruccion():
    print("En construcción.")

def manejarMenuPrincipal(opcion):
    if opcion == '1':
        gestionarPerfil()
    elif opcion == '2':
        gestionarCandidatos()
    else:
        enConstruccion()


def main():
    email = iniciarSesion()
    if email == False:
        print('Se introdujo una contraseña incorrecta 3 veces')
        return
    
    limpiarPantalla()
    mostrarMenuPrincipal()
    opcion = input('Seleccione una opción: ')
    while opcion != '0':
        manejarMenuPrincipal(opcion)

        opcion = input('Seleccione una opción: ')
    return
    
main()