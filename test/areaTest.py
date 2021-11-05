from abc import ABC,abstractmethod


import unittest
#list of elements
#coordinates of elements
#test of elements
import sys
sys.path.append('..')




class AreaTest(ABC):
    
    
    def setUp(self):
        self.area=self.createArea()
        
    @abstractmethod
    def createArea(self):
        pass
    @abstractmethod
    def test_getSurface(self):
        pass
    @abstractmethod
    def test_getListWalls(self):
        pass

        
        
        
        
        
if __name__ == '__main__':
     unittest.main()