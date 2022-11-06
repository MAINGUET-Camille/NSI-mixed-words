def make_wordlist(file):
    """
    Entrée : un fichier texte contenant une liste de mots (un par ligne)
    Crée un dictionaire contenant un dictionnaire par lettre de l'alphabet qui contiennent des listes de mots de même longueur.
    """
    with open(file, 'r', encoding='utf-8') as wordlist:
        dico_de_mots = {}

        for ligne in wordlist:
            #on enlève le "/n"
            ligne = ligne[:-1]

            #on cherche si le dictionnaire correspondant à la première lettre existe, sinon on le crée
            if ligne[0] in dico_de_mots:

                #on cherche si la liste correspondant à la longueur du mot existe, sinon on la crée
                if len(ligne) in dico_de_mots[ligne[0]]:
                    dico_de_mots[ligne[0]][len(ligne)].append(ligne)
                else :
                    dico_de_mots[ligne[0]][len(ligne)] = [ligne]
            else:
                dico_de_mots[ligne[0]] = {len(ligne):[ligne]}
                
        return dico_de_mots
