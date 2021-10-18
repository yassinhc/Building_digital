
import src.Element as Element

class Building():
    def __init__(self, listElements):
        """
        """
    
        self.__listElements= listElements
        

    def getLenArea(self):
        return len(self.__listArea)
         
    def getElements(self):
        return self.__listElements
    
    def addElement(self, x1, y1, x2, y2):
        self.__listElements.append(Element.Element(x1, y1, x2, y2))
        

        