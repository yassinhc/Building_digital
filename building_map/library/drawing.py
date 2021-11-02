
import matplotlib.pyplot as plt
import library.generate_element as generate_element


import sys
sys.path.append('..') 


import src.Building as Building 


    
def draw_element(element, color, marker = '', linewidth = 1 ):
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
                                markeredgewidth = 0.3, markeredgecolor=color)
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
                    plt.gca().add_line(draw_element(window,'deepskyblue', marker = '$\u27E1$', linewidth = 2.5))
            if len(wall.getListDoor()):
                for door in wall.getListDoor():
                    plt.gca().add_line(draw_element(door,'darkred', marker = '$\u27E1$' , linewidth =2.5))
    plt.axis('scaled')
    plt.show()
            



if __name__ == "__main__":
    
    b = Building.Building([])


    # generating walls 
    wall1 = generate_element.generate_wall([1, 1, 11, 1])
    wall2 = generate_element.generate_wall([11, 1, 11, 11])
    wall3 = generate_element.generate_wall([11, 11, 1, 11])
    wall4 = generate_element.generate_wall([1, 11, 1, 1])

    wall5 = generate_element.generate_wall([1, 7, 4, 7])
    wall6 = generate_element.generate_wall([4, 7, 4, 1])
    wall7 = generate_element.generate_wall([7, 1, 7, 7])
    wall8 = generate_element.generate_wall([7, 7, 11, 7])

    wall9 = generate_element.generate_wall([1, 8, 4, 8])
    wall10 = generate_element.generate_wall([4, 8, 4, 11])
    wall11 = generate_element.generate_wall([7, 8, 7, 11])
    wall12 = generate_element.generate_wall([7, 8, 11, 8])

    wall13 = generate_element.generate_wall([1, 4, 4, 4])
    wall14 = generate_element.generate_wall([7, 4, 11, 4])




    # adding walls to the building
    b.addElement(wall1)
    b.addElement(wall2)
    b.addElement(wall3)
    b.addElement(wall4)

    b.addElement(wall5)
    b.addElement(wall6)
    b.addElement(wall7)
    b.addElement(wall8)

    b.addElement(wall9)
    b.addElement(wall10)
    b.addElement(wall11)
    b.addElement(wall12)

    b.addElement(wall13)
    b.addElement(wall14)

    # generating windows
    window1 = generate_element.generate_window(wall4, [1, 2, 1, 3])
    window2 = generate_element.generate_window(wall4, [1, 5, 1, 6])

    window3 = generate_element.generate_window(wall3, [2, 11, 3, 11])
    window4 = generate_element.generate_window(wall3, [8, 11, 9, 11])

    window5 = generate_element.generate_window(wall2, [11, 2, 11, 3])
    window6 = generate_element.generate_window(wall2, [11, 5, 11, 6])

    #generating doors
    door1 = generate_element.generate_door(wall1, [4.5, 1, 6.5, 1])
    door2 = generate_element.generate_door(wall6, [4, 2, 4, 3])
    door3 = generate_element.generate_door(wall6, [4, 5, 4, 6])

    door4 = generate_element.generate_door(wall7, [7, 2, 7, 3])
    door5 = generate_element.generate_door(wall7, [7, 5, 7, 6])

    door6 = generate_element.generate_door(wall11, [7, 9, 7, 10])
    door7 = generate_element.generate_door(wall10, [4, 9, 4, 10])

    door8 = generate_element.generate_door(wall12, [8, 8, 9, 8])
    door9 = generate_element.generate_door(wall9, [2, 8, 3, 8])


    #door2 = generate_element.generate_door(wall2, [2, 5, 3, 5])


    draw_building(b)