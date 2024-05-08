import os
import pwinput as p
import time
import random as r

usuario_actual = None # se asigna al usuario que inicio sesion

# Datos estudiantes
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

# limpiar CLI
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# obtener mail login
def obtenerEmail():
    limpiarPantalla()
    email = input('Introduzca su email: ')
    while email != estudiante1_email and email != estudiante2_email and email != estudiante3_email:
        print('Usuario no encontrado')
        email = input('Introduzca su email: ')

    return email

# obtener contraseña login
def obtenerContrasena(email):
    intentos = 3

    if email == 'estudiante1@ayed.com':
        while intentos > 0:
            if p.pwinput(prompt = 'Introduzca la contraseña: ', mask = '*') != estudiante1_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False
        
    elif email == 'estudiante2@ayed.com':
        while intentos > 0:
            if p.pwinput(prompt = 'Introduzca la contraseña: ', mask = '*') != estudiante2_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False
        
    elif email == 'estudiante3@ayed.com':
        while intentos > 0:
            if p.pwinput(prompt = 'Introduzca la contraseña: ', mask = '*') != estudiante3_contrasena:
                print('Contraseña incorrecta, intente nuevamente.')
                intentos -= 1
            else:
                return True
        if intentos == 0:
            return False

# inicio de sesion       
def iniciarSesion():
    email = obtenerEmail()
    global usuario_actual
    usuario_actual = email
    logged = obtenerContrasena(email)
    if logged:
        print("Se inicio sesion correctamente, ", usuario_actual)
        time.sleep(1)
        return email
    else:
        return False

# menu principal
def mostrarMenuPrincipal():
    limpiarPantalla()
    print("Bienvenido, ", usuario_actual)
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir")

# gestionar perfil
def gestionarPerfil():
    limpiarPantalla()
    print("Estas gestionando tu perfil")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")
    print("c. Volver")
    opcion = input('Seleccione una opción: ')

    if opcion == 'a':
        editar_datos_personales()  
    elif opcion == 'b':
        enConstruccion()
        return
    elif opcion == 'c':
        return

# editar datos personales
def editar_datos_personales():
    limpiarPantalla()
    print("Estas editando tus datos personales")
    print("¿Qué datos deseas editar?")
    print("a. Fecha de nacimiento")
    print("b. Biografía")
    print("c. Hobbies")
    print("d. Volver")
    opcion = input("Seleccione una opcion: ")

    if opcion == 'a':
        nuevo_valor = input("Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ")
        if usuario_actual == 'estudiante1@ayed.com':
            estudiante1_fechaNacimiento = nuevo_valor
        elif usuario_actual == 'estudiante2@ayed.com':
            estudiante2_fechaNacimiento = nuevo_valor
        elif usuario_actual == 'estudiante3@ayed.com':
            estudiante3_fechaNacimiento = nuevo_valor
    elif opcion == 'b':
        nuevo_valor = input("Ingrese la nueva biografía: ")
        if usuario_actual == 'estudiante1@ayed.com':
            estudiante1_biografia = nuevo_valor
        elif usuario_actual == 'estudiante2@ayed.com':
            estudiante2_biografia = nuevo_valor
        elif usuario_actual == 'estudiante3@ayed.com':
            estudiante3_biografia = nuevo_valor
    elif opcion == 'c':
        nuevo_valor = input("Ingrese los nuevos hobbies: ")
        if usuario_actual == 'estudiante1@ayed.com':
            estudiante1_hobbies = nuevo_valor
        elif usuario_actual == 'estudiante2@ayed.com':
            estudiante2_hobbies = nuevo_valor
        elif usuario_actual == 'estudiante3@ayed.com':
            estudiante3_hobbies = nuevo_valor
    elif opcion == 'd':
        return

# gestionar candidatos
def gestionarCandidatos():
    limpiarPantalla()
    print("Gestionando candidatos")
    print("a. Ver candidatos disponibles")
    print("b. Contactar candidatos")
    print("c. Volver")
    opcion = input('Seleccione una opción: ')
    
    if opcion == 'a':
        VerCanditatos()
    elif opcion == 'b':
        enConstruccion()
        return
    elif opcion == 'c':
        return
    
