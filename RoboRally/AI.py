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
        print(IA.state)
        distanceMin = jeu.plateau.x ** 2 + jeu.plateau.y ** 2

        #Toutes les position possibles dans une liste
        possibleOutcomes = treeExplorer(IA.state, IA.mainJoueur, max(0,IA.pv - 4), jeu.plateau)
#        min(IA.pv - 4,5)
        
        arrivee = jeu.plateau.casesVictoire[0]      #position d'une case qui fait gagner
        indiceGagnant = 0
        for index, outcome in enumerate(possibleOutcomes):
            x,y = outcome[0][1],outcome[0][2]
            d = distance((x,y),arrivee)
            if d < distanceMin:
                distanceMin = d
                indiceGagnant = index
                print(distanceMin,x,y)
        
        listeIndices = possibleOutcomes[indiceGagnant][1]
#        print(listeIndices)
        print('cartes choisies par l\'IA')
        for idx,val in enumerate(listeIndices):
            IA.cartes[idx] = IA.mainJoueur[val]
            print(val,IA.cartes[idx])
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
    angle = state[3] + carte.angle
    if vitesse == -1: #si on recule
        angle = -angle
    angle = angle % 4 #ne pas réutiliser cet angle pour l'état final: si l'on recule il va se retourner!!

    matriceDirection = angleToMatrix[angle] #la matrice des contraintes dans la direction de déplacement du robot
    
    
    new_state = state * md.MatriceD(p.x,p.y,0,None,p.listeMurs) #On utilise la propriété des MatricesD
    for i in range(vitesse): #Si on bouge de plusieurs cases
        new_state = new_state * matriceDirection 
        
    new_state = new_state * p.mc
    (pv,x,y,o) = new_state
    o = (o + carte.angle) % 4
    new_state = (pv,x,y,o)
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
    state = (9,0,0,0)
    carte = Cartes.Translation(1)
#    print(p.m0)
#    print(estimatedStateCarte(state,carte, p))
    
    listeCartes = [Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(3),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Translation(1), Cartes.Translation(2),Cartes.Translation(1),
               Cartes.Rotation(1), Cartes.Rotation(3),Cartes.Rotation(2)]
               
    outcomes = treeExplorer(state, listeCartes[:], 2, p)
    for state,liste in outcomes:
        print(state,liste)
    




