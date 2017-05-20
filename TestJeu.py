#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:01:38 2017

@author: Corazza Alexandre
"""

import unittest
import Jeu

class TestJeu(unittest.TestCase):
    
    def testTri(self):

#        On test si les cartes sont rangées par ordre décroissant de vitesse
#        (2e paramètre des couples de la liste)

        liste = [(1,3),(2,3),(3,3)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(1, 3), (2, 3), (3, 3)])

        liste = [(1,1),(2,4),(3,6)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(3, 6), (2, 4), (1, 1)])
        
        liste = [(1,-1),(2,6),(3,2)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(2, 6), (3, 2), (1, -1)])
        
        liste = [(1,4),(2,1),(3,2)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(1, 4), (3, 2), (2, 1)])
        
        liste = [(1,-1),(2,1),(3,2)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(3, 2), (2, 1), (1, -1)])
        
        liste = [(1,1),(2,2),(3,-1)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(2, 2), (1, 1), (3, -1)])
        
        liste = [(1,3),(2,2),(3,-1)]
        Jeu.tri_bulle(liste)
        self.assertEqual(liste, [(1, 3), (2, 2), (3, -1)])     
        
        
    def TestTransitionPosition(self):
        
#        On test les positions intermediaires entre deux points
        
        
        liste = Jeu.transitionPositions((0,0),(2,0))
        self.assertEqual(liste, [(0, 0), (1, 0), (2, 0), (3, 0)])
        liste = Jeu.transitionPositions((0,0),(0,1))
        self.assertEqual(liste, [(0, 0), (0, 1), (0, 2)])
        liste = Jeu.transitionPositions((2,0),(0,0))
        self.assertEqual(liste, [(2, 0), (1, 0), (0, 0), (-1, 0)])
        liste = Jeu.transitionPositions((0,2),(0,0))
        self.assertEqual(liste, [(0, 2), (0, 1), (0, 0), (0, -1)])
        liste = Jeu.transitionPositions((0,0),(0,0))
        self.assertEqual(liste, [(0, 0)])
        
        
if __name__ == '__main__':
    unittest.main()