# Ver candidatos # agregar funcion de calculo edad # 
def VerCanditatos():
    limpiarPantalla()
    print("Los candidatos disponibles son: ")
    if usuario_actual == estudiante1_email:
        print("a. " + estudiante2_nombre + "\n" +
              "Biografía: " + estudiante2_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante2_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante2_hobbies)
        print("\nb. " + estudiante3_nombre + "\n" +
              "Biografía: " + estudiante3_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante3_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante3_hobbies)
        opcion = input("Elije con quien quieres hacer match (a/b): ")
        if opcion == "a":
            print("Hiciste match con", estudiante2_nombre)
            time.sleep(1)
        elif opcion == "b":
            print("Hiciste match con", estudiante3_nombre)
            time.sleep(1)
        else:
            print("Opción inválida")
            time.sleep(1)
    elif usuario_actual == estudiante2_email:
        print("a. " + estudiante1_nombre + "\n" +
              "Biografía: " + estudiante1_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante1_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante1_hobbies)
        print("\nb. " + estudiante3_nombre + "\n" +
              "Biografía: " + estudiante3_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante3_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante3_hobbies)
        opcion = input("Elije con quien quieres hacer match (a/b): ")
        if opcion == "a":
            print("Hiciste match con", estudiante1_nombre)
            time.sleep(1)
        elif opcion == "b":
            print("Hiciste match con", estudiante3_nombre)
            time.sleep(1)
        else:
            print("Opción inválida")
            time.sleep(1)
    elif usuario_actual == estudiante3_email:
        print("a. " + estudiante1_nombre + "\n" +
              "Biografía: " + estudiante1_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante1_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante1_hobbies)
        print("\nb. " + estudiante2_nombre + "\n" +
              "Biografía: " + estudiante2_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante2_fechaNacimiento + "\n" +
              "Hobbies: " + estudiante2_hobbies)
        opcion = input("Elije con quien quieres hacer match (a/b): ")
        if opcion == "a":
            print("Hiciste match con", estudiante1_nombre)
            time.sleep(1)
        elif opcion == "b":
            print("Hiciste match con", estudiante2_nombre)
            time.sleep(1)
        else:
            print("Opción inválida")
            time.sleep(1)
 
# Ruleta
def ruleta():
    limpiarPantalla()
    print("Ruleta")
    print("a. Iniciar ruleta")
    print("b. Volver")
    opcion = input('Seleccione una opción: ')
    if opcion == 'a':
        af1 = int(input('Introduzca la afinidad con Persona A: '))
        af2 = int(input('Introduzca la afinidad con Persona B: '))
        af3 = int(input('Introduzca la afinidad con Persona C: '))

        while af1 + af2 + af3 != 100:
            print('Los valores introducidos no suman 100, intente nuevamente.')
            af1 = int(input('Introduzca la afinidad con Persona A: '))
            af2 = int(input('Introduzca la afinidad con Persona B: '))
            af3 = int(input('Introduzca la afinidad con Persona C: '))

        buffer = r.randint(0, 100)
        if buffer > 100 - af1:
            print('¡Matcheaste con Persona A')
        elif buffer > 100 - af1 - af2:
            print('¡Matcheaste con Persona B')
        elif buffer > 100 - af1 - af2 - af3:
            print('¡Matcheaste con Persona C')

        input('Presione enter para continuar...')
    else:
        return

#
def enConstruccion():
    limpiarPantalla()
    print("En construcción.")
    time.sleep(1)

#
def manejarMenuPrincipal(opcion):
    if opcion == '1':
        gestionarPerfil()
    elif opcion == '2':
        gestionarCandidatos()
    elif opcion == '5':
        ruleta()
    else:
        enConstruccion()

# Funcion principal
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
        limpiarPantalla()
        mostrarMenuPrincipal()
        opcion = input('Seleccione una opción: ')
    return
    
main()