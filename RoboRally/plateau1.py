# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:01:20 2017

@author: oblivioner
"""

import Cases
import Cartes
import Murs
import Plateau



plateau = Plateau.Plateau(10,5)
tapis = Cases.Tapis((1,1),0,False)
engr = Cases.CaseEngrenage((3,1), -1)
tapis2 = Cases.Tapis((3,2),0,False)
engr2 = Cases.CaseEngrenage((4,3), -1)
trou = Cases.CaseArrivee((3,3))
mur = Murs.MurVertical((0,0),(1,0))
mur1 = Murs.MurVertical((9,0),(10,0))
mur2 = Murs.MurHorizontal((0,3),(0,4))
#robot1_start = (5,2)   # A ajouter dans le code


plateau.ajouterMur(mur)
plateau.ajouterMur(mur1)
plateau.ajouterMur(mur2)

Caz = [tapis,engr,tapis2,engr2,trou]
for case in Caz:
    plateau.mettreCase(case)


# Pour ce tableau, le robot doit commencer à la position O,1 avec une orientation de 0

#Kertwonky a pour mission de selectionner 5 cartes avance de 1
#pour atteindre le trou qui le detruira

listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]