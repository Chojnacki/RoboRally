# -*- coding: utf-8 -*-





class Robot:
    
    def __init__(self,position,orientation = 1):
        self.__pv = 9
        self.__position = position
        self.__orientation = orientation

    def __str__(self):
        s = " Points de vie: "
        s += str(self.__pv)
        s += " | Position: "
        s += str(self.__position)
        s += " | Orientation: "
        s += str(self.orientation)
        return s

    @property
    def orientation(self):
        """
        orientation: 0,1,2 ou 3
            direction du robot (0 = vers la droite, 1 = le haut, 2 = la gauche, 3 = le bas)
        """
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        """
        Met à jour l'orientation du robot.
        Garantit 0 <= orientation <= 3.
        """
        o = orientation
        o = max( min(o, 3), 0)

        self.__orientation = o
        
        return self.__orientation

    @property
    def position(self):
        """
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        """
        self.__position = position
        return self.__position

if __name__ == "__main__":
    
    twonky = Robot((1,1),1)
    print(twonky)




        