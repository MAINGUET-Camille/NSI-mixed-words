# Adapter la fonction précédente pour qu’elle prenne en paramètre : 
# le nom de fichier au format txt à transformer et le nom du fichier dans lequel ce texte transformé sera stocké

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


def question_3(tout_transformer, stockage):
    '''
    Entrée: un fichier texte contenant le texte à transformer
    Fonction qui applique les règles de mélange au texte et le stock dans un autre fichier
    '''
    try:
        t = open(tout_transformer,'r', encoding='utf-8') #ouverture du fichier en lecture seule sous le codage utf-8 (présence d'accents)
        #lecture du fichier
        fichier_de_sortie = t.read()
        #print(fichier_de_sortie)
        #fermeture du fichier
        t.close()

        #transformation du texte
        chaine_triee = tri_phrase(fichier_de_sortie)

        #ouverture du fichier de sortie et écriture du texte transformé
        file = open(stockage, 'w')
        #écriture du texte transformé dans le fichier de sortie
        file.write(chaine_triee)
        #fermeture le fichier
        file.close()
    except IOError:
        print ("Erreur: Erreur d'ouverture du fichier")
    return

#on définit en paramètre les chemins relatifs qui mènent vers les fichiers
question_3("C:\\Users\\utilisateur\\Desktop\\NSI\\NSI-mixed-words\\tout_transformer.txt", "C:\\Users\\utilisateur\\Desktop\\NSI\\NSI-mixed-words\\stockage.txt")