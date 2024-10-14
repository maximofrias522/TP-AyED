from datos import *
from interfaz import *
from common import *


estudianteActual = Estudiante()

def menuEstudiante(usuario): # menu principal
    global estudianteActual
    estudianteActual = usuario
    mostrarMenuEst()
    opcion = input('Seleccione una opción: ')
    
    while opcion != '0':
        if opcion == '1':
            if gestionarPerfil():
                return
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

def mostrarPerfil():
    limpiarPantalla()
    console.print("Estás viendo tu perfil", style='bold white')
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
            if eliminarPerfil():
                return True
        else:
            opcionInvalida() 

        mostrarGestionarPerfil()
        opcion = input('Seleccione una opción: ')

    return False

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
        fecha = input("Ingrese la nueva fecha de nacimiento (dd/mm/aaaa): ")
        try:
            dtfecha = datetime.strptime(fecha, "%d/%m/%Y") 
            if dtfecha > datetime.today(): 
                console.print("La fecha introducida no es válida. Intente nuevamente.", style='red') 
            else:
                formato_correcto = True

        except ValueError as ve:
            if "does not match format" in str(ve):
                console.print("El formato de fecha ingresado es incorrecto. Intente nuevamente.", style='red') 
            else:
                console.print("Fecha fuera de rango. Intente nuevamente.", style='red') 

    return dtfecha

