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
        self.nombreJoueurs = 2 # par défaut: 2 joueurs, à modifier lors de la création des plateaux
        self.listeMurs = []
        self.listeEtatsDepart = [(9,0,0,0),(9,x-1,0,3),(9,x-1,y-1,2),(9,0,y-1,1)] # par défaut: 9 pv, orientation sens horaire, 4 coins de la carte
        self.m0 = None #matrice de déplacement de 1 vers la droite (les murs sont pris en compte, pas les robots ni les cases)
        self.m1 = None #vers le haut
        self.m2 = None #la gauche
        self.m3 = None #le bas
        self.mc = None #Matrice de déplacement du plateau (effet des cases et murs)
    

    def __str__(self):
        s = ""
        for liste in self.cases:
            for case in liste:
                s += case.car
            s += "\n"
        return s    

# TRIED TO IMPLEMENT INDEXING
#    def __getitem__(self, y):
#        """Get a list item"""
#        return self.m[y]
#
#    def __delitem__(self, y):
#        """Delete an item"""
#        del self.m[y]
#
#    def __setitem__(self, ii, val):
#        # optional: self._acl_check(val)
#        self.m[y] = val
    
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
#        print(Id)
        self.m0 = Id*md.MatriceD(angle = 0, matrice = [[(0,i+1,j,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m1 = Id*md.MatriceD(angle = 1, matrice = [[(0,i,j - 1,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m2 = Id*md.MatriceD(angle = 2, matrice = [[(0,i - 1,j,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        self.m3 = Id*md.MatriceD(angle = 3, matrice = [[(0,i,j + 1,0) for i in range(self.x)] for j in range(self.y)], listeMurs = self.listeMurs)
        
        matriceEffetCases = md.MatriceD(self.x,self.y,0,None,self.listeMurs) #matrice d'effet des cases
        for y in range(self.y):
            for x in range(self.x):
                case = self.cases[y][x]
                matriceEffetCases.m[y][x] = case.MD

        self.mc = matriceEffetCases
        self.prepareTrou() #permet de mettre les pv à 0 dans les matrices de déplacement: en effet les trous sont les seules cases qui agissent en dynamique
    
    def prepareTrou(self):
        matriceTrous = md.MatriceD(self.x,self.y,0,None,self.listeMurs)
        for y,rangee in enumerate(self.cases):
            for x,case in enumerate(rangee):
                if isinstance(case,Cases.CaseTrou):
#                        print(case, x ,y)
                    matriceTrous.m[y][x] = 9,x,y,0
    
        listeMatricesD = [self.m0,self.m1,self.m2,self.m3,self.mc]
#        for matrice in listeMatricesD:
#            matrice = matrice * matriceTrous
            
        
        #Pour chaque trou : on regarde toutes les cases des matrices de déplacements qui renvoient dessus et on met les dégats à 9
        for yT,rangeeT in enumerate(self.cases):
            for xT,case in enumerate(rangeeT):
                if isinstance(case,Cases.CaseTrou):
                    for matrice in listeMatricesD:
                        for y,rangee in enumerate(matrice.m):
                            for x,s in enumerate(rangee):
                                if s[1] == xT and s[2] == yT:
                                    matrice.m[y][x] = 9,xT,yT,0
                                    

if __name__ == "__main__":
    import plateau0 as p
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
    print(plateau.mc((9,2,1,0)))
#    for mur in plateau.listeMurs:
#        print(mur)










