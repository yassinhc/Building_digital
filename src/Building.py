class Building():
    """
    A class to represent a Building.
    ...
    
    Attributes
    ----------
    listFloor : list of Floor
        The list of floors contained in the building
    
    Methods
    -------
    getListFloor():
        Return the list of floors contained in the building
    getLenFloor():
        Return the number of floors in the building
    addFloor(floor):
        Add floor to the list if not exists
    """
    def __init__(self,listFloor):
    
        self.__listFloor= listFloor
        

    def getLenFloor(self):
        """
        
        Returns
        -------
        TYPE Integer
            Return the number of floors in the building.

        """
        return len(self.__listFloor)
         
    def getListFloor(self):
        """
        
        Returns
        -------
        TYPE List of Floor
            Return the list of floor in the building.

        """
        return self.__listFloor
    
    def addFloor(self,floor):
        """
    
        Parameters
        ----------
        floor : Floor
            The floor to add to the building.

        Returns
        -------
        None. (add floor to the building if not exists)

        """
        if floor not in self.getListFloor():
            self.__listFloor.append(floor)


