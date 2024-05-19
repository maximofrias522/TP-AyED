# Convenciones:
# Todo se escribe en español, evitamos usar nombres de variables o funciones en inglés.
# Funciones declaradas en camelCase, variables declaradas en snake_case.
# Paréntesis se colocan al lado de la función, sin espacios. Ejemplo: print()
# La separación entre cada función será de un salto de línea, entre cada sección será de tres.

import os
from random import randint
from datetime import datetime
from maskpass import advpass

# Declaración de variable globales ___________________________________________________________________________________________________________

# Arte ASCII
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

# Datos de los estudiantes
estudiante1_nombre = 'Estudiante 1' # str
estudiante1_email = 'estudiante1@ayed.com' # str
estudiante1_contrasena = '111222' # str
estudiante1_fechaNacimiento = '24-11-2002' # str
estudiante1_biografia = 'Estudia ingeniería en sistemas, su materia favorita es análisis matemático, es de Rosario.' # str
estudiante1_hobbies = 'Pescar, jugar al fútbol.' # str

estudiante2_nombre = 'Estudiante 2' # str
estudiante2_email = 'estudiante2@ayed.com' # str
estudiante2_contrasena = '222333' # str
estudiante2_fechaNacimiento = '08-10-2003' # str
estudiante2_biografia = 'Estudia ingeniería en sistemas, su materia favorita es algoritmos, es de Rosario.' # str
estudiante2_hobbies = 'Salir a correr, cocinar.' # str

estudiante3_nombre = 'Estudiante 3' # str
estudiante3_email = 'estudiante3@ayed.com' # str
estudiante3_contrasena = '333444' # str
estudiante3_fechaNacimiento = '06-12-2004' # str
estudiante3_biografia = 'Estudia ingeniería en sistemas, su materia favorita es física, es de Rosario.' # str
estudiante3_hobbies = 'Leer libros de ficción, salir a remar.' # str

# Datos del usuario en sesión (NoneType // Declaradas pero vacias)
email_actual = None # NoneType 
nombre_actual = None # NoneType



# Funciones auxiliares _______________________________________________________________________________________________________________________

# Limpiar pantalla
# Utiliza la librería os para ejecutar el comando clear en la consola, así limpiar el contenido de la misma
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(asciiart)

# Función continuar
# Espera que el usuario presione enter antes de seguir con la ejecución del programa
def continuar():
    input("Presione enter para continuar...")

# Opción inválida
# Le avisa al usuario que la opción que introdujo no es válida y espera a que presione enter para continuar con la ejecución del programa
def opcionInvalida():
    print("Error: la opcion ingresada no es valida.")
    continuar()

# Función en contrucción
# Le avisa al usuario que la funcionalidad a la que quiere acceder no está disponible aún
def enConstruccion():
    limpiarPantalla()
    print("En construcción.")
    continuar()

# Obtener usuario a partir de email
# Busca el nombre de usuario asociado al email introducido
def obtenerNombre(email):
    if email == estudiante1_email:
        nombre = estudiante1_nombre
    elif email == estudiante2_email:
        nombre = estudiante2_nombre
    elif email == estudiante3_email:
        nombre = estudiante3_nombre

    return nombre

# Obtener fecha
# Solicita una fecha al usuario y la valida, en caso de introducirse en un formato incorrecto la vuelve a solicitar
def obtenerFecha():
    formato_correcto = False
    while not formato_correcto:
        fecha = input("Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ")
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            formato_correcto = True
        except ValueError:
            print("El formato de fecha ingresado es incorrecto. Intente nuevamente.")

    return fecha

# Calcula la edad a partir de una fecha
# Utiliza funciones de la librería datetime para converir un string en un formato de fecha válido, lo compara con el año actual
# y le resta 1 en caso de que aún no haya cumplido años.
def obtenerEdad(fecha):
    fecha = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fecha.year
    if (fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day):
        edad -= 1
    return str(edad)

# Imprimir los datos de un usuario
# Muestra en pantalla los datos del usuario que se le pasa como parámetro
def imprimirDatosDeUsuario(usuario):
    if usuario == estudiante1_email:
        print("Nombre: " + estudiante1_nombre + "\n" +
              "Biografía: " + estudiante1_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante1_fechaNacimiento + "\n" +
              "Edad: " + obtenerEdad(estudiante1_fechaNacimiento) + "\n" +
              "Hobbies: " + estudiante1_hobbies)
        
    elif usuario == estudiante2_email:
        print("Nombre: " + estudiante2_nombre + "\n" +
              "Biografía: " + estudiante2_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante2_fechaNacimiento + "\n" +
              "Edad: " + obtenerEdad(estudiante2_fechaNacimiento) + "\n" + 
              "Hobbies: " + estudiante2_hobbies)
        
    elif usuario == estudiante3_email:
        print("Nombre: " + estudiante3_nombre + "\n" +
              "Biografía: " + estudiante3_biografia + "\n" +
              "Fecha de nacimiento: " + estudiante3_fechaNacimiento + "\n" +
              "Edad: " + obtenerEdad(estudiante3_fechaNacimiento) + "\n" +
              "Hobbies: " + estudiante3_hobbies)
        


