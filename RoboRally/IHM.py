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
#import Joueur
#import Plateau
#import Cartes
#import Robot as rob
import Jeu
import time
import plateau1 #contient un plateau de jeu 'jouable'

class IHM(QtGui.QMainWindow):
    def __init__(self):
        print('init')
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_interface_ihm()
        self.ui.setupUi(self)
        self.plateau = plateau1.plateau
        self.pioche = plateau1.listeCartes
        self.jeu = Jeu.Jeu(self.plateau, self.pioche)
        self.timer = QtCore.QTimer()
        
        
        #Mise en place de l'arrière plan
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("images/tableau_jeu.png")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)


        ######################################################################
        #partie liée à la fsm qui DOIT se trouver dans init

        #liste des états admissibles:
        self.states = ["initialize","pick","play"]
        
        #état dans lequel se situe la fsm
        self.current_state = "initialize"
        
        #transition à effectuer au prochain appel de 'fsm': fonction et nouvel état
        self.transition = None
        
        #dictionnaire des transitions
        self.dict_tr = {
                        ("initialize",None):"initialize",("pick","play"):"play",
                        ("initialize","pick"):"pick",("pick","pick"):"pick",("play","play"):"play",
                        ("play","pick"):"pick"
                        }
        
        #dictionnaire des actions à effectuer lors de la transition
        self.dict_ac = {
                        None: (lambda *args: None), "play": self.play,
                        "pick":(lambda *args: None)                        
                        }
        
        #On lie le timeout à la fsm
        self.timer.start(500)
        self.timer.timeout.connect(self.fsm)
        ######################################################################
        

        #Connecte les boutons aux fonctions définies en dessous

        self.ui.bouton_partie.clicked.connect(self.nvellepartie)
        self.ui.bouton_distrib.clicked.connect(self.distrib)
        self.ui.bouton_instru.clicked.connect(self.chooseCard)



##############################################      FSM - FSM - FSM       ######################################################
        
        #Partie liée à la fsm
        #la fsm sert à faire l'affichage correctement, étape par étape: pratique puisque l'on doit pouvoir revenir en arrière



    def fsm(self):
        """
        fonction appelée à chaque timeout pour l'affichage du jeu
        il s'agit d'une 'finite state machine', qui change l'état en fonction de la transition et affiche ensuite le nouvel état
        la transition est gérée par les boutons de l'ihm
        Paramètres
        ----------
        aucun, à rajouter si l'on a besoin de réinitialiser la fsm pour X raison
        """
    
        try:
            new_state = self.dict_tr[(self.current_state,self.transition)]
            if new_state in self.states:
                if new_state != self.current_state:
                    print("{} -> {}".format(self.current_state,new_state))
                self.dict_ac[self.transition]()
                self.current_state = new_state
#                self.transition = None
        except KeyError as erreur:
            print ("transition ou état non définit dans le dictionnaire respectif", erreur)
        except Exception as VouD: #Victoire ou Défaite
            print ("C'est la {} Mamène".format(VouD))
            exit()
        
#        time.sleep(1) #juste pour débugger tranquillement
        self.affichage()


################################################################################################################################




    def nvellepartie(self):
        """Cette fonction n'est pas encore prête"""
        nbjoueur = self.ui.nbjoueur.value()
#        print(nbjoueur)
        
        
    def distrib(self):
        self.jeu.prepareTour()
        self.transition = "pick"
#        self.ui.tapiscarte.update()
        
    def chooseCard(self):
        listeChoix = []
        # Le joueur choisit ses cartes tout en etant limite par la vie de son robot
        valeurs = self.ui.choixcarte.toPlainText()
        valeurs = valeurs.split(' ')
        print(len(valeurs),self.jeu.listeJoueurs[0].robot.pv - 4)
        #Tant qu on ne choisi pas des cartes differentes
        if not(uniqueness(valeurs)) or (len(valeurs) != self.jeu.listeJoueurs[0].robot.pv - 4):
            print("Veuillez choisir {} cartes distinctes".format(self.jeu.listeJoueurs[0].robot.pv - 4) )
#            valeurs = self.ui.choixcarte.toPlainText()
#            valeurs = valeurs.split(' ')

        else:
            removeList = [] #liste des cartes à retirer de la pioche
            for valeur in valeurs:
                listeChoix.append(int(valeur))
                removeList.append(self.jeu.pioche[int(valeur)])
    
            # Une fois le choix effectue, on met les cartes choisies dans la variable joueur
            for i in range(self.jeu.listeJoueurs[0].robot.pv - 4):
                valeurs[i] = self.jeu.listeJoueurs[0].mainJoueur[listeChoix[i]]
                self.jeu.listeJoueurs[0].cartes[i] = self.jeu.listeJoueurs[0].mainJoueur[listeChoix[i]]
            
            self.transition = "play"

    def play(self):
        """
        Lance un tour
        """
        #penser a coder une liste qui retient les joueurs ayant déjà joué
        #penser à coder la priorité pour les cartes les plus rapides
        
        fin_tour = True
        for joueur in self.jeu.listeJoueurs:
#            print(joueur.cartes)
            if joueur.cartes:
                fin_tour = False
        
        if fin_tour:
            self.distrib()              #Si le tour est fini on redistribue
        
        else:
            for joueur in self.jeu.listeJoueurs:
                # On applique l'effet de la carte:
                carte = joueur.cartes.pop(0)
                carte.effet(joueur.robot)
                # On applique l'effet de la case:
                for row in self.plateau.cases:
                    for case in row:
                        if case.position == joueur.robot.position:
                            case.effet(joueur.robot)
                
            
            self.transition = "play"                    #Si le tour n'est pas fini, on continue de jouer
        

    def affichage(self):
        """
        fonction élémentaire pour lancer toutes fonctions servant à 'refresh' l'affichage du jeu
        """
        self.ui.centralwidget.update()


    #Affichage des robots sur le plateau
    def drawrobot(self, qp):
        for joueur in self.jeu.listeJoueurs:
            joueur.robot.dessin(qp, self)
            
        
    def paintEvent(self,e):
        qp = QtGui.QPainter(self)
        self.drawrobot(qp)
        qp.end()
     

def uniqueness(l):
    """
    Renvoie true si les éléments de la liste l sont uniques, false sinon
    ----------
    l: liste a vérifier (index dans la pioche des cartes choisies)
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return False
    return True
       

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = IHM()
    window.show()
    app.exec_()
