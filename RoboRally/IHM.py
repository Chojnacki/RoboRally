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
import Jeu

class IHM(QtGui.QMainWindow):
    def __init__(self):
        print('init')
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_interface_ihm()
        self.ui.setupUi(self)
        self.plateau = Plateau.Plateau(10,9)
        self.pioche = [Cartes.Translation(1) for i in range(9)]
        self.jeu = Jeu.Jeu(self.plateau, self.pioche)
        
#        QtCore.QObject.startTimer()
        
        #Mise en place de l'arrière plan
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("images/tableau_jeu.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)

        
        #Connecte les boutons aux fonctions définies ci-dessous
#        self.ui.bouton_partie.clicked.connect(           )
        self.ui.bouton_distrib.clicked.connect(self.distrib)
        self.ui.bouton_instru.clicked.connect(self.simuler)


    def distrib(self):
#        print('distrib')
        self.jeu.prepareTour()
#        self.ui.tapiscarte.update()

    def simuler(self):
#        print('simuler')

        def step_draw():
            self.ui.centralwidget.update()
            pass
        
        self.jeu.Tour(step_draw)
        self.ui.centralwidget.update()


    #Affichage des robots sur le plateau
    def drawrobot(self, qp):
#        print('drawrobot')
        for joueur in self.jeu.listeJoueurs:
            joueur.robot.dessin(qp, self)
            
            
#        pic = QtGui.QLabel(self.ui.conteneur)
#        pixmap = QtGui.QPixmap("cigale1.png")
#        if self.ui.conteneur.width() > self.ui.conteneur.height():
#            pixmap = pixmap.scaledToHeight(self.ui.conteneur.height())
#        else:
#            pixmap = pixmap.scaledToWidth(self.ui.conteneur.width())
#        pic.setPixmap(pixmap)    
            
        
    def paintEvent(self,e):

#        print('paintEvent')
        qp = QtGui.QPainter(self)
        self.drawrobot(qp)
        
#        
#        painter = QtGui.QPainter(self)
#        painter.setPen(QtGui.QPen(QtCore.Qt.red))
#        painter.drawArc(QtCore.QRectF(250, 250, 10, 10), 0, 5760)
        
        
        qp.end()
            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = IHM()
    window.show()
    app.exec_()
