import sys

sys.path.append('..')


from src.Element import Element

class Window(Element):
        """
        A class to represent a window.
        ...
        Attributes
        ----------
        coordinates : tuple of coordinates as (z1,z2) where z1=(x1,y1) and z2=(x2,y2)
        
        Methods
        -------
        getCoordinates():
                Get the coordinates of the window.
        getLenght():
                Return the lenght between the two coordinates designing the window.
    
        """
        pass