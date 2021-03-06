#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:11:06 2017

@author: Corazza
"""

import sys
from PyQt4 import QtGui, QtCore
from interface import Ui_interface_ihm
import Jeu


############### SELECTION DU PLATEAU DE JEU ###############
import plateauDemo as p #contient un plateau de jeu 'jouable'
############# ############## ############## #############

speed = 100 #vitesse de la fsm -> d'affichage du jeu

class IHM(QtGui.QMainWindow):
    def __init__(self):
        
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_interface_ihm()
        self.ui.setupUi(self)
        self.jeu = Jeu.Jeu(p.plateau, p.listeCartes, p.nombreJoueurs) #
        self.timer = QtCore.QTimer()
        
        #Mise en place de l'arrière plan
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("images/background.jpg")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)
        
        ######################################################################
        #partie liée à la fsm qui DOIT se trouver dans init

        #liste des états admissibles:
        self.states = ["pick","play","endGame"]
        
        #état dans lequel se situe la fsm au début
        self.current_state = "pick"
        
        #transition à effectuer au prochain appel de 'fsm' (valeur au démarrage)
        self.transition = "pick"
        
        #dictionnaire des transitions
        self.dict_tr = {
                        ("pick","play"):"play",
                        ("pick","pick"):"pick",
                        ("play","play"):"play",
                        ("play","pick"):"pick",
                        ("play","endGame"):"endGame",
                        ("endGame","endGame"):"endGame",
                        }
        
        #dictionnaire des actions à effectuer lors de la transition
        self.dict_ac = {
                        "play": self.play,
                        }
        
        #On lie le timeout à la fsm
        self.timer.start(speed)
        self.timer.timeout.connect(self.fsm)
        ######################################################################
        

        #Connecte les boutons aux fonctions définies en dessous

#        self.ui.bouton_partie.clicked.connect(self.restart)
        self.ui.bouton_instru.clicked.connect(self.chooseCard)
        self.ui.checkBox_1.stateChanged.connect(self.checkBox1)
        self.ui.checkBox_2.stateChanged.connect(self.checkBox2)
        self.ui.checkBox_3.stateChanged.connect(self.checkBox3)
        self.ui.checkBox_4.stateChanged.connect(self.checkBox4)
        self.ui.checkBox_5.stateChanged.connect(self.checkBox5)
        self.ui.checkBox_6.stateChanged.connect(self.checkBox6)
        self.ui.checkBox_7.stateChanged.connect(self.checkBox7)
        self.ui.checkBox_8.stateChanged.connect(self.checkBox8)
        self.ui.checkBox_9.stateChanged.connect(self.checkBox9)
        

        #Une fois que tout est pret on lance la partie
        self.jeu.plateau.prepare()
        self.jeu.prepareTour()

##############################################      FSM - FSM - FSM       ######################################################
        
        #Partie liée à la fsm
        #la fsm sert à faire l'affichage correctement, étape par étape.Elle permet également de suivre les différentes étapes de jeu



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
                    print('\n')
                    print("{} -> {}".format(self.current_state,new_state))
                    print('\n')
                action = self.dict_ac.get(self.transition,(lambda *args: None))
                action()
                self.current_state = new_state
#                self.transition = None
        except KeyError as erreur:
            print ("transition ou état non définit dans le dictionnaire concerné", erreur)

        self.affichage()


################################################################################################################################
    
    def checkBox1(self):
        checker = self.ui.checkBox_1
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(1)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(1))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox2(self):
        checker = self.ui.checkBox_2
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(2)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(2))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox3(self):
        checker = self.ui.checkBox_3
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(3)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(3))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox4(self):
        checker = self.ui.checkBox_4
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(4)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(4))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox5(self):
        checker = self.ui.checkBox_5
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(5)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(5))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox6(self):
        checker = self.ui.checkBox_6
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(6)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(6))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox7(self):
        checker = self.ui.checkBox_7
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(7)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(7))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox8(self):
        checker = self.ui.checkBox_8
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(8)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(8))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)

    def checkBox9(self):
        checker = self.ui.checkBox_9
        if checker.isChecked():
            self.jeu.listeJoueurs[0].cartesChoisies.append(9)
        else:
            self.jeu.listeJoueurs[0].cartesChoisies.pop(self.jeu.listeJoueurs[0].cartesChoisies.index(9))
        self.ui.choixcarte.setText("{}".format(self.jeu.listeJoueurs[0].cartesChoisies))
#        print(self.jeu.listeJoueurs[0].cartesChoisies)


    # Permet de lancer le choix des cartes et d'ignorer le bouton si l'on est pas dans la phase de pick      
    def chooseCard(self):
        
        if self.current_state == "pick":
            self.jeu.playerPick()
            if self.jeu.hasPicked:
                self.jeu.aiPick()
                self.transition = "play"
            else:
                self.transition = "pick"
        else:
            pass


    def play(self):
        """
        Lance une séquence de jeu
        """
        
        victoire = self.jeu.jouerTour() #par défaut victoire = None, victoire = 'Victoire' si qqn à gagné
        if victoire:
            print('\n ################ Victoire ############### \n')
            self.transition = "endGame"
        else:
            finSequence = self.jeu.finSequence
    
            if finSequence:     #Si la sequence de jeu est finie, on en lance une nouvelle
                
                self.jeu.prepareTour()
                self.transition = "pick"
            else:            #Si la séquence n'est pas finie, on continue de jouer en lancant un autre tour
                self.transition = "play" 
    
            self.ui.progress_pv.setValue(self.jeu.listeJoueurs[0].pv) #On met à jour les pv du joueur


    def affichage(self):
        """
        fonction élémentaire pour lancer toutes fonctions servant à 'refresh' l'affichage du jeu
        """
        self.ui.centralwidget.update()


    #Affichage des robots dans l'ihm
    def drawrobot(self, qp):
        for joueur in self.jeu.listeJoueurs:
            joueur.dessin(qp)
            
    #Affichage des cases et murs dans l'ihm
    def drawboard(self, qp):
        for rangee in self.jeu.plateau.cases:
            for case in rangee:
                case.dessin(qp, case.image)
        for mur in self.jeu.plateau.listeMurs:
            mur.dessin(qp)

    #Affichage des cartes du joueur dans l'ihm
    def drawcards(self, qp):
        c=0
        y=[0,0,0,1,1,1,2,2,2]
        for carte in self.jeu.listeJoueurs[0].mainJoueur:
            if carte:
                carte.dessin(qp, carte.image, c%3, y[c])
                c+=1

    #La fonction qui actualise l'affichage, appelée à chaque timeout de qtimer (intervalle de temps = speed)
    def paintEvent(self,e):
        qp = QtGui.QPainter(self)
        self.drawboard(qp)
        self.drawrobot(qp)
        self.drawcards(qp)
        qp.end()

#les paramètres de lancement
def start():
    app = QtGui.QApplication(sys.argv)
    window = IHM()
    window.setGeometry(100,50,1300,900)
    window.show()
    app.exec_()
    

if __name__ == "__main__":
    start()
