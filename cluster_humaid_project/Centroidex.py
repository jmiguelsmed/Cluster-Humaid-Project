# 2021-2022 Programação II
# Grupo 114
# 58607 José Medeiros
# 58559 Madalena Machado
"""
Handles the exception to raise when centroids were specified in the helpers file, but the quantity is different that k
"""


class Centroidex(Exception):
    """
    If the number of specified centroids is not equal to k then this exception will be raised
    """

    def __init__(self, centroids, clusters):
        super().__init__(centroids, clusters)
        self.centroids = centroids
        self.clusters = clusters

    def __str__(self):
        return f'Mismatch Error: centroids [{len(self.centroids)}] does not equal number of clusters [{self.clusters}]. '