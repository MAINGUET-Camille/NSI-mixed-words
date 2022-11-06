from melange_mot import melange_mot

def melange_phrase(phrase):
    """entrée : une ou plusieurs phrases (str)
       sortie : la/les phrase(s) avec chaque mot mélangé (la première
       et dernière lettre du mot ne change pas de place)"""

    import re  #importation du module re
    T=re.split(r'(\W+)',phrase) #création d'un tableau grâce à la fonction split() avec comme séparateur tout caractère non alphanumérique

    phrase_melange="" #variable vide dans laquelle on mettra la phrase melangée

    for i in T:
        phrase_melange += melange_mot(i) #pour chaque élément du tableau, on applique la fonction melange_mot() et on l'ajoute dans la variable phrase_melange

    return(phrase_melange)
