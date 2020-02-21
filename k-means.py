from math import sqrt
from random import randint
import matplotlib.pyplot as plt


class Point(object):
    """Creates the a Point object to be used in the k-means calculations"""

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __str__(self):
        str = "X- {:.5f}, Y- {:.5f}".format(self.X, self.Y)
        return str


# Points from ARIN lecture 2 example
# a0 = Point(1.0, 1.0)
# a1 = Point(1.0, 0.0)
# a2 = Point(0.0, 2.0)
# a3 = Point(2.0, 4.0)
# a4 = Point(3.0, 5.0)
# pointLst = [a0, a1, a2, a3, a4]


def get_points(n=100, min_val=0, max_val=10000):
    """Generates random points to be used to calculate the k-means clusters

    :param n: Number of points to generate
    :param min_val: Min value that the point can take
    :param max_val: Max value that the point can take
    """
    point_list = []
    for i in range(n):
        point_list.append(Point(randint(min_val, max_val), randint(min_val, max_val)))
    return point_list




def distance(p1, p2):
    """Return the euclidean distance between two point objects

    :param p1 : A Point object
    :param p2 : A Point object
    """
    s1 = (p1.X - p2.X) ** 2
    s2 = (p1.Y - p2.Y) ** 2
    return sqrt(s1 + s2)


def is_equal(p1, p2):
    """Checks to see if two points are equal to each other

    :param p1 : A Point Object
    :param p2 : A Point Object
    """
    return True if(p1.X == p2.X and p1.Y == p2.Y) else False


def average_point(points):
    """Calculates the average of a list of Points

    :param points : List of Points to calculate an average of

    """
    numOfPoints = len(points)
    sumX = 0.0
    sumY = 0.0

    for point in points:
        sumX += point.X
        sumY += point.Y

    return Point(sumX/numOfPoints, sumY/numOfPoints)


def k_means(k, points, iterations=10):
    """Runs the K-means iteration method

    Currently Supports up to k of 6 due to colour limitation
    when displaying graph.

    :param k : The number of means to be used
    :param points : List of Points to calculate k-means of
    :param iterations : Max Number of iterations to run before plotting graph
    """
    means = []

    # Randomly chooses
    startPoints = points
    for i in range(k):
        means.append(startPoints.pop(randint(0, len(startPoints)-1)))

    # means = [points[0], points[2]]

    for j in range(iterations):
        clusters = []

        for i in range(k):
            clusters.append([])

        for point in points:
            # Calculates distance from each of the means
            distances = [distance(point, mean) for mean in means]
            # Adds point to clustered_points of which ever mean point is closest
            index = distances.index(min(distances))
            clusters[index].append(point)

        for n in range(len(clusters)):
            means[n] = average_point(clusters[n])

    return means, clusters


pointList = get_points()
finalMeans, clustered_points = (k_means(3, pointList))
print("FINAL: ")

plt.title("Means")
c = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for key, val in enumerate(clustered_points):

    for clu in val:
        plt.scatter(clu.X, clu.Y, color=c[key])

for key, f in enumerate(finalMeans):
    plt.scatter(f.X, f.Y, color=c[key], marker='x')
    print("Mean: ", key, " Point: ", f)

plt.show()
