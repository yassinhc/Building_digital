class Floor():
    """
    A class to represent a Floor.
    ...
    
    Attributes
    ----------
    listElement : list of Elements
        The list of elements contained in the floor
    
    Methods
    -------
    getListElement():
        Return the list of elements contained in the floor
    getLenElement():
        Return the number of elements in the floor
    addElement(element):
        Add element to the list if not exists
    """

    def __init__(self,listElement):
        self.__listElement= listElement
        

    def getLenElement(self):
        """
        Returns
        -------
        TYPE Integer
            Return the number of elements in the floors
        """
        return len(self.__listElement)
         
    def getListElement(self):
        """
        
        Returns
        -------
        TYPE List of Element
            Return the list of element in the floor.

        """
        return self.__listElement
    
    def addElement(self,element):
        """
    
        Parameters
        ----------
        element : Element
            The element to add to the floor.

        Returns
        -------
        None. (add element to the floor if not exists)

        """
        if element not in self.getListElement():
            self.__listElement.append(element)
