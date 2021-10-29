
import matplotlib.pyplot as plt

import sys
sys.path.append('..') 


import src.Building as Building 
import src.Wall as Wall
import src.window as Window
import src.door as Door
import src.coordinate as Coordinate

def generate_wall(coord_wall, coord_door = None, coord_window = None):
    # TODO : This class is only used ofr test
    """Creates a wall from 2 points defined by 4 given coordinates


    Parameters
    ----------
    coord_wall : list of coordinates [x1, y1, x2, y2]
        * x1, y1 : coordinates of the first point that defines the wall
        * x2, y2 : coordinates of the second point that defines the wall

    coord_door : list of coordinates of a window on the wall 
        * default : None

    coord_door : list of coordinates of a door on the wall 
        * default : None

    Returns
    -------
    Wall Object
    """
    coordinate_1 = Coordinate.Coordinate(coord_wall[0], coord_wall[1])
    coordinate_2 = Coordinate.Coordinate(coord_wall[2], coord_wall[3])
    wall = Wall.Wall([coordinate_1, coordinate_2])

    # adding windows 
    if coord_door : 
        wall = generate_window
    return wall


def generate_window(wall, coord_window):
    # TODO :This class is only used for test
    """Creates a window of wall based in passed cooridates of the window (coord_window)

    Parameters
    ----------
    wall : 
        Wall Object
    coord_window : 
        list of coordinates [x1, y1, x2, y2]

    Returns
    -------
    Wall Object :
        wall containing windows

    """
    coordinate_1 = Coordinate.Coordinate(coord_window[0], coord_window[1])
    coordinate_2 = Coordinate.Coordinate(coord_window[2], coord_window[3])
    window = Window.Window([coordinate_1, coordinate_2])
    wall.addWindow(window)
    return wall

def generate_door(wall, coord_door):
    # TODO :This class is only used for test
    """Creates a window of wall based in passed cooridates of the window (coord_window)

    Parameters
    ----------
    wall : 
        Wall Object
    coord_window : 
        list of coordinates [x1, y1, x2, y2]

    Returns
    -------
    Wall Object :
        wall containing windows

    """
    coordinate_1 = Coordinate.Coordinate(coord_door[0], coord_door[1])
    coordinate_2 = Coordinate.Coordinate(coord_door[2], coord_door[3])
    door = Door.Door([coordinate_1, coordinate_2])
    wall.addDoor(door)
    return wall

    
def draw_element(wall, color):
    """Plot a wall on a 2D plan, with doors and windows

    Parameters
    ----------
    wall : 
        Wall Object
        
    Returns
    -------
    wall_plot : 
        Line2D instance
    """
    p0 = (wall.getCoordinates()[0].getx(), wall.getCoordinates()[0].gety())
    p1 = (wall.getCoordinates()[1].getx(), wall.getCoordinates()[1].gety())
    x0, x1 = p0[0], p1[0]
    y0, y1 = p0[1], p1[1]
    print((x0, x1), (y0, y1))
    wall_plot = plt.Line2D((x0, x1), (y0, y1), lw=1.5, c = color)
    return wall_plot

def draw_line(coordinates):
    pass




b = Building.Building([])


# generating walls 
wall1 = generate_wall([1, 2, 5, 2])
wall2 = generate_wall([5, 5, 1, 5])


b.addElement(wall1)
b.addElement(wall2)

plt.figure(figsize=(7,7))

for wall in b.getListElement():
   plt.gca().add_line(draw_element(wall,'r' ))


plt.axis('scaled')
plt.show()