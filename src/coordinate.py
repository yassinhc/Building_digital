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
    getVecor(coordinate):
        Return the vector from current coordinate to the new one.
    getLength(coordinate):
        Return the length of two coordinate
    isAfter(coordinate):
        Return True if the coordinate is after our current coordinate.
    """
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getx(self):
        '''
        Returns
        -------
        TYPE Integer
            return the abscissa of a coordiante
        '''
        return self.__x

    def gety(self):
        '''
        Returns
        -------
        TYPE Integer
            return the ordinate of a coordiante
        '''
        return self.__y
    
    def getVector(self,coordinate):
        '''
        Parameters
        ----------
        coordinate : Coordiante
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
        coordinate : Coordiante
            The coordinate to compute the length with

        Returns
        -------
        TYPE : Integer
            return the length between two coordinates
        '''
        vector= self.getVector(coordinate)
        return(sqrt(vector[0]**2 + vector[1]**2)) #norm of the vector 
   
    def isAfter(self,coordinate):
        '''
        Parameters
        ----------
        coordinate : Coordinate
            The coordiante to comapre if it is after our current coordinate or not

        Returns
        -------
        TYPE : Boolean
            return true if coordiante is after our current coordinate
        '''
        return coordinate.getx() >= self.getx() and coordinate.gety() >= self.gety()
    
    
