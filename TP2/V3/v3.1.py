### Detalles de integrantes y del tp en general en este repositorio https://github.com/maximofrias522/TP-AyED
### COMENTARIO PARA PROFESORA ### Debajo del cartel hay una funcion para autogenerar usuarios, si usted quiere probar el ingreso de datos y la validacion de cantidad de usuarios
# importar librerias 
import os 
import random  
from datetime import datetime
from maskpass import askpass

# declarar arrays de estudiantes y moderadores

MAX_ESTUDIANTES = 8
MIN_ESTUDIANTES = 4
MAX_MODERADORES = 4
MIN_MODERADORES = 1

# Estructuras de datos para estudiantes y moderadores
estudiantes = [[""]*8 for _ in range(MAX_ESTUDIANTES)]  # Cada estudiante tiene 8 campos | id - mail - contraseña - estado (1 habilitado/0 inhabilitado) - nombre - fecha de nacimiento - hobbies - biografia 
moderadores = [[""]*3 for _ in range(MAX_MODERADORES)]  # Cada moderador tiene 4 campoos | mail - contraseña - nombre

# Generador de IDs autoincrementales
for idx in range(MAX_ESTUDIANTES):
    estudiantes[idx][0] = f"{idx + 1:02d}"  # Genera IDs en formato "01", "02", ..., "08"
# La expresión f"{idx + 1:02d}" asegura que los números sean formateados como cadenas de dos dígitos, es decir, "01" a "08", para mantener consistencia en el formato de los IDs.

likes = [[random.choice(['0', '1']) for _ in range(MAX_ESTUDIANTES)] for _ in range(MAX_ESTUDIANTES)] # crea una matriz de 8x8 y la llena aleatoriamente de 0s y 1s // row = recibidos y column = dados
# likes = [['0']*8 for _ in range(MAX_ESTUDIANTES)] # esto era para test vacio

def imprimirLikes(likes):
    for fila in likes:
        print(fila)



reportes = [[''] * 3 for _ in range(8)] # matriz de 3x8, id del reportado, motivo, estado del reporte (0,1,2)

# valor asignado para sesion no iniciada
currentEstudiante = -1
currentModerador = -1

### Cartel

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

### Cartel

# Generador de datos de prueba 
def generarDatosPrueba():
    CANT_ESTUDIANTES = random.randint(MIN_ESTUDIANTES, MAX_ESTUDIANTES)
    CANT_MODERADORES = random.randint(MIN_MODERADORES, MAX_MODERADORES)

    nombres_estudiantes = ["Juan", "Ana", "Luis", "Marta", "Pedro", "Lucía", "Carlos", "Sofía"]
    nombres_moderadores = ["Carlos", "Elena", "Raúl", "Gabriela"]
    hobbies_list = ["leer", "viajar", "correr", "dibujar", "nadar"]
    biografia_list = ["Amo la tecnología.", "Me gusta la lectura.", "Apasionado por los deportes.", "Artista en mi tiempo libre.", "Explorador del mundo."]

    # Generar datos para estudiantes
    for i in range(CANT_ESTUDIANTES):
        estudiantes[i][1] = f"estudiante{i}@ayed.com"  # Email
        estudiantes[i][2] = f"pass{i}"  # Contraseña
        estudiantes[i][3] = "ACTIVO" if i < 4 else "INACTIVO"  # Estado
        estudiantes[i][4] = random.choice(nombres_estudiantes)  # Nombre
        estudiantes[i][5] = f"{random.randint(1, 28):02}-{random.randint(1, 12):02}-{random.randint(1990, 2005)}"  # Fecha de nacimiento
        estudiantes[i][6] = random.choice(hobbies_list)  # Hobbies
        estudiantes[i][7] = random.choice(biografia_list)  # Biografía

    # Generar datos para moderadores
    for i in range(CANT_MODERADORES):
        moderadores[i][0] = f"moderador{i}@ayed.com"  # Email
        moderadores[i][1] = f"pass{i}"  # Contraseña
        moderadores[i][2] = random.choice(nombres_moderadores)  # Nombre


