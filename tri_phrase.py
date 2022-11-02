from melange_mot import melange_mot
from trier_un_mot import tri_mot
import re as re

def tri_phrase(phrase: str) -> str:
    """
    entrée : une ou plusieurs phrases (str) 
    sortie : la/les phrase(s) avec chaque mot mélangé (la première et dernière lettre du mot ne change pas de place)
    """

    # séparation des mots et des marques de ponctuation
    T_mots = re.findall("\w+", phrase)
    T_ponctuation = re.findall("\W+", phrase)

    T_mots_tries = [] #création d'un tableau pour stocker les mots une fois triés
   
    for mot in T_mots:
        #le dictionnaire ne comporte pas de mots avec des majuscules, il faut les enlever
        if not mot.islower():

            #le mot peut avoir une majuscule au début (title) ou être entièrement compris de majuscules (upper)
            if mot.istitle():
                #on tri le mot et on remet la majuscule
                mot = mot.lower()
                mot_trie = tri_mot(mot)
                mot_trie = mot_trie.capitalize()
            elif mot.isupper():
                #on tri le mot et on le remet en majuscules
                mot = mot.lower()
                mot_trie = tri_mot(mot)
                mot_trie = mot_trie.upper()
        
        else:
            mot_trie = tri_mot(mot)

        #on ajoute le mot trié au tableau de mots triés.
        T_mots_tries.append(mot_trie)

    #si les deux tableaux ne sont pas de la même taille, c'est qu'il manque un point à la fin de la phrase.
    if len(T_mots) != len(T_ponctuation):
        T_ponctuation.append(".")

    #on remet les mots et la ponctuation ensemble pour reformer la phrase dans phrase_trie
    phrase_trie = ""
    for i in range(len(T_mots)):
        phrase_trie += T_mots_tries[i]
        phrase_trie += T_ponctuation[i]

    return phrase_trie
    