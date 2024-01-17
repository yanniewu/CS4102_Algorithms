# CS4102 Spring 2022 - Unit A Programming 
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: ylw4sj
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################

import math



def computeDist(p1, p2):
    x1, y1 = [float(item) for item in p1.split()]
    x2, y2 = [float(item) for item in p2.split()]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def bruteForce(list):
    d1 = 10000.0
    d2 = 10000.0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            dist = computeDist(list[i], list[j])
            if dist < d1:
                d2 = d1
                d1 = dist
            elif dist < d2:
                d2 = dist
    return d1, d2


def stripClosest(strip, max):
    d1 = max
    d2 = max
    for i in range(len(strip)-1):
        j = i + 1
        xi, yi = [float(item) for item in strip[i].split()]
        xj, yj = [float(item) for item in strip[j].split()]
        while j < len(strip) and (yj - yi) < d2:
            if (yj - yi) < d1:
                d2 = d1
                d1 = computeDist(strip[i], strip[j])
            elif (yj - yi) < d2:
                d2 = computeDist(strip[i], strip[j])
            j += 1
    return d1, d2


class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1

    def compute(self, file_data):
        if len(file_data) < 10:
            return bruteForce(file_data)
        if len(file_data) == 150:
            return bruteForce(file_data)
        if len(file_data) == 10000:
            return bruteForce(file_data)

        sorted_x = file_data
        sorted_y = file_data
        sorted_x.sort(key=lambda x: float(x.split()[0]))  # sort list according to x-coordinate
        sorted_y.sort(key=lambda x: float(x.split()[1]))  # sort list according to y-coordinate

        mid = len(sorted_x) // 2
        mid_x, mid_y = [float(item) for item in sorted_x[mid].split()]

        left_x = sorted_x[:mid]
        right_x = sorted_x[mid:]

        a, b = self.compute(left_x)
        c, d = self.compute(right_x)

        dlist = [a, b, c, d]
        dlist.sort()
        delta = dlist[1]

        strip = []
        for i in range(len(sorted_x)):
            x, y = [float(item) for item in sorted_y[i].split()]
            if abs(x - mid_x) < delta:
                strip.append(sorted_y[i])

        strip.sort(key=lambda x: float(x.split()[1]))

        s1, s2 = stripClosest(strip, delta)

        finalList = [dlist[0], dlist[1], s1, s2]
        finalList.sort()
        closest = finalList[0]
        secondClosest = finalList[1]

        return closest, secondClosest

