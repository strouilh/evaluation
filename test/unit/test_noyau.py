import pytest

from noyau import *
@pytest.mark.parametrize("n1, n2",  [(0,1), (1,0)])
def test_changer_joueur(n1, n2):
   assert changer_joueur(n1)==n2

def test_jeton_horizontal():
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1,  1, -1, -1, -1, -1, -1],
           [-1,  1, -1, -1, -1, -1, -1],
           [-1,  1, -1, -1, -1, -1, -1],
           [-1,  1, -1, -1, -1, -1, -1]]
   joueur=0
   posx=5
   posy=0
   depx=0
   depy=-1
   assert jeton(joueur, posx, posy, depx, depy, grille)==0

def test_maj_jeu_ligne_vide():
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1]]
   niveau=[5, 5, 5, 5, 5, 5, 5]
   joueur=0
   case=(5,0)
   maj_jeu(case, grille, niveau, joueur)
   assert niveau == [4, 5, 5, 5, 5, 5, 5]
   assert grille[5][0] == joueur

def test_maj_jeu_ligne():
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [ 1, -1, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1],
           [ 1, -1, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1]]
   niveau=[1, 5, 5, 5, 5, 5, 5]
   joueur=0
   case=(1,0)
   maj_jeu(case, grille, niveau, joueur)
   assert niveau == [0, 5, 5, 5, 5, 5, 5]
   assert grille[1][0] == joueur 

@pytest.mark.xfail
def test_maj_jeu_ligne_pleine():
   grille=[[ 1, -1, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1],
           [ 1, -1, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1],
           [ 1, -1, -1, -1, -1, -1, -1],
           [ 0, -1, -1, -1, -1, -1, -1]]
   niveau=[-1, 5, 5, 5, 5, 5, 5]
   joueur=0
   case=(-1,0)
   maj_jeu(case, grille, niveau, joueur)
   assert niveau == [-1, 5, 5, 5, 5, 5, 5]
  