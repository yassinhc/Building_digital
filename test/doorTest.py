

import unittest

import sys
sys.path.append('..')


import src.door as door
import src.coordinate as Coordinate

from test.elementTest import ElementTest


class Test_Door(ElementTest,unittest.TestCase):
    
    
    def createElement(self):        
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)        
        element = door.Door((c1,c2))
        return element
        
    
    def test_getLength(self):
        length = self.element.getLength()
        self.assertEqual(length, 10)
        
        
        
        
if __name__ == '__main__':
    unittest.main()