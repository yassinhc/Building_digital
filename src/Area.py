from abc import ABC, abstractmethod



class Area():
    """
    A class to represent a Area.
    ...
    
    Attributes
    ----------
    listElement : list of Elements
        The list of elements disigning the area
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the area.
    getSurface():
        Return the surface of an element
    """
    def __init__(self,listElement):
        self.__listElement=listElement
        super().__init__()
        
    def getListElement(self):
        '''
        Returns
        -------
        TYPE List of Elements
            return the list of elements designing the area
        '''
        return self.__listElement
        
    @abstractmethod
    def getSurface(self):
        '''
        Returns
        -------
        TYPE Float
            return the surface of an area
        '''
        pass
        
        
        
