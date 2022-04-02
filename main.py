# Michael Langdon
# Assignment 6 - Clustering

"""
The file urbanGB.txt contains 360177 lines.  Each line is of the form:
longitude, latitude
where longitude and latitude are given as floating point numbers.
Each of these points will begin in its own cluster.  First we'll merge the
clusters using the single-linkage method, where we compare the nearest neighbors in each
cluster.  Then we'll run the whole thing again using the complete-linkage method, that is,
comparing the most distant members. Finally, we'll use the average-linkage method.
"""

# list containing all the clusters
clusters = []


# Initialize clusters by starting with clusters of size 1.
def initialize_clusters():
    """
    Reads file urbanGB.txt and creates a tuple for each line, representing the
    longitude and latitude.  This tuple will be put into a list which represents
    a cluster.  At first, all tuples are in their own cluster (360177 in total).
    The clusters[] list will store all clusters, so each of these lists will be added
    to it.
    :return:
    """

    with open('../urbanGB.all/urbanGB.txt') as f:
        for line in f:
            print(line)


if __name__ == '__main__':
    initialize_clusters()

