
if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import library.generate_element as generate_element
	import library.drawing as drawing
	import numpy as np
	import library.convex_hull as convex_hull
	

	import sys
	sys.path.append('..') 

	import src.Building as Building
	import src.Floor as Floor
	import src.SubArea as SubArea

	# creating a building and a floor 
	floor = Floor.Floor([])
	building = Building.Building([])
	building.addFloor(floor)

	# -------------------------------------------------------------------------------------------------------
	# 			Creating a building of one floor containing some elememnts (walls, doors, windows)
	# -------------------------------------------------------------------------------------------------------



	# 	------- generating walls : we use generate_element module to simply the creation of elements -------- 
	# outer walls of the floor
	wall1 = generate_element.generate_wall([0, 0, 12, 0])
	wall2 = generate_element.generate_wall([12, 0, 12, 12])
	wall3 = generate_element.generate_wall([12, 12, 0, 12])
	wall4 = generate_element.generate_wall([0, 12, 0, 0])
	
	# walls of the rooms in the bottom left
	wall5 = generate_element.generate_wall([0, 7, 4, 7])
	wall6 = generate_element.generate_wall([4, 7, 4, 0])
	wall13 = generate_element.generate_wall([0, 4, 4, 4])

	# walls of the rooms in the bottom right
	wall7 = generate_element.generate_wall([7, 0, 7, 7])
	wall8 = generate_element.generate_wall([7, 7, 12, 7])
	wall14 = generate_element.generate_wall([7, 4, 12, 4])
	
	# walls of the rooms in the top left
	wall9 = generate_element.generate_wall([0, 8, 4, 8])
	wall10 = generate_element.generate_wall([4, 8, 4, 12])

	# walls of the rooms in the top right
	wall11 = generate_element.generate_wall([7, 8, 7, 12])
	wall12 = generate_element.generate_wall([7, 8, 12, 8])
	

	
	#  --- adding walls to the building ---
	floor.addElement(wall1)
	floor.addElement(wall2)
	floor.addElement(wall3)
	floor.addElement(wall4)
	
	floor.addElement(wall5)
	floor.addElement(wall6)
	floor.addElement(wall7)
	floor.addElement(wall8)
	
	floor.addElement(wall9)
	floor.addElement(wall10)
	floor.addElement(wall11)
	floor.addElement(wall12)
	
	floor.addElement(wall13)
	floor.addElement(wall14)



    # -------- generating windows --------
	window1 = generate_element.generate_window(wall4, [0, 2, 0, 3])
	window2 = generate_element.generate_window(wall4, [0, 5, 0, 6])
	
	window3 = generate_element.generate_window(wall3, [2, 12, 3, 12])
	window4 = generate_element.generate_window(wall3, [8, 12, 9, 12])
	
	window5 = generate_element.generate_window(wall2, [12, 2, 12, 3])
	window6 = generate_element.generate_window(wall2, [12, 5, 12, 6])
	
	

	# -------- generating doors --------
	door1 = generate_element.generate_door(wall1, [4.5, 0, 6.5, 0])
	door2 = generate_element.generate_door(wall6, [4, 2, 4, 3])
	door3 = generate_element.generate_door(wall6, [4, 5, 4, 6])
	
	door4 = generate_element.generate_door(wall7, [7, 2, 7, 3])
	door5 = generate_element.generate_door(wall7, [7, 5, 7, 6])
	
	door6 = generate_element.generate_door(wall11, [7, 9, 7, 10])
	door7 = generate_element.generate_door(wall10, [4, 9, 4, 10])
	
	door8 = generate_element.generate_door(wall12, [8, 8, 9, 8])
	door9 = generate_element.generate_door(wall9, [2, 8, 3, 8])


	#  ---- drawing the building ----- 
	drawing.draw_floor(floor)




	# ------------------------------------------------------------------------------------------------------
	# 				Asserting if a visitor is within some subArea (defined by some walls)
	# ------------------------------------------------------------------------------------------------------


	# ------ creating subArea ------
	sub_area = SubArea.SubArea([])


	# -------- list of elements(walls) for subArea --------
	wall_sub1 = generate_element.generate_wall([2, 7, 8, 1])
	wall_sub2 = generate_element.generate_wall([1, 5, 6, 4])
	wall_sub3 = generate_element.generate_wall([10, 6, 9, 3])


	# ------ Adding Elements to subArea ------
	sub_area.addElement(wall_sub1)
	sub_area.addElement(wall_sub2)
	sub_area.addElement(wall_sub3)
	

	# ---- get cloud of points defining subArea ----
	points = sub_area.getPoints()



	#  ---------------- testing convex hull of some points ----------------
	# a visitor is within a certain area defined by some points in the space if and only if : 
	# the convex_hull (points without the visitor) == convex_hull (points with the visitor)
	cv_hull = np.array(convex_hull.convex_hull(points))


	# ----- choose a random position for a visitor -----
	visitor = np.random.randint(0, 13, size = (1,2 ))[0]


	#  ----- plot position of the visitor ----- 
	plt.plot(visitor[0], visitor[1], 'r*', markeredgewidth = 5 )          # visitor == red dot on the 2D plan

	
	# --------- testing  if the visitor is within the given subArea ----- 
	points_with_visitor = np.append(points, [visitor], axis = 0)          # new cloud of points = subArea points + visitor

	newcv_hull = np.array(convex_hull.convex_hull(points_with_visitor))	  # new convex_hull
	print(newcv_hull)
	print(cv_hull)
	print("The visitor is with the subArea? --> "+ str(newcv_hull.shape == cv_hull.shape 
				and (newcv_hull == cv_hull).all()))
	print(newcv_hull.shape == cv_hull.shape and (newcv_hull == cv_hull).all())



	# ------- plotting convex hull ------ 
	plt.plot(cv_hull[:, 0], cv_hull[:, 1], 'y:')
	plt.scatter(cv_hull[:, 0], cv_hull[:, 1], color = 'orange')
	

	plt.grid(linewidth=0.1)
	plt.show()
	



