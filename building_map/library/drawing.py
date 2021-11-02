
import matplotlib.pyplot as plt
import library.generate_element as generate_element


import sys
sys.path.append('..') 


import src.Building as Building 


    
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
    #print((x0, x1), (y0, y1))
    element_plot = plt.Line2D((x0, x1), (y0, y1), lw=linewidth, c = color, marker=marker, 
                                markeredgewidth = 0.3, markeredgecolor=color, label = label)
    return element_plot



def draw_building(building):
    """Plots the building on the basis of its list of elements 

    Parameters
    ----------
    building : 
        Building Object

    """
    plt.figure(figsize=(7,7))
    if building.getLenElement():
        for wall in building.getListElement():
            plt.gca().add_line(draw_element(wall,'grey'))
            if len(wall.getListWindow()):
                for window in wall.getListWindow():
                    plt.gca().add_line(draw_element(window,'deepskyblue', marker = '$\u27E1$', linewidth = 2.5, label="window"))
            if len(wall.getListDoor()):
                for door in wall.getListDoor():
                    plt.gca().add_line(draw_element(door,'darkred', marker = '$\u27E1$' , linewidth =2.5))
    plt.axis('scaled')
    #plt.show()
            