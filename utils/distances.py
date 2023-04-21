from unsupervised.k_means import KMeans
from unsupervised.k_mediodes import KMedoids
import numpy as np


def calculate_distances(X):
    centroids = KMeans(n_clusters=5).fit(X)
    distances = KMeans.pairwise_distances(centroids, centroids)
    n_rows, n_cols = distances.shape
    distances_cluster = []
    for i in range(n_rows):
        for j in range(i + 1, n_cols):
            distances_cluster.append(
                {"Distance between cluster #" + str(i + 1) + " and cluster #" + str(j + 1): round(distances[i, j], 3)})
    return distances_cluster