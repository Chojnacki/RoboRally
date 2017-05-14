# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

from PyQt4 import QtGui, QtCore

class Mur:
    def __init__(self, voisin1, voisin2):
        
        #petite boucle pour que les murs soient définis de gauche à droite et de haut en bas
        if voisin1[0] <= voisin2[0] and voisin1[1] <= voisin2[1]:
            pass
        else:
            voisin1,voisin2 = voisin2,voisin1
        self.v1, self.v2 = voisin1, voisin2
        self.x = (self.v1[0] + self.v2[0])/ 2
        self.y = (self.v1[1] + self.v2[1])/ 2

    
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

        
        
    def dessin(self, qp):
        pass
        

class MurHorizontal(Mur):
    def __init__(self, voisin1, voisin2):
        super().__init__(voisin1,voisin2)
        self.image = 'images/murHorizontal.png'
        
        
    def dessin(self, qp):
        
        image_mur = QtGui.QImage(self.image)
        largeur = 50   #dimensions du mur en pixels
        hauteur = 7
        square_size = 50 #côté du carré d'une case
                
        qp.drawImage(QtCore.QRectF(self.x*square_size + 18, self.y*square_size + 66, largeur, hauteur),image_mur)
        qp.resetTransform()


class MurVertical(Mur):
    def __init__(self, voisin1, voisin2):
        super().__init__(voisin1,voisin2)
        self.image = 'images/murVertical.png'
    
        
    def dessin(self, qp):
        
        image_mur = QtGui.QImage(self.image)
        largeur = 7   #dimensions du mur en pixels
        hauteur = 50
        square_size = 50 #côté du carré d'une case
                
        qp.drawImage(QtCore.QRectF(self.x*square_size + 40, self.y*square_size + 43, largeur, hauteur),image_mur)
        qp.resetTransform()

        
class Laser(Mur):
    def __init__(self, voisin1, voisin2):
        super().__init__(voisin1, voisin2)
        
        
if __name__ == "__main__":
    mur = Mur((0,0),(1,0))
    print(mur)
    
    
    liste_murs = [mur]
    
    mur2 = Mur((0,0),(1,0))
    
    for mur in liste_murs:
        if mur2 == mur:
            print(True)