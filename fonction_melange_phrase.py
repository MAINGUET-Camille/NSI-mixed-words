from melange_mot import melange_mot
def melange_phrase(phrase):
    """entrée : une ou plusieurs phrases (str)
       sortie : la/les phrase(s) avec chaque mot mélangé (la première
       et dernière lettre du mot ne change pas de place)"""

    mot=""  # variable vide afin de stocker un mot
    T=[]    # tableau vide qui permettra de stocker tout les mots

    for i in phrase:
        if i != " ":
            mot+=i   #si i(chaque caractère de la phrase) est différent d'un espace, on l'ajoute à la variable "mot"

    #si i est séparateur de mot(espace,apostrophe,point,virgule...), on ajoute le contenu de la variable "mot" au tableau "T" et on vide la variable "mot"
        if i == " ":
            T.append(mot)
            mot=""
        if i == "'":
            T.append(mot)
            mot=""
        if i == ".":
            T.append(mot)
            mot=""
        if i == "?":
            T.append(mot)
            mot=""
        if i == "!":
            T.append(mot)
            mot=""
        if i == ";":
            T.append(mot)
            mot=""
        if i == ",":
            T.append(mot)
            mot=""

    phrase_melange=""  #variable vide pour stocker la phrase mélangée

    for i in T:
        phrase_melange+=melange_mot(i) + " " # ajout dans la variable "phrase_melange" chaque éléments du tableau "T", en appliquant à chaque éléments la fonction "melange_mot" et on met un espace entre chaque mot

    # suppression des espaces en trop après les séparateurs
    phrase_melange2 = phrase_melange.replace("' ","'")
    phrase_melange3 = phrase_melange2.replace(". ",".")
    phrase_melange4 = phrase_melange3.replace("? ","?")
    phrase_melange5 = phrase_melange4.replace("! ","!")
    phrase_melange6 = phrase_melange5.replace("; ",";")
    phrase_melange7 = phrase_melange6.replace(", ",",")

    return phrase_melange7

#exemple
phrase="Selon une étude de l'Université de Cambridge, l'ordre des lettres dans les mots n'a pas d'importance, la seule chose importante est que la première et la dernière soit à la bonne place. Le reste peut être dans un désordre total et vous pouvez toujours lire sans problème."
print(melange_phrase(phrase))