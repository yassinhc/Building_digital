import unittest
import numpy as np
 
import sys
sys.path.append('..') 

import library.k_means as k_means


class Test_K_Means(unittest.TestCase):

    def test_valid_centroids(self):
        """ - Asserts the number of generated centroids by initializing_centroids() function
         is the nb of the given number of clusters
            - Asserts the centroids are actually picked from the list of the given points 
        """

        low = [1, 1]
        high = [10, 10]
        nb_samples = 100
        X0 = np.random.default_rng().uniform(low, high, size = (nb_samples, 2))   # generating a random array of points 

        k = 3                        # number of clusters

        centroids = k_means.initializing_centroids(X0, k)                         # picked centroids 
        self.assertTrue(centroids.shape[0] == k)
        for i in range(k):
            self.assertTrue(centroids[i] in X0)


    def test_distance(self):
        """ Asserts the right distance between 2 given vectors is returned 
        """
        
        point1 = np.array([3, 1])    # 1st point
        point2 = np.array([6, 5])    # 2nd point

        distance = k_means.compute_distance(point1, point2)                       # distance between point1 and point2

        self.assertTrue(distance == 5)


    def test_valid_clusters(self):
        """ Asserts the assigned clusters are valid (in the range of [0, nb_clusters])
        """
        low = [1, 1]
        high = [10, 10]
        nb_samples = 100
        X0 = np.random.default_rng().uniform(low, high, size = (nb_samples, 2))   # generating a random array of points 

        k = 3                        # number of clusters
        centroids = k_means.initializing_centroids(X0, k)                         # picked centroids 
        iter = 10                    # number of iterations

        clusters = k_means.closest_centroids(centroids, X0)                  # set of assigned clusters 

        classes = set(i for i in range(k))             # possible clusters

        self.assertTrue(set(clusters).issubset(classes))   





if __name__ == "__main__":
    unittest.main()
