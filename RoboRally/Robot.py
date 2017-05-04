# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import Murs
from PyQt4 import QtGui, QtCore

dico_orientation = {0: "Droite", 1: "Haut", 2: "Gauche", 3: "Bas"} # Ce dictionaire permet de traduire la direction à l'affichage


class Robot():
    
    def __init__(self,position,orientation = 0, liste_murs = []):
        self.__pv = 9
        self.__position = position
        self.__orientation = orientation
        self.murs = liste_murs
        self.image = 'images/gwenHaDu.jpg'
        self.image = 'images/triskel.png'

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
        
        mur_test = Murs.Mur(self.position,position)
        # Mur avec lequel on compare les murs de la liste
#        print(mur_test)
        
        if not (mur_test in self.murs):
            self.__position = position
        
        
        
        """ Ce test ne marche que pour un déplacement d'une case """
        
        
        
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
        return self.__pv

    def dessin(self, qp, ihm):
        
        image_robot = QtGui.QImage(self.image)
        square_size = 67
        
        painter = QtGui.QPainter(ihm)
        painter.drawImage(QtCore.QRectF(self.position[0]*square_size + 20,self.position[1]*square_size + 45, 50, 50),image_robot)
        
        
#        painter.setPen(QtGui.QPen(QtCore.Qt.red))
#        painter.drawArc(QtCore.QRectF(self.position[0]*100 + 35,self.position[1]*100 + 65, 10, 10), 0, 5760)
        

    
if __name__ == "__main__":
    
    twonky = Robot((1,1),1)
    print(twonky)
    print(twonky.position)
    
    
    
    
    
    
    
    
    
    
    
    