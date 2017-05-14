# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""


#import Murs
from PyQt4 import QtGui, QtCore

dico_orientation = {0: "Droite", 1: "Haut", 2: "Gauche", 3: "Bas"} # Ce dictionaire permet de traduire la direction à l'affichage


class Robot():
    
    def __init__(self,position,orientation = 0, liste_murs = []):
        self.__pv = 9
        self.__position = position
        self.__orientation = orientation
        self.state = [self.pv,self.position[0],self.position[1],self.orientation]

        self.image = 'images/gwenHaDu.png'

    def __str__(self):
        s = " Points de vie: "
        s += str(self.__pv)
        s += " | Position: "
        s += str(self.__position)
        s += " | Orientation: "
        s += str(dico_orientation[self.orientation])
        return s

    @property
    def orientation(self):
        """
        orientation: 0,1,2 ou 3
            direction du robot (0 = vers la droite, 1 = le haut, 2 = la gauche, 3 = le bas)
        """
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        """
        Met à jour l'orientation du robot.
        Garantit 0 <= orientation <= 3.
        """
        o = orientation
        o = max( min(o, 3), 0)

        self.state[3] = o
        self.__orientation = o
        
        return self.__orientation

    @property
    def position(self):
        """
        accesseur en lecture de la position du robot
        """
        return self.__position
    
    @position.setter
    def position(self, position):
        """
        accesseur en ecriture de la position du robot
        on passe les murs en argument
        """
        
        if self.pv == 0:
            None
        else:

                
#            mur_test = Murs.Mur(self.position,position)
#            # Mur avec lequel on compare les murs de la liste
#            print(mur_test)
#            
#            if not (mur_test in self.murs):

            self.state[1] = position[0]
            self.state[2] = position[1]

            self.__position = position
            
        
        return self.__position


    @property
    def pv(self):
        """
        """
        return self.__pv


    @pv.setter
    def pv(self, pv):
        """
        """
        self.__pv = pv
        self.state[0] = pv
        return self.__pv



    def set_state(self,given_state):
        [pv,x,y,o] = given_state
        self.pv = pv
        self.position = (x,y)
        self.orientation = o
        pass
    

    def dessin(self, qp):
        
        image_robot = QtGui.QImage(self.image)
        side = 48   #côté du carré qui représente le robot
        image_robot = image_robot.scaled(side,side)
        square_size = 50 #côté du carré d'une case
        

#        qp.rotate(self.orientation*20)  #Pour prendre en compte l'orientation du robot dans l'affichage
#        
#        if (self.orientation == 1 or self.orientation == 2):
#            correction_x  = side
#        else:
#            correction_x  = 0
#        if (self.orientation == 2 or self.orientation == 3):
#            correction_y  = side
#        else:
#            correction_y  = 0
#                    
#        qp.translate(correction_x,correction_y)           #Pour corriger le décalage créé par la fonction 'rotate'
#                         
#        qp.drawImage(QtCore.QRectF(self.position[0]*square_size + 20,self.position[1]*square_size + 45, side, side),image_robot)
#        qp.resetTransform()
        
        


        qp.rotate((-self.orientation%4)*90)  #Pour prendre en compte l'orientation du robot dans l'affichage
        
        x , y = self.position[0]*square_size + 20,self.position[1]*square_size + 45
        if self.orientation == 1:
            x,y = - square_size - y , x
        elif self.orientation == 2:
            x,y = - square_size - x , - square_size - y
        elif self.orientation == 3:
            x,y = y, - square_size-x
                    
        qp.drawImage(QtCore.QRectF(x, y, side, side),image_robot)
        qp.resetTransform()


    
if __name__ == "__main__":
    
    twonky = Robot((1,1),1)
    twonky.set_state((8,4,4,1))
    print(twonky)

    print(twonky.position)

#    print(twonky.state)
