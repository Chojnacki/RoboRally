# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""


from Robot import Robot
from random import randint

class Joueur(Robot):
    """
    Le joueur est une liste de cartes, qui possède un numero, un robot et qui peut être une IA
    """
    number = 0
    def __init__(self,start_state):
        
        super().__init__(start_state)
        self.mainJoueur = [None] * 9             # Cartes que le joueur s'est vu distribues
        self.cartesChoisies = []
        self.cartes = [None] * 5                 # Cartes que le joueur va jouer
        self.__num = Joueur.number
        if self.numero != 0:                     # Les IA jouent avec des triskels
            self.image = 'images/triskel.png'
        Joueur.number += 1
        pass
    
    def __str__(self):
        return 'Le joueur n°{} joue le robot: {}.'.format(self.__num, self.robot)
    
    @property               #permet de protéger la variable statique number et que le joueur ait tjrs 0 pour numéro
    def numero(self):
        return self.__num
 
    def distribuer(self, pioche, show = False):
        """
        Prend une liste 'pioche' et renvoie une liste de 'nbCartes' elements pris au hasard.
        
        Paramètres
        ----------
        listeCarte: liste des cartes de la pioche
        """
        self.mainJoueur = [None] * 9
        length = len(pioche)
        # Cartes que l'on a distribuees au joueur de façon aleatoire:
        for i in range(9):
            self.mainJoueur[i] = pioche[randint(0,length-1)]
        
        # On affiche sa main au joueur pour qu'il puisse faire son choix
        if show:
            for i in range(len(self.mainJoueur)):
                print(i," - ",self.mainJoueur[i])
            print('\n')


    
if __name__ == "__main__":
    joueur = Joueur((0,0),3)
    print(joueur.numero)
    joueur = Joueur((0,0),3)
    print(joueur.numero)
    
    
    
    
    
    
    
    
    