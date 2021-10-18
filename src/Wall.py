import sys

sys.path.append('..')

from src.Element import Element

class Wall(Element):
    def __init__(self,coordinates):
        super().__init__(coordinates)
        self.__listWindow = []
        self.__listDoor=[]
        P1,P2=self.getCoordinates()[0],self.getCoordinates()[1]
        self.__vector=P1.getVector(P2) #vecteur associé au mur
     
    def getVector(self):
        return self.__vector 
    
    
    def addWindow(window):
        isAfter = self.getCoordinates()[0].isAfter(window.getCoordinates()[0])
        isBefore = window.getCoordinates()[1].isAfter(self.getCoordinates()[1])
        isContain = isAfter and isBefore
        if window not in self.listWindow and isContain:
            self.__listWindow.append(window)
    
    def addDoor(door):
        isAfter = self.getCoordinates()[0].isAfter(window.getCoordinates()[0])
        isBefore = window.getCoordinates()[1].isAfter(self.getCoordinates()[1])
        isContain = isAfter and isBefore
        if door not in self.listDoor and isContain:
            self.__listDoor.append(door)
        
    def getListWindow(self):
        return self.__listWindow
    
    def getListDoor(self):
        return self.__listDoor
    