#Question 1: Ce texte à été mélangé de manière à ce que les lettres de chaque mot soient mélangés, tout en conservant la première et la dernière lettre intactes.

from random import randrange

#fonction pour mélanger un mot
def melange_mot(mot:str) -> str:
    """
    entrée: un mot (str)
    sortie: le mot mélangé (la première et dernière lettre du mot ne change pas de place.)
    """
    if len(mot) <= 3:   #Si le mot a trois ou moins de lettres, le mélange ne change rien
        return mot

    T = []
    for LETTRE in mot:
        T.append(LETTRE)
    
    mot = ""
    for i in range(len(T)-2):
        aleat = randrange(1,len(T)-1) #permet d'obtenir l'indice d'une lettre aléatoirement, ne prends pas en compte le premier et dernier élément du tableau.
        mot += T.pop(aleat)


    return T[0] + mot + T[1] #remet les premières et dernières lettres qui étaient restées dans le tableau à leur place.






