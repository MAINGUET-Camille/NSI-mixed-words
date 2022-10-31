WORDLIST = open("liste_des_mots_français.txt", 'r', encoding='utf-8')

def tri_mot(MOT):
    """
    Entrée : un mot (str) mélangé de façon a toujours garder la première et dernière lettre au bon endroit, ne doit pas comporter de majuscule au début.
    Sortie : le mot non-mélangé (str), None si le mot n'a pas été trouvé dans la liste de mots.
    """
    if len(MOT)<= 3:
        return MOT

    for ligne in WORDLIST:
        if MOT[0] == ligne[0] and len(MOT) == len(ligne)-1 and MOT[-1] == ligne[-2] :  #on fait un premier tri (on a ligne[-2] et len(ligne)-1 car chaque ligne se termine par "/n")
            mot_possible = ligne[:-1]

            #on met les lettres dans deux tableaux (T => MOT et T2 => mot_possible)
            T = []
            T2 = []
            for x in MOT:
                T.append(x)
            for y in mot_possible:
                T2.append(y)

            #on vérifie si les deux mots ont exactement les mêmes lettres
            for lettre in mot_possible:
                if lettre in T:
                    T2.pop(T2.index(lettre))
                    T.pop(T.index(lettre))
            if T == []:
                return mot_possible
    return 

