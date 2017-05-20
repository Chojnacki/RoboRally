# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:31:49 2017

@author: Chojnacki
"""

import Cases
import Cartes
import Murs
import Plateau



plateau = Plateau.Plateau(10,5)
engr = Cases.CaseEngrenage((3,1), -1)
tapis2 = Cases.Tapis((3,2),0,False)
engr2 = Cases.CaseEngrenage((4,3), -1)
arrivee = Cases.CaseArrivee((3,3))
mur = Murs.MurVertical((0,0),(1,0))
#robot1_start = (5,2)   # A ajouter dans le code
plateau.ajouterMur(mur)


for y in range(0,plateau.y,1):
    mur = Murs.MurVertical((-1,y),(0,y))
    plateau.ajouterMur(mur)
    mur = Murs.MurVertical((plateau.x-1,y),(plateau.x,y))
    plateau.ajouterMur(mur)

for x in range(0,plateau.x,1):
    mur = Murs.MurHorizontal((x,-1),(x,0))
    plateau.ajouterMur(mur)
    mur = Murs.MurHorizontal((x,plateau.y-1),(x,plateau.y))
    plateau.ajouterMur(mur)


case0 = Cases.Tapis((0,2),0)
case1 = Cases.Tapis((1,2),0)
case2 = Cases.Tapis((2,2),0)
case3 = Cases.Tapis((2,1),0)

cases = [case0, case1, case2, case3]
Caz = [engr,tapis2,engr2,arrivee]
for case in Caz:
    plateau.mettreCase(case)
for case in cases:
    plateau.mettreCase(case)

nombreJoueurs = 2
plateau.nombreJoueurs = nombreJoueurs

# Pour ce tableau, le robot doit commencer à la position O,1 avec une orientation de 0

#Kertwonky a pour mission de selectionner 5 cartes avance de 1
#pour atteindre le trou qui le detruira

listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]