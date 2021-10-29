# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:04:20 2021

@author: user
"""

from Area import Area

class SubArea(Area):
        def __init__(self,listArea):
            self.__listArea=listArea
            self.__res=self.
            super().__init__()
        
        def getListArea(self):
            return self.__listArea
        
        def addArea(self,area):
            if area not in self.__listArea:
                self.__listArea.append(area)
        
        def getSurface(self):
            return self.__res
        
        def calculateArea(self):
            for area in self.__listArea:
                