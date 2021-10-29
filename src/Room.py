from ElementaryArea import ElementaryArea

class Room(ElementaryArea):

    #on suppose que les
    def getSurface(self): 
        Longueurs=[element.getLenght() for element in self.getListElement() if element.getLenght() not in Longueurs] #c'est un rectangle,on récupère les deux longueurs diff si ce n'est pas un carré.
        if len(Longueurs) == 1: #C'est un carré
            return self.getListElement()[0].getLenght()**2
        else: return Longueurs[0]*Longueurs[1]
        

