
if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import library.generate_element as generate_element
	import library.drawing as drawing
	import numpy as np
	import library.convex_hull as convex_hull
	import library.k_means as k_means
	

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



	while True : 
		# -------- choosing what to visualize --------
		print("  Pick one option:")
		print("			1: Assert a visitor is within a certain area?")
		print("			2: Heat-map of the floor?")
		print("			3: Exit")
		user_choice = input()


		# ------------------------------------------------------------------------------------------------------
		# 				Asserting if a visitor is within some subArea (defined by some walls)
		# ------------------------------------------------------------------------------------------------------

		if int(user_choice) == 1:
			#  ---------------- testing convex hull of some points ----------------
			# a visitor is within a certain area defined by some points in the space if and only if : 
			# the convex_hull (points without the visitor) == convex_hull (points with the visitor)
			cv_hull = np.array(convex_hull.convex_hull(points))


			# ----- choose a random position for a visitor -----
			visitor = np.random.randint(0, 13, size = (1,2 ))[0]


			# --------- testing  if the visitor is within the given subArea ----- 
			points_with_visitor = np.append(points, [visitor], axis = 0)          # new cloud of points = subArea points + visitor

			newcv_hull = np.array(convex_hull.convex_hull(points_with_visitor))	  # new convex_hull
			print("			The visitor is within the subArea? --> "+ str(newcv_hull.shape == cv_hull.shape 
						and (newcv_hull == cv_hull).all()))



			# -------------- drawings  -------------
			drawing.draw_floor(floor)                         # draw floor
			plt.plot(cv_hull[:, 0], cv_hull[:, 1], 'y:')      # draw convex hull
			plt.plot(visitor[0], visitor[1], 'r*', markeredgewidth = 5 )          # visitor's position == red dot on the 2D plan
			plt.scatter(cv_hull[:, 0], cv_hull[:, 1], color = 'orange')
			

			plt.grid(linewidth=0.1)
			plt.xlim([0, 12])
			plt.ylim([0, 12])
			plt.show()


		# ------------------------------------------------------------------------------------------------------
		# 		Drawing clusters of a given area (for the purpose of the example, the area is the whole floor) 
		# ------------------------------------------------------------------------------------------------------

		elif int(user_choice) ==2 : 

			# ----- params -----
			k = 3                   # number of clusters
			iter = 8                # number of iterattions
		

			# ----- random points generation : random visited locations by visitors -----
			# ------ FEEL FREE TO CHANGE !  ------
			nb_samples = 100
			
			
			low = [1, 1]
			high = [10, 10]
			X0 = np.random.default_rng().uniform(low, high, size = (nb_samples, 2))     # 1st list of points generated using uniform distribution 
			
			mean1 = [3, 3]
			cov1 = [[3, 0], [0, 3]]
			X1 = np.random.default_rng().multivariate_normal(mean1, cov1, nb_samples)   # 2nd list of points using multivariate_normal distribution
			
			mean2 = [7, 7]
			cov2 = [[1, 0], [0, 1]]
			X2 = np.random.default_rng().multivariate_normal(mean2, cov2, nb_samples)   # 3rd list of points using multivariate_normal distribution
			
			
			X = np.append(X0, X1, axis = 0)           # concatenating the  list of points
			X = np.append(X, X2, axis = 0)
			
			
			# ----- plotting -----
			drawing.draw_floor(floor) 
			k_means.plot_clusters (X, k, iter)        # computing and plotting the clusters of points 
		

			plt.xlim([-0.5, 12.5])
			plt.ylim([-0.5, 12.5])
			plt.show()



		elif int(user_choice) ==3:
			print("See you later ...")
			break
			
		else  :
			print("Please pick from the set of choices (1 or 2)!")
	



