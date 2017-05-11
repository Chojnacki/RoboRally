#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:58:02 2017

@author: corazzal
"""

import abc
import Robot as rob
from PyQt4 import QtGui, QtCore


class Case():
    """
    Classe decrivant les differents types de cases.
    """
    
    __metaclass__ = abc.ABCMeta


    def __init__(self,position):
        """
        Cree une case aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple d'entiers
            Les coordonnees (x,y) auxquelles la case se trouvera  
            Par convention, x croit vers la droite et y vers le bas.
        """
        self.__pos = position
        self.image = 'images/caseNeutre.png'
        
        
    @property
    def position(self):
        return self.__pos
        
        
    def __str__(self):
        """
        Affiche la position de la case.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichee via ''print''
        """
        return "La case se trouve à la position " + str(self.__pos)
    
        
    @abc.abstractmethod
    def effet(self,robot):
        """
        Applique l'effet de la case sur le robot suivant le type de la case
        
        Paramètres
        ----------
        Aucun
        """
        return robot.state[:]
    
    def dessin(self, qp, image = 'images/caseNeutre.png'):
        
        image = QtGui.QImage(self.image)
        side = 50 #côté du carré d'une case
        qp.drawImage(QtCore.QRectF(self.position[0]*side + 20, self.position[1]*side + 45, side, side),image)
        qp.resetTransform()

    
    
class CaseNeutre(Case):
    """
    La case neutre n'a aucun effet sur le robot
    """
    
    def __init__(self,position):
        """
        Cree une case neutre aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple d'entiers
            Les coordonnees (x,y) auxquelles la case se trouvera  
            Par convention, x croit vers la droite et y vers le bas.
        """
        super().__init__(position) #On invoque le constructeur de la classe-mère
     
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la case neutre.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "N"
        
    


class CaseArrivee(Case):
    """
    La case arrivee fait gagner le premier robot qui l'atteint
    """
    
    def __init__(self,position):
        """
        Cree une case arrivee aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple d'entiers
            Les coordonnees (x,y) auxquelles la case se trouvera  
            Par convention, x croit vers la droite et y vers le bas.
        """
        super().__init__(position)
        self.image = 'images/caseArrivee.png'
        
        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la case arrivee.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "A"
    
    
    def effet(self,robot):
        """       
        Paramètres
        ----------
        robot: Robot
            autre idee: teleporte le robot sur une case à part
        """
        raise Exception('Victoire')
        pass

    
        
class CaseTrou(Case):
    """
    Le trou detruit immediatement le robot qui y tombe.
    """
    
    def __init__(self,position):
        """
        Cree une case Trou aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple d'entiers
            Les coordonnees (x,y) auxquelles la case se trouvera  
            Par convention, x croit vers la droite et y vers le bas.
        """
        super().__init__(position)
        self.image = 'images/trou.png'
        
        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la case trou.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "X"
    
        
    def effet(self,robot):
        """
        Detruit le robot.
        
        Paramètres
        ----------
        robot: Robot
            Le robot qui se trouve sur la case Trou perd tous ses points de vie.
        """
#        robot.pv = 0
        estimated_state = robot.state[:]
        estimated_state[0] = 0
        return estimated_state
        
        
        
        
        
class CaseReparation(Case):
    """
    La case reparation repare le robot et sauvegarde sa position.
    """
    def __init__(self,position):
        """
        Cree une case de reparation aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple d'entiers
            Les coordonnees (x,y) auxquelles la case se trouvera  
            Par convention, x croit vers la droite et y vers le bas.
        """
        super().__init__(position)
        self.image = 'images/reparation.png'
        
        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la case Reparation.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "R"
    
    
    def effet(self,robot):
        """
        Repare le robot et sauvegarde sa position.
        
        Paramètres
        ----------
        robot: Robot
            Le robot qui se trouve sur la case Reparation regagne un point de vie.
        """
        estimated_state = robot.state[:]
        if estimated_state[0] < 9:
            estimated_state[0] += 1
        return estimated_state
        
        
class CaseEngrenage(Case):
    """
    La case engrenage fait tourner le robot
    """
    
    def __init__(self,position,sens):
        """
        Cree une case engrenage aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple
            Les coordonnees (x,y) auxquelles la case se trouvera
            
        sens: int
            {-1: droite, 1: gauche}
            
        """
        super().__init__(position)
        self.__sens = sens
        self.image = 'images/engrenage{}.png'.format(self.__sens)
        
    @property    
    def car(self):
        """
        Renvoie l'identifiant de la case Engrenage.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "E"
    
    
    def effet(self,robot):
        """
        Fait pivoter le robot d'un quart de tour selon le sens de l'engrenage.
        
        Paramètres
        ----------
        robot: Robot
            Le robot qui se trouve sur la case tourne sur lui même.
        """
        
        estimate = (robot.orientation + self.__sens) % 4
        estimated_state = robot.state[:]
        estimated_state[3] = estimate
        return estimated_state
        
    
