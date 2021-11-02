
if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import library.generate_element as generate_element
	import library.drawing as drawing
	import numpy as np
	import library.convex_hull as convex_hull
	

	import sys
	sys.path.append('..') 

	import src.Building as Building 

	# creating a building 
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

	# drawing the building 
	drawing.draw_building(b)

	# testing convex hull of some points 
	# a visitor is within a certain area defined by some points in the space if and only if : 
	# the convex_hull (points without the visitor) == convex_hull (points with the visitor)
	
	number_points = 7
	points = np.random.randint(1, 11, size = (number_points, 2))
	cv_hull = np.array(convex_hull.convex_hull(points))


	# choose a random position of a visitor 
	visitor = np.random.randint(1, 11, size = (1,2 ))[0]

	# the visitor is marked as a red dot on the plot 
	plt.plot(visitor[0], visitor[1], 'r*', markeredgewidth = 5 )

	# plotting convex hull 
	plt.plot(cv_hull[:, 0], cv_hull[:, 1], 'y:')
	plt.scatter(cv_hull[:, 0], cv_hull[:, 1], color = 'orange')
	
	plt.grid(linewidth=0.1)
	plt.legend()
	plt.show()



