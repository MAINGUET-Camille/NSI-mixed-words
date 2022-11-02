from wordlist import make_wordlist

WORDLIST = make_wordlist("liste_des_mots_français.txt")

def tri_mot(mot:str) -> str:
    """
    Entrée : un mot (str) mélangé de façon a toujours garder la première et dernière lettre au bon endroit, ne doit pas comporter de majuscules.
    Sortie : le mot non-mélangé (str), le mot mélangé si le mot n'a pas été trouvé dans la liste de mots.
    """
    if len(mot)<= 3:
        return mot

    for mot_possible in WORDLIST[mot[0]][len(mot)]:

            #on vérifie si la dernière lettre est la même
            if mot_possible[-1] == mot[-1]:

                #on met les lettres dans deux tableaux (T => mot et T2 => mot_possible)
                T = sorted(list(mot))
                T2 = sorted(list(mot_possible))

                #on vérifie si les deux mots ont exactement les mêmes lettres
                if T == T2:
                    return mot_possible
    return mot
