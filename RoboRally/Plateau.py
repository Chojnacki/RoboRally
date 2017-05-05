# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import Cases
import Cartes
import Murs

class Plateau:
    def __init__(self, x = 10, y = 10):
        """
        x = nombre de colonnes; y = nombre de lignes; default = 10 par 10
        l'axe X est oriente de gauche a droite
        l'axe Y est oriente de haut en bas
        l'origine du repère se situe en haut à gauche du tableau
        """
        self.cases = [[Cases.CaseNeutre((a,b)) for a in range(x)] for b in range(y)]
        self.x = x
        self.y = y
        self.listeMurs = []
    

    def __str__(self):
        s = ""
        for liste in self.cases:
            for case in liste:
                s += case.car
            s += "\n"
        return s
    
    def mettreCase(self, case):
        """
        Insère la case dans le tableau de jeu
        
        Paramètres
        ----------
        case: la case à inserer
        """
        x,y = case.position
        self.cases[y][x] = case
    
    def ajouterMur(self, mur):
        self.listeMurs.append(mur)

#On cree des plateau prêt à l'emploi pour le jeu, avec leur jeux de cartes associes
plateau1 = Plateau(10,5)
mur = Murs.Mur((0,0),(1,0))
case = Cases.Tapis((1,1),0,False)
plateau1.mettreCase(case)
plateau1.ajouterMur(mur)
listeCartes1 = [Cartes.Carte() for i in range(20)]


plateau = Plateau(10,5)
tapis = Cases.Tapis((1,1),0,False)
engr = Cases.CaseEngrenage((3,1), -1)
tapis2 = Cases.Tapis((3,2),0,False)
engr2 = Cases.CaseEngrenage((4,3), -1)
trou = Cases.CaseArrivee((3,3))
plateau.ajouterMur(mur)

Caz = [tapis,engr,tapis2,engr2,trou]
for case in Caz:
    plateau.mettreCase(case)


# Pour ce tableau, le robot doit commencer à la position O,1 avec une orientation de 0

#Kertwonky a pour mission de selectionner 5 cartes avance de 1
#pour atteindre le trou qui le detruira

listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1)]


if __name__ == '__main__':
    plateau = Plateau(10,5)
    mur = Murs.Mur((0,0),(1,0))
    case = Cases.Tapis((1,1),0,False)
    plateau.mettreCase(case)
    plateau.ajouterMur(mur)
    print(plateau)
    print(plateau.listeMurs[0])











