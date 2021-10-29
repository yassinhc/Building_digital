# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:04:20 2021

@author: user
"""

from src.Area import Area

class SubArea(Area):
        def __init__(self,listArea):
            self.__listArea=listArea
            self.__res=0
            super().__init__([])
        
        def getListArea(self):
            return self.__listArea
        
        def addArea(self,area):
            if area not in self.__listArea:
                self.__listArea.append(area)
                self.computeSurface(area)
        
        def computeSurface(self,area):
            self.__res+=area.getSurface()
        
        def getSurface(self):
            return self.__res
        
                