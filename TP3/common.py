from datos import *


def obtenerPosicionUsuario(dbFisica, dbLogica, email): # devuelve la posición en bytes de un usuario o -1 si no lo encuentra
    tam = os.path.getsize(dbFisica)
    dbLogica.seek(0)
    while dbLogica.tell() < tam:
        pos = dbLogica.tell()
        usuarioActual = pickle.load(dbLogica)
        if (usuarioActual.estado == True) and (usuarioActual.email == email):
            return pos
    return -1

def obtenerUsuario(dbFisica, dbLogica, email): # devuelve un usuario o -1 si no lo encuentra
    pos = obtenerPosicionUsuario(dbFisica, dbLogica, email)
    if pos == -1:
        return -1
    dbLogica.seek(pos)
    return pickle.load(dbLogica)

def sobrescribirUsuario(dbFisica, dbLogica, estudiante):
    pos = obtenerPosicionUsuario(dbFisica, dbLogica, estudiante.email)
    dbLogica.seek(pos)
    pickle.dump(estudiante, dbLogica)