# Generar datos de prueba
generarDatosPrueba()

### Validacion email INICIO
def buscarEstudiante(email): 
    index = -1 
    for i in range(MAX_ESTUDIANTES): 
        if estudiantes[i][1] == email: 
            index = i 

    return index # aca o devuelve el valor i encontrado o -1 en caso de no encontrar nada

def buscarModerador(email):
    index = -1
    for i in range(MAX_MODERADORES):
        if moderadores[i][0] == email:
            index = i

    return index
### Validacion email FIN

### Validacion contraseña INICIO
def validarContrasenaEstudiante(index): # toma index como parametro
    global currentEstudiante # se establece currentEstudiante como variable global
    intentos = 3 # se establece un numero maximo de intentos

    while intentos > 0: # mientras los intentos sean mayores que 0
        contrasena = askpass(prompt='Introduzca la contraseña: ') # se pide la contraseña
        if estudiantes[index][2] == contrasena: # si en el array estudiantes [index](fila del mail)[2](posicion de la contraseña) == contraseña
            currentEstudiante = index # se actualiza valor de index a la posicion encontrada
            return True # se retorna true
        else: # en otro caso, se resta un intento y si los ententos son mayores que 0 se menciona que la contraseña es incorrecta
            intentos -= 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')

    if intentos == 0: # si los intentos llegan a 0, la funcion retorna false y se cierra el programa
        return False

def validarContrasenaModerador(index):
    global currentModerador
    intentos = 3

    while intentos > 0:
        contrasena = askpass(prompt='Introduzca la contraseña: ')
        if moderadores[index][1] == contrasena:
            currentModerador = index
            return True
        else:
            intentos -= 1
            if intentos > 0:
                print('Contraseña incorrecta, intente nuevamente.')

    if intentos == 0:
        return False    
### Validacion contraseña FIN

### Validar inicio de sesion INICIO
def iniciarSesion():
    email = input('Introduzca su email: ')
    estudiante = buscarEstudiante(email)
    moderador = buscarModerador(email)
    
    while estudiante == -1 and moderador == -1:
        print('Usuario no encontrado, intente nuevamente: ')
        email = input('Introduzca su email: ')
        estudiante = buscarEstudiante(email)
        if estudiante == -1:
            moderador = buscarModerador(email)

    if estudiante != -1:
        if estudiantes[estudiante][3] == 'INACTIVO':
            print("Tu cuenta de estudiante ha sido inhabilitada. Para más información, contáctate con los administradores.")
            continuar()
            menuInicial()
            return False, None  # No se puede iniciar sesión si la cuenta está inactiva

    if estudiante != -1 and moderador != -1:
        aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')
        while aux not in ['0', '1']:
            opcionInvalida()
            aux = input('Está registrado como estudiante y moderador, presione 0 si desea iniciar como estudiante o 1 si desea iniciar sesión como moderador: ')

        if aux == '1':
            estudiante = -1
        else:
            moderador = -1

    if estudiante != -1:
        if validarContrasenaEstudiante(estudiante):
            return True, "estudiante"
        else:
            return False, None
  
    else:
        if validarContrasenaModerador(moderador):
            return True, "moderador"
        else:
            return False, None
### Validar inicio de sesion FIN 

### Validacion de condiciones para log INICIO
def utnMatch():
    if MIN_ESTUDIANTES < 4 or MIN_MODERADORES < 1: # si los estudiantes registrados son menos de 4 y los moderadores son menos de 1
        print('El inicio de sesión no está disponible.') # no se puede iniciar sesion
        continuar() # usa la funcion continuar
        return # no devuelve nada, terrible ortiva
    
    sesion_iniciada, tipo_usuario = iniciarSesion() # la asigna el valor de salida bool de iniciarSesion
    if not sesion_iniciada: # Si no se inició sesión exitosamente imprime el error y finaliza el programa
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
        continuar()

    else:
        if tipo_usuario == "estudiante":
            menuPrincipal()
        elif tipo_usuario == "moderador":
            menuMod()
### Validacion de condiciones para log FIN

