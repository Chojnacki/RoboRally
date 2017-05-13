#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:51:29 2017

@author: corazzal
"""

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
        self.__vitesse = 0
        self.__angle = 0
        
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
        
    @property
    def vitesse(self):
        return self.__vitesse
        
    @property
    def angle(self):
        return self.__angle
        
    @abc.abstractmethod
    def effet(self,robot):
        """
        Applique l'effet de la carte sur le robot
        
        Paramètres
        ----------
        Le robot sur lequel l'action doit être effectuée
        """
        return robot.state[:]
    
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
        self.__angle = 0
        self.image = 'images/avance{}.png'.format(self.__vitesse)
        
    @property
    def vitesse(self):
        return self.__vitesse
        
    @property
    def angle(self):
        return self.__angle
        
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
        v = self.__vitesse
        if v > 0:
            if robot.orientation == 0:
                estimate = (robot.position[0]+1*v,robot.position[1])

            elif robot.orientation == 1:
                estimate = (robot.position[0],robot.position[1]-1*v)

            elif robot.orientation == 2:
                estimate = (robot.position[0]-1*v,robot.position[1])

            elif robot.orientation == 3:
                estimate = (robot.position[0],robot.position[1]+1*v)

        else:
            if robot.orientation == 0:
                estimate = (robot.position[0]-1*v,robot.position[1])

            elif robot.orientation == 1:
                estimate = (robot.position[0],robot.position[1]+1*v)

            elif robot.orientation == 2:
                estimate = (robot.position[0]+1*v,robot.position[1])

            elif robot.orientation == 3:
                estimate = (robot.position[0],robot.position[1]-1*v)

        estimated_state = robot.state[:]
        estimated_state[1] = estimate[0]
        estimated_state[2] = estimate[1]
        return estimated_state

        
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
        self.__vitesse = 0
        # Un angle de 3 correspond à 1/4 de tour à droite 
        # (3/4 de tour à gauche)
        self.image = 'images/rotat{}.png'.format(self.__angle)
        
    @property
    def vitesse(self):
        return self.__vitesse
        
    @property
    def angle(self):
        return self.__angle
        

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
            estimate = robot.orientation + self.__angle
            

        else:
            for i in range(1,4):
                    if robot.orientation == 4-i and self.__angle >= i:
                        estimate = self.__angle - i
                        break #pour eviter de rentrer dans un autre if
                              #une fois la modification effectuee.
                        
        estimated_state = robot.state[:]
        estimated_state[3] = estimate % 4
        
        return estimated_state
                    
if __name__ == '__main__':
    print("OK")
