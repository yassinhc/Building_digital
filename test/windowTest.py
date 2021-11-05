

import unittest

import sys
sys.path.append('..')


import src.window as window
import src.coordinate as Coordinate

from test.elementTest import ElementTest


class Test_Wall(ElementTest,unittest.TestCase):
    
    
    def createElement(self):        
        c1 = Coordinate.Coordinate(1,2)
        c2 = Coordinate.Coordinate(-3,-1)        
        element = window.Window((c1,c2))
        return element
        
    
    def test_length(self):
        
        length = self.element.getLength()
        self.assertEqual(length, 5)
        
        
        
        
if __name__ == '__main__':
    unittest.main()