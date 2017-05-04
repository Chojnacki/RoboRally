# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Corazza
"""


import unittest
from Cases import *
import Robot as rob
from Cartes import *
import Master as M
import Plateau as P
import Joueur as J

class TestJoueur(unittest.TestCase):
    
        
    def test_distribuer(self):
        listeCartes1 = [Cartes.Carte() for i in range(20)]
        
        
        self.assertEqual()

        
if __name__ == '__main__':
    unittest.main()