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
import plateau0 as p #contient un plateau de jeu 'jouable'


speed = 100 #vitesse de la fsm -> du jeu

class IHM(QtGui.QMainWindow):
    def __init__(self):
        
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_interface_ihm()
        self.ui.setupUi(self)
        self.plateau = p.plateau
        self.pioche = p.listeCartes
        self.jeu = Jeu.Jeu(self.plateau, self.pioche, 2)
        self.timer = QtCore.QTimer()
        
        #Mise en place de l'arrière plan
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("images/background.jpg")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette)
        
        ######################################################################
        #partie liée à la fsm qui DOIT se trouver dans init

        #liste des états admissibles:
        self.states = ["initialize","pick","play","endGame"]
        
        #état dans lequel se situe la fsm
        self.current_state = "initialize"
        
        #transition à effectuer au prochain appel de 'fsm': fonction et nouvel état
        self.transition = None
        
        #dictionnaire des transitions
        self.dict_tr = {
                        ("initialize",None):"initialize",
                        ("initialize","pick"):"pick",
                        ("pick","play"):"play",
                        ("pick","pick"):"pick",
                        ("play","play"):"play",
                        ("play","pick"):"pick",
                        ("play","endGame"):"endGame",
                        ("endGame","endGame"):"endGame",
                        }
        
        #dictionnaire des actions à effectuer lors de la transition
        self.dict_ac = {
#                        None: (lambda *args: None),
                        "play": self.play,
#                        "pick": (lambda *args: None),
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
        
        
        self.nvllePartie() #Une fois que tout est pret on lance la partie

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
                    print('\n')
                    print("{} -> {}".format(self.current_state,new_state))
                    print('\n')
                action = self.dict_ac.get(self.transition,(lambda *args: None))
                action()
                self.current_state = new_state
#                self.transition = None
        except KeyError as erreur:
            print ("transition ou état non définit dans le dictionnaire respectif", erreur)
#        except Exception as VouD: #Victoire ou Défaite
#            print ("C'est la {} Mamène".format(VouD))
#            exit()
        
#        time.sleep(1) #juste pour débugger tranquillement
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


    def nvllePartie(self):
        self.jeu.plateau.prepare()
#        print(self.jeu.plateau.mc)
        self.jeu.prepareTour()
        self.transition = "pick"
#        self.ui.tapiscarte.update()
        pass
        
    
        
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
        #penser a coder une liste qui retient les joueurs ayant déjà joué
        #penser à coder la priorité pour les cartes les plus rapides
        
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


    
    def FaireAffichage(self):
        """
        Fonction qui affiche les cartes et les pv du joueur
        """
        self.faireAffichageDesCartes = True

    def affichage(self):
        """
        fonction élémentaire pour lancer toutes fonctions servant à 'refresh' l'affichage du jeu
        """
        self.ui.centralwidget.update()


    #Affichage des robots sur le plateau
    def drawrobot(self, qp):
        for joueur in self.jeu.listeJoueurs:
            joueur.dessin(qp)
            
    def drawboard(self, qp):
        for rangee in self.jeu.plateau.cases:
            for case in rangee:
                case.dessin(qp, case.image)
        for mur in self.jeu.plateau.listeMurs:
            mur.dessin(qp)

    def drawcards(self, qp):
        c=0
        y=[0,0,0,1,1,1,2,2,2]
        for carte in self.jeu.listeJoueurs[0].mainJoueur:
            if carte:
                carte.dessin(qp, carte.image, c%3, y[c])
                c+=1

    def paintEvent(self,e):
        qp = QtGui.QPainter(self)
        self.drawboard(qp)
        self.drawrobot(qp)
        self.drawcards(qp)
        qp.end()

def realState(state1,state2,jeu):
    """
    renvoie l'état réel en tenant compte des murs et autres obstacles
    ----------
    state1: état de départ
    state2: état prévu par les cartes / cases en ignorant les conditions externes
    jeu: le jeu, contient toutes les variables nécessaires à la création de realState
    """
    listeMurs = jeu.plateau.listeMurs
    real_state = state2
    for mur in listeMurs:
        real_state = correctedStateMur(state1,real_state,mur)
    
    return real_state

    
def correctedStateMur (state1,state2,mur):
    """
    renvoie l'état corrigé, en prenant en compte le mur passé en argument
    ----------
    state1: état de départ
    state2: état prévu par les cartes / cases en ignorant les conditions externes
    mur: le mur considéré
    """
    a, b = state1[1], state1[2]
    correctedState = state2[:]
#    print(state1,state2)

    #en fonction de la direction du robot un des deux blocs ne sera pas executé: 'in range' est vide    
    
    #si le robot va de gauche à droite ou de haut en bas
    for x in range(state1[1],state2[1]+1,1):
        for y in range(state1[2],state2[2]+1,1):
#            print('gauche,droite',a,b,x,y) #pour vérifier quel mur est testé et dans quelle direction
            if mur.v1 == (a,b) and mur.v2 == (x,y):
                correctedState[1],correctedState[2] = a,b
                break
            #si on peut avancer d'une case, le problème se ré-itère au cran suivant:
            a,b = x,y
    
    #si le robot va de droite à gauche ou de bas en haut
    for x in range(state1[1],state2[1]-1,-1):
        for y in range(state1[2],state2[2]-1,-1):
#            print('droite,gauche',x,y,a,b)
            if mur.v1 == (x,y) and mur.v2 == (a,b):
                correctedState[1],correctedState[2] = a,b
                break
            a,b = x,y
    return correctedState
    
    
class Victoire(Exception):
    pass

def start():
    app = QtGui.QApplication(sys.argv)
    window = IHM()
#    window.nvllePartie()
    window.setGeometry(100,50,1300,900)
    window.show()
    app.exec_()
    

if __name__ == "__main__":
    start()
