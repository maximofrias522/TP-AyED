from datos import *
from interfaz import limpiarPantalla


def obtenerPosicionUsuario(dbFisica, dbLogica, emailOId): # devuelve la posición en bytes de un usuario o -1 si no lo encuentra
    tam = os.path.getsize(dbFisica)
    dbLogica.seek(0)
    try:
        id = int(emailOId)
        while dbLogica.tell() < tam:
            pos = dbLogica.tell()
            usuarioActual = pickle.load(dbLogica)
            if (usuarioActual.estado == True) and (usuarioActual.id == id):
                return pos
        return -1
    except:
        while dbLogica.tell() < tam:
            pos = dbLogica.tell()
            usuarioActual = pickle.load(dbLogica)
            if (usuarioActual.estado == True) and (usuarioActual.email == emailOId):
                return pos
        return -1

def obtenerUsuario(dbFisica, dbLogica, emailOId): # devuelve un usuario o -1 si no lo encuentra
    pos = obtenerPosicionUsuario(dbFisica, dbLogica, emailOId)
    if pos == -1:
        return -1
    dbLogica.seek(pos)
    return pickle.load(dbLogica)

def sobrescribirUsuario(dbFisica, dbLogica, usuario):
    pos = obtenerPosicionUsuario(dbFisica, dbLogica, usuario.email)
    dbLogica.seek(pos)
    pickle.dump(usuario, dbLogica)
    dbLogica.flush()

def obtenerCantUsuario(dbFisica, dbLogica): # devuelve la cantidad de usuarios registrados
    c = 0

    tam = os.path.getsize(dbFisica)
    dbLogica.seek(0)
    while dbLogica.tell() < tam:
        usuarioActual = pickle.load(dbLogica)
        if usuarioActual.estado == True:
            c += 1

    return c

def esIdValida(dbFisica, dbLogica, id):
    idValida = False
    tam = os.path.getsize(dbFisica)
    dbLogica.seek(0)
    while dbLogica.tell() < tam:
        usuario = pickle.load(dbLogica)
        if usuario.id == id and usuario.estado == True:
            idValida = True

    return idValida

def eliminarUsuario(dbFisica, dbLogica, usuario):
    usuario.estado = False
    sobrescribirUsuario(dbFisica, dbLogica, usuario)
    if isinstance(usuario, Estudiante):
        tam = os.path.getsize(likesDbFisica)
        likesDbLogica.seek(0)
        while likesDbLogica.tell() < tam:
            pos = likesDbLogica.tell()
            likeActual = pickle.load(likesDbLogica)
            if ((likeActual.idEmisor == usuario.id) or (likeActual.idReceptor == usuario.id)) and (likeActual.estado == True):
                likeActual.estado = False
            likesDbLogica.seek(pos)
            pickle.dump(likeActual, likesDbLogica)
            likesDbLogica.flush()

        tam = os.path.getsize(reportesDbFisica)
        reportesDbLogica.seek(0)
        while reportesDbLogica.tell() < tam:
            pos = reportesDbLogica.tell()
            reporteActual = pickle.load(reportesDbLogica)
            if ((reporteActual.idEmisor == usuario.id) or (reporteActual.idReceptor == usuario.id)) and (reporteActual.estado == 0):
                reporteActual.estado = 1
            reportesDbLogica.seek(pos)
            pickle.dump(reporteActual, reportesDbLogica)
            reportesDbLogica.flush()

def obtenerEdad(fechaNacimiento): 
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fechaNacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fechaNacimiento.month, fechaNacimiento.day):
        edad -=1
    return str(edad)

def imprimirDatosDeEstudiante(estudiante):
    print("ID: " + str(estudiante.id) + "\n" +
          "Email: " + estudiante.email + "\n" +
          "Nombre: " + estudiante.nombre + "\n" +
          "Fecha de nacimiento: " + datetime.strftime(estudiante.fechaNacimiento, '%d/%m/%Y') + "\n" +
          "Edad: " + obtenerEdad(estudiante.fechaNacimiento) + "\n" +
          "Biografía: " + estudiante.biografia + "\n" +
          "Hobbies: " + estudiante.hobbies)

def mostrarTodosLosEstudiantes(idUsuarioActual):
    limpiarPantalla()
    tam = os.path.getsize(estudiantesDbFisica)
    estudiantesDbLogica.seek(0)
    while estudiantesDbLogica.tell() < tam:
        estudiante = pickle.load(estudiantesDbLogica)
        if (estudiante.estado == True) and (estudiante.email != idUsuarioActual):
            imprimirDatosDeEstudiante(estudiante)
            print('\n_________________\n')