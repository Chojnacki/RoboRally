#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:11:06 2017

@author: Alexandre Corazza
"""
import os
import sys
from PyQt4 import QtGui, QtCore
from interface import Ui_interface_ihm
import Joueur
import Plateau
import Cartes
import Robot as rob
import Master

class IHM(QtGui.QMainWindow):
    def __init__(self):
        print('init')
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_interface_ihm()
        self.ui.setupUi(self)
        xfen = self.ui.conteneur.width()
        yfen = self.ui.conteneur.height()
        self.plateau = Plateau.Plateau(xfen,yfen)
        self.pioche = [Cartes.Translation(1) for i in range(9)]
        self.jeu = Master.Jeu(self.plateau, self.pioche)

        
        #Mise en place de l'arrière plan
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("images/tableau_jeu.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)

        
        #Connecte les boutons aux fonctions définies ci-dessous
        self.ui.bouton_partie.clicked.connect(self.nvellepartie)
        self.ui.bouton_distrib.clicked.connect(self.distrib)
        self.ui.bouton_instru.clicked.connect(self.simuler)

    def nvellepartie(self):
        nbjoueur = self.ui.nbjoueur.value()
        
        
    def distrib(self):
        self.jeu.prepareTour()
        self.ui.tapiscarte.update()

        
    def simuler(self):
        
        listeChoix = []
        # Le joueur choisit ses cartes tout en etant limite par la vie de son robot
        valeurs = self.ui.choixcarte.toPlainText()
        valeurs = valeurs.split(' ')
        #Tant qu on ne choisi pas des cartes differentes
        while not(Joueur.uniqueness(valeurs)):
            print('Cannot pick same card twice')
            valeurs = self.ui.choixcarte.toPlainText()
            valeurs = valeurs.split(' ')

        removeList = [] #liste des cartes à retirer de la pioche
        for valeur in valeurs:
            listeChoix.append(int(valeur))
            removeList.append(self.jeu.pioche[int(valeur)])

        # Une fois le choix effectue, on met les cartes choisies dans la variable joueur
        for i in range(self.jeu.listeJoueurs[0].robot.pv - 4):
            valeurs[i] = self.jeu.listeJoueurs[0].mainJoueur[listeChoix[i]]
            self.jeu.listeJoueurs[0].cartes[i] = self.jeu.listeJoueurs[0].mainJoueur[listeChoix[i]]


        self.jeu.Tour()
        self.ui.conteneur.update()



    #Affichage des robots sur le plateau
    def drawrobot(self, qp):
        for joueur in self.jeu.listeJoueurs:
            joueur.robot.dessin(qp, self)
            
        
    def paintEvent(self,e):
        qp = QtGui.QPainter(self)
        self.drawrobot(qp)
        qp.end()
            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = IHM()
    window.show()
    app.exec_()
