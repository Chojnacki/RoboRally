#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:07:07 2017

@author: Corazza
"""

from Cases import *
import Robot as rob
from Cartes import *
import Master as M
import Plateau as P
import Joueur as J


plateau = Plateau(10,5)
tapis = Cases.Tapis((1,1),0,False)
engr = Cases.CaseEngrenage((3,1), -1)
tapis2 = Cases.Tapis((3,2),0,False)
engr2 = Cases.CaseEngrenage((4,3), -1)
trou = Cases.CaseTrou(3,3)

Caz = [tapis,engr,tapis2,engr2,trou]
for case in Caz:
    plateau.mettreCase(case)


Kertwonky = rob.Robot((0,1),0)

#Kertwonky a pour mission de selectionner 5 cartes avance de 1
#pour atteindre le trou qui le detruira

listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1)]