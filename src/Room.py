from Area import Area

class Room(Area):
    #on suppose que les
    def getSurface(self): 
        Longueurs=[element.lenght for element in self.listElement if element.lenght not in Longueurs] #c'est un rectangle,on récupère les deux longueurs diff si ce n'est pas un carré.
        if len(Longueurs) == 1: #C'est un carré
            return self.listElement[0].lenght**2
        else: return Longueurs[0]*Longueurs[1]
        
