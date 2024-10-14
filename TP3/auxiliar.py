import pickle
from datos import *

# devuelve todos los likes
tam = os.path.getsize(likesDbFisica)
likesDbLogica.seek(0)
while likesDbLogica.tell() < tam:
    like = pickle.load(likesDbLogica)
    print(like.idEmisor, like.idReceptor, like.estado)