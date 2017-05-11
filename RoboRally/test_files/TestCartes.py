# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Corazza
"""


import unittest
from Cases import *
import Robot as rob
from Cartes import *

class TestCartes(unittest.TestCase):
    
        
    def test_translat(self):
        
        Carte_Avance1 = Translation(1)
        twonky = rob.Robot((2,3),0)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 0)
        Carte_Avance1.effet(twonky)
        self.assertEqual(twonky.position, (3,3))
        self.assertEqual(twonky.orientation, 0)
        
        Carte_Avance2 = Translation(2)
        twonky = rob.Robot((2,3),1)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)
        Carte_Avance2.effet(twonky)
        self.assertEqual(twonky.position, (2,1))
        self.assertEqual(twonky.orientation, 1)
        
        Carte_Avance3 = Translation(3)
        twonky = rob.Robot((2,3),2)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 2)
        Carte_Avance3.effet(twonky)
        self.assertEqual(twonky.position, (-1,3)) #Coordonnee negative
        self.assertEqual(twonky.orientation, 2)
        
        Carte_Recule = Translation(-1)
        twonky = rob.Robot((2,3),3)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        Carte_Recule.effet(twonky)
        self.assertEqual(twonky.position, (2,2))
        self.assertEqual(twonky.orientation, 3)
        
        
        
    def test_rotat(self):
        
        Carte_DemiTour = Rotation(2)
        twonky = rob.Robot((2,3),3)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        Carte_DemiTour.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)
        
        
        Carte_Droite3 = Rotation(3)
        twonky = rob.Robot((2,3),3)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        Carte_Droite3.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 2)
        
        Carte_Droite2 = Rotation(3)
        twonky = rob.Robot((2,3),2)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 2)
        Carte_Droite2.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)
        
        Carte_Droite1 = Rotation(3)
        twonky = rob.Robot((2,3),1)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)
        Carte_Droite1.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 0)
        
        Carte_Droite0 = Rotation(3)
        twonky = rob.Robot((2,3),0)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 0)
        Carte_Droite0.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        
        
        Carte_Gauche3 = Rotation(1)
        twonky = rob.Robot((2,3),3)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        Carte_Gauche3.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 0)
        
        Carte_Gauche2 = Rotation(1)
        twonky = rob.Robot((2,3),2)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 2)
        Carte_Gauche2.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 3)
        
        Carte_Gauche1 = Rotation(1)
        twonky = rob.Robot((2,3),1)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)
        Carte_Gauche1.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 2)
        
        Carte_Gauche0 = Rotation(1)
        twonky = rob.Robot((2,3),0)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 0)
        Carte_Gauche0.effet(twonky)
        self.assertEqual(twonky.position, (2,3))
        self.assertEqual(twonky.orientation, 1)

        
if __name__ == '__main__':
    unittest.main()