# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

from PyQt4 import QtGui, QtCore

class Mur:
    def __init__(self, voisin1, voisin2):
        self.v1, self.v2 = voisin1, voisin2

    
    def __str__(self):
        s = "Mur entre les cases: "
        s += str(self.v1)
        s += " et: "
        s += str(self.v2)
        return s
    
    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

        
    def dessin(self, qp, ihm):
        pass
        

class MurHorizontal(Mur):
    def __init__(self, voisin1, voisin2):
        super().__init__(voisin1,voisin2)
        self.image = 'images/murHorizontal.png'
    
        
    def dessin(self, qp, ihm):
        
        image_mur = QtGui.QImage(self.image)
        largeur = 7   #dimensions du mur en pixels
        hauteur = 40
        square_size = 50 #côté du carré d'une case
        
        painter = QtGui.QPainter(ihm)
        painter.drawImage(QtCore.QRectF(self.v1.position[0]*1.5*square_size + 20, self.v1.position[1]*1.5*square_size + 45, largeur, hauteur),image_mur)
        painter.resetTransform()


class MurVertical(Mur):
    def __init__(self, voisin1, voisin2):
        super().__init__(voisin1,voisin2)
        self.image = 'images/murVertical.png'
    
        
    def dessin(self, qp, ihm):
        
        image_mur = QtGui.QImage(self.image)
        largeur = 7   #dimensions du mur en pixels
        hauteur = 40
        square_size = 50 #côté du carré d'une case
        
        painter = QtGui.QPainter(ihm)
        painter.drawImage(QtCore.QRectF(self.v2.position[0]*1.5*square_size + 20, self.position[1]*1.5*square_size + 45, hauteur, largeur),image_mur)
        painter.resetTransform()

        
if __name__ == "__main__":
    mur = Mur((0,0),(1,0))
    print(mur)
    
    
    liste_murs = [mur]
    
    mur2 = Mur((0,0),(1,0))
    
    for mur in liste_murs:
        if mur2 == mur:
            print(True)