class Tapis(Case):
    def __init__(self,position,orientation,virage,vitesse=1):
        """
        Cree un tapis roulant aux coordonnees desirees.
        
        Paramètres
        ----------
        position: Couple
            Les coordonnees (x,y) auxquelles la case se trouvera  
            
        orientation : int 
            {0: Droite, 1: Haut, 2: Gauche, 3: Bas}

        virage: str ou bool 
            {Droite, Gauche, False}
        
        vitesse: int
            {1, 2}
        """
        super().__init__(position)
        self.__orientation = orientation
        self.__virage = virage
        self.__vitesse = vitesse 
        self.image = 'images/tapis{}{}{}.png'.format(self.__orientation, self.__virage, self.__vitesse)
        

        
    @property
    def car(self):
        """
        Renvoie l'identifiant de la case Tapis.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère representant la case.
        """
        return "T"
        
    
    def effet(self,robot):
        """
        Tapis droit
        
            Le robot se deplace simplement vers la case où le tapis est dirige.
        _______________________________________________________________________
        
        Tapis virage à droite ou gauche
        
            Le robot se deplace vers la case où le tapis est dirige et pivote
            d'un quart de tour à droite ou à gauche.
        _______________________________________________________________________        
        
        Paramètres
        ----------
        robot: Robot
            Le robot sur la case se deplace vers une autre case ou pivote.
        """
        
        #Convention x vers le droite, y vers le bas importante ici
        
        estimatetr = (robot.state[1],robot.state[2])
        estimateor = robot.state[3]
        
        for i in range(self.__vitesse):
            if self.__virage == False and self.__orientation == 0:
                estimatetr = (robot.position[0]+1,robot.position[1])
    
            elif self.__virage == False and self.__orientation == 1:
                estimatetr = (robot.position[0],robot.position[1]-1)
                
            elif self.__virage == False and self.__orientation == 2:
                estimatetr = (robot.position[0]-1,robot.position[1])
                
            elif self.__virage == False and self.__orientation == 3:
                estimatetr = (robot.position[0],robot.position[1]+1)
    
    
            
                
            if self.__virage == "Droite" and self.__orientation == 0:
                estimatetr = (robot.position[0],robot.position[1]+1)
                estimateor = robot.orientation - 1
    
            elif self.__virage == "Droite" and self.__orientation == 1:
                estimatetr = (robot.position[0]+1,robot.position[1])
                estimateor = robot.orientation - 1
                
            elif self.__virage == "Droite" and self.__orientation == 2:
                estimatetr = (robot.position[0],robot.position[1]-1)
                estimateor = robot.orientation - 1
                
            elif self.__virage == "Droite" and self.__orientation == 3:
                estimatetr = (robot.position[0]-1,robot.position[1])
                estimateor = robot.orientation - 1
                
                
                
                
            if self.__virage == "Gauche" and self.__orientation == 0:
                estimatetr = (robot.position[0],robot.position[1]-1)
                estimateor = robot.orientation + 1
    
            elif self.__virage == "Gauche" and self.__orientation == 1:
                estimatetr = (robot.position[0]-1,robot.position[1])
                estimateor = robot.orientation + 1
                
            elif self.__virage == "Gauche" and self.__orientation == 2:
                estimatetr = (robot.position[0],robot.position[1]+1)
                estimateor = robot.orientation + 1
                
            elif self.__virage == "Gauche" and self.__orientation == 3:
                estimatetr = (robot.position[0]+1,robot.position[1])
                estimateor = robot.orientation + 1
                
        estimated_state = robot.state[:]
        estimated_state[1],estimated_state[2],estimated_state[3] = estimatetr[0],estimatetr[1],estimateor
        return estimated_state
            
            
        
        
if __name__ == "__main__":
    case = Tapis((1,2),0,False)
    print(case)
    twonky = rob.Robot((1,1),1)
    print(twonky)
    case.effet(twonky)
    print(twonky)