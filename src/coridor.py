from src.Wall import Wall
from src.ElementaryArea import ElementaryArea

# supposed that the Corridor is composed from two Wall parallel with the same length and
#their two Wall can compose a rectangle if joined

class Corridor(ElementaryArea):
    """
    A class to represent a Corridor that extends the ElementArea class.
    ...
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the corridor
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the corridor.
    getSurface():
        Return the surface of the corridor
    """
    def __init__(self,ListWalls):
        super().__init__(ListWalls)
        assert(len(ListWalls)==2 and type(ListWalls[0]) == Wall and type(ListWalls[1]) == Wall) #we're verifying that the instance of Area is indeed a corridor
    
    
    def getSurface(self):
        '''
        Returns
        -------
        TYPE Float
            return the surface of the corridor
        '''
        length = self.getListWalls()[0].getLength()
        a = self.getListWalls()[0].getCoordinates()[0]
        b = self.getListWalls()[1].getCoordinates()[0]
        c = self.getListWalls()[1].getCoordinates()[1]
        width = min(a.getLength(b),a.getLength(c))
        
        return length*width
        
