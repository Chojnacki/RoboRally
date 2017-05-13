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
        self.listeMurs = []
        self.m0 = None #matrice de déplacement de 1 vers la droite
        self.m1 = None #vers le haut
        self.m2 = None #la gauche
        self.m3 = None #le bas
        self.mc = None #Matrice de déplacement du plateau (cases et murs inclus)
#        self.prepare()
    

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
        Id = md.MatriceD(self.x,self.y,None,self.listeMurs) #la multiplication par "l'identité" permet de prendre en compte les murs 
        self.m0 = Id*md.MatriceD(matrice = [[(i+1,j) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m1 = Id*md.MatriceD(matrice = [[(i,j - 1) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m2 = Id*md.MatriceD(matrice = [[(i - 1,j) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m3 = Id*md.MatriceD(matrice = [[(i,j + 1) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        
        md.MatriceD_cases = Id
        for y in range(self.y):
            for x in range(self.x):
                case = self.cases[y][x]
                if isinstance(case,Cases.Tapis):
#                    print('true')
                    vitesse = case.vitesse
                    o = case.orientation
                    if o == 0:
                        matrice = self.m0
                    if o == 1:
                        matrice = self.m0
                    if o == 2:
                        matrice = self.m0
                    if o == 3:
                        matrice = self.m0
                    destination = matrice.m[y][x] #On récupère la destination (avec l'influence des murs)
                    md.MatriceD_cases.m[y][x] = destination  #On place la destination dans la matrice avec l'effet des cases
        self.mc = md.MatriceD_cases
        
                

        


#    def __rmul__(self, other):
#        print ('__rmul__')
#        return other


if __name__ == "__main__":
    plateau = Plateau(10,5)
    tapis = Cases.Tapis((1,1),0,False)
    engr = Cases.CaseEngrenage((3,1), -1)
    tapis2 = Cases.Tapis((3,2),0,False)
    engr2 = Cases.CaseEngrenage((4,3), -1)
    trou = Cases.CaseArrivee((3,3))

    Caz = [tapis,engr,tapis2,engr2,trou]
    for case in Caz:
        plateau.mettreCase(case)
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










