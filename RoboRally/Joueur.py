# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""


from Cases import *
from Cartes import *
import Robot as rob
from random import randint

class Joueur():
    """
    Le joueur est une liste de cartes, qui possède un numero, un robot et qui peut être une IA
    """
    def __init__(self, numero, robot = None, AI = True):
        
        self.mainJoueur = [0 for i in range(9)]   # Cartes que le joueur s'est vu distribues
        self.cartes = [0 for i in range(5)]   # Cartes que le joueur va jouer
        self.__num = numero
        self.robot = robot
        self.__AI = AI
        pass
    
    def __str__(self):
        return 'Le joueur n°{} joue le robot: {}.'.format(self.__num, self.robot)
    
#    @property
#    def mainJoueur(self):
#        return self.mainJoueur
#    
#    @mainJoueur.setter
#    def mainJoueur(self, carte, indice):
#        """
#        Permet de mettre les cartes dans la main du joueur
#        
#        Paramètres
#        ----------
#        carte: la carte à mettre dans la liste
#        indice: position à laquelle mettre la carte
#        """
#        self.mainJoueur[indice] = carte
#        pass    
#    
#    @property
#    def cartes(self):
#        return self.mainJoueur
#    
#    @cartes.setter
#    def carte(self, carte, indice):
#        """
#        Permet de mettre une carte dans la liste de cartes actives
#        
#        Paramètres
#        ----------
#        carte: la carte à mettre dans la liste
#        indice: position à laquelle mettre la carte
#        """
#        self.cartes[indice] = carte
#        pass
    
 
    def distribuer(self, pioche):
        """
        Prend une liste 'pioche' et renvoie une liste de 'nbCartes' elements pris au hasard.
        
        Paramètres
        ----------
        listeCarte: liste des cartes de la pioche
        """

        length = len(pioche)
        # Cartes que l'on a distribuees au joueur de façon aleatoire:
        for i in range(9):
            self.mainJoueur[i] = pioche[randint(0,length-1)]
        # On affiche sa main au joueur pour qu'il puisse faire son choix
        for i in range(len(self.mainJoueur)):
            print(i," - ",self.mainJoueur[i])
        print('\n')
        
#        listeChoix = []
#        # Le joueur choisit ses cartes tout en etant limite par la vie de son robot
#        valeurs = input("Choisissez vos cartes (par numero): ")
#        valeurs = valeurs.split(' ')
#        while not(uniqueness(valeurs)):
#            print('Cannot pick same card twice')
#            valeurs = input("Choisissez vos cartes (par numero): ")
#            valeurs = valeurs.split(' ')
#
#        removeList = [] #liste des cartes à retirer de la pioche
#        for valeur in valeurs:
#            listeChoix.append(int(valeur))
#            removeList.append(pioche[int(valeur)])
#    
##        for item in removeList:
##            pioche.remove(item)
#
#        """Les deux lignes ci dessus sont commentées car la pioche ne se remplit pas à la fin de chaque tour"""
#
#        
#        # Une fois le choix effectue, on met les cartes choisies dans la variable joueur
#        for i in range(self.robot.pv - 4):
#            self.cartes[i] = self.mainJoueur[listeChoix[i]]
#
#        # Cette fonction ne renvoie rien
#        pass


def creerJoueur(numero, robot_options = (0,0,0)):
    """
    Permet d'instancier un joueur en demandant les paramètres à l'utilisateur
    robot_options permet de choisir l'orientation du robot par défaut depuis les fichiers Master / IHM
    """

    ################ automatique ##################

    x,y,o = robot_options

     ############### manuel ##################

#    valeurs = input("Entrez la position de depart du robot et son orientation.")
#    x,y,o = valeurs.split(' ')
#    x,y,o = int(x),int(y),int(o)
    
    return Joueur(numero, rob.Robot((x,y),o))



    
    
    
    
    
    
    
    
    
    
    