def editarFechaNacimiento():
    nueva_fecha = obtenerFecha() 
    estudianteActual.fechaNacimiento = nueva_fecha
    console.print(f"Fecha de nacimiento actualizada a {nueva_fecha.strftime('%d/%m/%Y')}", style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def editarBiografia():
    nueva_biografia = input("Ingrese la nueva biografía: ") 
    while nueva_biografia == '': 
        console.print('La biografía no puede estar vacía.', style='red')
        nueva_biografia = input("Ingrese la nueva biografía: ")

    estudianteActual.biografia = nueva_biografia.ljust(50)
    console.print('Su nueva biografía es: ', nueva_biografia, style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def editarHobbies():
    nuevos_hobbies = input("Ingrese los nuevos hobbies: ")
    while nuevos_hobbies == '':
        console.print('Los hobbies no pueden estar vacíos', style='red')
        nuevos_hobbies = input("Ingrese los nuevos hobbies: ")

    estudianteActual.hobbies = nuevos_hobbies.ljust(50)
    console.print("Sus nuevos hobbies son: ", nuevos_hobbies, style='green')

    sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    continuar()

def eliminarPerfil():
    opcion = input('¿Está seguro de que desea eliminar su perfil? s/n: ').lower()
    while opcion != 'n':
        if opcion == 's':
            eliminarUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
            console.print('Su perfil se eliminó correctamente.', style='green')
            continuar()
            return True
        else:
            opcionInvalida()
        opcion = input('¿Está seguro de que desea eliminar su perfil? s/n: ').lower()

    return False
# Gestion perfil F


# Gestion candidatos S 

# Submenú de gestionar candidatos
def mostrarGestionarCandidatos():
    limpiarPantalla()
    console.print('[bold white]Estas gestionando tus candidatos[/bold white]')
    console.print('1. Ver candidatos disponibles')
    console.print('2. Reportar a un candidato')
    if estudianteActual.revelarCandidatos == True:
        console.print('3. Revelar candidatos')
    console.print('0. Volver')


def gestionarCandidatos():
    mostrarGestionarCandidatos()
    opcion = input('Seleccione una opcion: ')
    while opcion != '0':
        if opcion == '1':
            verCandidatos()
        elif opcion == '2':
            reportarCandidato()
        elif opcion == '3' and estudianteActual.revelarCandidatos == True:
            revelarCandidatos()
        else:
            opcionInvalida()

        mostrarGestionarCandidatos()
        opcion = input('Seleccione una opcion: ')

def darLike():
    nuevoLike = Like()
    nuevoLike.idEmisor = estudianteActual.id

    try:
        nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle like: '))
        if nuevoLike.idEmisor == nuevoLike.idReceptor:
            idValida = False
        else:
            idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
    except:
        idValida = False

    while not idValida:
        print('ID de usuario no válida.')
        try:
            nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle like: '))
            if nuevoLike.idEmisor == nuevoLike.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
        except:
            idValida = False


    yaTeGusta = False
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if (like.idEmisor == nuevoLike.idEmisor) and (like.idReceptor == nuevoLike.idReceptor) and (like.estado == True):
            yaTeGusta = True


    if yaTeGusta:
        console.print(f'Ya le diste me gusta en el pasado a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
        continuar()

    else:
        likesDbLogica.seek(0, os.SEEK_END)
        pickle.dump(nuevoLike, likesDbLogica)
        likesDbLogica.flush()
        console.print(f'Le diste like a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
        continuar()

def darSuperLike():
    if estudianteActual.superlike == True:
        nuevoLike = Like()
        nuevoLike.idEmisor = estudianteActual.id

        try:
            nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle un super-like: '))
            if nuevoLike.idEmisor == nuevoLike.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
        except:
            idValida = False

        while not idValida:
            print('ID de usuario no válida.')
            try:
                nuevoLike.idReceptor = int(input('Ingrese el ID del usuario para darle un super-like: '))
                if nuevoLike.idEmisor == nuevoLike.idReceptor:
                    idValida = False
                else:
                    idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor)
            except:
                idValida = False

        leDisteLike = False
        teDioLike = False
        tam = os.path.getsize(likesDbFisica)
        likesDbLogica.seek(0)
        while likesDbLogica.tell() < tam:
            like = pickle.load(likesDbLogica)
            if like.idEmisor == nuevoLike.idEmisor and like.idReceptor == nuevoLike.idReceptor and like.estado == True:
                leDisteLike = True
            if like.idReceptor == nuevoLike.idEmisor and like.idEmisor == nuevoLike.idReceptor and like.estado == True:
                teDioLike = True

        if teDioLike and leDisteLike:
            print('Ya hiciste match con este usuario')
        else:
            likesDbLogica.seek(0, os.SEEK_END)
            pickle.dump(nuevoLike, likesDbLogica)
            nuevoLike2 = Like()
            nuevoLike2.idEmisor = nuevoLike.idReceptor
            nuevoLike2.idReceptor = nuevoLike.idEmisor
            pickle.dump(nuevoLike2, likesDbLogica)
            likesDbLogica.flush()
            console.print(f'Le diste un super-like a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoLike.idReceptor).nombre}', style='green')
            estudianteActual.superlike = False
            sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)
    else:
        print('Ya usaste tu super-like en el pasado.')
    continuar()

def verCandidatos():
    mostrarTodosLosEstudiantes(estudianteActual.id)

    opcion = input('¿Querés darle like a algún estudiante? s/n o "super" para dar un super-like: ').lower()
    while opcion != 'n':
        if opcion == 's':
            darLike()
        elif opcion == 'super':
            darSuperLike()
        else:
            opcionInvalida()
        
        mostrarTodosLosEstudiantes(estudianteActual.id)
        opcion = input('¿Querés darle like a algún estudiante? s/n: ').lower()


def reportar():
    nuevoReporte = Reporte()
    nuevoReporte.idEmisor = estudianteActual.id

    try:
        nuevoReporte.idReceptor = int(input('Ingrese el ID o email del usuario para reportarlo: '))
        if nuevoReporte.idEmisor == nuevoReporte.idReceptor:
            idValida = False
        else:
            idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor)
    except:
        idValida = False

    while not idValida:
        console.print('ID de usuario no válida.', style='red')
        try:
            nuevoReporte.idReceptor = int(input('Ingrese el ID o email del usuario para reportarlo: '))
            if nuevoReporte.idEmisor == nuevoReporte.idReceptor:
                idValida = False
            else:
                idValida = esIdValida(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor)
        except:
            idValida = False


    yaLoReportaste = False
    tam = os.path.getsize(reportesDbFisica)
    reportesDbLogica.seek(0)
    while reportesDbLogica.tell() < tam:
        reporte = pickle.load(reportesDbLogica)
        if (reporte.idEmisor == nuevoReporte.idEmisor) and (reporte.idReceptor == nuevoReporte.idReceptor):
            yaLoReportaste = True


    if yaLoReportaste:
        console.print(f'Ya reportaste en el pasado a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor).nombre}', style='green')
        continuar()

    else:
        reportesDbLogica.seek(0, os.SEEK_END)
        pickle.dump(nuevoReporte, reportesDbLogica)
        reportesDbLogica.flush()
        console.print(f'Reportaste a {obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, nuevoReporte.idReceptor).nombre}', style='green')
        continuar()
        

def reportarCandidato():
    mostrarTodosLosEstudiantes(estudianteActual.id)

    opcion = input('¿Querés reportar a algún estudiante? s/n: ').lower()
    while opcion != 'n':
        if opcion == 's':
            reportar()
        else:
            opcionInvalida()
        
        mostrarTodosLosEstudiantes(estudianteActual.id)
        opcion = input('¿Querés reportar a algún estudiante? s/n: ').lower()


def revelarCandidatos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)

    hayCandidatos = False
    limpiarPantalla()
    for id in likesRecibidos:
        if id not in likesDados:
            hayCandidatos = True
            imprimirDatosDeEstudiante(obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, id))

    if not hayCandidatos:
        print('No hay candidatos para mostrar')
    else:
        estudianteActual.revelarCandidatos = False
        sobrescribirUsuario(estudiantesDbFisica, estudiantesDbLogica, estudianteActual)

    continuar()


