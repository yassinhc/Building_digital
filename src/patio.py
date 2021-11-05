from src.ElementaryArea import ElementaryArea


from numpy import linalg as LA #pour la norme

import numpy as np

from math import sqrt

class Patio(ElementaryArea): #4 murs d'angles qqc
    """
    A class to represent a Patio.
    ...
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the patio
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the patio.
    getSurface():
        Return the surface of the patio
    getAngle():
        Return the list of angles between each two wall contiguous
    """

    def getAngle(self): # we suppose Walls are tried by their contiguity
        '''
        Returns
        -------
        TYPE : List of floats
            return a list of angles between each walls designing the patio
        '''
        angles=[]
        for i in range(0,len(self.getListWalls())-1):
            mur1=self.getListWalls()[i].getVector()
            mur2=self.getListWalls()[i+1].getVector()
            angle= np.arccos((mur1[0]*mur2[0]+mur1[1]*mur2[1])/(LA.norm(mur1)*LA.norm(mur2)))
            angles.append(angle)
        return angles
    
    def getSurface(self): #Bretschweider formula
        '''
        Returns
        -------
        TYPE Float
            return the surface of the corridor
        '''
        L=[i.getLength() for i in self.getListWalls()]
        a,b,c,d=L[0],L[1],L[2],L[3]
        s=(a+b+c+d)/2
        angles=self.getAngle()
        alpha,gamma=angles[0],angles[2]
        return (sqrt((s-a)*(s-b)*(s-c)*(s-d) -a*b*c*d*np.cos((alpha+gamma)/2)**2)) #retourne la surface
    
