#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:58:02 2017

@author: Corazza
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
    @property
    def x(self):
        return self.__pos[0]
    @property
    def y(self):
        return self.__pos[1]

    @property    
    def MD(self):
        """
        Représentation de la case dans l'espace des Matrices-D
        """
        return (0,self.x,self.y,0) #Par défaut une case ne fait rien
       
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
    def copy(self, x=None,y=None,tourne=None, sym=None):
        """
        Applique l'effet de la case sur le robot suivant le type de la case
        
        Paramètres
        ----------
        x,y position de la nouvelle case
        tourne: fait tourner la case
        sym: pour changer la direction des tapis d'angle
        """
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return Case((x,y))
    
    
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
        
    def copy(self, x=None,y=None,tourne=None, sym=None):
        
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return Case((x,y))


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
        pass
    
    def copy(self, x=None,y=None,tourne=None,sym=None):
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return CaseArrivee((x,y))
        
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
        
    @property    
    def MD(self):
        """
        Représentation de la case dans l'espace des Matrices-D
        """
        return (9,self.x,self.y,0) #inflige 9 dégats
    
        
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
        
        
    def copy(self, x=None,y=None,tourne=None,sym=None):
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return CaseTrou((x,y))
        
        
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
        
    @property    
    def MD(self):
        """
        Représentation de la case dans l'espace des Matrices-D
        """
        return (-1,self.x,self.y,0) #inflige -1 dégats
    
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
    
    def copy(self, x=None,y=None,tourne=None,sym=None):
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return CaseReparation((x,y))
        
        
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
    def sens(self):
        return self.__sens
        
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


    @property
    def MD(self):
        """
        Représentation de la case dans l'espace des Matrices-D
        
        Fait pivoter le robot d'un quart de tour selon le sens de l'engrenage.
        
        Paramètres
        ----------
        robot: Robot
            Le robot qui se trouve sur la case tourne sur lui même.
        """
        return (0,self.x,self.y, self.sens)
        
        
    def copy(self, x=None,y=None, tourne=None,sym=1):
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]
            
        return CaseEngrenage((x,y), self.sens*sym)
    
#dictionnaires utiles pour la fonction copy
dico_virage = {0: "Gauche", 1: "Droite"}
dico_inv_virage = {"Gauche": 0, "Droite":1}
    
class Tapis(Case):
    def __init__(self,position,orientation,virage = False, vitesse = 1):
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
        if vitesse != 1:
            raise Exception('vitesse de tapis non prévue')
        super().__init__(position)
        self.__orientation = orientation
        self.__virage = virage
        self.__vitesse = vitesse
        self.image = 'images/tapis{}{}{}.png'.format(self.__orientation, self.__virage, self.__vitesse)
        
    @property
    def vitesse(self):
        return self.__vitesse
    
    @property
    def orientation(self):
        return self.__orientation
    
    @property
    def virage(self):
        return self.__virage

        
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
        
    @property    
    def MD(self):
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
        
        #Modifie l'etat du robot (degat, +x, +y, orientation)
        for i in range(self.__vitesse):
            if self.__virage == False and self.__orientation == 0:
                return (0,self.x+1,self.y,0)
            elif self.__virage == False and self.__orientation == 1:
                return (0,self.x,self.y-1,0)
            elif self.__virage == False and self.__orientation == 2:
                return (0,self.x-1,self.y,0)
            elif self.__virage == False and self.__orientation == 3:
                return (0,self.x,self.y+1,0)
    
            
                
            if self.__virage == "Droite" and self.__orientation == 0:
                return (0,self.x,self.y+1,-1)
            elif self.__virage == "Droite" and self.__orientation == 1:
                return (0,self.x+1,self.y,-1)
            elif self.__virage == "Droite" and self.__orientation == 2:
                return (0,self.x-1,self.y,-1)
            elif self.__virage == "Droite" and self.__orientation == 3:
                return (0,self.x-1,self.y,-1)
                
                
                
            if self.__virage == "Gauche" and self.__orientation == 0:
                return (0,self.x,self.y-1,1)
            elif self.__virage == "Gauche" and self.__orientation == 1:
                return (0,self.x-1,self.y,1)
            elif self.__virage == "Gauche" and self.__orientation == 2:
                return (0,self.x,self.y+1,1)
            elif self.__virage == "Gauche" and self.__orientation == 3:
                return (0,self.x+1,self.y,1)
                
            
            
        
    def copy(self, x=None,y=None,tourne=0,sym=1):
        """
        tourne = 0 ou 2 (2 pour symetrie)
        sym = 0 ou 1 selon le cadre de symetrie
        """
        if not x:
            x = self.position[0]
        if not y:
            y = self.position[1]    
            
        if self.__virage == False:
                return Tapis((x,y), (self.orientation + tourne)%4, False, self.vitesse)
            
        else:
                return Tapis((x,y), (self.orientation + tourne)%4, dico_virage[(dico_inv_virage[self.virage]+sym)%2], self.vitesse)
            
        
if __name__ == "__main__":
    case = Tapis((1,2),0,False)
    print(case.MD)
    print(isinstance(case,Tapis))
    print(case)
    twonky = rob.Robot((1,1),1)
    print(twonky)
    case.effet(twonky)
    print(twonky)