from datos import *
from interfaz import *

estudianteActual = Estudiante()

def menuEstudiante(): # menu principal
    
    mostrarMenuEst(estudianteActual.nombre)
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarPerfil()
        elif opcion == '2':
            gestionarCandidatos()
        elif opcion == '3':
            matcheos()
        elif opcion == '4':
            reportesEstadisticos()
        else:
            opcionInvalida()

        mostrarMenuEst()
        opcion = input('Seleccione una opción: ')

# Aux S
def obtenerEdad(estudiante): 
    fecha = estudiante.fechaNacimiento
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fecha.year
    if (fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day):
        edad -=1
    return str(edad)

def imprimirDatosDeEstudiante(estudiante):
    print("Nombre: " + estudiante.nombre + "\n" +
          "Fecha de nacimiento: " + estudiante.fechaNacimiento + "\n" +
          "Edad: " + obtenerEdad(estudiante.fechaNacimiento) + "\n" +
          "Biografía: " + estudiante.biografia + "\n" +
          "Hobbies: " + estudiante.hobbies)

def mostrarPerfil():
    limpiarPantalla()
    print("Estás viendo tu perfil")
    imprimirDatosDeEstudiante(estudianteActual)

    continuar()
# Aux F



# Gestion perfil S
def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != '0':
        if opcion == '1':
            mostrarPerfil()  
        elif opcion == '2':
            editarDatosPersonales()
        elif opcion == '3':
            eliminarPerfil()
        else:
            opcionInvalida() 

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

def editarDatosPersonales():
    mostrarEditarDatos()
    opcion = input('Seleccione una opcion: ')
    while opcion != '0':
        if opcion == '1':
            editarFechaNacimiento()
        elif opcion == '2':
            editarBiografia()
        elif opcion == '3':
            editarHobbies()
        else:
            opcionInvalida()
        mostrarEditarDatos()
        opcion = input('Seleccione una opcion: ')

def obtenerFecha(): # para edicion
    formato_correcto = False 
    while not formato_correcto: 
        fecha = input("Ingrese la nueva fecha de nacimiento (dd-mm-aaaa): ")
        try:
            dtfecha = datetime.strptime(fecha, "%d-%m-%Y") 
            if dtfecha > datetime.today(): 
                console.print("La fecha introducida no es válida. Intente nuevamente.", style='red') 
            else:
                formato_correcto = True

        except ValueError as ve:
            if "does not match format" in str(ve):
                console.print("El formato de fecha ingresado es incorrecto. Intente nuevamente.", style='red') 
            else:
                console.print("Fecha fuera de rango. Intente nuevamente.", style='red') 

    return fecha

def editarFechaNacimiento(estudiante):
    nueva_fecha = obtenerFecha() 
    estudiante.fechaNacimiento = nueva_fecha
    console.print(f"Fecha de nacimiento actualizada a {nueva_fecha.strftime('%d/%m/%Y')}", style='green')

    continuar()

def editarBiografia(estudiante):
    nueva_biografia = input("Ingrese la nueva biografía: ") 
    while nueva_biografia == '': 
        console.print('La biografía no puede estar vacía.', style='red')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudiante.biografia = nueva_biografia
    console.print('Su nueva biografía es: ', nueva_biografia, style='green')

    continuar()

def editarHobbies(estudiante):
    nuevo_hobbie = input("Ingrese los nuevos hobbies: ")
    while nuevo_hobbie == '':
        console.print('Los hobbies no pueden estar vacíos', style='red')
        nuevo_hobbie = input("Ingrese los nuevos hobbies: ")

    estudiante.hobbie = nuevo_hobbie 
    console.print("Sus nuevos hobbies son: ", nuevo_hobbie, style='green')

    continuar()

def eliminarPerfil():
    enConstruccion()
# Gestion perfil F


# Gestion candidatos S 
def gestionarCandidatos():
    mostrarGestionarCandidatos()
    opcion = input('Seleccione una opcion: ')
    while opcion != '0':
        if opcion == '1':
            verCandidatos()
        elif opcion == '2':
            reportarCandidato()
        else:
            opcionInvalida()

        mostrarGestionarCandidatos()
        opcion = input('Seleccione una opcion: ')

def verCandidatos(estudiantes, estudianteActual):
    hayCandidatos = False 

    for estudiante in estudiantes:
        if estudiante.estado and estudiante.id != estudianteActual.id:  
            edad = obtenerEdad(estudiante)  
            print(f"ID: {estudiante.id}")
            print(f"Nombre: {estudiante.nombre}")
            print(f"Email: {estudiante.email}")
            print(f"Fecha de Nacimiento: {estudiante.fechaNacimiento.strftime('%d/%m/%Y')}")
            print(f"Edad: {edad} años")
            print(f"Biografía: {estudiante.biografia}")
            print(f"Hobbies: {estudiante.hobbies}")
            print("-" * 40) 
            hayCandidatos = True  

    if not hayCandidatos:  
        print("No hay estudiantes disponibles para mostrar.")

    condicion = input('¿Quieres enviar un match? (escribe "si" para enviar o presiona ENTER para volver): ')
    if condicion.lower() == 'si':  
        eleccion = input('Escribe el ID de tu candidato: ')
        
        if any(estudiante.id == int(eleccion) for estudiante in estudiantes):  
            print(f"Match enviado para el estudiante con ID: {eleccion}.")
            # Logica de la clase likes 
            # ...

        else:
            print("El ID ingresado no existe en la lista de estudiantes.")

def reportarCandidato():
    


        

    
 
