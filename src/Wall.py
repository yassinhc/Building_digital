import os

print(os.getcwd())


from src.Element import Element

class Wall(Element):
    def __init__(self):
        P1,P2=getCoordinates(self)[0],getCoordinates(self)[1]
        self.__vector=getVector(P1,P2) #vecteur associé au mur
     
    def getVector(self):
        return self.__vector 
    
