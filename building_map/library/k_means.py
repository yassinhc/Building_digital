import random
import numpy as np
import matplotlib.pyplot as plt

#X : the input should be a number of points  (the path of visitors in the building)
# TODO : We assume data is a numpy array containing points in 2D 


def initializing_centroids(data, nb_centroids):
    """Initializes nb_centroids-Centroids from the input data 

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
    new_centroids = np.zeros(shape = (k, 2))  
    for j in range(k):
        current_cluster = np.array([X[i] for i in range(X.shape[0]) if clusters[0][i] == j])
        cluster_mean = np.mean(current_cluster, axis = 0)
        new_centroids[j] = cluster_mean
    return new_centroids


if __name__ == "__main__":
    import random
    import numpy as np
    import matplotlib.pyplot as plt 

    # generating a random numpy array
    X= -2 * np.random.rand(150,2)
    X1 = 1 + 2 * np.random.rand(50,2)
    X2 = 3 + 2*np.random.rand(50,2)
    X[50:100, :] = X1
    X[100:150, :] = X2
    #plt.scatter(X[:, 0], X[:, 1])
    #plt.show()

    k = 3

    init_cent = initializing_centroids(X,k )
    print(init_cent)

    #clos_cent = closest_centroids(init_cent, X)
    #print(clos_cent)

    N = 4
    for i in range(N):
        clos_cent = closest_centroids(init_cent, X)
        init_cent = reinit_centroids(clos_cent, k, X)
    




    pt_class1 = np.array([X[i] for i in range(X.shape[0]) if clos_cent[0][i]==0])
    pt_class2 = np.array([X[i] for i in range(X.shape[0]) if clos_cent[0][i]==1])
    pt_class3 = np.array([X[i] for i in range(X.shape[0]) if clos_cent[0][i]==2])

    # plotting clusters 
    plt.scatter(pt_class1[:, 0],pt_class1[:, 1], color = 'red')
    plt.scatter(pt_class2[:, 0],pt_class2[:, 1], color = 'green')
    plt.scatter(pt_class3[:, 0],pt_class3[:, 1], color = 'yellow')

    plt.scatter(init_cent[:, 0], init_cent[:, 1], color = 'black')

    plt.show()
