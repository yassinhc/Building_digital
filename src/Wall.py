import sys

sys.path.append('..')

from src.Element import Element

class Wall(Element):
    """
    A class to represent a wall.
    ...
    
    Parameters
    ----------
    coordinates : Tuple of Coordiante
        The coordinate of the wall

    Attributes
    ----------
    listWindow : List
        The list of window on the wall
    listDoor : List
        The list of door on the wall
    listCanBeContain: List
        The list of list of 2 coordinates where we can add a new element
    vector: Numpy Array
        The vector of coordinates

    Methods
    -------
    getVector():
        Get the attribute vector 
    getListCanBeContain():
        Get the attribute listCanBeContain
    getLength(coordinate):
        Return the length of two coordinate
    listContainAfterAddingElement(element):
        Return true if we can add the element on the wall and add it, false else
    canBeContain(selfcoordinate,elem):
        Return true if the coordiante of elem are on the sequence of selfcoordinate
    addWindow(window):
        Add window if possible
    addDoor(door):
        Add door if possible
    getListWindow():
        Get the  list of window 
    getListDoor():
        Get the list of door
    """
    def __init__(self,coordinates):
        super().__init__(coordinates)
        self.__listWindow = []
        self.__listDoor=[]
        self.__listCanBeContain=[[self.getCoordinates()[0],self.getCoordinates()[1]]]
        self.__vector=self.getCoordinates()[0].getVector(self.getCoordinates()[1]) #vecteur associé au mur
     
    def getVector(self):
        '''
        Returns
        -------
        TYPE Numpy Array
            Get the vector of the coordiantes
        '''
        return self.__vector
    
    def getListCanBeContain(self):
        '''
        Returns
        -------
        TYPE List
            Get the list of list of 2 coordinates where can we add a window or door
        '''
        return self.__listCanBeContain
    
    
    def listContainAfterAddingElement(self,element):
        '''
        Parameters
        ----------
        element : Element(window or door)
            The element that we hope add on the wall

        Returns
        -------
        found : Boolean
            Return true if we can add element to the wall, false else
        '''
        found = False
        for i in range(len(self.__listCanBeContain)):
            if self.canBeContain(self.__listCanBeContain[i], element):
                found = True
                if element.getCoordinates()[0] == self.__listCanBeContain[i][0]:
                    if element.getCoordinates()[1] != self.__listCanBeContain[i][1]:
                        self.__listCanBeContain[i][0]=element.getCoordinates()[1]
                    else:
                        self.__listContain.remove(self.__listCanBeContain[i])
                elif element.getCoordinates()[1] == self.__listCanBeContain[i][1]:
                    self.__listCanBeContain[i][1]=element.getCoordinates()[0]
                else:
                    self.__listCanBeContain.append([element.getCoordinates()[1],self.__listCanBeContain[i][1]])
                    self.__listCanBeContain[i][1]=element.getCoordinates()[0]
                return found
        return found
    
    def canBeContain(self,selfcoordinate,element):
        '''
        Parameters
        ----------
        selfcoordinate : List
            The list of 2 coordinate where we try to add element
        element : Element
            The element that we hope add

        Returns
        -------
        TYPE Boolean
            Return True if the coordinates of element are in the sequence of the coordinates of selfelem
        '''
        isAfter1 = selfcoordinate[0].isAfter(element.getCoordinates()[0])
        isBefore1 = element.getCoordinates()[1].isAfter(selfcoordinate[1])
        isAfter2 = selfcoordinate[0].isAfter(element.getCoordinates()[1])
        isBefore2 = element.getCoordinates()[0].isAfter(selfcoordinate[1])
        onTheLine1 = selfcoordinate[0].onTheLine(selfcoordinate[1],element.getCoordinates()[0])
        onTheLine2 = selfcoordinate[0].onTheLine(selfcoordinate[1],element.getCoordinates()[1])
        return isAfter1 and isBefore1 and onTheLine1 and onTheLine2 and isAfter2 and isBefore2
    
    def addWindow(self,window):
        '''
        Parameters
        ----------
        window : Window
            The window that we hope add on the wall

        Returns
        -------
        None. (add window on the wall if possible)

        '''
        if (window not in self.__listWindow) and (self.listContainAfterAddingElement(window)):
            self.__listWindow.append(window)
    
    def addDoor(self,door):
        '''
        Parameters
        ----------
        door : Door
            The door that we hope add on the wall

        Returns
        -------
        None. (add door on the wall if possible)

        '''
        if (door not in self.listDoor) and (self.listContainAfterAddingElement(door)):
            self.__listDoor.append(door)
        
    def getListWindow(self):
        '''
        Returns
        -------
        TYPE List
            The list of window on the wall
        '''
        return self.__listWindow
    
    def getListDoor(self):
        '''
        Returns
        -------
        TYPE List
            The list of door on the wall
        '''
        return self.__listDoor
