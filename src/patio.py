from ElementaryArea import ElementaryArea
from numpy import linalg as LA #pour la norme
import numpy as np
class Patio(ElementaryArea): #4 murs d'angles qqc
    def getAngle(self): #retourne une liste des angles entre chaque mur contigus , on suppose les murs triés selon leur contiguité
        angles=[]
        for i in range(0,len(self.__listElement)-1):
            mur1=self.getListElement()[i].getVector()
            mur2=self.getListElement()[i+1].getVector()
            angle= np.arccos(mur1*mur2/(LA.norm(mur1)*LA.norm(mur2)))
            angles.append(angle)
        return angles
    def getSurface(self): #Bretschweider formula
        Longueurs=[i.getLenght() for i in self.getListElement()]
        a,b,c,d=L[0],L[1],L[2],L[3]
        s=(a+b+c+d)/2
        alpha,gamma=angles[0],angles[2]
        return(sqrt((s-a)*(s-b)*(s-c)*(s-d) -a*b*c*d*np.cos((alpha+gamma)/2))) #retourne la surface
        
