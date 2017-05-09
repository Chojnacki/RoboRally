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




if __name__ == '__main__':
    plateau = Plateau(10,5)
    mur = Murs.Mur((0,0),(1,0))
    case = Cases.Tapis((1,1),0,False)
    plateau.mettreCase(case)
    plateau.ajouterMur(mur)
    print(plateau)
    print(plateau.listeMurs[0])











