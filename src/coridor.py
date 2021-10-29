from src.ElementaryArea import ElementaryArea

# supposed that the Corridor is composed from two Wall parallel with the same length and
#their two Wall can compose a rectangle if joined

class Coridor(ElementaryArea):
    
    def getSurface(self): 
        length = self.getListElement()[0].getLength()
        a = self.getListElement()[0].getCoordinates()[0]
        b = self.getListElement()[1].getCoordinates()[0]
        c = self.getListElement()[1].getCoordinates()[1]
        width = min(a.getLength(b),a.getLength(c))
        
        return length*width
        

