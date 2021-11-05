
from abc import ABC, abstractmethod



class Area():
    """
    A class to represent a Area.
    ...
    
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the area
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the area.
    getSurface():
        Return the surface of the area
    """
    def __init__(self,ListWalls):
        self.__ListWalls=ListWalls
        super().__init__()
        
    def getListWalls(self):
        '''
        Returns
        -------
        TYPE List of Walls
            return the list of walls designing the area
        '''
        return self.__ListWalls
        
    @abstractmethod
    def getSurface(self):
        '''
        Returns
        -------
        TYPE Float
            return the surface of the area
        '''
        pass
        
        
    
