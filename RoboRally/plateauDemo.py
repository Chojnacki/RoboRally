# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:07:39 2017

@author: chojnaal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:31:49 2017

@author: Chojnacki
"""

import Cases
import Cartes
import Murs
import Plateau



plateau = Plateau.Plateau(3,2)


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

#
case0 = Cases.Tapis((0,1),0)

engr = Cases.CaseEngrenage((1,0), -1)
engr2 = Cases.CaseEngrenage((1,1), 1)
mur = Murs.MurVertical((1,0),(2,0))
arrivee = Cases.CaseArrivee((2,0))
trou = Cases.CaseTrou((2,1))

#robot1_start = (5,2)   # A ajouter dans le code
#plateau.ajouterMur(mur)

cases = [case0]
Caz = [engr,engr2,arrivee,trou]
for case in Caz:
    plateau.mettreCase(case)
for case in cases:
    plateau.mettreCase(case)

nombreJoueurs = 1
plateau.nombreJoueurs = nombreJoueurs

# Pour ce tableau, le robot doit commencer à la position O,1 avec une orientation de 0

#Kertwonky a pour mission de selectionner 5 cartes avance de 1
#pour atteindre le trou qui le detruira

listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]