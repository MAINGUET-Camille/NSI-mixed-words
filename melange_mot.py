from random import randrange

def melange_mot(mot:str) -> str:
    """
    entrée: un mot (str)
    sortie: le mot mélangé (la première et dernière lettre du mot ne change pas de place.)
    """
    #Si le mot a trois ou moins de lettres, le mélanger ne change rien
    if len(mot) <= 3:
        return mot

    T = []
    for LETTRE in mot:
        T.append(LETTRE)
    
    mot = ""
    for i in range(len(T)-2):
        #permet d'obtenir l'indice d'une lettre aléatoirement, ne prends pas en compte le premier et dernier élément du tableau.
        aleat = randrange(1,len(T)-1) 
        mot += T.pop(aleat)

    #on remet les premières et dernières lettres qui étaient restées dans le tableau à leur place.
    return T[0] + mot + T[1] 







