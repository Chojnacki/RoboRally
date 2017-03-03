

import abc
import Robot as rob



class Case():
    
    __metaclass__ = abc.ABCMeta

    def __init__(self,position):
        """
        Crée une case aux coordonnées désirées.
        
        Paramètres
        ----------
        position: couple
            Les coordonnées auxquelles la case se trouvera  
        """
        self.__pos = position
        
    def __str__(self):
        """
        Affiche la position de la case.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        """
        return str(self.__pos)
        
    @abc.abstractmethod
    def Effet(self):
        """
        Applique l'effet de la case sur le robot suivant le type de la case
        
        Paramètres
        ----------
        Aucun
        """
        return
    
class CaseNeutre(Case):
    def __init__(self,position):
        """Le constructeur de la classe CaseNeutre.
        position : couple

        Note : On invoquer le constructeur de la
        classe-mère.
        """
        super().__init__(position)

class CaseArrivee(Case):
    def __init__(self,position):
        super().__init__(position)
    
class Tapis(Case):
    def __init__(self,position,orientation,virage,vitesse=1):
        """
        Crée un tapis roulant aux coordonnées désirées.
        
        Paramètres
        ----------
        position: couple
            Les coordonnées auxquelles la case se trouvera  
            
        orientation: {0,1,2,3}
        0: Droite
        1: Haut
        2: Gauche
        3: Bas
            
        virage: Droite, Gauche ou False
        """
        super().__init__(position)
        self.__orientation = orientation
        self.__virage = virage
        self.__vitesse = vitesse
        
    def Effet(self,robot):
        if self.__virage == False and self.__orientation == 0:
            robot.position = (robot.position[0]+self.__vitesse,robot.position[1])
        
        

        
        
if __name__ == "__main__":
    case = Tapis((1,2),0,False)
    print(Case)
    twonky = rob.Robot((1,1),1)
    print(twonky)
    case.Effet(twonky)
    print(twonky)
    
    
    
    
    
    
    
    
    
    
    
    
    