### Funciones auxiliares INICIO
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear') # si el sistema es win usa el comando cls, en caso contrario asume que es unix y usa clear
    print(asciiart) # zarpado cartel

def continuar():
    input("Presione enter para continuar...") # flaco te imprime un continuar, no es tan dificil

def opcionInvalida():
    print("Error: la opcion ingresada no es valida.") # error, sos un pelotudo. ingresa lo que te pido
    continuar()

def enConstruccion():
    limpiarPantalla() 
    print("En construcción.")
    continuar()
### Funciones auxiliares FIN

### Calculo de edad a partir de la fecha INICIO
def obtenerEdad(fecha): # toma el parametro fecha
    fecha = datetime.strptime(fecha, '%d-%m-%Y') # convierte un string (del formato dd-mm-aaaa) en un objeto datetime para operarlo como fecha
    fecha_actual = datetime.today() # ¿que dia es hoy?
    edad = fecha_actual.year - fecha.year # calcula la edad
    if (fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day): # Si el cumpleaños aún no sucedió le resta 1 a la diferencia de años
        edad -= 1
    return str(edad) # devuelve la edad como un str
### Calculo de edad a partir de la fecha FIN

### Ver perfil INICIO
def imprimirDatosDeEstudiante(estudiante):
    print("Nombre: " + estudiantes[estudiante][4] + "\n" +
          "Fecha de nacimiento: " + estudiantes[estudiante][5] + "\n" +
          "Edad: " + obtenerEdad(estudiantes[estudiante][5]) + "\n" +
          "Biografía: " + estudiantes[estudiante][7] + "\n" +
          "Hobbies: " + estudiantes[estudiante][6])

def mostrarPerfil():
    limpiarPantalla()
    print("Estás viendo tu perfil")
    imprimirDatosDeEstudiante(currentEstudiante)

    continuar()
### Ver perfil FIN

### Validacion de fecha de nacimient al editar INICIO
def obtenerFecha():
    formato_correcto = False # se predefine que el formato esta mal
    while not formato_correcto: # mientras el formato no sea correcto, pide ingresar la fecha  
        fecha = input("Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ")
        try:
            dtfecha = datetime.strptime(fecha, "%d-%m-%Y") # convierte un string (del formato dd-mm-aaaa) en un objeto datetime para operarlo como fecha 
            if dtfecha > datetime.today(): 
                print("La fecha introducida no es válida. Intente nuevamente.") # Si la fecha introducida es del futuro devuelve un mensaje de error
            else:
                formato_correcto = True

        except ValueError as ve:
            if "does not match format" in str(ve):
                print("El formato de fecha ingresado es incorrecto. Intente nuevamente.") # Si la fecha se introdujo en formato incorrecto devuelve un mensaje de error
            else:
                print("Fecha fuera de rango. Intente nuevamente.") # Si la fecha introducida está fuera de rango devuelve un mensaje de error

    return fecha

def editarFechaNacimiento():
    nueva_fecha = obtenerFecha() # se asigna el valor retornado de obtenerFecha a nueva_fecha
    estudiantes[currentEstudiante][5] = nueva_fecha # se actualiza el array en la fila [currentEstudiante] columna [3] (posicion de fecha de nacimiento)

    continuar()
### Validacion de fecha de nacimiento al editar FIN

### Edicion de perfil Exepto fecha INICIO
def editarBiografia():
    nueva_biografia = input("Ingrese la nueva biografía: ") 
    while nueva_biografia == '': # mientras la biografia este vacia, la pide devuelta
        print('La biografía no puede estar vacía.')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudiantes[currentEstudiante][7] = nueva_biografia 
    print('Su nueva biografía es: ', nueva_biografia)

    continuar()

def editarHobbies():
    nuevo_hobbie = input("Ingrese los nuevos hobbies: ")
    while nuevo_hobbie == '':
        print('Los hobbies no pueden estar vacíos')
        nuevo_hobbie = input("Ingrese los nuevos hobbies: ")

    estudiantes [currentEstudiante][6] = nuevo_hobbie # si hasta este punto no entendiste el tema de las posiciones, deja la carrera
    print("Sus nuevos hobbies son: ", nuevo_hobbie)

    continuar()
