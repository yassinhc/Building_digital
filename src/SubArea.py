
from src.Area import Area
from src.coordinate import Coordinate
import numpy as np

class SubArea(Area):
        def __init__(self,listArea):
            self.__listArea=listArea
            self.__res=0
            self.__listElements=[]
            super().__init__([])
        
        def getListArea(self):
            return self.__listArea
        
        def addArea(self,area):
            if area not in self.__listArea:
                self.__listArea.append(area)
                self.computeSurface(area)
        
        def computeSurface(self,area):
            self.__res+=area.getSurface()
        
        def getSurface(self):
            return self.__res
        
        def getListElements(self):
            return self.__listElements
        
        def addElement(self,element):
            if element not in self.getListElements():
                self.__listElements.append(element)

        def getPoints(self):
            points = []
            for element in self.__listElements:
                coord1, coord2 = element.getCoordinates()[0], element.getCoordinates()[1]
                x1, y1, x2, y2 = coord1.getx(), coord1.gety(), coord2.getx(), coord2.gety()
                if [x1, y1] not in points:
                    points.append([x1, y1])
                if [x2, y2] not in points:
                    points.append([x2, y2])
            return np.array(points)