def eliminarMatch(likesDados):
    valido = False
    while not valido:
        matchAEliminar = int(input('Ingrese el ID del usuario para eliminar el match: '))
        if matchAEliminar in likesDados:
            valido = True
            tam = os.path.getsize(likesDbFisica)
            likesDbLogica.seek(0)
            while likesDbLogica.tell() < tam:
                pos = likesDbLogica.tell()
                like = pickle.load(likesDbLogica)
                if like.idEmisor == estudianteActual.id and like.idReceptor == matchAEliminar and like.estado == True:
                    like.estado = False
                    likesDbLogica.seek(pos)
                    pickle.dump(like, likesDbLogica)
                    likesDbLogica.flush()
                    tam = 0

            console.print('Eliminaste el match', style='green')

def matcheos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)

    limpiarPantalla()
    hayMatchs = False
    for id in likesDados:
        if id in likesRecibidos:
            hayMatchs = True
            imprimirDatosDeEstudiante(obtenerUsuario(estudiantesDbFisica, estudiantesDbLogica, id))
            print('\n_________________\n')
    
    if not hayMatchs:
        console.print('No tenés matchs', style='blue')
    else:
        opcion = input('¿Querés eliminar algún match? s/n: ').lower()
        while opcion != 'n':
            if opcion == 's':
                eliminarMatch(likesDados)
                continuar()
            else:
                opcionInvalida()
            opcion = 'n'
            

def reportesEstadisticos():
    likesDados = []
    likesRecibidos = []
    tam = os.path.getsize(likesDbFisica)
    likesDbLogica.seek(0)
    while likesDbLogica.tell() < tam:
        like = pickle.load(likesDbLogica)
        if like.idEmisor == estudianteActual.id and like.estado == True:
            likesDados.append(like.idReceptor)
        if like.idReceptor == estudianteActual.id and like.estado == True:
            likesRecibidos.append(like.idEmisor)
    
    limpiarPantalla()
    matcheos = 0
    likesDadosYNoDevueltos = 0
    for id in likesDados:
        if id in likesRecibidos:
            matcheos += 1
        else:
            likesDadosYNoDevueltos += 1
    likesRecibidosYNoDevueltos = 2 * matcheos - likesDadosYNoDevueltos
    estudiantesDbLogica.seek(0)
    cantidadDeEstudiantes = obtenerCantUsuario(estudiantesDbFisica, estudiantesDbLogica)

    print(f'Matcheaste con el {matcheos * 100 / cantidadDeEstudiantes}% de los estudiantes')
    print(f'Likes dados y no devueltos: {likesDadosYNoDevueltos}')
    print(f'Likes recibidos y no devueltos: {likesRecibidosYNoDevueltos}')
    continuar()