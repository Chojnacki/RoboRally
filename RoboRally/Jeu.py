# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import AI as ai
import Joueur as j
import Plateau as p
import Cartes
import Murs

#import Robot

class Jeu():
    
    def __init__(self,plateau = p.Plateau(), pioche = [Cartes.Carte() for i in range(9)], nbJoueurs = 1):
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
        self.__finSequence = False
        self.__hasPicked = False   #est-ce que l'humain a pioché correctement?
        
#        nbJoueurs = int(input("Nombre de joueurs?"))
        self.nbJoueurs = nbJoueurs
        
        self.listeJoueurs = [j.creerJoueur(i) for i in range(nbJoueurs)]
        
        for joueur in self.listeJoueurs:
            joueur.murs = self.plateau.listeMurs
            #print(joueur.robot.murs[0])
        
#        self.verification();
        
    @property
    def finSequence(self):
        return self.__finSequence
        
    @property
    def hasPicked(self):
        return self.__hasPicked
        
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
            joueur.cartes = [None]*5
        pass
    
    def playerPick(self):
        self.__hasPicked = True
    
        listeChoix = [] #les cartes que le joueur choisit sur l'ihm
        
        valeurs = self.listeJoueurs[0].cartesChoisies
        valeurs = [int(valeurs[i])-1 for i in range(len(valeurs))] #On décale de 1 parce que Python
        for carte in valeurs:
            if int(carte) > 8 or int(carte) < 0:            #vérification que les indices sont entre 0 et 8
                self.__hasPicked = False
                print('valeurs')
        if not(uniqueness(valeurs)):                         #2 cartes identiques
            self.__hasPicked = False
            print('unique')
        if len(valeurs) != max(0,self.listeJoueurs[0].pv - 4):     #Nombre de cartes incorrect
            if valeurs:
                self.__hasPicked = False
                print('last')
                
        
        if self.hasPicked and valeurs: #si le joueur a joué et qu'il a choisit des cartes
#            removeList = [] #liste des cartes à retirer de la pioche
            for valeur in valeurs:
                listeChoix.append(int(valeur))
#                removeList.append(self.pioche[int(valeur)])
        
                # Une fois le choix effectue, on met les cartes choisies dans la variable joueur
            for i in range(self.listeJoueurs[0].pv - 4):
#                valeurs[i] = self.listeJoueurs[0].mainJoueur[listeChoix[i]]
                self.listeJoueurs[0].cartes[i] = self.listeJoueurs[0].mainJoueur[listeChoix[i]]
        elif not(valeurs): #si il n'a pas choisit de cartes:
#            valeurs[i] = self.listeJoueurs[0].mainJoueur[listeChoix[i]]
            self.listeJoueurs[0].cartes = []
        else:
            print("Veuillez choisir {} cartes distinctes entre 1 et 9".format(max(0,self.listeJoueurs[0].pv - 4)) )
            self.__hasPicked = False
            

        pass
    
    def aiPick(self):
        ai.pick(self)
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

    def jouerTour(self):
        """
        Lance un tour (tout le monde joue une carte)
        Si la séquence de jeu est finie: ne fait rien
        """

        self.__finSequence = True
        for joueur in self.listeJoueurs:
            if joueur.cartes:                   #Si un joueur à encore des cartes
                self.__finSequence = False      #La séquence n'est pas finie, on lance le tour
        
        if self.finSequence:
            pass
        else:
            for joueur in self.listeJoueurs:
                print('chacun son tour, priorités à régler')
                # On applique l'effet de la carte:
                carte = None #Au cas ou le joueur décide de ne rien choisir comme carte
                if joueur.cartes:
                    carte = joueur.cartes.pop(0)
                if carte:
                    print('état du joueur',joueur.state)
                    estimated_state = carte.effet(joueur)
                    print('estimation Carte',estimated_state)
                    real_state = realState(joueur.state,estimated_state,self)
                    print('réel carte',real_state)
#                    joueur.set_state(real_state)
    
#                    try:
                    real_state = self.plateau.mc(real_state)
                    joueur.set_state(real_state)

                    #condition de victoire:
                    if joueur.position in self.plateau.casesVictoire:
                        return 'Victoire'
                    
            print(self.listeJoueurs[1].state)
        
    def simpleAction(self,joueur):
        """
        Lance une action: Le joueur concerné joue 1 carte
        """
        pass

class Victoire(Exception):
    pass

#les deux fonctions qui suivent sont la pour prendre en compte les murs et différents obstacles que peut recontrer le robot
#et pour lui donner l'état dans lequel il sera après avoir fait la commande que l'on lui donne
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

#Fonction pour déterminer si une liste est composée d'éléments uniques
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
        

def main():
    
#    plateau = input("Sur quel plateau voulez vous jouer?")
#    listeCartes = input("Quelles sont les cartes disponibles?")
    
#   Pour le tableau, le robot doit commencer à la position O,1 avec une orientation de 0
#   On le fait avance d'un cran à chaque coup 
#   Choisir pour ce faire 5 fois la même case 'avancer de 1'
#    jeu = Jeu(p.plateau, p.listeCartes)
#    print(jeu.plateau.listeMurs[0])
#    print(jeu)
#    
#    print(jeu.pioche)
#    jeu.Jouer()
    
    pass
    
    
    
    
if __name__ == "__main__":
    main()