### Edicion de perfil Exepto fecha FIN

### Menu editar datos personales INICIO
def mostrarEditarDatosPersonales():
    limpiarPantalla()
    print("Estas editando tus datos personales")
    print("¿Qué datos deseas editar?")
    print("a. Fecha de nacimiento")
    print("b. Biografía")
    print("c. Hobbies")
    print("d. Volver")

def editarDatosPersonales(): # logica del menu
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
### menu editar datos personales FIN

### Eliminar perfil INICIO
def eliminarPerfil():
    limpiarPantalla()
    print("¿Estas seguro que deseas eliminar tu perfil? Esta accion no tiene vuelta atras!")

    nuevo_estado = "INACTIVO"

    valid = input("Ingresa [si] para continuar o presiona [ENTER] para volver: ")
    if valid == 'si':
        estudiantes[currentEstudiante][3] = "INACTIVO"
        print("Su usuario ha sido deshabilitado, gracias por usar nuestro sistema!")
        continuar()
        menuInicial()
    else: 
        gestionarPerfil()

### eliminar perfil fin

### Gestionar perfil INICIO
def mostrarGestionarPerfil():
    limpiarPantalla()
    print("Estas gestionando tu perfil")
    print("a. Editar mis datos personales")
    print("b. Ver mi perfil")
    print("c. Eliminar mi perfil")
    print("d. Volver")

def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != 'd':
        if opcion == 'a':
            editarDatosPersonales()
        elif opcion == 'b':
            mostrarPerfil()  
        elif opcion == 'c':
            eliminarPerfil()
        else:
            opcionInvalida()

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')
### Gestionar perfil FIN

### Gestionar candidatos INICIO
def mostrarGestionarCandidatos():
    limpiarPantalla()
    print("Gestionando candidatos")
    print("a. Ver candidatos disponibles")
    print("b. Reportar a un candidato")
    print("c. Volver")

def gestionarCandidatos():
    mostrarGestionarCandidatos()
    opcion = input('Seleccione una opción: ')
    
    while opcion != 'c':
        if opcion == 'a':
            verCandidatos()
        elif opcion == 'b':
            reportar()
        else:
            opcionInvalida()

        mostrarGestionarCandidatos()
        opcion = input('Seleccione una opción: ')
### Gestionar candidatos FIN

### Menu principal INICIO
def mostrarMenuPrincipal():
    limpiarPantalla()
    print("Bienvenido, ", estudiantes[currentEstudiante][4])
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir")

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
            mostrarEstadisticos()
        elif opcion == '5':
            enConstruccion()
        else:
            opcionInvalida()

        mostrarMenuPrincipal()
        opcion = input('Seleccione una opción: ')
### Menu principal FIN

### Ver candidatos INICIO
def verCandidatos():
    limpiarPantalla()

    #imprimirLikes(likes)
    print("¿Con quién quieres hacer match?")

    candidatos_disponibles = False  # verificar si hay candidatos para mostrar
    ids = [''] * MAX_ESTUDIANTES  
    index = 0

    for idx, estudiante in enumerate(estudiantes):
        if estudiante[0] != '':  # Verificar si la fila no está vacía
            if estudiante[3] == 'ACTIVO' and idx != currentEstudiante:  # Excluir al estudiante actual y sólo mostrar activos
                if estudiante[1] and estudiante[5]:  # Verificar si el email y la fecha de nacimiento no están vacíos
                    candidatos_disponibles = True
                    nombre = estudiante[4]
                    email = estudiante[1]
                    fecha_nacimiento = estudiante[5]
                    biografia = estudiante[7]
                    hobbies = estudiante[6]
                    idl = estudiante[0]

                    print(f"ID: {idl}")
                    print(f"Nombre: {nombre}")
                    print(f"Email: {email}")
                    print(f"Fecha de Nacimiento: {fecha_nacimiento}")
                    print(f"Edad: {obtenerEdad(fecha_nacimiento)}")
                    print(f"Biografía: {biografia}")
                    print(f"Hobbies: {hobbies}")
                    print("-" * 20)  # Separador entre estudiantes

                    ids[index] = idl
                    index += 1

    if not candidatos_disponibles:
        print("No hay candidatos disponibles para mostrar.")

    seleccion = input("Ingresa el ID de con quién quieres hacer match: ")  # Agregar lógica de likes, modificar la matriz de likes
    if len(seleccion) == 2 and int(seleccion) >= 1 and int(seleccion) <= MAX_ESTUDIANTES:
        for idx, estudiante in enumerate(estudiantes):
            if estudiante[0] == seleccion:
                print("Solicitud enviada a " + estudiante[4])
                likes[currentEstudiante][idx] = '1'

                # imprimirLikes(likes)
                continuar()
                return
                # menuPrincipal()
        else:
            print("Estudiante no encontrado")
            continuar()
            # menuPrincipal()
            return

    # print("Solicitud de match enviada!")
    # continuar()
