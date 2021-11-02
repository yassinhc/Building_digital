from abc import ABC



class Element(ABC):
    """
    A class to represent a Element.
    ...
    
    Attributes
    ----------
    coordinates : tuple of coordinates as (z1,z2) where z1=(x1,y1) and z2=(x2,y2)
        
    Methods
    -------
    getCoordinates():
        Get the coordinates of an element.
    getLenght():
        Return the lenght between the two coordinates designing the element.
    
    """
    def __init__(self,coordinates):
        self.__coordinates=coordinates
        super().__init__()
        
    def getCoordinates(self):
        '''
        Returns
        -------
        TYPE : Integer
            Return the two coordinates designing the element.
        '''
        return self.__coordinates
        
    def getLength(self):
        '''
        Returns
        -------
        TYPE : float
            Return the lenght between the two coordinates designing the element.
        '''
        return self.getCoordinates()[0].getLength(self.getCoordinates()[1])
         
        
