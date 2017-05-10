# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Corazza
"""


import abc
from PyQt4 import QtGui, QtCore

class Carte():
    """
    Classe decrivant les differents types de cartes
    """
    
    __metaclass__ = abc.ABCMeta


    def __init__(self):
        """
        Cree une carte.
        
        Paramètres
        ----------
        """
        
    def __str__(self):
        """
        Affiche le type de l'objet
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichee via ''print''
        """
        return "Carte"
        
    @abc.abstractmethod
    def effet(self):
        """
        Applique l'effet de la carte sur le robot
        
        Paramètres
        ----------
        Aucun
        """
        pass
    
    def dessin(self, qp, image, x, y):
        
        image = QtGui.QImage(self.image)
        side1 = 100 #dimensions d'une carte
        side2 = 200
        qp.drawImage(QtCore.QRectF(x*side1 + 900, y*side2 + 50, side1, side2),image)
        qp.resetTransform()

    
class Translation(Carte):
    """
    La carte translation fait avancer ou reculer le robot.
    """
    
    def __init__(self, vitesse):
        """
        Cree une carte translation
        
        Paramètres
        ----------
        vitesse: int
            [-1,3]
        """
        super().__init__()
        self.__vitesse = vitesse
        self.image = 'images/avance{}.png'.format(self.__vitesse)
        
    def __str__(self):
        """
        Affiche le type de l'objet
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichee via ''print''
        """
        return 'Carte translation {}'.format(self.__vitesse)

        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la carte
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la carte.
        """
        return "T"
    
    
    def effet(self,robot):
        """
        Le robot se deplace suivant son orientation
        
        Paramètres
        ----------
        robot: Robot
           
        """
        if self.__vitesse > 0:
            for i in range(self.__vitesse):
                if robot.orientation == 0:
                    robot.position = (robot.position[0]+1,robot.position[1])

                elif robot.orientation == 1:
                    robot.position = (robot.position[0],robot.position[1]-1)

                elif robot.orientation == 2:
                    robot.position = (robot.position[0]-1,robot.position[1])

                elif robot.orientation == 3:
                    robot.position = (robot.position[0],robot.position[1]+1)

        else:
                if robot.orientation == 0:
                    robot.position = (robot.position[0]-1,robot.position[1])

                elif robot.orientation == 1:
                    robot.position = (robot.position[0],robot.position[1]+1)

                elif robot.orientation == 2:
                    robot.position = (robot.position[0]+1,robot.position[1])

                elif robot.orientation == 3:
                    robot.position = (robot.position[0],robot.position[1]-1)


        
class Rotation(Carte):
    """
    La carte rotation fait tourner le robot
    """
    
    def __init__(self, angle):
        """
        Cree une carte rotation
        
        Paramètres
        ----------
        angle: int
            [1, 2, 3]
        """
        super().__init__()
        self.__angle = angle
        # Un angle de 3 correspond à 1/4 de tour à droite 
        # (3/4 de tour à gauche)
        self.image = 'images/rotat{}.png'.format(self.__angle)
        

    def __str__(self):
        """
        Affiche le type de l'objet
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichee via ''print''
        """
        dico_angle = {1: "Gauche", 2: "Demi-tour", 3: "Droite"}
        return 'Carte rotation {}'.format(dico_angle[self.__angle])
        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la carte
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la carte.
        """
        return "R"
    
    
    def effet(self,robot):
        """
        Le robot pivote
        
        Paramètres
        ----------
        robot: Robot
           
        """
        
        if robot.orientation + self.__angle <= 3:
            robot.orientation += self.__angle
            

        else:
            for i in range(1,4):
                    if robot.orientation == 4-i and self.__angle >= i:
                        robot.orientation = self.__angle - i
                        break #pour eviter de rentrer dans un autre if
                              #une fois la modification effectuee.       
                    
                    
if __name__ == '__main__':
    print("OK")
