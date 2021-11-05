
from src.Area import Area

from src.coordinate import Coordinate
import numpy as np

class SubArea(Area):
    """
    A class to represent a SubArea of Area.
    ...
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the area
    res: Float
        The sum of all surface in the list surface
    listElements: List(Element)
        The list of elements that well be added
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the area.
    getSurface():
        Return the surface of the area
    getListArea():
        Return the list of area
    addArea(area):
        Add area to the list if it is didn't contain it yet
    computeSurface(area):
        Compute the new surface after adding area
    getSurface():
        Return the sum of all the surface containing in the list of areas
    addElement(element):
        Add element to the list of elements if it is didn't contain yet
    getNbElements():
        Return the number of elements in the list of elements
    getPoints():
        Return a numpy array of each point extract from element's coordinate
    """
    def __init__(self,listArea):
        self.__listArea=listArea
        self.__res=0
        self.__listElements=[]
        super().__init__([])
    
    def getListArea(self):
        """
        Returns
        -------
        List(Area)
            Return the list of area.
        """
        return self.__listArea
    
    def addArea(self,area):
        """
        Parameters
        ----------
        area : Area
            The area that we wish to add

        Returns
        -------
        None.(Add area to the list of area if not exists)

        """
        if area not in self.__listArea:
            self.__listArea.append(area)
            self.computeSurface(area)
    
    #The surface off different area from list area without the area created by the list of element(it's more an abstract area)
    def computeSurface(self,area):
        """
        Parameters
        ----------
        area : Area
            The area that we have added to the list of area.

        Returns
        -------
        None.(add the surface od area to the global surface)
        """
        self.__res+=area.getSurface()
    
    def getSurface(self):
        """
        Returns
        -------
        Float
            Return the surface of the area(only conposed from list area and not from different elements added)

        """
        return self.__res
    
    def getListElements(self):
        """
        Returns
        -------
        List(Element)
            Return the list of elements added.

        """
        return self.__listElements
    
    def addElement(self,element):
        '''
        Parameters
        ----------
        element : Element
            The element that we hope add to the area

        Returns
        -------
        None. (add element if possible)

        '''
        if element not in self.getListElements():
            self.__listElements.append(element)
    
    def getNbElements(self):
        """
        Returns
        -------
        Int
            Return the number of elements in the list of elements.

        """
        return len(self.getListElements())

    def getPoints(self):
        """
        Returns
        -------
        NumpyArray([Int,Int])
            Return the numpy array of the points extract from the elements coordinates.

        """
        points = []
        for element in self.__listElements:
            coord1, coord2 = element.getCoordinates()[0], element.getCoordinates()[1]
            x1, y1, x2, y2 = coord1.getx(), coord1.gety(), coord2.getx(), coord2.gety()
            if [x1, y1] not in points:
                points.append([x1, y1])
            if [x2, y2] not in points:
                points.append([x2, y2])
        return np.array(points)
