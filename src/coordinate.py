from math import sqrt

import numpy as np

class Coordinate():
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
    
    def getVector(self,coordinate): #from self to coordinate
        X=coordinate.getx()-self.getx()
        Y=coordinate.gety()-self.gety()
        return(np.array([X,Y]))
    
    def getLength(self,coordinate):
       vector= self.getVector(coordinate)
       return(sqrt(vector[0]**2 + vector[1]**2)) #norm of the vector 
   
    def isAfter(self,coordinate):
        '''

        Parameters
        ----------
        coordinate : Coordinate
            The coordiante to comapre with

        Returns
        -------
        TYPE : Boolean
            return true if coordiante is after our current coordinate

        '''
        return coordinate.getx() >= self.getx() and coordinate.gety() >= self.gety()
    
    
