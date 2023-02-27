import pytest

from noyau import coup_gagnant

def test_coup_gagnant_vide():
   joueur=0
   i=0
   j=0
   grille=[[-1]*7 for _ in range(6)]
   assert coup_gagnant(joueur, i, j, grille)==False

def test_coup_gagnant_vertical():
   joueur=0
   i=2
   j=0
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [0, -1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1]]
   assert coup_gagnant(joueur, i, j, grille)==True

def test_coup_gagnant_horizontal():
   joueur=0
   i=5
   j=3
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1,  1, -1, -1, -1, -1, -1],
           [ 0,  0,  0,  0,  1,  1, -1]]
   assert coup_gagnant(joueur, i, j, grille)==True

def test_coup_gagnant_diagonale():
   joueur=0
   i=2
   j=3
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1,  0, -1, -1, -1],
           [-1, -1,  0,  1, -1, -1, -1],
           [-1,  0,  1,  1, -1, -1, -1],
           [ 0,  0,  1,  1,  0, -1, -1]]
   assert coup_gagnant(joueur, i, j, grille)==True