#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:39:49 2017

@author: alex
"""



import Cases
import Cartes
import Murs
import Plateau


#Creation du plateau
plateau = Plateau.Plateau(16,12)
platx = plateau.x - 1
platy = plateau.y - 1

#implementation des murs sur le plateau
mur = Murs.MurVertical((3,2),(4,2))
mur2 = Murs.MurHorizontal((7,2),(7,3))
listeMurs= [mur,mur2]

for murs in listeMurs:
    plateau.ajouterMur(murs)

#implementation des cases sur 1/4 du plateau puis symetrie
tapis = Cases.Tapis((2,1),0,False)
tapis2 = Cases.Tapis((3,1),0,False)
tapis3 = Cases.Tapis((4,1),0,"Droite")
tapis4 = Cases.Tapis((5,1),0,False)
tapis5 = Cases.Tapis((6,1),0,"Droite")
tapis6 = Cases.Tapis((6,2),3,False)
tapis7 = Cases.Tapis((4,2),3,False)
engr = Cases.CaseEngrenage((6,3), -1)
engr2 = Cases.CaseEngrenage((4,3), 1)
trou = Cases.CaseTrou((5,3))
trou2 = Cases.CaseTrou((5,2))
repa = Cases.CaseReparation((7,2))
arrivee = Cases.CaseArrivee((7,5))

#listes differentes car parametres differents dans la fonction copy
listeCases = [trou,trou2,arrivee,repa]
listeTapisHor = [tapis,tapis2,tapis3,tapis4,tapis5]
listeTapisVer = [tapis6,tapis7]
listeEngr = [engr,engr2]

for case in listeCases:
    plateau.mettreCase(case)
    caseCopy=case.copy(platx-case.position[0])
    plateau.mettreCase(caseCopy)
    caseCopy2=case.copy(None,platy-case.position[1])
    plateau.mettreCase(caseCopy2)
    caseCopy3=case.copy(platx-case.position[0],platy-case.position[1])
    plateau.mettreCase(caseCopy3)
    
for case in listeTapisHor:
    plateau.mettreCase(case)
    caseCopy=case.copy(platx-case.position[0],None, 2, 1)
    plateau.mettreCase(caseCopy)
    caseCopy2=case.copy(None,platy-case.position[1],0,1)
    plateau.mettreCase(caseCopy2)
    caseCopy3=case.copy(platx-case.position[0], platy-case.position[1], 2, 0)
    plateau.mettreCase(caseCopy3)
    
for case in listeTapisVer:
    plateau.mettreCase(case)
    caseCopy=case.copy(platx-case.position[0],None, 0, 1)
    plateau.mettreCase(caseCopy)
    caseCopy2=case.copy(None,platy-case.position[1],2,1)
    plateau.mettreCase(caseCopy2)
    caseCopy3=case.copy(platx-case.position[0], platy-case.position[1], 2, 0)
    plateau.mettreCase(caseCopy3)
    
for case in listeEngr:
    plateau.mettreCase(case)
    caseCopy=case.copy(platx-case.position[0], 0, -1)
    plateau.mettreCase(caseCopy)
    caseCopy2=case.copy(None,platy-case.position[1], -1)
    plateau.mettreCase(caseCopy2)
    caseCopy3=case.copy(platx-case.position[0],platy-case.position[1])
    plateau.mettreCase(caseCopy3)
    
#robot1_start = (5,2)   # A ajouter dans le code

#mise en place des murs autour du plateau
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




# Pour ce tableau, le robot doit commencer à la position O,1 avec une orientation de 0



listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(-1), Cartes.Translation(-1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]