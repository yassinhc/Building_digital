

from src.Coordinate import Coordinate



class Element:

    def __init__(self, x1, y1, x2, y2):
        self.__coordinates = (Coordinate(x1, y1), Coordinate(x2, y2))
        
    def getCoordinate(self):
        return self.__coordinates
    
    def getLength(self):
        first_coord = self.getCoordinate()[0]
        second_coord = self.getCoordinate()[1]

        distance = ((first_coord[0] - second_coord[0])**2 + (first_coord[1] - second_coord[1])**2 )**0.5
        return distance



    
        