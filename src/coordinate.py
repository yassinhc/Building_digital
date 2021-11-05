from math import sqrt
import numpy as np

class Coordinate():
    """
    A class to represent a coordinate.
    ...
    
    Attributes
    ----------
    x : int
        the abscissa of the coordinate
    y : int
        the ordinate of the coordinate

    Methods
    -------
    getx():
        Get the abscissa of the coordinate.
    gety():
        Get the ordinate of the coordinate.
    getVector(coordinate):
        Return the vector from current coordinate to the new one.
    getLength(coordinate):
        Return the length of two coordinate
    isAfter(coordinate):
        Return True if the coordinate is after our current coordinate.
    onTheLine(coordiante,coo):
        Return true if coo belong to the segment of self coordinate and coordiante
    """
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getx(self):
        '''
        Returns
        -------
        TYPE Integer
            return the abscissa of a coordinate
        '''
        return self.__x

    def gety(self):
        '''
        Returns
        -------
        TYPE Integer
            return the ordinate of a coordinate
        '''
        return self.__y
    
    def getVector(self,coordinate):
        '''
        Parameters
        ----------
        coordinate : Coordinate
            The coordinate to compute the Vector with

        Returns
        -------
        TYPE : NUMPY.ARRAY
            return the vector from self to coordinate
        '''
        X=coordinate.getx()-self.getx()
        Y=coordinate.gety()-self.gety()
        return(np.array([X,Y]))
    
    
    def getLength(self,coordinate):
        '''
        Parameters
        ----------
        coordinate : Coordinate
            The coordinate to compute the length with

        Returns
        -------
        TYPE : Float
            return the length between two coordinates
        '''
        vector= self.getVector(coordinate)
        return(sqrt(vector[0]**2 + vector[1]**2)) #norm of the vector 
   
    def isAfter(self,coordinate):
        '''
        Parameters
        ----------
        coordinate : Coordinate
            The coordiante to compare if it is after our current coordinate or not

        Returns
        -------
        TYPE : Boolean
            return true if coordinate is after our current coordinate
        '''
        return coordinate.getx() >= self.getx() and coordinate.gety() >= self.gety()
    
    def onTheLine(self,coordinate,coo):
        '''
        Parameters
        ----------
        coordinate : Coordinate
            The coordinate that we will use to create the line with self coordinate
        coo : Coordinate
            The coordiante we use to check if it is on the line or not

        Returns
        -------
        TYPE : Boolean
            return true if coo belong to the segment of self coordinate and coordinate
        '''
        X,Y = self.getVector(coordinate)
        if X == 0:
            return coo.getx() == self.getx()
        a = Y/X
        b = self.gety()-a*self.getx()
        return coo.gety() == a*coo.getx()+b
    
