from abc import ABC,abstractmethod


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:05:45 2021

@author: user
"""

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