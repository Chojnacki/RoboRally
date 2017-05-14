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