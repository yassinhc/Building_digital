
import matplotlib.pyplot as plt
import generate_building

import sys
sys.path.append('..') 


import src.Building as Building 


    
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
wall1 = generate_building.generate_wall([1, 2, 5, 2])
wall2 = generate_building.generate_wall([5, 5, 1, 5])


b.addElement(wall1)
b.addElement(wall2)

# generating windows and doors 
window1 = generate_building.generate_window(wall1, [3, 2, 4, 2])
door2 = generate_building.generate_door(wall2, [2, 5, 3, 5])

plt.figure(figsize=(7,7))

for wall in b.getListElement():
    plt.gca().add_line(draw_element(wall,'lightgrey' ))
    if len(wall.getListWindow()):
        for window in wall.getListWindow():
            plt.gca().add_line(draw_element(window,'cyan' ))
    if len(wall.getListDoor()):
        for door in wall.getListDoor():
            plt.gca().add_line(draw_element(door,'darkred' ))
            
 


plt.axis('scaled')
plt.show()