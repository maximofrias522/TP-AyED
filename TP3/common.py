from datos import *


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

def sobrescribirUsuario(dbFisica, dbLogica, estudiante):
    pos = obtenerPosicionUsuario(dbFisica, dbLogica, estudiante.email)
    dbLogica.seek(pos)
    pickle.dump(estudiante, dbLogica)
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