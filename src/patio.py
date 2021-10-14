from ElementaryArea import ElementaryArea

class Patio(ElementaryArea): #4 murs d'angles qqc
    def getAngle(self): #retourne une liste des angles entre chaque mur contigus
        Walls=[self.listElement[0]] #on crée une liste qui retrie nos murs selon leurs contiguité.
        Walls.append( i for i self.listElement if Walls[-1].__coordinates[1]= i.__coordinates[0])]
    def getSurface(self): 
        
