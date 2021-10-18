from abc import ABC



class Element(ABC):
    
    def __init__(self,coordinates):
        self.__coordinates=coordinates
        self.length=0
        super().__init__()
        
    def getCoordinates(self):
            return self.__coordinates
        
    def getLength(self):
            self.length =  self.getCoordinates()[0].getLength(self.getCoordinates()[1])
            return self.length
        
