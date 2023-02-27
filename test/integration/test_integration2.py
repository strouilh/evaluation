import pytest

from gui import construire_gui
from noyau import jouer

def test_jouer():
   joueur=[('Laurel', 'orange'), ('Hardy', 'green')]
   rang=0
   grille=[[-1]*7 for _ in range(6)]  
   niveau=[5]*7
   etat="en cours"

   (f, gbouton, message)=construire_gui(joueur[rang])
   jouer("02", gbouton, message) #lc

   assert gbouton[5][2]["bg"]==joueur[rang][1]