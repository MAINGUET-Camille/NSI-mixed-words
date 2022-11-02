from melange_mot import melange_mot

def melange_phrase(phrase):
    """entrée : une ou plusieurs phrases (str)
       sortie : la/les phrase(s) avec chaque mot mélangé (la première
       et dernière lettre du mot ne change pas de place)"""

    T=phrase.split()  # création d'un tableau qui contient chaque mots de la phrase grâce à la fonction split()

    phrase_melange=""  #variable vide pour stocker la phrase mélangée

    for i in T:
        if i[-1] == ",":
            i=i[:-1]
            i=melange_mot(i) + ","
            phrase_melange+=i + " " # si le mot se termine par une virgule, on enleve la virgule, on mélange le mot, on rajoute la vrigule et on ajoute le mot dans la variable phrase_melange
        elif i[-1] == ".":
            i=i[:-1]
            i=melange_mot(i) + "."
            phrase_melange+=i + " "  # si le mot se termine par un point, on enleve le point, on mélange le mot, on rajoute le point et on ajoute le mot dans la variable phrase_melange
        else:
            i=melange_mot(i)
            phrase_melange+=i + " " # ajout dans la variable "phrase_melange" les autres éléments du tableau "T", en appliquant à chaque éléments la fonction "melange_mot" et on met un espace entre chaque mot

    return phrase_melange

#exemple
phrase="Selon une étude de l'Université de Cambridge, l'ordre des lettres dans les mots n'a pas d'importance, la seule chose importante est que la première et la dernière soit à la bonne place. Le reste peut être dans un désordre total et vous pouvez toujours lire sans problème. C'est parceque le cerveau humain ne lit pas chaque lettres elle-même mais le mot comme un tout."
print(melange_phrase(phrase))