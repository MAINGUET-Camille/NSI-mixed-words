from melange_mot import melange_mot

def melange_phrase2(phrase: str) -> str:
    """
    entrée : une ou plusieurs phrases (str) (ne prends pas en compte le formatage comme le retour à la ligne)
    sortie : la/les phrase(s) avec chaque mot mélangé (la première et dernière lettre du mot ne change pas de place)
    """

    T_de_mots = phrase.split()
    T_mots_melange = []

    for mot in T_de_mots:
    
        T_mots_melange.append(melange_mot(mot))   

        #on enlève les signes de ponctuation
        for ponctuation in ".,;:?!\"'-":

            if ponctuation in mot:
                #on sépare le mot et on mélange chaque partie 
                mot_compose = mot.rpartition(ponctuation)
                mot_melange = ""

                for x in mot_compose:
                    mot_melange += melange_mot(x)

                #on le remplace dans le tableau de mots
                T_mots_melange.pop()
                T_mots_melange.append(mot_melange)

    return " ".join(T_mots_melange)








