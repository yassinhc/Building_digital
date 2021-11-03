from abc import ABC,abstractmethod


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:05:45 2021

@author: user
"""

import unittest
#list of elements
import src.door as door
import src.window as window
import src.Wall as Wall
#coordinates of elements
import src.coordinate as Coordinate
#test of elements
from elementTest import ElementTest
import sys
sys.path.append('..')


import src.Area as Area


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