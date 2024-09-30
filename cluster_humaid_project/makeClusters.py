# 2021-2022 Programação II
# Grupo 114
# 58607 José Medeiros
# 58559 Madalena Machado

import random
from Cluster import Cluster
from Centroidex import Centroidex

def kmeans(helpers,centroids,k, verbose):
    """
    K-means clustering
    Requires:
    helpers a list of helpers of a same type;
    centroids a list of centroids of a same type;
    verbose Boolean, printing details on/off
    Ensures:
    list containing k clusters, k representing the numbers of centroids;
    if verbose is True, result of each iteration
    of k-means is printed
    """
    if len(centroids) == 0:
        initialCentroids = random.sample(helpers, k)
    else:
        if k != len(centroids):
            raise Centroidex(centroids, k)
        initialCentroids = centroids

    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    # Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:

        numIterations += 1

        # Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        # Associate each example with closest centroid
        for e in helpers:
            # Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            # Add e to the list of helpers for the appropriate cluster
            newClusters[index].append(e)

        # Avoid having empty clusters
        for c in newClusters:
            if len(c) == 0:
                raise ValueError("Empty Cluster")

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

        # Trace intermediate levels of clustering if verbose on
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print(dissimilarity(clusters))  # add blank line

    return clusters

def dissimilarity(clusters):
    """
    Dissimilarity among clusters
    Ensures:
    dissimilarity among clusters as the summation
    of each cluster variance
    """
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist


def trykmeans(helpers,centroids,numClusters, numTrials,
              verbose=False):
    """
    Best clustering outcome within a given number of trials
    of k-means clustering
    Requires:
    examples a list of examples of a same type;
    numClusters positive int, number of clusters;
    numTrials positive int, number of trials with k-means clustering
    Ensures:
    The clusters obtained with the lowest dissimilarity among them
    after running k-means clustering numTrials times over examples
    """
    best = kmeans(helpers,centroids,numClusters, verbose)
    minDissimilarity = dissimilarity(best)

    for trial in range(1, numTrials):
        clusters = kmeans(helpers,centroids,numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity

    return best

