from abc import ABC,abstractmethod


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:05:45 2021

@author: user
"""

import unittest

import sys
sys.path.append('..')


import src.Area as Area


class AreaTest(ABC):
    
    
    def setUp(self):
        self.area=self.createArea()
        
    @abstractmethod
    def createArea(self):
        pass
    
        
        
        
        
        
#if __name__ == '__main__':
 #   unittest.main()