# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Corazza
"""

import unittest
from Cases import *
import Robot as rob
import MatriceD

class TestCases(unittest.TestCase):
    
    def test_init(self):
        
        Case_Neutre = CaseNeutre((1,1))
        Case_Arrivee = CaseArrivee((2,2))
        Case_Trou = CaseTrou((3,3))
        Case_Reparation = CaseReparation((4,4))
        Case_Engrenage = CaseEngrenage((5,5),-1)
        Case_Tapis = Tapis((2,3),0,False)
        self.assertEqual(Case_Neutre.position, (1,1))
        self.assertEqual(Case_Arrivee.position, (2,2))
        self.assertEqual(Case_Trou.position, (3,3))
        self.assertEqual(Case_Reparation.position, (4,4))
        self.assertEqual(Case_Engrenage.position, (5,5))
        self.assertEqual(Case_Tapis.position, (2,3))

    

    def test_effet_trou(self):
        
        Case_Trou = CaseTrou((4,6))
        twonky = rob.Robot((4,6))
        self.assertEqual(twonky.pv, 9)
        Case_Trou.effet(twonky)
        self.assertEqual(twonky.pv, 0)
        

    def test_effet_reparation(self):
        
        Case_Reparation = CaseReparation((4,6))
        twonky = rob.Robot((4,6))
        self.assertEqual(twonky.pv, 9)
        Case_Reparation.effet(twonky)
        self.assertEqual(twonky.pv, 10)
        
        
    def test_effet_engrenage(self):
        
        Case_EngrenageD = CaseEngrenage((1,1),-1)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Case_EngrenageD.effet(twonky)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 0)

        Case_EngrenageG = CaseEngrenage((1,1),1)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Case_EngrenageG.effet(twonky)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 2)
        
        Case_EngrenageG3 = CaseEngrenage((1,1),1)
        twonky = rob.Robot((1,1),3)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 3)
        Case_EngrenageG3.effet(twonky)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 0)
        
        Case_EngrenageD3 = CaseEngrenage((1,1),-1)
        twonky = rob.Robot((1,1),3)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 3)
        Case_EngrenageD3.effet(twonky)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 2)


    def test_effet_tapis(self):
        
        Tapisdroite = Tapis((1,1),0,False)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Tapisdroite.effet(twonky)
        self.assertEqual(twonky.position, (2,1))
        self.assertEqual(twonky.orientation, 1)
        
        Tapishaut = Tapis((1,1),1,False)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Tapishaut.effet(twonky)
        self.assertEqual(twonky.position, (1,0))
        self.assertEqual(twonky.orientation, 1)
        
        Tapisgauche = Tapis((1,1),2,False)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Tapisgauche.effet(twonky)
        self.assertEqual(twonky.position, (0,1))
        self.assertEqual(twonky.orientation, 1)
        
        Tapisbas = Tapis((1,1),3,False)
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        Tapisbas.effet(twonky)
        self.assertEqual(twonky.position, (1,2))
        self.assertEqual(twonky.orientation, 1)


        VirageDdroite = Tapis((1,1),0,"Droite")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageDdroite.effet(twonky)
        self.assertEqual(twonky.position, (1,2))
        self.assertEqual(twonky.orientation, 0)
        
        VirageDhaut = Tapis((1,1),1,"Droite")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageDhaut.effet(twonky)
        self.assertEqual(twonky.position, (2,1))
        self.assertEqual(twonky.orientation, 0)
        
        VirageDgauche = Tapis((1,1),2,"Droite")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        VirageDgauche.effet(twonky)
        self.assertEqual(twonky.position, (1,0))
        self.assertEqual(twonky.orientation, 0)
        
        VirageDbas = Tapis((1,1),3,"Droite")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageDbas.effet(twonky)
        self.assertEqual(twonky.position, (0,1))
        self.assertEqual(twonky.orientation, 0)
        
        
        VirageGdroite = Tapis((1,1),0,"Gauche")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageGdroite.effet(twonky)
        self.assertEqual(twonky.position, (1,0))
        self.assertEqual(twonky.orientation, 2)
        
        VirageGhaut = Tapis((1,1),1,"Gauche")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageGhaut.effet(twonky)
        self.assertEqual(twonky.position, (0,1))
        self.assertEqual(twonky.orientation, 2)
        
        VirageGgauche = Tapis((1,1),2,"Gauche")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageGgauche.effet(twonky)
        self.assertEqual(twonky.position, (1,2))
        self.assertEqual(twonky.orientation, 2)
        
        VirageGbas = Tapis((1,1),3,"Gauche")
        twonky = rob.Robot((1,1),1)
        self.assertEqual(twonky.position, (1,1))
        self.assertEqual(twonky.orientation, 1)
        VirageGbas.effet(twonky)
        self.assertEqual(twonky.position, (2,1))
        self.assertEqual(twonky.orientation, 2)
        

if __name__ == '__main__':
    unittest.main()