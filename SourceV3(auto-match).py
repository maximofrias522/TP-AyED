import os
import getpass
import time
from datetime import datetime

# Funcion para limpiar la pantalla 
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Datos de los estudiantes
estudiantes = [
    {
        "email": "estudiante1@ayed.com",
        "contraseña": "111222",
        "nombre": "Estudiante 1",
        "fecha_nacimiento": "2000-01-01",
        "biografia": "Soy el estudiante 1 y estoy emocionado por aprender.",
        "hobbies": ["Fútbol", "Lectura"]
    },
    {
        "email": "estudiante2@ayed.com",
        "contraseña": "333444",
        "nombre": "Estudiante 2",
        "fecha_nacimiento": "2001-02-02",
        "biografia": "Soy el estudiante 2 y me encanta programar.",
        "hobbies": ["Ajedrez", "Videojuegos"]
    },
    {
        "email": "estudiante3@ayed.com",
        "contraseña": "555666",
        "nombre": "Estudiante 3",
        "fecha_nacimiento": "2002-03-03",
        "biografia": "Soy el estudiante 3 y me gusta viajar.",
        "hobbies": ["Senderismo", "Fotografía"]
    }
]

# Funcion para calcular la edad a partir de la fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Menu principal
def mostrar_menu_principal():
    limpiar_pantalla()
    print("Menú Principal:")
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadísticos")
    print("0. Salir")

# Modulo para gestionar el perfil del estudiante
def gestionar_perfil(estudiante):
    limpiar_pantalla()
    print("Gestionando perfil de", estudiante['nombre'])
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")
    print("c. Volver")

# Modulo para editar datos personales
def editar_datos_personales(estudiante):
    limpiar_pantalla()
    print("Editando datos personales de", estudiante['nombre'])
    print("¿Qué datos deseas editar?")
    print("1. Fecha de nacimiento")
    print("2. Biografía")
    print("3. Hobbies")
    print("4. Volver")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nueva_fecha_nacimiento = input("Introduce la nueva fecha de nacimiento (YYYY-MM-DD): ")
        estudiantes[estudiantes.index(estudiante)]['fecha_nacimiento'] = nueva_fecha_nacimiento
        print("Fecha de nacimiento actualizada correctamente.")
    elif opcion == "2":
        nueva_biografia = input("Introduce la nueva biografía: ")
        estudiantes[estudiantes.index(estudiante)]['biografia'] = nueva_biografia
        print("Biografía actualizada correctamente.")
    elif opcion == "3":
        nuevos_hobbies = input("Introduce los nuevos hobbies separados por comas: ")
        nuevos_hobbies = nuevos_hobbies.split(',')
        estudiantes[estudiantes.index(estudiante)]['hobbies'] = nuevos_hobbies
        print("Hobbies actualizados correctamente.")
    elif opcion == "4":
        return
    else:
        en_construccion()

    input("Presiona Enter para continuar...")

# Modulo para gestionar candidatos
def gestionar_candidatos():
    limpiar_pantalla()
    print("Gestionando candidatos")
    print("a. Ver candidatos")
    print("b. Reportar un candidato")
    print("c. Volver")

# Modulo para ver candidatos
def ver_candidatos(estudiante_autenticado):
    candidatos_mostrados = False
    while not candidatos_mostrados:
        limpiar_pantalla()
        print("Ver candidatos:")
        for i, estudiante in enumerate(estudiantes, start=1):
            if estudiante == estudiante_autenticado:  # No ver mi propio perfil
                continue
            edad = calcular_edad(estudiante['fecha_nacimiento'])
            print(f"{i}. Nombre: {estudiante['nombre']}")
            print(f"   Fecha de nacimiento: {estudiante['fecha_nacimiento']} (Edad: {edad} años)")
            print(f"   Biografía: {estudiante['biografia']}")
            print(f"   Hobbies: {', '.join(estudiante['hobbies'])}")

        opcion = input("Elige un candidato por su número: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(estudiantes):
            # Obtener el candidato seleccionado
            candidato_seleccionado = estudiantes[int(opcion) - 1]
            
            if candidato_seleccionado == estudiante_autenticado:
                print("¡No puedes auto-matchearte!")
            else:
                # Logica para permitir al usuario ingresar el nombre para hacer un Matcheo
                nombre_matcheo = input("Ingresa el nombre del estudiante con el que te gustaría hacer un Matcheo en el futuro: ")
                if nombre_matcheo == candidato_seleccionado['nombre']:
                    print("¡Matcheo exitoso! Has seleccionado al candidato correctamente.")
                else:
                    print("El nombre ingresado no coincide con el candidato seleccionado.")
                input("Presiona Enter para continuar...")
                candidatos_mostrados = True
        else:
            print("Opción inválida.")

# Funcion para mostrar que la opcion esta en construccion
def en_construccion():
    print("En construcción.")

# Funcion principal
def main():
    intentos = 3
    usuario_autenticado = False
    estudiante_autenticado = None

    while intentos > 0 and not usuario_autenticado:
        email = input("Email: ")
        contraseña = getpass.getpass("Contraseña: ")
        for estudiante in estudiantes:
            if email == estudiante['email'] and contraseña == estudiante['contraseña']:
                print("¡Inicio de sesión exitoso!")
                usuario_autenticado = True
                estudiante_autenticado = estudiante
        if not usuario_autenticado:
            print("Email o contraseña incorrectos.")
            intentos -= 1

    if not usuario_autenticado:
        print("Has agotado tus intentos. Programa cerrado.")
        return

    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            gestionar_perfil(estudiante_autenticado)
            sub_opcion = input("Elige una opción: ")
            if sub_opcion == "a":
                editar_datos_personales(estudiante_autenticado)
            elif sub_opcion == "c":
                continue
            else:
                print("Opción no válida.")
        elif opcion == "2":
            gestionar_candidatos()
            sub_opcion = input("Elige una opción: ")
            if sub_opcion == "a":
                ver_candidatos(estudiante_autenticado)  # Pasar estudiante_autenticado como argumento
            elif sub_opcion == "c":
                continue
            else:
                print("Opción no válida.")
        else:
            en_construccion()
            time.sleep(1)  

if __name__ == "__main__":
    main()