# Funciones de inicio de sesión ______________________________________________________________________________________________________________

# Obtener mail login
# Solicita al usuario introducir un email y lo compara con los email válidos, en caso de no introducir un email válido
# vuelve a solicitarlo hasta que se introduzca uno
def obtenerEmail():
    limpiarPantalla()
    email = input('Introduzca su email: ')
    while (email != estudiante1_email) and (email != estudiante2_email) and (email != estudiante3_email):
        print('Usuario no encontrado')
        continuar()
        limpiarPantalla()  
        email = input('Introduzca su email: ')

    return email

# Obtener contraseña login
# Solicita al usuario una contraseña y la compara con la asociada al mail leído previamente, en caso de que la introduzca
# incorrectamente se la vuelve a solicitar hasta 3 veces. Si se introduce 3 veces mal retorna False, en caso contrario retorna True
def obtenerContrasena():
    intentos = 3

    while intentos > 0:
        contrasena = advpass(prompt='Introduzca la contraseña: ', mask='*')
        if (email_actual == estudiante1_email and contrasena == estudiante1_contrasena) or (email_actual == estudiante2_email and contrasena == estudiante2_contrasena) or (email_actual == estudiante3_email and contrasena == estudiante3_contrasena):
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')

    if intentos == 0:
        return False

# Inicio de sesion
# Si se inicia sesión exitosamente retorna True y asigna a las variables globales email_actual y nombre_actual los valores
# correspondientes, en caso contrario retorna False
def iniciarSesion():
    limpiarPantalla()
    global email_actual
    email_actual = obtenerEmail()
    contrasena_valida = obtenerContrasena()
    if contrasena_valida:
        global nombre_actual
        nombre_actual = obtenerNombre(email_actual)
        print("Se inicio sesion correctamente, ", nombre_actual)
        continuar()
        return True
    else:
        return False



# Funciones de impresión de menús y submenús _________________________________________________________________________________________________

# Imprimir menú principal
def mostrarMenuPrincipal():
    limpiarPantalla()
    print("Bienvenido, ", nombre_actual)
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir del programa")

# Imprimir submenú gestionar perfil
def mostrarGestionarPerfil():
    limpiarPantalla()
    print("Estas gestionando tu perfil")
    print("a. Editar mis datos personales")
    print("b. Ver mi perfil")
    print("c. Eliminar mi perfil")
    print("d. Volver")

# Imprimir submenú editar datos personales
def mostrarEditarDatosPersonales():
    limpiarPantalla()
    print("Estas editando tus datos personales")
    print("¿Qué datos deseas editar?")
    print("a. Fecha de nacimiento")
    print("b. Biografía")
    print("c. Hobbies")
    print("d. Volver")

# Imprimir submenú gestionar candidatos
def mostrarGestionarCandidatos():
    limpiarPantalla()
    print("Gestionando candidatos")
    print("a. Ver candidatos disponibles")
    print("b. Contactar candidatos")
    print("c. Volver")

def mostrarVerCandidatos(opcion_a, opcion_b):
    limpiarPantalla()
    print("Los candidatos disponibles son: ")

    print('Opción a:')
    imprimirDatosDeUsuario(opcion_a)

    print('\nOpción b:')
    imprimirDatosDeUsuario(opcion_b)

def mostrarRuleta():
    limpiarPantalla()
    print("Ruleta")
    print("a. Iniciar ruleta")
    print("b. Volver")



# Funcionamiento de submenús _________________________________________________________________________________________________________________

# Editar la fecha de nacimiento del usuario
# Solicita al usuario una nueva fecha de nacimiento, la valida y la guarda en la variable correspondiente
def editarFechaNacimiento():
    global estudiante1_fechaNacimiento, estudiante2_fechaNacimiento, estudiante3_fechaNacimiento

    nueva_fecha = obtenerFecha()
    if email_actual == 'estudiante1@ayed.com':
        estudiante1_fechaNacimiento = nueva_fecha
        print("Su nueva fecha de nacimiento es:", nueva_fecha)

    elif email_actual == 'estudiante2@ayed.com':
        estudiante2_fechaNacimiento = nueva_fecha
        print("Su nueva fecha de nacimiento es:", nueva_fecha)

    elif email_actual == 'estudiante3@ayed.com':
        estudiante3_fechaNacimiento = nueva_fecha
        print("Su nueva fecha de nacimiento es:", nueva_fecha)

    continuar()

# Editar la biografía del usuario
# Solicita al usuario la nueva biografía y la almacena en la variable correspondiente
def editarBiografia():
    global estudiante1_biografia, estudiante2_biografia, estudiante3_biografia

    nueva_biografia = input("Ingrese la nueva biografía: ")
    if email_actual == 'estudiante1@ayed.com':
        estudiante1_biografia = nueva_biografia
        print("Su nueva biografia es: ", nueva_biografia)

    elif email_actual == 'estudiante2@ayed.com':
        estudiante2_biografia = nueva_biografia
        print("Su nueva biografia es: ", nueva_biografia)

    elif email_actual == 'estudiante3@ayed.com':
        estudiante3_biografia = nueva_biografia
        print("Su nueva biografia es: ", nueva_biografia)

    continuar()

