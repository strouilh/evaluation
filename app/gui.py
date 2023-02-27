'''
Puissance 4 : deux joueurs s'affrontent pour aligner 4 jetons de même couleur
Version : 1.0.0
Author : John Doe

Partie concernant l'interaction avec l'utilisateur
'''

from tkinter import *



def construire_gui(joueur):
    '''
    Interface graphique (ne pas tester)
    affichage d'un label et d'une grille 6 lignes x 7 colonnes de boutons
    Params : joueur le nom et la couleur du joueur qui commence
    '''
    from noyau import jouer
    f = Tk()
    f.title('Puissance 4')
    fram1= Frame(f);
    fram1.pack(side=BOTTOM)
    message=Label(fram1, text="A toi "+str(joueur[0]))
    message.pack(side=TOP)
    fram2= Frame(f)
    fram2.pack(side=TOP)
    gbouton=[[-1]*7 for _ in range(6)]
    for l in range(6):
        for c in range(7):
            b = Button(fram2, text = "  ", bg = "white", relief = RAISED, activebackground = "white", bd = 2, textvariable=str(l) + str(c))
            b.config(command=lambda bt=b : jouer(str(bt.cget("textvariable")), gbouton, message))
            b.grid(row = l, column = c, padx = 5, pady = 5) 
            gbouton[l][c]=b
    return (f, gbouton, message)
