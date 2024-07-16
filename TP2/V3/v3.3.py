import random
import os   
from datetime import datetime
from maskpass import askpass

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

MAX_ESTUDIANTES = 8
MIN_ESTUDIANTES = 4
MAX_MODERADORES = 4
MIN_MODERADORES = 1

# Estructuras de datos para estudiantes y moderadores
estudiantes = [[""]*7 for _ in range(MAX_ESTUDIANTES)]  # Cada estudiante tiene 7 campos | id - mail - contraseña - nombre - fecha de nacimiento - hobbies - biografia
moderadores = [[""]*3 for _ in range(MAX_MODERADORES)]  # Cada moderador tiene 3 campoos | mail - contraseña - nombre 

# Inicializar matriz de likes (8x8) con 0s y 1s aleatorios
likes = [[random.randint(0, 1) for _ in range(MAX_ESTUDIANTES)] for _ in range(MAX_ESTUDIANTES)]

# def inicializar_datos():
#     # Inicializar estudiantes
#     for i in range(MIN_ESTUDIANTES):
#         estudiantes[i] = [i, f"estudiante{i}@example.com", f"password{i}", "ACTIVO", f"info{i}"]
    
#     # Inicializar moderadores
#     for i in range(MIN_MODERADORES):
#         moderadores[i] = [i, f"moderador{i}@example.com", f"password{i}", "ACTIVO"]

#     # Inicializar matriz de likes (8x8) con 0s y 1s aleatorios
#     likes = [[random.randint(0, 1) for _ in range(MAX_ESTUDIANTES)] for _ in range(MAX_ESTUDIANTES)]
    
#     return likes

def registrar_usuario(tipo):
    if tipo == "estudiante":
        if any(estudiante[1] == "" for estudiante in estudiantes):
            id = next(i for i, est in enumerate(estudiantes) if est[1] == "")
            email = input("Ingrese email: ")
            contraseña = input("Ingrese contraseña: ")
            estado = "ACTIVO"
            info = input("Ingrese información personal: ")
            estudiantes[id] = [id, email, contraseña, estado, info]
        else:
            print("Ya se ha alcanzado el máximo de estudiantes.")
    elif tipo == "moderador":
        if any(moderador[1] == "" for moderador in moderadores):
            id = next(i for i, mod in enumerate(moderadores) if mod[1] == "")
            email = input("Ingrese email: ")
            contraseña = input("Ingrese contraseña: ")
            estado = "ACTIVO"
            moderadores[id] = [id, email, contraseña, estado]
        else:
            print("Ya se ha alcanzado el máximo de moderadores.")

def logueo():
    email = input("Ingrese email: ")
    contraseña = input("Ingrese contraseña: ")
    
    for estudiante in estudiantes:
        if estudiante[1] == email and estudiante[2] == contraseña and estudiante[3] == "ACTIVO":
            print("Bienvenido Estudiante")
            menu_estudiante(estudiante[0])
            return
    
    for moderador in moderadores:
        if moderador[1] == email and moderador[2] == contraseña and moderador[3] == "ACTIVO":
            print("Bienvenido Moderador")
            menu_moderador(moderador[0])
            return
    
    print("Credenciales incorrectas o usuario inactivo")

def menu_estudiante(id):
    while True:
        print("1. Gestionar mi perfil")
        print("2. Gestionar candidatos")
        print("3. Matcheos (En Construcción)")
        print("4. Reportes Estadísticos")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            gestionar_perfil(id)
        elif opcion == 2:
            gestionar_candidatos(id)
        elif opcion == 4:
            reportes_estadisticos(id)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def menu_moderador(id):
    while True:
        print("1. Gestionar usuarios")
        print("2. Gestionar reportes")
        print("3. Reportes Estadísticos (En Construcción)")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            gestionar_usuarios()
        elif opcion == 2:
            gestionar_reportes()
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def gestionar_perfil(id):
    while True:
        print("1. Editar mis datos personales")
        print("2. Eliminar mi perfil")
        print("0. Volver")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            editar_datos_personales(id)
        elif opcion == 2:
            eliminar_perfil(id)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def editar_datos_personales(id):
    fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input("Ingrese su sexo: ")
    biografia = input("Ingrese su biografía: ")
    hobbies = input("Ingrese sus hobbies: ")
    estudiantes[id][4] = f"Fecha Nacimiento: {fecha_nacimiento}, Sexo: {sexo}, Biografía: {biografia}, Hobbies: {hobbies}"
    print("Datos personales actualizados")

def eliminar_perfil(id):
    confirmacion = input("¿Realmente desea eliminar su perfil? (si/no): ")
    if confirmacion.lower() == "si":
        estudiantes[id][3] = "INACTIVO"
        print("Perfil eliminado. Volviendo a la pantalla de login...")
        logueo()

def gestionar_candidatos(id):
    while True:
        print("1. Ver candidatos")
        print("2. Reportar un candidato")
        print("0. Volver")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            ver_candidatos()
        elif opcion == 2:
            reportar_candidato(id)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def ver_candidatos():
    for estudiante in estudiantes:
        if estudiante[3] == "ACTIVO":
            print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Información: {estudiante[4]}")

def reportar_candidato(id):
    id_reportado = int(input("Ingrese el ID del candidato a reportar: "))
    motivo = input("Ingrese el motivo del reporte: ")
    reporte = [id, id_reportado, motivo, 0]  # Estado 0: no visto
    print(f"Reporte realizado: {reporte}")

def gestionar_usuarios():
    while True:
        print("1. Desactivar usuario")
        print("0. Volver")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            desactivar_usuario()
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def desactivar_usuario():
    id = int(input("Ingrese el ID del usuario a desactivar: "))
    for estudiante in estudiantes:
        if estudiante[0] == id:
            estudiante[3] = "INACTIVO"
            print("Usuario desactivado")
            return
    for moderador in moderadores:
        if moderador[0] == id:
            moderador[3] = "INACTIVO"
            print("Usuario desactivado")
            return
    print("Usuario no encontrado")

def gestionar_reportes():
    while True:
        print("1. Ver reportes")
        print("0. Volver")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            ver_reportes()
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

def ver_reportes():
    # Aquí mostrarías los reportes, el estado, y pedirías acción a tomar (ignorar o bloquear)
    print("Funcionalidad de gestión de reportes aún no implementada")

def reportes_estadisticos(id):
    # Aquí deberías calcular y mostrar los reportes estadísticos
    print("Funcionalidad de reportes estadísticos aún no implementada")

def main():
    while True:
        print("1. Logueo")
        print("2. Registrarse")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            logueo()
        elif opcion == 2:
            tipo = input("Ingrese el tipo de usuario a registrar (estudiante/moderador): ")
            registrar_usuario(tipo)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
