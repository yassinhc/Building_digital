from src.ElementaryArea import ElementaryArea

# supposed that the Room are rectangle or square
class Room(ElementaryArea):
    """
    A class to represent a Room.
    ...
    
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the room
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the room.
    getSurface():
        Return the surface of the room
    """
    
    def getSurface(self):
        '''
        Returns
        -------
        TYPE Float
            return the surface of the room
        ''' 
        Longueurs = [self.getListWalls()[0].getLength()]
        
        for element in self.getListWalls():
            if element.getLength() not in Longueurs:
                Longueurs.append(element.getLength())
        
        if len(Longueurs) == 1: #It's a square
            return Longueurs[0]**2
        else: return Longueurs[0]*Longueurs[1]
        

