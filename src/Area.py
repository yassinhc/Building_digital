from src.Element import Element

class Area:

    def __init__(self, list_elem = None):
        self.__list_elements = list_elem


    def getListElements(self):
        return self.__list_elements

    def getNbElements(self):
        return len(self.getListElements())

    