# Editar los hobbies del usuario
# Solicita al usuario los nuevos hobbies y los almacena en la variable correspondiente
def editarHobbies():
    global estudiante1_hobbies, estudiante2_hobbies, estudiante3_hobbies

    nuevo_hobbie = input("Ingrese los nuevos hobbies: ")
    if email_actual == 'estudiante1@ayed.com':
        estudiante1_hobbies = nuevo_hobbie
        print("Sus nuevos hobbies son: ", nuevo_hobbie)

    elif email_actual == 'estudiante2@ayed.com':
        estudiante2_hobbies = nuevo_hobbie
        print("Sus nuevos hobbies son: ", nuevo_hobbie)

    elif email_actual == 'estudiante3@ayed.com':
        estudiante3_hobbies = nuevo_hobbie
        print("Sus nuevos hobbies son: ", nuevo_hobbie)

    continuar()

# Editar datos personales del usuario
# Maneja las opciones de edición de datos personales del usuario correspondiente
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

# Mostrar el perfil del usuario
# Imprime los datos del usuario que corresponda
def mostrarPerfil():
    limpiarPantalla()
    print("Estás viendo tu perfil")
    imprimirDatosDeUsuario(email_actual)

    continuar()

# Submenú gestionar perfil
# Maneja el funcionamiento del submenú gestionar perfil
def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != 'd':
        if opcion == 'a':
            editarDatosPersonales()
        elif opcion == 'b':
            mostrarPerfil()  
        elif opcion == 'c':
            enConstruccion()
        else:
            opcionInvalida()

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

# Ver los candidatos y darle me gusta al seleccionado
# Muestra los candidatos posible (todos los usuarios distintos del logueado) y le pide al usuario que seleccione uno para darle me gusta.
def verCandidatos():

    if email_actual == estudiante1_email:
        opcion_a = estudiante2_email
        opcion_b = estudiante3_email

    elif email_actual == estudiante2_email:
        opcion_a = estudiante1_email
        opcion_b = estudiante3_email

    elif email_actual == estudiante3_email:
        opcion_a = estudiante1_email
        opcion_b = estudiante2_email

    mostrarVerCandidatos(opcion_a, opcion_b)
    opcion = input("Selecciona qué usuario le gusta o presione 'c' para salir: ")
    
    while opcion != 'c':
        if opcion == "a":
            print("Te gusta", obtenerNombre(opcion_a))
        elif opcion == "b":
            print("Te gusta", obtenerNombre(opcion_b))
        else:
            opcionInvalida()

        continuar()
        mostrarVerCandidatos(opcion_a, opcion_b)
        opcion = input("Selecciona qué usuario le gusta o presione 'c' para salir: ")

# Submenú gestionar candidatos
# Maneja el funcionamiento del submenú gestionar candidatos
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



# Funcionamiento de la ruleta ________________________________________________________________________________________________________________

# Submenú ruleta
# Maneja el funcionamiento del submenú ruleta
def ruleta():
    mostrarRuleta()
    opcion = input('Seleccione una opción: ')

    while opcion != 'b':
        if opcion == 'a':
            try:    
                af1 = int(input('Introduzca la afinidad con Persona A: '))
                af2 = int(input('Introduzca la afinidad con Persona B: '))
                af3 = int(input('Introduzca la afinidad con Persona C: '))

                while af1 + af2 + af3 != 100:
                    print('Los valores introducidos no suman 100, intente nuevamente.')
                    af1 = int(input('Introduzca la afinidad con Persona A: '))
                    af2 = int(input('Introduzca la afinidad con Persona B: '))
                    af3 = int(input('Introduzca la afinidad con Persona C: '))

                buffer = randint(0, 100)
                if buffer > 100 - af1:
                    print('Matcheaste con Persona A')
                elif buffer > 100 - af1 - af2:
                    print('Matcheaste con Persona B')
                elif buffer > 100 - af1 - af2 - af3:
                    print('Matcheaste con Persona C')

            except ValueError:
                print("Error: los valores ingresados tienen que ser numericos.")

            continuar()
            
        else:
            opcionInvalida()

        mostrarRuleta()
        opcion = input('Seleccione una opción: ')



# Funcionamiento del menú principal __________________________________________________________________________________________________________

# Manejador del menú principal
# En función de la opción introducida por el usuario, redirige a la función correspondiente
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
        elif opcion == '5':
            ruleta()
        else:
            opcionInvalida()

        mostrarMenuPrincipal()
        opcion = input('Seleccione una opción: ')




def main():
    sesion_iniciada = iniciarSesion()
    if not sesion_iniciada: # Si no se inició sesión exitosamente imprime el error y finaliza el programa
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
        continuar()

    else:
        menuPrincipal()

main()