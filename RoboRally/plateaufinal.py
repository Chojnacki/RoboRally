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
plateau.listeDeparts = [(0,0),(15,0),(0,11),(15,11)]

#implementation des cases sur 1/4 du plateau
tapis = Cases.Tapis((2,1),0,False)
tapis2 = Cases.Tapis((3,1),0,False)
tapis3 = Cases.Tapis((4,1),0,"Droite")
tapis4 = Cases.Tapis((5,1),0,False)
tapis5 = Cases.Tapis((6,1),0,"Droite")
tapis6 = Cases.Tapis((6,2),3,False)
tapis7 = Cases.Tapis((4,2),3,False)
tapis8 = Cases.Tapis((7,3),0,"Droite")
tapis9 = Cases.Tapis((6,4),3,"Gauche")
engr = Cases.CaseEngrenage((6,3), -1)
engr2 = Cases.CaseEngrenage((4,3), 1)
trou = Cases.CaseTrou((5,3))
trou2 = Cases.CaseTrou((5,2))
trou3 = Cases.CaseTrou((7,4))
repa = Cases.CaseReparation((7,2))
arrivee = Cases.CaseArrivee((7,5))

#listes differentes car parametres differents dans la fonction copy
listeCases = [trou,trou2,trou3,arrivee,repa]
listeTapisHor = [tapis,tapis2,tapis3,tapis4,tapis5,tapis8]
listeTapisVer = [tapis6,tapis7,tapis9]
listeEngr = [engr,engr2]


    
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
    

#implementation des murs sur le plateau
mur1 = Murs.MurHorizontal((7,2),(7,3))
mur2 = Murs.MurVertical((3,2),(4,2))
mur3 = Murs.MurVertical((7,0),(8,0))
mur4 = Murs.MurVertical((7,1),(8,1))
mur5 = Murs.MurVertical((0,4),(1,4))
mur6 = Murs.MurVertical((0,5),(1,5))
mur7 = Murs.MurHorizontal((1,5),(1,6))
mur8 = Murs.MurHorizontal((2,5),(2,6))
listeMursH = [mur1,mur7,mur8]
listeMursV = [mur2,mur3,mur4,mur5,mur6]

for mur in listeMursH:
    plateau.ajouterMur(mur)
    murCopy = Murs.MurHorizontal((platx-mur.v1[0], mur.v1[1]), (platx-mur.v2[0],mur.v2[1]))
    plateau.ajouterMur(murCopy)
    murCopy = Murs.MurHorizontal((platx-mur.v1[0], platy - mur.v1[1]),(platx-mur.v2[0], platy - mur.v2[1]))
    plateau.ajouterMur(murCopy)
    murCopy = Murs.MurHorizontal((mur.v1[0],platy-mur.v1[1]),(mur.v2[0], platy-mur.v2[1]))
    plateau.ajouterMur(murCopy)
    
for mur in listeMursV:
    plateau.ajouterMur(mur)
    murCopy = Murs.MurVertical((platx-mur.v1[0], mur.v1[1]), (platx-mur.v2[0],mur.v1[1]))
    plateau.ajouterMur(murCopy)
    murCopy = Murs.MurVertical((platx-mur.v1[0], platy - mur.v1[1]),(platx-mur.v2[0], platy - mur.v2[1]))
    plateau.ajouterMur(murCopy)
    murCopy = Murs.MurVertical((mur.v1[0],platy-mur.v1[1]),(mur.v2[0], platy-mur.v2[1]))
    plateau.ajouterMur(murCopy)
    
    
#Symetrie de toutes les cases et les murs
for case in listeCases:
    plateau.mettreCase(case)
    caseCopy=case.copy(platx-case.position[0])
    plateau.mettreCase(caseCopy)
    caseCopy2=case.copy(None,platy-case.position[1])
    plateau.mettreCase(caseCopy2)
    caseCopy3=case.copy(platx-case.position[0],platy-case.position[1])
    plateau.mettreCase(caseCopy3)
    

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


nombreJoueurs = 2
    
listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(-1), Cartes.Translation(-1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]