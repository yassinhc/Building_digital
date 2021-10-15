import os

print(os.getcwd())


from src.Element import Element

class Wall(Element):
    def __init__(self):
        P1,P2=self.getCoordinates()[0],self.getCoordinates()[1]
        self.__vector=P1.getVector(P2) #vecteur associé au mur
     
    def getVector(self):
        return self.__vector 
    
