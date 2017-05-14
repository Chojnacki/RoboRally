# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import Cases
import Murs
import MatriceD as md

class Plateau():
    def __init__(self, x = 10, y = 10):
        """
        x = nombre de colonnes; y = nombre de lignes; default = 10 par 10
        l'axe X est oriente de gauche a droite
        l'axe Y est oriente de haut en bas
        l'origine du repère se situe en haut à gauche du tableau
        """
        self.cases = [[Cases.CaseNeutre((a,b)) for a in range(x)] for b in range(y)]
        self.casesVictoire = []
        self.x = x
        self.y = y
        self.listeDeparts = []
        self.listeMurs = []
        self.m0 = None #matrice de déplacement de 1 vers la droite
        self.m1 = None #vers le haut
        self.m2 = None #la gauche
        self.m3 = None #le bas
        self.mc = None #Matrice de déplacement du plateau (dû aux cases, murs compris)
    

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
        if isinstance(case,Cases.CaseArrivee):
            self.casesVictoire.append((x,y))
    
    def ajouterMur(self, mur):
        self.listeMurs.append(mur)
    
    def prepare(self):
        Id = md.MatriceD(self.x,self.y,0,None,self.listeMurs) #la multiplication par "l'identité" permet de prendre en compte les murs 
        self.m0 = Id*md.MatriceD(angle = 0, matrice = [[(0,i+1,j,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m1 = Id*md.MatriceD(angle = 1, matrice = [[(0,i,j - 1,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m2 = Id*md.MatriceD(angle = 2, matrice = [[(0,i - 1,j,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m3 = Id*md.MatriceD(angle = 3, matrice = [[(0,i,j + 1,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        
        matriceEffetCases = Id #matrice d'effet des cases
        for y in range(self.y):
            for x in range(self.x):
                case = self.cases[y][x]
                matriceEffetCases.m[y][x] = case.MD
        self.mc = matriceEffetCases
        

if __name__ == "__main__":
    import plateau1 as p
    plateau = p.plateau
    plateau.prepare()
    
    print('m0')
    print(plateau.m0)
    print('m1')
    print(plateau.m1)
    print('m2')
    print(plateau.m2)
    print('m3')
    print(plateau.m3)
    print('mc')
    print(plateau.mc)
    print(plateau.m0.position((9,0)))
#    for mur in plateau.listeMurs:
#        print(mur)










