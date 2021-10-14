from math import sqrt

class Coordinate():
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getLength(self,coordinate):
        X=coordinate.getx()-self.getx()
        Y=coordinate.gety()-self.gety()
        return sqrt(X**2+Y**2)
