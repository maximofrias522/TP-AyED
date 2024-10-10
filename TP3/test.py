import pickle
from datos import *

# devuelve todos los likes
tam = os.path.getsize(likesDbFisica)
likesDbLogica.seek(0)
while likesDbLogica.tell() < tam:
    like = pickle.load(likesDbLogica)
    if like.estado == True:
        print(like.idEmisor, like.idReceptor)