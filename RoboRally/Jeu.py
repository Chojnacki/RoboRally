# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

#import numpy as np
import Joueur as j
import Plateau as p
import Cartes
#import Robot as r


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
    
    def Tour(self, fonction = lambda *args: None):
        """
        Lance un tour de la partie, personne ne peut intervenir pendant l'execution de cette fonction
        Paramètres
        ----------
        plateau: le plateau de jeu pour la partie
        pioche: une liste de cartes
        """
        for compteur in range(5):
            for joueur in self.listeJoueurs:
                carte = joueur.cartes[compteur]
                carte.effet(joueur.robot)
                fonction()
            
            for row in self.plateau.cases:
                for case in row:
                    for joueur in self.listeJoueurs:
                        if case.position == joueur.robot.position:
                            case.effet(joueur.robot)
                            fonction()
            print(self)
          
        pass
    
    def Tour2(self):
        """
        permet de lancer le tour carte par carte et action par action
        cela devrait permettre d'afficher le jeu en dynamique depuis IHM.py
        """
        if self.step == 9:
            self.step = 0
#            print('fin')
#            return False
        
        if self.step % 2 == 0:
            for joueur in self.listeJoueurs:
                carte = joueur.cartes[self.step % 2]
                carte.effet(joueur.robot)
                self.step += 1
#            return True
                  
        if self.step % 2 == 1:
            for row in self.plateau.cases:
                for case in row:
                    for joueur in self.listeJoueurs:
                        if case.position == joueur.robot.position:
                            case.effet(joueur.robot)
            self.step += 1
#            return True
            
    
    def Jouer(self):
        """
        Lance le jeu et le fait tourner jusqu'à ce qu'il y ait un vainqueur
        """
        try:
            Vainqueur = False
            while not(Vainqueur):
                self.prepareTour()
                self.Tour()
        except Exception as v:
            Vainqueur = True
            print(self)
            print(v)
            
    
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
    jeu.Jouer()
    
    
    
    
if __name__ == "__main__":
    main()