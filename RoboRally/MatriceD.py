# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:34:03 2017

@author: oblivioner
"""


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
        
    def position(self, start):
        return self.m[start[1]][start[0]]
        























