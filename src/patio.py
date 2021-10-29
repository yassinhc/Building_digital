from src.ElementaryArea import ElementaryArea


from numpy import linalg as LA #pour la norme

import numpy as np

from math import sqrt

class Patio(ElementaryArea): #4 murs d'angles qqc

    def getAngle(self): #retourne une liste des angles entre chaque mur contigus , on suppose les murs triés selon leur contiguité
        angles=[]
        for i in range(0,len(self.getListElement())-1):
            mur1=self.getListElement()[i].getVector()
            mur2=self.getListElement()[i+1].getVector()
            angle= np.arccos((mur1[0]*mur2[0]+mur1[1]*mur2[1])/(LA.norm(mur1)*LA.norm(mur2)))
            angles.append(angle)
        return angles
    
    def getSurface(self): #Bretschweider formula
        L=[i.getLength() for i in self.getListElement()]
        a,b,c,d=L[0],L[1],L[2],L[3]
        s=(a+b+c+d)/2
        angles=self.getAngle()
        alpha,gamma=angles[0],angles[2]
        return (sqrt((s-a)*(s-b)*(s-c)*(s-d) -a*b*c*d*np.cos((alpha+gamma)/2)**2)) #retourne la surface
    