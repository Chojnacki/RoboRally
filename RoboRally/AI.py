# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:37:40 2017

@author: oblivioner
"""

import MatriceD as md
from random import randint

def pick(jeu):
    Puissante(jeu)
#    Brownienne(jeu)
    pass



def Brownienne(jeu):
    listeIA = jeu.listeJoueurs[1:]
    for IA in listeIA:
#        removeList = []             #liste des cartes à retirer de la pioche
        
        for i in range(len(IA.cartes)): #On remplit la liste des cartes
            IA.cartes[i] = IA.mainJoueur[randint(0,len(IA.mainJoueur)-1)]   #carte prise au hasard
            IA.mainJoueur.remove(IA.cartes[i])



def Puissante(jeu):
    listeIA = jeu.listeJoueurs[1:]
    for IA in listeIA:
#        removeList = []             #liste des cartes à retirer de la pioche
#        for carte in IA.mainJoueur:
#            print('cartes disponibles pour l\'ia')
#            print(carte)
#        print(IA.state)

        #Toutes les position possibles dans une liste
        possibleOutcomes = treeExplorer(IA.state, IA.mainJoueur, max(0,IA.pv - 4), jeu.plateau)
        
        arrivee = jeu.plateau.casesVictoire[0]      #position d'une case qui fait gagner
        indiceGagnant = None                        #Si jamais on ne trouve rien on 'Shut Down'
        distanceMin = distance((IA.state[1],IA.state[2]),arrivee)       #Distance actuelle à l'arrivée
#        print(distanceMin)
#        print(possibleOutcomes)
        for index, outcome in enumerate(possibleOutcomes):
            new_state = outcome[0]
#            if new_state[0] != 0:
#                if new_state[2] == 1 and new_state[1] == 2:
#                    print('erreur')
#            print(new_state)
            x,y = new_state[1],new_state[2]
            d = distance((x,y),arrivee)
            if d < distanceMin:
                if new_state[0] > 0: #si la distance est meilleur et que l'on vit
#                    print(new_state)
                    distanceMin = d
                    indiceGagnant = index
#                    print('meilleur combinaison: d,x,y',distanceMin,x,y)
        
#        print(listeIndices)
        if indiceGagnant: #si l'on a trouvé une solution meilleure que d'être immobile
            print('état final supposé:',possibleOutcomes[indiceGagnant][0])
            print('cartes choisies par l\'IA:')
            listeIndices = possibleOutcomes[indiceGagnant][1]
            for idx,val in enumerate(listeIndices):
                IA.cartes[idx] = IA.mainJoueur[val]
                print(val,IA.cartes[idx])
#            print('\n')
        else:
            print('l\'IA ne bouge pas')
#        for carte in IA.cartes:
#            print(carte)
#        for i in range(len(IA.cartes)): #On remplit la liste des cartes
# 
#        
#            IA.mainJoueur.remove(IA.cartes[i])
            
            
def treeExplorer(state, mainIA, choixRestants, plateau, indexChoisis = []):
    """
    state: l'état du robot
    indexChoisis: les indices des cartes sélectionnées pour arriver à cet état
    mainIA: la main de l'IA
    choixRestants: le nombre de cartes à choisir pour avoir le compte
    """
    if choixRestants == 0:
        return [(state,indexChoisis)]
    
    else:
        l = [] #la liste des résultats a récupérer de l'exploration d'arbre
        for index, carte in enumerate(mainIA):
            if index in indexChoisis:
                pass
            else:
                indexChoisis2 = indexChoisis[:] #on copie la liste pour pas foutre le bordel
                indexChoisis2.append(index)
                new_state = estimatedStateCarte(state,carte,plateau)
                l += treeExplorer(new_state,mainIA,choixRestants - 1, plateau,indexChoisis2)
        return l
        
#        récupérer le __str__, dico ,matrice de déplacement associée

def estimatedStateCarte(state,carte,p):
    """
    renvoie l'état d'un parti d'un état 'state' avec la carte 'carte' sur le plateau 'p'
    """
    angleToMatrix = {0: p.m0,1: p.m1, 2: p.m2, 3: p.m3}
    vitesse = carte.vitesse
    angle = state[3]
    if vitesse == -1: #si on recule
        angle = state[3] + 2
        angle = angle % 4 #ne pas réutiliser cet angle pour l'état final: si l'on recule il va se retourner!!
#        print(angle)
    matriceDirection = angleToMatrix[angle] #la matrice des contraintes dans la direction de déplacement du robot
    
#    print('state',state)
#    new_state = state * matriceDirection #On utilise la propriété des MatricesD
    new_state = state[:]
    for i in range(abs(vitesse)): #Si on bouge de plusieurs cases
        new_state = matriceDirection(new_state)
        
#    print(new_state)
#    print('new_state',new_state) 
    
#    if new_state[1] == 2 and new_state[2] == 1:
#        print('avant',new_state)
    new_state = p.mc(new_state)
#    print('new_state',new_state) 
    (pv,x,y,o) = new_state
    o = (o + carte.angle) % 4
    new_state = (pv,x,y,o)    
#    if new_state[1] == 2 and new_state[2] == 1:
#        print('après',new_state)
    return new_state


def scalaire(A,B):
    """
    renvoie la distance entre A et B
    """
    xa,ya = A
    xb,yb = B
    return xa * xb + ya * yb


def distance(A,B):
    """
    renvoie la distance entre A et B
    """
    xa,ya = A
    xb,yb = B
    return scalaire((xa-xb,ya-yb),(xa-xb,ya-yb))


#Pour faire quelques tests:
if __name__ == "__main__":
    import Cartes
    import plateau3
    p = plateau3.plateau
    p.prepare()
    state = (9,3,0,0)
    carte = Cartes.Translation(-1)
    print('carte',carte)
    print('départ',state,'arrivée',estimatedStateCarte(state,carte,p))
#    print(p.m0)
#    print(estimatedStateCarte(state,carte, p))
    
#    listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
#               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
#               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
#               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]
#    
#    listeCartes = [Cartes.Translation(2),Cartes.Translation(3),
#               Cartes.Rotation(3), Cartes.Rotation(3),Cartes.Rotation(2)]
#               
    listeCartes = [Cartes.Rotation(2),Cartes.Rotation(3),Cartes.Translation(2),Cartes.Rotation(3),Cartes.Translation(3)]
#               
    outcomes = treeExplorer(state, listeCartes[:], 5, p)
#    for state,liste in outcomes:
#        print(state,liste)
    for index, outcome in enumerate(outcomes):
        state = outcome[0]
        liste = outcome[1]
        if liste == [0,1,2,3,4]:
            print(state)
            pass
#        if state[0] == 1 and state[2] ==3:
#            print(state)

#    state = (9,1,1,3)
#    print(state,listeCartes[0])
##    print(state)
#    state = estimatedStateCarte(state,listeCartes[0], p)
#    print(state,listeCartes[1])
#    state = estimatedStateCarte(state,listeCartes[1], p)
#    print(state,listeCartes[2])
#    state = estimatedStateCarte(state,listeCartes[2], p)
#    print(state,listeCartes[3])
#    state = estimatedStateCarte(state,listeCartes[3], p)
#    print(state,listeCartes[4])
#    state = estimatedStateCarte(state,listeCartes[4], p)
#    print(state)

#    state = (9,1,1,3)
#    carte = listeCartes[0]
#    angleToMatrix = {0: p.m0,1: p.m1, 2: p.m2, 3: p.m3}
#    vitesse = carte.vitesse
#    angle = state[3] + carte.angle
#    if vitesse == -1: #si on recule
#        angle = -angle
#    angle = angle % 4 #ne pas réutiliser cet angle pour l'état final: si l'on recule il va se retourner!!
#    print(angle)
#    matriceDirection = angleToMatrix[angle] #la matrice des contraintes dans la direction de déplacement du robot
#    print(matriceDirection)
#    print(p.m1)
    
#    state = (9,1,1,0)
#    carte = listeCartes[2]
#    print(state,carte)
#    print(estimatedStateCarte(state,carte, p))
#    angleToMatrix = {0: p.m0,1: p.m1, 2: p.m2, 3: p.m3}
#    vitesse = carte.vitesse
#    angle = state[3]
#    if vitesse == -1: #si on recule
#        angle = -state[3]
#        angle = angle % 4 #ne pas réutiliser cet angle pour l'état final: si l'on recule il va se retourner!!
#
#    print(angle)
#    matriceDirection = angleToMatrix[angle] #la matrice des contraintes dans la direction de déplacement du robot
#    print(matriceDirection(state))
##    print(p.m1)



















