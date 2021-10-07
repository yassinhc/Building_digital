# -*- coding: utf-8 -*-

import unittest

import sys
sys.path.append('..')


import src.Element as Element


class Test_Element(unittest.TestCase):
    
    def test_Coordinate(self):
        element  = Element.Element(0, 0, 10, 0)
        coordinates = element.getCoordinate()
        
        self.assertTrue(coordinates == ((0, 0), (10, 0)))
        
        
    def test_length(self):
        element  = Element.Element(0, 0, 10, 0)
        length = element.getLength()
        self.assertEqual(length, 10)
        
        
        
        
if __name__ == '__main__':
    unittest.main()

