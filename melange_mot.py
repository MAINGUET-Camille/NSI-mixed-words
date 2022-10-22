#Question 1: Ce texte à été mélangé de manière à ce que les lettres de chaque mot soient mélangés, tout en conservant la première et la dernière lettre intactes.

from random import randrange

#fonction pour mélanger un mot
def melange_mot(mot:str):
    """
    entrée: un mot (str)
    sortie: le mot mélangé (la première et dernière lettre du mot ne change pas de place.)
    """
    if len(mot) <= 3:   #Si le mot a trois ou moins de lettres, le mélange ne change rien
        return mot

    #prend les premières et dernières lettres du mot et les retire
    P = mot[0]
    mot = mot[1:]
    D = mot[-1]
    mot = mot[:-1]

    T=[]
    for LETTRE in mot:
        T.append(LETTRE)    #crée un tableau contenant chaque lettre du mot

    #mélange les lettres contenues dans le tableau T
    for i in range(len(T),1,-1): #i tourne les indexes possibles des différents charactères du mot dans l'ordre décroissant
        aleat = randrange(i-1)
        T[i-1], T[aleat] = T[aleat], T[i-1]

    mot = ""
    for LETTRE in T:
        mot += LETTRE    #remet toutes les lettres du tableau T dans un même string

    return P + mot + D 





