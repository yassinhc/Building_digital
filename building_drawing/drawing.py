
import matplotlib.pyplot as plt
import sys
sys.path.append('..') 
import src.Building as Building 


def draw_wall(p0, p1):
    x0, x1 = p0[0], p1[0]
    y0, y1 = p0[1], p1[1]
    print((x0, x1), (y0, y1))
    wall = plt.Line2D((x0, x1), (y0, y1), lw=1.5, c = 'r')
    return wall

def draw_window(p0, p1):
    x0, x1 = p0[0], p1[0]
    y0, y1 = p0[1], p1[1]
    pass
    #wall = plt.Line2D((x0, x1), (y0, y1), lw=2, c = 'blue')
    #return wall






b = Building.Building([])
b.addElement(1, 2, 2, 7)
plt.figure


for element in b.getElements():
   p0 = element.getCoordinate()[0].getCoordinate()
   p1 = element.getCoordinate()[1].getCoordinate()
   plt.gca().add_line(draw_wall(p0, p1))


plt.axis('scaled')
plt.show()