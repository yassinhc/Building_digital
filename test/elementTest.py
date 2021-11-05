from abc import ABC,abstractmethod


import unittest

import sys
sys.path.append('..')


import src.Element as Element


class ElementTest(ABC):
    
    
    def setUp(self):
        self.element=self.createElement()
        
    @abstractmethod
    def createElement(self):
        pass
    
    def test_Coordinate(self):
        coordinates = self.element.getCoordinates()        
        self.assertTrue(len(coordinates)==2)
        
        
        
        
        
#if __name__ == '__main__':
 #   unittest.main()