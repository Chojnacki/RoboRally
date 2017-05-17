# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:46:17 2017

@author: Chojnacki
"""

import IA as ia
import Joueur as j
import Plateau as p

class Jeu():
    
    def __init__(self,plateau = p.Plateau(), pioche = [None for i in range(9)], nbJoueurs = 1):
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
        
        try:
            self.listeJoueurs = [j.Joueur(self.plateau.listeEtatsDepart[i]) for i in range(nbJoueurs)]
        except IndexError:
            print('les positions de départ ne sont pas définies')
        
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
#                print('valeurs')
        if not(uniqueness(valeurs)):                         #2 cartes identiques
            self.__hasPicked = False
#            print('unique')
        if len(valeurs) != max(0,self.listeJoueurs[0].pv - 4):     #Nombre de cartes incorrect
            if valeurs:
                self.__hasPicked = False
#                print('last')
                
        
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
        ia.pick(self)
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
            #On détermine l'ordre de jeu:
            ordre = []
            for index,joueur in enumerate(self.listeJoueurs):
                carte = None #Au cas ou le joueur décide de ne rien choisir comme carte
                if joueur.cartes:
                    carte = joueur.cartes[0] #non destructif
                if carte:
                    vitesse = abs(carte.vitesse)
                    ordre.append((joueur,vitesse))
                
            tri_bulle(ordre)

            #on remplace la vitesse par la carte pour ensuite lancer les actions
            for joueur,v in ordre:
                carte = None
                if joueur.cartes:
                    carte = joueur.cartes.pop(0) #destructif
                if not carte: #si le joueur ne joue pas on le retire de la liste
                    ordre.remove((joueur,v))
                else:
                    ordre[ordre.index((joueur,v))] = (joueur,carte)

                
            # On lance enfin les actions, dans le bon ordre
            # On note que le joueur 0 à la priorité sur le 1 etc...
            for joueur,carte in ordre:
                print("le joueur {} joue la carte {}".format(joueur.numero,carte))
                victoire = self.simpleAction(joueur,carte) # permet de jouer une carte et de stopper si le joueur gagne
                print(carte, " | ", joueur.state)
                if victoire:
                    return victoire
            print('\n')
#            print(self.listeJoueurs[1].state)
        
        
        
    def simpleAction(self,joueur,carte):
        """
        Lance une action: Le joueur concerné joue 1 carte
        """
        
        estimated_state = carte.effet(joueur)
        estimated_state = realState(joueur.state,estimated_state,self)

        
        #gestion des obstacles avec le déplacement du à la carte joué
            
        real_state_carte = self.forceMove(joueur,joueur.state,estimated_state) #état réél après l'effet de la carte
#        print(real_state_carte)

        
        estimated_state = self.plateau.mc(real_state_carte)
        #gestion des obstacles avec le déplacement du à la carte joué
        
        real_state = self.forceMove(joueur,joueur.state,estimated_state) #l'état final après le tour du joueur
#        joueur.set_state(real_state)


#        print(self.listeJoueurs[0])


        #condition de victoire:
        if joueur.position in self.plateau.casesVictoire:
            return 'Victoire'
        pass

    def obstacle(self,joueur,pos1,pos2):
        """
        Détecte si un robot empêche le déplacement du joueur
        renvoie False si il n'y a pas d'obstacle
        renvoie le joueur qui gène et le point ou l'on doit le pousser et la direction de poussée si le cas se présente
        """
        positions,orientation = transitionPositions(pos1,pos2)
        
        for player in self.listeJoueurs:
            if player.position in positions[:-1] and player != joueur: #on ignore la dernière case, la on l'on pousse le joueur adverse
                return player,positions[-1],orientation #la dernière position est celle ou l'on pousse l'autre joueur
#        print("il n'ya a pas dobstacle au joueur:", joueur.numero)
        return False
        
        
    def forceMove(self,joueur,state1,state2):
#        if joueur.numero == 1:
#            print(joueur,state1,state2)
        """
        Déplace le robot du joueur de l'état vers l'état 2 en poussant les joueurs qui gênent le passage
        si le déplacement n'est pas possible, bloque le joueur à sa position (initiale ou intermédiaire)
        cette fonction est récursive pour pousser tous les joueurs
        """
        pos1 = state1[1],state1[2]
        pos2 = state2[1],state2[2]        
        obstacle = self.obstacle(joueur,pos1,pos2)
        if not obstacle:
            o = getDirection(state1,state2)
            d = getDistance(state1,state2)
            dic = {0:self.plateau.m0,1:self.plateau.m1,2:self.plateau.m2,3:self.plateau.m3}
            m = dic[o]
#            print(o,m)
            resultingState = state1[0],state1[1],state1[2],state2[3]      # variable contenant le résultat à l'issue de la manoeuvre
#            resultingState[3] = state2[3] # si on fait une rotation, il faut le prendre en compte
#            print('before',joueur.numero,resultingState,"distance",d)
            for i in range(d):
                resultingState = m(resultingState)
                resultingState = [resultingState[0],resultingState[1],resultingState[2],resultingState[3]]
            joueur.set_state(resultingState)
#            print('after',joueur.numero,resultingState,joueur.state)
            return resultingState
        else:
            player, pos, o = obstacle
#            print(pos,o)
            shovedState = (player.state[0],pos[0],pos[1],player.state[3]) #l'état dans lequel le player doit se retrouver
            shovedState = self.forceMove(player,player.state,shovedState) #l'état dans lequel il est au final

            if o == 0: #si on poussait vers la droite:
                new_state = (joueur.state[0],shovedState[1]-1,shovedState[2],joueur.state[3]) #le joueur s'arrete une case avant son adversaire
            if o == 1: #vers le haut:
                new_state = (joueur.state[0],shovedState[1],shovedState[2]+1,joueur.state[3]) #le joueur s'arrete une case avant son adversaire
            if o == 2: #si on poussait vers la gauche:
                new_state = (joueur.state[0],shovedState[1]+1,shovedState[2],joueur.state[3]) #le joueur s'arrete une case avant son adversaire
            if o == 3: #si on poussait vers le bas:
                new_state = (joueur.state[0],shovedState[1],shovedState[2]-1,joueur.state[3]) #le joueur s'arrete une case avant son adversaire
            joueur.set_state(new_state)
#            print('fin')
            return new_state
            



def transitionPositions(pos1,pos2):
    """
    renvoie la liste des positions intermédiaires en allant de l'état 1 vers l'état 2
        -> on veut savoir on l'on envoie le robot percuté donc on calcule la case d'après dans la direction
    ignore les pvs et l'orientation: non affectés par des translations (l'effet de case s'effectue après)
    """
    if pos1 == pos2:
        return [pos1],None
    else:
        x1,y1 = pos1
        x2,y2 = pos2
        d = 1
        if x1 == x2:
            o = 3 #on pousse vers le bas
            if y1 > y2:
                d = -1 #la direction change si on va de bas en haut
                o = 1 #on pousse vers le haut
            l = [(x1,y1)] * (abs(y2-y1)+2) #la liste des états de transition
            for i in range(0,abs(y2-y1)+1):
                l[i+1] = (x1,y1+d*(i+1))
        elif y1 == y2:
            o = 0 # on pousse vers la droite
            if x1 > x2:
                d = -1 #la direction change si on va de droite à gauche
                o = 2 # on pousse vers la gauche
            l = [(x1,y1)] * (abs(x2-x1)+2) #la liste des états de transition
            for i in range(0,abs(x2-x1)+1):
                l[i+1] = (x1+d*(i+1),y1)
#        print('transition',l)
        return l,o

    

def tri_bulle(liste):
    l = len(liste)
    for i in range(l):
        for j in range(i+1,l):
            if liste[i][1] < liste[j][1]:   #on compare les vitesses des cartes et on échange si besoin
                liste[i],liste[j] = liste[j],liste[i]
    pass

def getDirection(state1,state2):
    """renvoie la direction de l'état 1 vers l'état 2"""
    x1,y1 = state1[1],state1[2]
    x2,y2 = state2[1],state2[2]
    if x1 == x2:
        o = 3 #on pousse vers le bas
        if y1 > y2:
            o = 1 #on pousse vers le haut
    elif y1 == y2:
        o = 0 # on pousse vers la droite
        if x1 > x2:
            o = 2 # on pousse vers la gauche
    return o
    
def getDistance(state1,state2):
    """renvoie la distance entre l'état 1 et l'état 2"""
    x1,y1 = state1[1],state1[2]
    x2,y2 = state2[1],state2[2]
    return abs(x2-x1) + abs(y2-y1)


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
    
    
    #test du tri à bulles
#    liste = [(1,1),(2,4),(3,6)]
#    tri_bulle(liste)
#    print(liste)
    
    
    #test des positions de transition
    liste = transitionPositions((0,0),(2,0))
    print(liste)
    liste = transitionPositions((0,0),(0,1))
    print(liste)
    liste = transitionPositions((2,0),(0,0))
    print(liste)
    liste = transitionPositions((0,1),(0,2))
    print(liste)
    liste = transitionPositions((0,0),(0,0))
    print('immobilité',liste)
#    print(liste[:-1])
    
    #test de getDirection
    o = getDirection((9,0,0,0),(9,2,0,0))
    print(o)
    o = getDirection((9,0,0,0),(9,0,2,0))
    print(o)
    o = getDirection((9,1,0,0),(9,0,0,0))
    print(o)
    o = getDirection((9,0,1,0),(9,0,0,0))
    print(o)
    
    
    
    pass
    
    
    
    
if __name__ == "__main__":
    main()