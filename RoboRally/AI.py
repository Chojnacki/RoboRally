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
        for carte in IA.mainJoueur:
            print(carte)
        distanceMin = jeu.plateau.x ** 2 + jeu.plateau.y ** 2
        
        #Toutes les position possibles dans une liste
        possibleOutcomes = treeExplorer(IA.state, IA.mainJoueur, 5, jeu.plateau)
#        min(IA.pv - 4,5)
        
        arrivee = jeu.plateau.casesVictoire[0]      #position d'une case qui fait gagner
        bestOutcome = possibleOutcomes[0]
        indiceGagnant = 0
        for index, outcome in enumerate(possibleOutcomes):
            x,y = outcome[0][1],outcome[0][2]
            d = distance((x,y),arrivee)
            if d < distanceMin:
                distanceMin = d
                indiceGagnant = index
                print(distanceMin,x,y)
        
        listeIndices = possibleOutcomes[indiceGagnant][1]
        print(listeIndices)
        for idx,val in enumerate(listeIndices):
            IA.cartes[idx] = IA.mainJoueur[val]
            print(val)
        for carte in IA.cartes:
            print(carte)
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
#    print(1)
    """
    renvoie l'état d'un parti d'un état 'state' avec la carte 'carte' sur le plateau 'p'
    """
    angleToMatrix = {0: p.m0,1: p.m1, 2: p.m2, 3: p.m3}
    vitesse = carte.vitesse
    angle = state[3] + carte.angle % 4
#    print(angle)
    if vitesse == -1:
        angle = -angle %4
#    print(angle)
    angle = angle % 4
    try:
        matriceDirection = angleToMatrix[angle]
    except KeyError as k:
        print(k,angle)
    #matrice qui donne la position du robot après la case:
    matricePosition = md.MatriceD(p.x,p.y,None,p.listeMurs)
#    print(vitesse)
    for i in range(vitesse):
#        print(matricePosition,matriceDirection)
        matricePosition = matricePosition * matriceDirection
    matricePosition = matricePosition * p.mc
#    print(matriceDirection)
#    print(matricePosition)
    x,y = matricePosition.position((state[1],state[2]))
    new_state = (state[0],x,y,angle)
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
    import plateau1
    p = plateau1.plateau
    p.prepare()
    state = (0,4,1,0)
    carte = Cartes.Translation(1)
#    print(p.m0)
#    print(estimatedStateCarte(state,carte, p))
    
    listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]
               
    outcomes = treeExplorer(state, listeCartes[:9], 5, p)
    for state,liste in outcomes:
        print(state,liste)
    




