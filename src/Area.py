from abc import ABC, abstractmethod



class Area(ABC):
    
    def __init__(self,listElement):
        self.__listElement=listElement
        super().__init__()
        
        def getListElement(self):
            return self.__listElement
        
        @abstractmethod
        def getSurface(self):
            pass
        
        
        
