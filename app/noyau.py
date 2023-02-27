'''
Puissance 4 : deux joueurs s'affrontent pour aligner 4 jetons de même couleur
Version : 1.0.0
Author : John Doe
'''


import sys
from gui import construire_gui

# fonction de callback (appelé à chaque événement clic sur un bouton)
def jouer(case, gbouton, message):
    '''
    Jouer un coup : récupérer la proposition, mettre à jouer le jeu, vérifier la fin du jeu
    Params : case       le label du bouton qui a été cliqué (chaîne de caractères)
             gbouton    la grille de boutons graphiques cliquables (widget)
             message    le label pour les messages à l'utilsateur (widget)
    '''
    global joueur
    global rang
    global grille
    global niveau
    global etat

    if etat != "fini":
        (i,j)=maj_jeu(case, grille, niveau, rang)
        gbouton[i][j].config(bg=joueur[rang][1])
        
        print("clic sur"+str(i)+" "+str(j))
   
        if coup_gagnant(rang, i, j, grille):
            message.config(text="Bravo, tu as gagné "+str(joueur[rang][0]))          
            etat="fini"
        else:
            rang=changer_joueur(rang)
            message.config(text="A toi "+str(joueur[rang][0]))

def jeton(joueur, posx, posy, depx, depy, grille):
    '''
    Regarder les jetons à côté (selon la direction courante)
    en vérifiant que l'on ne passe pas à l'extérieur de la grille
    Params :    joueur        numéro du joueur (0 ou 1)
                posx, posy  coordonnées de la case à tester
                depx, depy  direction
                grille      grille d'occupation par les jetons
    Return : nombre de jetons alignés selon une direction (entier >= 0) 
    '''
    if posx>=0 and posx<6 and posy>=0 and posy<7 and grille[posx][posy] == joueur:
        return 1+jeton(joueur, posx+depx, posy+depy, depx, depy, grille)
    else:
        return 0

def coup_gagnant(joueur, i, j, grille):
    '''
    Rechercher si 4 jetons de même couleur sont alignés dans toutes les directions possibles
    Params :    joueur      numéro du joueur (0 ou 1)
                i, j        coordonnées de la dernière case proposée
                grille      grille d'occupation par les jetons
    Return :    True si le joueur a 4 jetons dans une direction autorisée
                False sinon 
    '''
    #recherche verticale : i varie
    nb=1+jeton(joueur, i-1,j, -1, 0, grille)+jeton(joueur, i+1, j, +1, 0, grille)
    if nb>=4:
        return True
    #recherche horizontale
    nb=1+jeton(joueur, i, j-1, 0, -1, grille)+jeton(joueur, i, j+1, 0, 1, grille)
    if nb>=4:
        return True
    #recherche diagonales
    nb=1+jeton(joueur, i-1, j-1, -1, -1, grille)+jeton(joueur, i+1, j+1, 1, 1, grille)
    if nb>=4:
        return True
    nb=1+jeton(joueur, i-1, j+1, -1, 1, grille)+jeton(joueur, i+1, j-1, 1, -1, grille)
    if nb>=4:
        return True
    else:
        return False

def changer_joueur(rang):
    '''
    Passer d'un joueur à l'autre
    Params : rang numéro du joueur (0 ou 1)
    '''
    return ((rang+1)%2)

def maj_jeu(case, grille, niveau, joueur):
    '''
    Mettre à jour la grille avec le nouveau coup joué   
    ATTENTION : il y a un pb --> détectable avec test unitaire (test aux limites)
    Params : case   le label du bouton cliqué (chaîne de caractères)
            grille  la grille d'occupation des jetons des joueurs (-1, O et 1)
            niveau  le nombre de cases vides pour chaque colonne (tableau)
            joueur  le numéro du joueur (0 ou 1) 
    Return : (i, j) numéro de ligne et numéro de colonne de la dernière case remplie
    '''
    j=int(case[1])
    i=niveau[j]
    niveau[j]=niveau[j]-1
    grille[i][j]=joueur
    return (i, j)


#programme principal

grille=[[-1]*7 for _ in range(6)]  # la grille 7 colonnes x 6 lignes 
                                   # -1=case non jouée
niveau=[5]*7 #indice de la première case vide de chaque colonne (5 au début)
#       colonne
#           0   1   2   ... 6
# ligne 0 
#       1
#       2
#       ...
#       5
joueur=[('Laurel', 'orange'), ('Hardy', 'green')]
rang=0

etat="en cours"

(f, gbouton, message)=construire_gui(joueur[rang]) 

f.mainloop()