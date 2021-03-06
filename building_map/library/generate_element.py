import sys
sys.path.append('..') 

import src.coordinate as Coordinate
import src.Wall as Wall
import src.window as Window
import src.door as Door



def generate_wall(coord_wall):
    # TODO : This class is only used ofr test
    """Creates a wall from 2 points defined by 4 given coordinates


    Parameters
    ----------
    coord_wall : list of coordinates [x1, y1, x2, y2]
        * x1, y1 : coordinates of the first point that defines the wall
        * x2, y2 : coordinates of the second point that defines the wall

    Returns
    -------
    Wall Object
    """
    coordinate_1 = Coordinate.Coordinate(coord_wall[0], coord_wall[1])
    coordinate_2 = Coordinate.Coordinate(coord_wall[2], coord_wall[3])
    wall = Wall.Wall([coordinate_1, coordinate_2])

    return wall


def generate_window(wall, coord_window):
    # TODO :This class is only used for test
    """Creates a window on wall based in passed coordinates of the window (coord_window)

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
    """Creates a window on wall based in passed coordinates of the door (coord_door)

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