from datos import *
from interfaz import *

estudianteActual = Estudiante()

def obtenerEdad(fecha): # toma el parametro fecha
    fecha = datetime.strptime(fecha, '%d-%m-%Y') # convierte un string (del formato dd-mm-aaaa) en un objeto datetime para operarlo como fecha
    fecha_actual = datetime.today() # ¿que dia es hoy?
    edad = fecha_actual.year - fecha.year # calcula la edad
    if (fecha_actual.month, fecha_actual.day) < (fecha.month, fecha.day): # Si el cumpleaños aún no sucedió le resta 1 a la diferencia de años
        edad -= 1
    return str(edad) # devuelve la edad como un str

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

def gestionarPerfil():
    mostrarGestionarPerfil()
    opcion = input('Seleccione una opción: ')

    while opcion != 'd':
        if opcion == 'a':
            mostrarPerfil()  
        """ elif opcion == 'b':
            editarDatosPersonales()
        elif opcion == 'c':
            eliminarPerfil()
        else:
            opcionInvalida() """

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

def menuEstudiante(estudiante):
    global estudianteActual
    estudianteActual = estudiante
    
    mostrarMenuEstudiante(estudianteActual.nombre)
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            gestionarPerfil()
        """ elif opcion == '2':
            gestionarCandidatos()
        elif opcion == '3':
            matcheos()
        elif opcion == '4':
            reportesEstadisticos()
        else:
            opcionInvalida() """

        mostrarMenuEstudiante()
        opcion = input('Seleccione una opción: ')