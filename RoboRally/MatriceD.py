# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:34:03 2017

@author: oblivioner
"""


class MatriceD(object): #Matrice de Déplacement
    def __init__(self,x = 0,y = 0,angle = 0,matrice = None,listeMurs = []):
        if matrice:
            self.x = len(matrice[0])
            self.y = len(matrice)
            self.m = matrice[:][:]
        else:
            self.x, self.y = x,y
            self.m = [[(0,a,b,angle) for a in range(x)] for b in range(y)]
        self.listeMurs = listeMurs[:]
    
    def __call__(self,state):
        pv,x,y,o = state
        damage,new_x,new_y,angle = self.m[y][x]
        new_pv = max(0,pv - damage)
        new_o = (o + angle) % 4
        return new_pv,new_x,new_y,new_o
    
    def __mul__(self, other):
        
#        print ('__mul__')
        
        matrice = MatriceD(self.x,self.y,0,None,self.listeMurs)
        if not (self.x == other.x and self.y == other.y):
            raise Exception ('Matrices-D de taille différentes')
        
        for x in range(self.x):
            for y in range(self.y):
                target = self.m[y][x]
                (damage,targetx,targety,angle) = target
                if (0 <= targetx < self.x) and (0 <= targety < self.y):
                    new_target = other.m[targety][targetx]
                    new_damage,new_targetx,new_targety,new_angle = new_target
                    new_damage += damage                     #On prend en compte les dégats d'avant
                    damage += damage                         #idem, si on reste sur la même case
                    new_angle += angle % 4                  #On prend en compte l'angle
                    angle += angle % 4                      #idem
                    for mur in self.listeMurs:
                        if ((mur.v1 == (targetx,targety) and mur.v2 == (new_targetx,new_targety)) or (mur.v2 == (targetx,targety) and mur.v1 == (new_targetx,new_targety))):
#                            damage += new_target[0] #on ajoute les nouveaux dégats
#                            angle += new_target[3] % 4 #et la rotation
                            matrice.m[y][x] = damage,targetx,targety,angle
#                            print(mur.v1,targetx,targety,mur.v2,new_targetx,new_targety)
#                            print(target)
                            break
                        else:
                            matrice.m[y][x] = new_damage,new_targetx,new_targety,new_angle
                        
                else:
                    matrice.m[y][x] = None
        return matrice

    def __rmul__(self, other):
        if len(other) == 2:     #muliplication à gauche par une position
            x,y = other
            return self.m[y][x]
        elif len(other) == 4:   #muliplication à gauche par un état
            x,y = other[1],other[2]
            pv = other[0]
            o = other[3]
            if x and y:         #Permet de tenir compte des non déplacements (None)
                damage,x,y,angle = self.m[y][x]
                pv = max(0,other[0] - damage)
                o = other[3] + angle
            return pv,x,y,o
        else:
            raise TypeError('vous ne multipliez pas la MatriceD par un état / une position')


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
        

if __name__ == "__main__":
    
    
    #TESTS POUR LA MULTPLICATION PAR UN EXTERNE
    matrice = MatriceD(2,2,1,matrice = [[(1,0,0,1),(0,0,0,0)],[(3,0,1,0),(0,0,1,2)]],listeMurs = [])
    print(matrice)
#    print((0,1)*matrice)
#    print(matrice*(0,1))
#    print(matrice*(0,1)*matrice)
    print((9,0,0,0)*matrice)
    print((9,1,0,0)*matrice)
    print((9,0,1,0)*matrice)
    print((9,1,1,0)*matrice)
    state = (9,0,0,0)
    print(matrice(state))
#    print(matrice*matrice*(0,1))





















