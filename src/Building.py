
import src.Element as Element

class Building():
    def __init__(self,listElement):
        """
        """
    
        self.__listElement= listElement

    def getLenElement(self):
        return len(self.__listElement)
         
    def getListElement(self):
        return self.__listElement
    
    def addElement(self,element):
        self.__listElement.append(element)

