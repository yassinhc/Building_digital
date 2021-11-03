
import matplotlib.pyplot as plt
import library.generate_element as generate_element


import sys
sys.path.append('..') 


#import src.Floor as Floor 


    
def draw_element(element, color, marker = '', linewidth = 1 , label = ''):
    """Plots an element on a 2D plan, with doors and windows

    Parameters
    ----------
    wall : 
        Wall Object
        
    Returns
    -------
    wall_plot : 
        Line2D instance
    """
    p0 = (element.getCoordinates()[0].getx(), element.getCoordinates()[0].gety())
    p1 = (element.getCoordinates()[1].getx(), element.getCoordinates()[1].gety())
    x0, x1 = p0[0], p1[0]
    y0, y1 = p0[1], p1[1]

    element_plot = plt.Line2D((x0, x1), (y0, y1), lw=linewidth, c = color, marker=marker, 
                                markeredgewidth = 0.3, markeredgecolor=color, label = label)
    return element_plot



def draw_floor(floor):
    """Plots the floor on the basis of its list of elements 

    Parameters
    ----------
    floor : 
        floor Object

    """
    plt.figure(figsize=(7,7))
    if floor.getLenElement():
        for wall in floor.getListElement():                    # drawing walls
            plt.gca().add_line(draw_element(wall,'grey'))

            if len(wall.getListWindow()):                       # drawing windows
                for window in wall.getListWindow():
                    plt.gca().add_line(draw_element(window,'deepskyblue', marker = '$\u27E1$', linewidth = 2.5))

            if len(wall.getListDoor()):                         # drawing doors
                for door in wall.getListDoor():
                    plt.gca().add_line(draw_element(door,'darkred', marker = '$\u27E1$' , linewidth =2.5))
    plt.axis('scaled')
    
            