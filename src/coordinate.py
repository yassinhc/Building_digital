class Coordinate:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def getCoordinate(self):
        return (self.__x, self.__y)

    # def getY(self):
    #     return self.y