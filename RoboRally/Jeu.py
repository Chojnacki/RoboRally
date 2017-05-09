# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

#import numpy as np
import Joueur as j
import Plateau as p
import Cartes
#import Robot

class Jeu():
    
    def __init__(self,plateau = p.Plateau(), pioche = [Cartes.Carte() for i in range(9)]):
        """
        Initialise le jeu.
        1 - Recupère le plateau de jeu
        2 - Recupère les cartes de la pioche
        3 - Cree les joueurs avec la methode definie dans Joueur.py
        4 - Verifie que toutes les variables sont bien instanciees
        Paramètres
        ----------
        plateau: le plateau de jeu pour la partie
        pioche: une liste de cartes
        """
        
        self.plateau = plateau
        self.pioche = pioche
        self.step = 0
        
#        nbJoueurs = int(input("Nombre de joueurs?"))
        nbJoueurs = 1
        
        self.listeJoueurs = [j.creerJoueur(i) for i in range(nbJoueurs)]
        
        for joueur in self.listeJoueurs:
            joueur.robot.murs = self.plateau.listeMurs
            #print(joueur.robot.murs[0])
        
#        self.verification();
        
        
        
    def verification(self):
        """
        Verifie que tous les paramètres entres sont corrects sinon declenche une exception
        ----------
        Aucun paramètre
        """
        pass
    
    def prepareTour(self):
        """
        Prepare un tour pour la partie
        1 - Distribue les cartes à chaque joueur
        ----------
        """
        for joueur in self.listeJoueurs:
            joueur.distribuer(self.pioche)
            joueur.cartes = [None]*(joueur.robot.pv - 4)
        pass
    
    
    def __str__(self):
        """
        Affiche le plateau de jeu avec les robots et les murs
        Sous-traite l'essentiel du travail à la fonction imprime qui print ce qui se trouve sur une case specifiee
        """
        s = ""
        for a in range(self.plateau.y):
            for b in range(self.plateau.x):
                s += self.imprime((b,a))
            s += '\n'
        return s
    
    def imprime(self,position):
        """
        Print la case ou ce qui se trouve dessus
        ----------
        position: la position ou l'on souhaite print ce qu'il y a
        """
        for joueur in self.listeJoueurs:
            if joueur.robot.position == position:
                c = 'R'
            else:
                x,y = position
                c = self.plateau.cases[y][x].car
        return c
    
    def moveRobot(self, robot):
        mur_test = Murs.Mur(robot.position,position)
            # Mur avec lequel on compare les murs de la liste
    #        print(mur_test)
            
        if not (mur_test in self.plateau.listeMurs):
            print('move')
        
        

def main():
    
#    plateau = input("Sur quel plateau voulez vous jouer?")
#    listeCartes = input("Quelles sont les cartes disponibles?")
    
#   Pour le tableau, le robot doit commencer à la position O,1 avec une orientation de 0
#   On le fait avance d'un cran à chaque coup 
#   Choisir pour ce faire 5 fois la même case 'avancer de 1'
    jeu = Jeu(p.plateau, p.listeCartes)
    print(jeu.plateau.listeMurs[0])
    print(jeu)
    
#    print(jeu.pioche)
#    jeu.Jouer()
    
    
    
    
if __name__ == "__main__":
    main()