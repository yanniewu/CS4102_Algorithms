# CS4102 Spring 2022 -- Unit D Programming
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
import networkx as nx


class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):

        rows = len(lines)
        cols = len(lines[0])

        # create graph
        g = nx.Graph()
        checked = {}
        for i in range(rows):
            for j in range(cols):
                if lines[i][j] == '#':
                    key = (i, j)
                    checked[key] = False
                    if i != rows - 1 and lines[i + 1][j] == '#':  # bottom
                        g.add_edge(key, (i + 1, j))
                    if j != cols - 1 and lines[i][j + 1] == '#':  # right
                        g.add_edge(key, (i, j + 1))

        # nx.draw(g)
        # plt.show()

        # check that number of tiles is even
        if g.number_of_nodes() % 2 == 1:
            return ["impossible"]

        # look at each component
        ans = []
        components = [g.subgraph(c).copy() for c in nx.connected_components(g)]
        for c in components:
            tiling = nx.bipartite.maximum_matching(c)  # pair up adjacent nodes
            for i in tiling:
                if not checked[i]:  # check for duplicates
                    x, y = i
                    x2, y2 = tiling[i]
                    checked[i] = True
                    checked[tiling[i]] = True
                    ans.append(str(y) + " " + str(x) + " " + str(y2) + " " + str(x2))

        # check that every # has been covered
        for i in checked:
            if not checked[i]:
                return ["impossible"]

        return ans
