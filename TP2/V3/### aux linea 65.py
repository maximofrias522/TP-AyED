### aux linea 65

### Validacion email INICIO
def buscarEstudiante(email): # toma email como parametro
    index = -1 # se usa el valor -1 para indicar que no se ha encontrado nada
    for i in range(MAX_ESTUDIANTES): # itera desde i hasta cantidad maxima de estudiantes -1 (7)
        if estudiantes[i][0] == email: # se verifica que el correo buscado este en la posicion [i](fila)[0](columna de emails) del array
            index = i # si se cumple la condicion, se actualiza el index a la posicion del mail

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
        print('Estudiante no encontrado, intente nuevamente: ')
        email = input('Introduzca su email: ')
        estudiante = buscarEstudiante(email)
        if estudiante == -1:
            moderador = buscarModerador(email)

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
        return validarContrasenaEstudiante(estudiante)
    else:
        return validarContrasenaModerador(moderador)
### Validar inicio de sesion FIN 

### Validacion de condiciones para log INICIO
def utnMatch():
    if estudiantesLen < 4 or moderadoresLen < 1: # si los estudiantes registrados son menos de 4 y los moderadores son menos de 1
        print('El inicio de sesión no está disponible.') # no se puede iniciar sesion
        continuar() # usa la funcion continuar
        return # no devuelve nada, terrible ortiva
    
    sesion_iniciada = iniciarSesion() # la asigna el valor de salida true or false de iniciarSesion
    if not sesion_iniciada: # Si no se inició sesión exitosamente imprime el error y finaliza el programa
        print('Se introdujo una contraseña incorrecta 3 veces y finalizó el programa.')
        continuar()

    else:
        menuPrincipal()
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
    print("Nombre: " + estudiantes[estudiante][1] + "\n" +
          "Fecha de nacimiento: " + estudiantes[estudiante][3] + "\n" +
          "Edad: " + obtenerEdad(estudiantes[estudiante][3]) + "\n" +
          "Biografía: " + estudiantes[estudiante][4] + "\n" +
          "Hobbies: " + estudiantes[estudiante][5])

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
    estudiantes[currentEstudiante][3] = nueva_fecha # se actualiza el array en la fila [currentEstudiante] columna [3] (posicion de fecha de nacimiento)

    continuar()
### Validacion de fecha de nacimiento al editar FIN

### Edicion de perfil Exepto fecha INICIO
def editarBiografia():
    nueva_biografia = input("Ingrese la nueva biografía: ") 
    while nueva_biografia == '': # mientras la biografia este vacia, la pide devuelta
        print('La biografía no puede estar vacía.')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudiantes[currentEstudiante][4] = nueva_biografia 
    print('Su nueva biografía es: ', nueva_biografia)

    continuar()

def editarHobbies():
    nuevo_hobbie = input("Ingrese los nuevos hobbies: ")
    while nuevo_hobbie == '':
        print('Los hobbies no pueden estar vacíos')
        nuevo_hobbie = input("Ingrese los nuevos hobbies: ")

    estudiantes [currentEstudiante][5] = nuevo_hobbie # si hasta este punto no entendiste el tema de las posiciones, deja la carrera
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
    opcion = input('Presione 1 si está seguro de que desea eliminar su perfil o 0 para volver: ')
    while opcion != '0' and opcion != '1': 
        opcionInvalida()
        opcion = input('Presione 1 si está seguro de que desea eliminar su perfil o 0 para volver: ')

    if opcion == 1: # si la opcion es 1, se recorre el array en la fila currentEstudiante y se borra todo 
        i = 0 
        seguir = True
        while seguir:
            try:
                estudiantes[currentEstudiante][i] = ['']
                i += 1
            except IndexError: 
                seguir = False
        print('Sus datos han sido eliminados correctamente')



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
    print("Bienvenido, ", estudiantes[currentEstudiante][1])
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("5. Ruleta")
    print("0. Salir del programa")

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
            estadisticos()
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
    print("¿Con quién quieres hacer match?")

    candidatos_disponibles = False  # verificar si hay candidatos para mostrar

    for idx, estudiante in enumerate(estudiantes):
        if estudiante[0] != '':  # Verificar si la fila no está vacía
            if idx != currentEstudiante:  # Excluir al estudiante actual
                candidatos_disponibles = True
                nombre = estudiante[1]
                email = estudiante[0]
                fecha_nacimiento = estudiante[3]
                biografia = estudiante[4]
                hobbies = estudiante[5]

                print(f"#{idx + 1}")
                print(f"Nombre: {nombre}")
                print(f"Email: {email}")
                print(f"Fecha de Nacimiento: {fecha_nacimiento}")
                print(f"Edad: {obtenerEdad(fecha_nacimiento)}")
                print(f"Biografía: {biografia}")
                print(f"Hobbies: {hobbies}")
                print("-" * 20)  # Separador entre estudiantes

    if not candidatos_disponibles:
        print("No hay candidatos disponibles para mostrar.") 

    seleccion = input("Ingresa el número de con quién quieres hacer match: ") #agregar logica de likes, modifican la matriz de likes
    continuar()