### Ver candidatos FIN

def reportar():
    limpiarPantalla()
    print("Menu de reportes:")
    estado_nuevo_reporte = "0"

    valid = input("Ingresa [si] para continuar o presiona [ENTER] para volver: ")
    if valid == 'si': 
        idp = input("Ingresa el ID del usuario a reportar: ")
        # Validación del formato
        if len(idp) == 2 and int(idp) >= 1 and int(idp) <= MAX_ESTUDIANTES:
            for idx, estudiante in enumerate(estudiantes):
                if estudiante[0] == idp:
                    print("Datos usuario: ")
                    print("Email: " + estudiante[1])
                    print("Nombre: " + estudiante[4])
                    print("¿Es el usuario a reportar?")
                    validar = input("Ingresa [si] para continuar o presiona [ENTER] para volver: ")
                    if validar == 'si':
                        motivo = input("¿Porque quiere reportar a este usuario? Escriba su respuesta: ")
                        print(f"Reportando usuario con ID {idp}")

                        # Guardar el reporte en la matriz reportes
                        for i in range(len(reportes)):
                            if reportes[i][0] == '':  # Buscar la primera fila vacía
                                reportes[i][0] = idp
                                reportes[i][1] = motivo
                                reportes[i][2] = '0'  # Estado inicial del reporte
                                print("Reporte guardado exitosamente")
                                continuar()
                                return

                    else:
                        return
                        # menuPrincipal()
        else:
            print("El ID ingresado no es válido o no existe.")
            continuar()
            return
            # menuPrincipal()  
            
    else:
        return
        # menuPrincipal()

def mostrarEstadisticos():
    likes_no_respondidos_por_nos = likesNoRespondidosPorNos(likes, currentEstudiante)
    likes_no_respondidos_por_otros = likesQueNoNosRespondieron(likes, currentEstudiante)
    porcentaje_likes_dobles = likesDobles(likes)
    limpiarPantalla()
    print("Estadisticas:")
    print(f"\nUsuario {estudiantes[currentEstudiante][4]} no respondio likes a: {likes_no_respondidos_por_nos} usuarios")
    print(f"\nAl usuario {estudiantes[currentEstudiante][4]} no le respondieron el like: {likes_no_respondidos_por_otros} usuarios")
    print(f'\nPorcentaje de likes dobles respecto al total de likes: {porcentaje_likes_dobles:.2f}%')

    continuar()
    menuPrincipal()

# likes recibidos y no respondidos por nos
def likesNoRespondidosPorNos(likes, currentEstudiante):
    likes_no_respondidos_por_nos = 0
    
    for i in range(MAX_ESTUDIANTES):
        if i != currentEstudiante:  # Excluir a currentEstudiante
            if likes[i][currentEstudiante] == '0' and likes[currentEstudiante][i] == '1':
                likes_no_respondidos_por_nos += 1
            else:
                continue     

    return likes_no_respondidos_por_nos

