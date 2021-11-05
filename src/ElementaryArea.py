# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:58:34 2021

@author: user
"""
from abc import ABC

from src.Area import Area

class ElementaryArea(Area,ABC):
    """
    A class to represent an ElementaryArea(it'a a real area like room or patio).
    ...
    
    Attributes
    ----------
    listWall : list of Walls
        The list of walls disigning the elementaryarea
    
    Methods
    -------
    getListElement():
        Return the list of elements designing the elementaryarea.
    getSurface():
        Return the surface of the elementaryarea
    """
    pass