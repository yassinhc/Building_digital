import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# X : the input should be a number of points  (the path of visitors in the building)
# TODO : We assume data is a numpy array containing points in 2D 


def initializing_centroids(data, nb_centroids):
    """Initializes centroids by randomly picking 'nb_centroids' of points for data 

    Parameters
    ----------
    data : list of points
        visited spots in the building 
    nb_centroids : int
        number of clusters

    Returns
    -------
    nb_centroids_ number of points 
        initial centroids of the K_mean
    """
    index_centroids = random.sample(range(0, data.shape[0]), nb_centroids)
    centroids = []
    for i in index_centroids:
        centroids.append(data[i])
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


def closest_centroids(cent, X):
    """assigns a centroid to each point(vector) in the data

    Parameters
    ----------
    cent : numpy array of 2D
        array of centroids
    X : numpy array of 2D 
        input data (set of vectors)

    Returns
    -------
    numpy array
        indexes of the closest centroid to each vector in the data
    """
    nb_cent = cent.shape[0]
    data_size = X.shape[0]

    assigned_centroids = np.zeros(shape = (1, data_size))
    for i in range(data_size):
        distance = []   #  a row vector
        for j in range(nb_cent):
            distance.append(compute_distance(X[i], cent[j]))
        assigned_centroids[0][i] = np.argmin(distance)

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
        current_cluster = np.array([X[i] for i in range(X.shape[0]) if clusters[0][i] == j])   # points belonging to the j-th cluster
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
    """
    init_cent = initializing_centroids(X, k)             # initializing centroids
    clos_cent = closest_centroids(init_cent, X)          # closest centroids ot each point

    for i in range(iter):
        clos_cent = closest_centroids(init_cent, X)      # updating closest centroids 
        init_cent = reinit_centroids(clos_cent, k, X)    # updating centroids 

    # ------ plotting ------
    color = plt.cm.rainbow(np.linspace(0, 1, k)) 

    pt_classes = dict()                                  # dictinary of points fitting into each cluster 

    for j, c in zip(range(k), color):
        pt_classes[j] = np.array([X[i] for i in range(X.shape[0]) if clos_cent[0][i]==j])
        plt.scatter(pt_classes[j][:, 0], pt_classes[j][:, 1], color = c, marker = '.')

    plt.scatter(init_cent[:, 0], init_cent[:, 1], color = 'black')  # plotting final centroids 



if __name__ == "__main__":
    import random
    import numpy as np
    import matplotlib.pyplot as plt 

    # ----- params -----
    k = 3                   # number of clusters 
    iter = 8                # number of iterattions
    

    # ----- random points generation ----- 
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
    plot_clusters(X, k, iter)                 # computing and plotting the clusters of points 

    plt.show()
