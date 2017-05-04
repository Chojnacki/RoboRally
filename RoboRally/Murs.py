# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""


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


if __name__ == "__main__":
    mur = Mur((0,0),(1,0))
    print(mur)
    
    
    liste_murs = [mur]
    
    mur2 = Mur((0,0),(1,0))
    
    for mur in liste_murs:
        if mur2 == mur:
            print(True)