# likes dados y no recibidos
def likesQueNoNosRespondieron(likes, currentEstudiante):
    likes_no_respondidos_por_otros = 0
    likes_totales = 0

    for i in range(MAX_ESTUDIANTES):
        for j in range(MAX_ESTUDIANTES):
            if likes [j][i] == 1:
                likes_totales += 1
            else:
                continue


    for i in range(MAX_ESTUDIANTES):
        if i != currentEstudiante:  # Excluir a currentEstudiante
            if likes[i][currentEstudiante] == '1' and likes[currentEstudiante][i] == '0':
                likes_no_respondidos_por_otros += 1
            else:
                continue

    return likes_no_respondidos_por_otros

def likesDobles(likes):
    likes_dobles = 0
    likes_totales = 0

    # Contar el total de likes en la matriz
    for i in range(MAX_ESTUDIANTES):
        for j in range(MAX_ESTUDIANTES):
            if likes[j][i] == '1':
                likes_totales += 1
    
    # Contar la cantidad de likes dobles
    for i in range(MAX_ESTUDIANTES):
        for j in range(MAX_ESTUDIANTES):
            if likes[i][j] == '1' and likes[j][i] == '1':
                likes_dobles += 1

    # Calcular el porcentaje de likes dobles
    if likes_totales == 0:
        return 0  # Evitar división por cero

    porcentaje_likes_dobles = (likes_dobles / likes_totales) * 100
    return porcentaje_likes_dobles
    
### sign INICIO ######################################################################
def registrarEstudiante(): # MODULARIZAR ESTA FUNCIÓN
    global MIN_ESTUDIANTES, estudiantes
    if MIN_ESTUDIANTES == 8:
        print('El registro de estudiantes no está disponible')
        continuar()
        return
    
    datosEstudiante = [''] * 8
    datosEstudiante[1] = input('Introduzca su email: ')
    
    aux = 0
    while aux < MIN_ESTUDIANTES:
        if estudiantes[aux][1] == datosEstudiante[1]:
            aux = -1
            print('El estudiante ya está registrado.')
            continuar()
            return
        aux += 1

    datosEstudiante[4] = input('Introduzca su nombre: ')
    datosEstudiante[2] = input('Introduzca la contraseña: ')
    datosEstudiante[5] = obtenerFecha()# input('Introduzca su fecha de nacimiento(dd-mm-aaaa): ') # Añadir validación de fecha de nacimiento # probar que funcione
    datosEstudiante[7] = input('Introduzca su biografía: ')
    datosEstudiante[6] = input('Introduzca sus hobbies: ')

    index = buscarEstudiante('')

    estudiantes[index] = datosEstudiante
    MIN_ESTUDIANTES += 1

    print('El estudiante se registró exitosamente.')
    continuar()  

def registrarModerador(): # MODULARIZAR
    global MIN_MODERADORES, moderadores
    datosModerador = [''] * 3
    datosModerador[0] = input('Introduzca su email: ')

    aux = 0
    while aux < MIN_MODERADORES:
        if estudiantes[aux][0] == datosModerador[0]:
            print('El moderador ya está registrado.')
            continuar()
            return
        aux += 1

    datosModerador[2] = input('Introduzca su nombre: ')
    datosModerador[1] = input('Introduzca la contraseña: ')

    index = buscarModerador('')

    moderadores[index] = datosModerador
    MIN_MODERADORES += 1

    print('El moderador se registró exitosamente.')
    continuar()
### sign FIN #########################################################################

# empezar

### Menu registro INICIO
def mostrarRegistrarse():
    limpiarPantalla()
    print('a. Registrarse como estudiante')
    print('b. Registrarse como moderador')
    print('c. Volver')

def registrarse():
    mostrarRegistrarse()
    opcion = input('Seleccione una opción: ')

    while opcion != 'c':
        if opcion == 'a':
            registrarEstudiante()
        elif opcion == 'b':
            registrarModerador()
        else:
            opcionInvalida()
        

        mostrarRegistrarse()
        opcion = input('Seleccione una opción: ')
### Menu registro FIN

### Menu inicial INICIO
def mostrarMenuInicial():
    limpiarPantalla()
    print('1. Iniciar sesión')
    print('2. Registrarse')
    print('0. Salir')

