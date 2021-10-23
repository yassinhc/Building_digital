import sys

sys.path.append('..')

from src.Element import Element

class Wall(Element):
    def __init__(self,coordinates):
        super().__init__(coordinates)
        self.__listWindow = []
        self.__listDoor=[]
        self.__listCanBeContain=[(self.getCoordinates()[0],self.getCoordinates()[1])]
        self.__vector=self.getCoordinates()[0].getVector(self.getCoordinates()[1]) #vecteur associé au mur
     
    def getVector(self):
        return self.__vector
    
    def getListCanBeContain(self):
        return self.__listCanBeContain
    
    
    def listContainAfterAddingElement(self,element):
        found = False
        for i in range(len(self.__listCanBeContain)):
            found = True
            if self.canBeContain(self.__listCanBeContain[i], element):
                if element.getCoordinates()[0] == self.__listCanBeContain[i].getCoordinates()[0]:
                    if element.getCoordinates()[1] != self.__listCanBeContain[i].getCoordinates()[1]:
                        self.__listCanBeContain[i][0]=element.getCoordinates()[1]
                    else:
                        self.__listContain.remove(self.__listCanBeContain[i])
                elif element.getCoordinates()[1] == self.__listCanBeContain[i].getCoordinates()[1]:
                    self.__listCanBeContain[i][1]=element.getCoordinates()[0]
                else:
                    self.__listCanBeContain.append((element.getCoordinates()[1],self.__listCanBeContain[i][1]))
                    self.__listCanBeContain[i][1]=element.getCoordinates()[0]
                return found
        return found
    
    def canBeContain(self,selfelem,element):
        isAfter = selfelem.getCoordinates()[0].isAfter(element.getCoordinates()[0])
        isBefore = element.getCoordinates()[1].isAfter(selfelem.getCoordinates()[1])
        onTheLine1 = selfelem.getCoordinates()[0].onTheLine(selfelem.getCoordinates()[1],element.getCoordinates()[0])
        onTheLine2 = selfelem.getCoordinates()[0].onTheLine(selfelem.getCoordinates()[1],element.getCoordinates()[1])
        return isAfter and isBefore and onTheLine1 and onTheLine2
    
    def addWindow(self,window):
        if window not in self.listWindow and self.listContainAfterAddingElement(window):
            self.__listWindow.append(window)
    
    def addDoor(self,door):
        if door not in self.listDoor and self.listContainAfterAddingElement(door):
            self.__listDoor.append(door)
        
    def getListWindow(self):
        return self.__listWindow
    
    def getListDoor(self):
        return self.__listDoor
    
#    [(1,5)] => add(2,3) [(1,2),(3,5)]
 #           => add(3,4) [(1,2),(4,5)]