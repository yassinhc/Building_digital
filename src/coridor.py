from src.Area import Area
from src.Wall import Wall
from src.coordinate import Coordinate
from src.ElementaryArea import ElementaryArea

# supposed that the Corridor is composed from two Wall parallel with the same length and
#their two Wall can compose a rectangle if joined

class Corridor(ElementaryArea):
    """
   def __init__(self,ListWalls):
        self.__ListWalls=ListWalls
        assert(len(ListWalls)==2 and type(ListWalls[0]) == Wall and type(ListWalls[1]) == Wall   ) #we're verifying that the instance of Area is indeed a corridor
    """
    def getSurface(self): 
        length = self.getListWalls()[0].getLength()
        a = self.getListWalls()[0].getCoordinates()[0]
        b = self.getListWalls()[1].getCoordinates()[0]
        c = self.getListWalls()[1].getCoordinates()[1]
        width = min(a.getLength(b),a.getLength(c))
        
        return length*width
        
