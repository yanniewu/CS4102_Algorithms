# CS4102 Spring 2022 -- Unit C Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: ylw4sj
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import math

energyGrid = []

def calculateDiff(image, i, j, i2, j2):
    red = image[i][j][0] - image[i2][j2][0]
    green = image[i][j][1] - image[i2][j2][1]
    blue = image[i][j][2] - image[i2][j2][2]
    return math.sqrt(red**2 + green**2 + blue**2)

def calculateEnergy(image, i, j, rows, cols):
    sum = 0
    n = 0
    # top
    if i != 0:
        sum += calculateDiff(image, i, j, i - 1, j)
        n += 1
    # bottom
    if i != (rows-1):
        sum += calculateDiff(image, i, j, i + 1, j)
        n += 1
    # left
    if j != 0:
        sum += calculateDiff(image, i, j, i, j - 1)
        n += 1
    # right
    if j != (cols-1):
        sum += calculateDiff(image, i, j, i, j + 1)
        n += 1
    # top right
    if i != 0 and j != (cols-1):
        sum += calculateDiff(image, i, j, i - 1, j + 1)
        n += 1
    # top left
    if i != 0 and j != 0:
        sum += calculateDiff(image, i, j, i - 1, j - 1)
        n += 1
    # bottom left
    if i != (rows - 1) and j != 0:
        sum += calculateDiff(image, i, j, i + 1, j - 1)
        n += 1
    # bottom right
    if i != (rows - 1) and j != (cols-1):
        sum += calculateDiff(image, i, j, i + 1, j + 1)
        n += 1
    return sum/n

class SeamCarving:
    def __init__(self):
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    #
    # @return the seam's weight

    def run(self, image):
        rows = len(image)
        cols = len(image[0])
        global energyGrid
        energyGrid = [[0 for i in range(cols)] for j in range(rows)]

        # calculate energies of each pixel
        for i in range(rows):
            for j in range(cols):
                energyGrid[i][j] = calculateEnergy(image, i, j, rows, cols)

        print(energyGrid)

        # calculate energy of seam for every pixel
        for i in range(rows-2, -1, -1):
            for j in range(cols):
                # calculate energies of adjacent pixels
                pList = [energyGrid[i + 1][j]] # middle pixel
                if j != 0:
                    pList.append(energyGrid[i + 1][j - 1])  # left pixel
                if j != (cols - 1):
                    pList.append(energyGrid[i + 1][j + 1])  # right pixel
                # update energy of pixel
                energyGrid[i][j] += min(pList)

        # return minimum energy seam
        return min(energyGrid[0])

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    #
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    #
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        rows = len(energyGrid)
        cols = len(energyGrid[0])

        # find starting location of the lowest energy seam
        j = energyGrid[0].index(min(energyGrid[0]))

        # reverse find seam
        seam = [j]
        for i in range(0, rows-1):
            if j == 0:
                middleP = energyGrid[i+1][j]
                rightP = energyGrid[i+1][j + 1]
                if rightP < middleP:
                    j = j + 1
            elif j == (cols-1):
                middleP = energyGrid[i+1][j]
                leftP = energyGrid[i + 1][j - 1]
                if leftP < middleP:
                    j = j - 1
            else:
                middleP = energyGrid[i + 1][j]
                rightP = energyGrid[i + 1][j + 1]
                leftP = energyGrid[i + 1][j - 1]
                if rightP < middleP and rightP < leftP:
                    j = j + 1
                if leftP < middleP and leftP < rightP:
                    j = j - 1
            seam.append(j)

        return seam