def menuInicial():
    mostrarMenuInicial()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            utnMatch()
        elif opcion == '2':
            registrarse()
        else:
            opcionInvalida()
        

        mostrarMenuInicial()
        opcion = input('Seleccione una opción: ')
### Menu inicial FIN        

################# modder    

# menu MOD 
def mostrarMenuMod():
    limpiarPantalla()
    print("Bienvenido, ", moderadores[currentModerador][2])
    print("Menu de Moderador:")
    print("1. Gestionar usuarios")
    print("2. Gestionar reportes")
    print("3. Reportes estadisticos")
    print("0. Salir")

def menuMod():
    mostrarMenuMod()
    opcion = input('Seleccione una opcion: ')

    while opcion != '0':
        if opcion == '1':
            gestionarUsuarios()
        elif opcion == '2':
            gestionarReportes()
        elif opcion == '3':
            enConstruccion()
        else:
            opcionInvalida()

        mostrarMenuMod()
        opcion = input('Seleccione una opcion: ')

# menu MOD sub 1
def mostrarGestionarUsuarios():
    limpiarPantalla()
    print("Gestionando usuarios:")
    print("a. Desactivar un usuario")
    print("b. Volver")

# menu MOD sub 2
def mostrarGestionReportes():
    limpiarPantalla()
    print("Gestionando reportes:")
    print("a. Ver reportes") 
    print("b. Volver")

def gestionarReportes():
    mostrarGestionReportes()
    opcion = input("Seleccione una opcion: ")

    while opcion != 'b':
        if opcion == 'a':
            verReportes()
        else:
            opcionInvalida()
        
        mostrarGestionReportes()
        opcion = input("Seleccione una opcion: ")

# menu MOD sub 2 sub a
def verReportes(): # aca se debe mostrar con alguna forma de tabla los reportes para visualizar bien la matriz
    limpiarPantalla()
    print("Reportes registrados:")
    
    # Encabezados de la tabla
    print(f"{'Número':<10} {'ID Reportado':<15} {'Motivo':<60} {'Estado':<10}")
    print("=" * 100)  # Línea divisoria
    
    num = 1
    # Mostrar cada reporte en la tabla
    for idx, reporte in enumerate(reportes):
        if reporte[0] != '':  # Verificar si la fila no está vacía
            id_reportado = reporte[0]
            motivo = reporte[1]
            estado = reporte[2]
            print(f"{num:<10} {id_reportado:<15} {motivo:<60} {estado:<10}")
            num += 1
    
    print("=" * 100)  # Línea divisoria

    # Solicitar al usuario seleccionar un reporte por su ID
    seleccion = input("Ingrese el numero de reporte que desea modificar el estado o [0] para volver: ")
    
    if int(seleccion) >= 0 and int(seleccion) <= MAX_ESTUDIANTES:
        seleccion = int(seleccion) - 1  # Convertir a índice de lista
        if 0 <= seleccion < len(reportes):
            id_reporte = reportes[seleccion][0]
            nuevo_estado = input(f"Ingrese el nuevo estado para el reporte ID (1 o 2):{id_reporte}: ")
            if nuevo_estado == '1':
                reportes[seleccion][2] = "1"
            elif nuevo_estado == "2":
                reportes[seleccion][2] = "2"
            else:
                print("Formato incorrecto")
                continuar()
                return
                # gestionarReportes()

            print(f"Estado del reporte {id_reporte} actualizado exitosamente.")
            continuar()
            return
            # gestionarReportes()
        else:
            print("Número de reporte inválido.")
    elif seleccion == 0:
        print("Volver")
        continuar()
        return
        # gestionarReportes()
    else:
        continuar()
        return
    
    # gestionarReportes()

def mostrarGestionarUsuarios():
    limpiarPantalla()
    print("Gestionando usuarios")
    print("a. Desactivar usuario")
    print("b. Volver")

def gestionarUsuarios():
    mostrarGestionarUsuarios()
    opcion = input("Seleccione una opcion: ")

    while opcion != 'b':
        if opcion == 'a':
            desactivarUsuario()
        else:
            opcionInvalida()
        
        mostrarGestionarUsuarios()
        opcion = input("Seleccione una opcion: ")

