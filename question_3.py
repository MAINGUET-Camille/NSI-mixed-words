# Adapter la fonction précédente pour qu’elle prenne en paramètre : 
# le nom de fichier au format txt à transformer et le nom du fichier dans lequel ce texte transformé sera stocké

from fonction_melange_phrase import melange_phrase

def question_3(tout_transformer, stockage):
    '''
    Entrée: un fichier texte contenant le texte à transformer (tout_transformer) et le nom sous lequel le nouveau fichier va être crée (stockage)
    Fonction qui applique les règles de mélange au texte et le stock dans un autre fichier
    '''

    t = open(tout_transformer,'r', encoding='utf-8') #ouverture du fichier en lecture seule sous le codage utf-8 (présence d'accents)
    #lecture du fichier
    fichier_de_sortie = t.read()
    #print(fichier_de_sortie)
    #fermeture du fichier
    t.close()

    #transformation du texte
    chaine_triee = melange_phrase(fichier_de_sortie)

    #ouverture du fichier de sortie et écriture du texte transformé
    file = open(stockage, 'w', encoding="utf-8")
    #écriture du texte transformé dans le fichier de sortie
    file.write(chaine_triee)
    #fermeture du fichier
    file.close()
    return

# #on définit en paramètre les chemins relatifs qui mènent vers les fichiers
# question_3("C:\\Users\\utilisateur\\Desktop\\NSI\\NSI-mixed-words\\tout_transformer.txt", "C:\\Users\\utilisateur\\Desktop\\NSI\\NSI-mixed-words\\stockage.txt")
