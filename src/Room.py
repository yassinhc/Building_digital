from src.ElementaryArea import ElementaryArea

# supposed that the Room are rectangle or square
class Room(ElementaryArea):
    
    def getSurface(self): 
        Longueurs = [self.getListElement()[0].getLength()]
        
        for element in self.getListElement():
            if element.getLength() not in Longueurs:
                Longueurs.append(element.getLength())
        
        if len(Longueurs) == 1: #It's a square
            return Longueurs[0]**2
        else: return Longueurs[0]*Longueurs[1]
        