### Ver candidatos FIN

def reportar():
    enConstruccion()
    continuar()

def estadisticos():
    enConstruccion()
    enConstruccion()
    
### sign INICIO ######################################################################
def registrarEstudiante(): # MODULARIZAR ESTA FUNCIÓN
    global estudiantesLen, estudiantes
    if estudiantesLen == 8:
        print('El registro de estudiantes no está disponible')
        continuar()
        return
    
    datosEstudiante = [''] * 6
    datosEstudiante[0] = input('Introduzca su email: ')
    
    aux = 0
    while aux < estudiantesLen:
        if estudiantes[aux][0] == datosEstudiante[0]:
            aux = -1
            print('El estudiante ya está registrado.')
            continuar()
            return
        aux += 1

    datosEstudiante[1] = input('Introduzca su nombre: ')
    datosEstudiante[2] = input('Introduzca la contraseña: ')
    datosEstudiante[3] = obtenerFecha()# input('Introduzca su fecha de nacimiento(dd-mm-aaaa): ') # Añadir validación de fecha de nacimiento # probar que funcione
    datosEstudiante[4] = input('Introduzca su biografía: ')
    datosEstudiante[5] = input('Introduzca sus hobbies: ')

    index = buscarEstudiante('')

    estudiantes[index] = datosEstudiante
    estudiantesLen += 1

    print('El estudiante se registró exitosamente.')
    continuar()  

def registrarModerador(): # MODULARIZAR
    global moderadoresLen, moderadores
    datosModerador = [''] * 3
    datosModerador[0] = input('Introduzca su email: ')

    aux = 0
    while aux < moderadoresLen:
        if estudiantes[aux][0] == datosModerador[0]:
            print('El moderador ya está registrado.')
            continuar()
            return
        aux += 1

    datosModerador[1] = input('Introduzca su nombre: ')
    datosModerador[2] = input('Introduzca la contraseña: ')

    index = buscarModerador('')

    moderadores[index] = datosModerador
    moderadoresLen += 1

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
menuInicial() # EJECUCION

##################################################################################################################################################################

### Bonus track1 INICIO
def bonus_track_1():
    index = 0 # posicion 0 del arreglo   datosEstudiante[6] = input("Introduzca su sexo(M o F): ") # Agregar validacion M o F
    edades = [0] * estudiantesLen # se crea una arreglo unidimensional de la cantidad de estudiantes activos
    for est in estudiantes: # se itera por los estudiantes del array ### busca las edades, basicamente ### 
        if est[0] != '': # verifica que el primer elemento no este vacio
            edades[index] = obtenerEdad(est[3]) # si se cumple el if, se llama a la funcion obtenerEdad con el cuarto elemento de est como argumento
            index += 1 # el index se aumenta en 1 para que la proxima iteracion sea en el siguente elemento 

    for i in range(estudiantesLen): # se itera desde 0 hasta la cantidad minima de estudiantes para iniciar sesion-1 ### se ordena el arreglo, basicamente ###
        for j in range(0, estudiantesLen-i-1): # se itera desde 0 hasta (estudiantesLen-i)-2
            if edades[j] > edades[j+1]: # se verifica que el argumento actual sea mayor que el siguiente
                aux = edades[j+1] # Guardar el valor de edades[j+1]
                edades[j+1] = edades[j] # Mover edades[j] a la posición j+1
                edades[j] = aux # coloca el valor original de edades[j+1] en la posicion j
# Al final de cada pasada, el elemento más grande de la sección no ordenada se mueve a su posición final.

    for i in range(estudiantesLen): # se itera desde 0 hasta estudiantesLen-1
        if edades[i] + 1 != edades[i + 1]: # se verifica que los elementos consecutivos no sean numeros consecutivos  
            print(f'Existe un hueco entre {edades[i]} y {edades[i+1]}')  
### Bonus track1 FIN

### Bonus track2 INICIO
def bonus_track_2(): # lógica: el primer estudiante puede matchear con estudiantesLen -1 estudiante (todos menos él mismo),
                     # el segundo también tiene estudiantesLen -1 matcheos disponibles pero no se cuenta el matcheo que se
                     # registró con el primer estudiante, se puede probar que la secuencia es
                     # e_n = estudiantesLen - n, estudiantesLen >= n >= 1
    acum = 0
    for i in range(estudiantesLen): # se itera desde 0 hasta estudiantesLen-1
        acum += estudiantesLen - i # se suma estudiantesLen - i en cada iteracion, se resta el iterador para que no cuente matcheos anteriores 

    print(f'Hay {acum} matcheos posibles')
### Bonus track2 FIN