def desactivarUsuario():
    limpiarPantalla()
    print("Menu de desactivacion")

    nuevo_estado = "INACTIVO"

    valid = input("Ingresa [si] para continuar o presiona [ENTER] para volver: ")
    if valid == 'si': 
        idp = input("Ingresa el ID del usuario a desactivar: ")
        
        # Validación del formato
        if len(idp) == 2 and int(idp) >= 1 and int(idp) <= MAX_ESTUDIANTES:
            for idx, estudiante in enumerate(estudiantes):
                if estudiante[0] == idp:
                    print("Datos usuario: ")
                    print("Email: " + estudiante[1])
                    print("Nombre: " + estudiante[4])
                    print("¿Es el usuario a desactivar?")
                    validar = input("Ingresa [si] para continuar o presiona [ENTER] para volver: ")
                    if validar == 'si':
                        print(f"Desactivando usuario con ID {idp}")
                        estudiante[3] = nuevo_estado
                        # print(estudiante[3])
                        continuar()
                    else:
                        return
                        # gestionarUsuarios()
        else:
            print("El ID ingresado no es válido o no existe.")
            continuar()
            return
            # gestionarUsuarios()  
            
    else:
        return
        # gestionarUsuarios()

menuInicial() # EJECUCION
##################################################################################################################################################################

### Bonus track1 INICIO
def bonus_track_1():
    index = 0 # posicion 0 del arreglo   datosEstudiante[6] = input("Introduzca su sexo(M o F): ") # Agregar validacion M o F
    edades = [0] * MIN_ESTUDIANTES # se crea una arreglo unidimensional de la cantidad de estudiantes activos
    for est in estudiantes: # se itera por los estudiantes del array ### busca las edades, basicamente ### 
        if est[0] != '': # verifica que el primer elemento no este vacio
            edades[index] = obtenerEdad(est[3]) # si se cumple el if, se llama a la funcion obtenerEdad con el cuarto elemento de est como argumento
            index += 1 # el index se aumenta en 1 para que la proxima iteracion sea en el siguente elemento 

    for i in range(MIN_ESTUDIANTES): # se itera desde 0 hasta la cantidad minima de estudiantes para iniciar sesion-1 ### se ordena el arreglo, basicamente ###
        for j in range(0, MIN_ESTUDIANTES-i-1): # se itera desde 0 hasta (MIN_ESTUDIANTES-i)-2
            if edades[j] > edades[j+1]: # se verifica que el argumento actual sea mayor que el siguiente
                aux = edades[j+1] # Guardar el valor de edades[j+1]
                edades[j+1] = edades[j] # Mover edades[j] a la posición j+1
                edades[j] = aux # coloca el valor original de edades[j+1] en la posicion j
# Al final de cada pasada, el elemento más grande de la sección no ordenada se mueve a su posición final.

    for i in range(MIN_ESTUDIANTES): # se itera desde 0 hasta MIN_ESTUDIANTES-1
        if edades[i] + 1 != edades[i + 1]: # se verifica que los elementos consecutivos no sean numeros consecutivos  
            print(f'Existe un hueco entre {edades[i]} y {edades[i+1]}')  
### Bonus track1 FIN

### Bonus track2 INICIO
def bonus_track_2(): # lógica: el primer estudiante puede matchear con MIN_ESTUDIANTES -1 estudiante (todos menos él mismo),
                     # el segundo también tiene MIN_ESTUDIANTES -1 matcheos disponibles pero no se cuenta el matcheo que se
                     # registró con el primer estudiante, se puede probar que la secuencia es
                     # e_n = MIN_ESTUDIANTES - n, MIN_ESTUDIANTES >= n >= 1
    acum = 0
    for i in range(MIN_ESTUDIANTES): # se itera desde 0 hasta MIN_ESTUDIANTES-1
        acum += MIN_ESTUDIANTES - i # se suma MIN_ESTUDIANTES - i en cada iteracion, se resta el iterador para que no cuente matcheos anteriores 

    print(f'Hay {acum} matcheos posibles')
### Bonus track2 FIN