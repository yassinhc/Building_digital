

from src.Element import Element

class Wall(Element):
    def __init__(self):
        self.__listWindow = []
        self.__listDoor=[]
        P1,P2=self.getCoordinates()[0],self.getCoordinates()[1]
        self.__vector=P1.getVector(P2) #vecteur associé au mur
     
    def getVector(self):
        return self.__vector 
    
    
    def addWindow(window):
        self.__listWindow.append(window)
    
    def addDoor(door):
        self.__listDoor.append(door)
        
    def getListWindow(self):
        return self.__listWindow
    
    def getLitDoor(self):
        return self.__listDoor
    