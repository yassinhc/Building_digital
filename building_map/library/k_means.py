import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from scipy.interpolate import make_interp_spline, BSpline



import building_map.library.convex_hull as convex_hull



# X : the input should be a number of points  (the path of visitors in the building)
# TODO : We assume X is a numpy array containing points in 2D 


def initializing_centroids(X, nb_centroids):
    """Initializes centroids by randomly picking 'nb_centroids' of points for X 

    Parameters
    ----------
    X : list of points
        visited spots in the building 
    nb_centroids : int
        number of clusters

    Returns
    -------
    nb_centroids_ number of points 
        initial centroids of the K_mean
    """
    index_centroids = random.sample(range(0, X.shape[0]), nb_centroids)    # random indexes of centroids 
    centroids = []
    for i in index_centroids:
        centroids.append(X[i])
    return np.array(centroids)



def compute_distance(x1, x2):
    """computes the distance between 2 vectors/points

    Parameters
    ----------
    x1 : point/vector 1
    x2 : point/vector 2

    Returns
    -------
    float
        distance between x1 and x2
    """
    return (np.sum((x1-x2)**2))**0.5


def closest_centroids(centroids, X):
    """ Assigns a centroid to each point(vector) in X

    Parameters
    ----------
    centroids : numpy array of 2D
        array of centroids
    X : numpy array of 2D 
        input list of points 

    Returns
    -------
    numpy array
        indexes of the closest centroid to each point (vector) in X
    """
    nb_centroids = centroids.shape[0]
    X_size = X.shape[0]

    assigned_centroids = np.zeros(shape = X_size)
    for i in range(X_size):
        distance = []   #  a row vector
        for j in range(nb_centroids):
            distance.append(compute_distance(X[i], centroids[j]))
        assigned_centroids[i] = np.argmin(distance)

    return assigned_centroids


def reinit_centroids(clusters, k, X):
    """ Reinitialising centroids by computing the average of points with respect to each centroid 
        and move the centroid to that average

    Parameters
    ----------
    clusters : numpy array 2D
        assigned cluster for each point in X
    k : int
        number of clusters
    X : numpy array of 2D 
        array of points

    Returns
    -------
    numpy array of 2D
        new centroids 
    """
    new_centroids = np.zeros(shape = (k, 2))  
    for j in range(k):
        current_cluster = np.array([X[i] for i in range(X.shape[0]) if clusters[i] == j])      # points belonging to the j-th cluster
        cluster_mean = np.mean(current_cluster, axis = 0)                                      # computing the mean point of the cluster's points
        new_centroids[j] = cluster_mean
    return new_centroids



def plot_clusters(X, k, iter): 
    """ Clusters points in X into k clusters using iter-nb of iterations and plots the clusters  

    Parameters
    ----------
    X : numpy array of 2D
        array of points 
    k : int 
        number of clusters
    iter : int
        number of iterations

    Returns
    -------
    dict
        final clusters : points belonging to each cluster
    """
    init_cent = initializing_centroids(X, k)                             # initializing centroids
    clos_cent = closest_centroids(init_cent, X)                          # closest centroids ot each point

    for i in range(iter):
        clos_cent = closest_centroids(init_cent, X)                      # updating closest centroids 
        init_cent = reinit_centroids(clos_cent, k, X)                    # updating centroids 

    # ------ plotting ------
    color = plt.cm.rainbow(np.linspace(0, 1, k)) 

    pt_classes = dict()                                                  # dictinary of points fitting into each cluster 

    for j in range(k):
        pt_classes[j] = np.array([X[i] for i in range(X.shape[0]) if clos_cent[i]==j])

    
    for j, c in zip(range(k), color):
        #pt_classes[j] = np.array([X[i] for i in range(X.shape[0]) if clos_cent[i]==j])
        rate = round(pt_classes[j].shape[0]/X.shape[0], 2)
        plt.scatter(pt_classes[j][:, 0], pt_classes[j][:, 1], color = c, marker = '.', alpha=0.3)
        
        c_hull = np.array(convex_hull.convex_hull(pt_classes[j]))

        plt.plot(c_hull[:, 0], c_hull[:, 1], color = c, marker = ',', label = 'rate of visits : '+str(rate))      # draw convex hull


