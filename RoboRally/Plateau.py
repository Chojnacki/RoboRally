# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import Cases
import Murs

class Plateau():
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
        self.m0 = None #matrice de déplacement de 1 vers la droite
        self.m1 = None #vers le haut
        self.m2 = None #la gauche
        self.m3 = None #le bas
        self.mc = None #Matrice de déplacement du plateau (cases et murs inclus)
    

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
    
    def prepare(self):
        Id = MatriceD(self.x,self.y,None,self.listeMurs) #la multiplication par "l'identité" permet de prendre en compte les murs 
        self.m0 = Id*MatriceD(matrice = [[(i+1,j) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m1 = Id*MatriceD(matrice = [[(i,j - 1) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m2 = Id*MatriceD(matrice = [[(i - 1,j) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m3 = Id*MatriceD(matrice = [[(i,j + 1) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        
        matriceD_cases = Id
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
                    matriceD_cases.m[y][x] = destination  #On place la destination dans la matrice avec l'effet des cases
        self.mc = matriceD_cases
        
                

class MatriceD(object): #Matrice de Déplacement
    def __init__(self,x = 0,y = 0,matrice = None,listeMurs = []):
        if matrice:
            self.x = len(matrice[0])
            self.y = len(matrice)
            self.m = matrice[:][:]
        else:
            self.x, self.y = x,y
            self.m = [[(a,b) for a in range(x)] for b in range(y)]
        self.listeMurs = listeMurs[:]
        
    def __mul__(self, other):
        
#        print ('__mul__')
        
        matrice = MatriceD(self.x,self.y,None,self.listeMurs)
        if not (self.x == other.x and self.y == other.y):
            raise Exception ('matrices de taille différentes')
        
        for x in range(self.x):
            for y in range(self.y):
                target = self.m[y][x]
                (targetx,targety) = target
#                print(targetx,targety)
#                print(0 <= targetx < x)
                if (0 <= targetx < self.x) and (0 <= targety < self.y):
                    new_target = other.m[targety][targetx]
#                    print(target,new_target)
                    for mur in self.listeMurs:
                        if (mur.v1 == target and mur.v2 == new_target) or (mur.v2 == target and mur.v1 == new_target):
                            matrice.m[y][x] = target
#                            print(target)
                            break
                        else:
                            matrice.m[y][x] = new_target
                        
                else:
                    matrice.m[y][x] = None
        return matrice
        
    def __str__(self):
        s = ""
        for y in range(self.y):
            for x in range(self.x):
                s += str(self.m[y][x])
                s += " "
            s += "\n"
        return s
        


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
#    for mur in plateau.listeMurs:
#        print(mur)










