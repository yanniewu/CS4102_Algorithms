# CS4102 Spring 2022 - Unit B Programming
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
# Your Computing ID:ylw4sj
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################


# helper function to find parent of node
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# helper function to join two trees
def union(parent, rank, u, v):
    u_parent = find(parent, u)
    v_parent = find(parent, v)

    if rank[u_parent] < rank[v_parent]:
        parent[u_parent] = v_parent
    elif rank[u_parent] > rank[v_parent]:
        parent[v_parent] = u_parent
    else:
        parent[v_parent] = u_parent
        rank[u_parent] += 1


# helper function to determine if edge is valid
def valid(u, v, id_to_name, type, assigned_center):
    if type[u] == "port" and type[v] == "port":
        return False
    if type[u] == "port" and type[v] == "store":
        return False
    if type[v] == "port" and type[u] == "store":
        return False
    if type[u] == "rail-hub" and type[v] == "store":
        return False
    if type[v] == "rail-hub" and type[u] == "store":
        return False
    if type[u] == "dist-center" and type[v] == "dist-center":
        return False
    if type[u] == "store" and type[v] == "dist-center":
        if id_to_name[v] != assigned_center[u]:
            return False
    if type[u] == "dist-center" and type[v] == "store":
        if id_to_name[u] != assigned_center[v]:
            return False
    return True


class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement

    def compute(self, file_data):
        #return file_data
        edgeWeightSum = 0

        # your function to compute the result should be called here
        num_nodes, num_links = (int(item) for item in file_data[0].split())

        #setup
        name_to_id = {}
        type = {}
        id_to_name = {}
        assigned_center = {}
        curr_center = ""
        for id in range(1, num_nodes + 1):
            n, t = file_data[id].split()
            name_to_id[n] = id
            type[id] = t
            id_to_name[id] = n
            # assign distribution center to stores
            if t == "dist-center":
                curr_center = n
            if t == "store":
                assigned_center[id] = curr_center

        # create graph of places
        graph = []
        for i in range(num_nodes + 1, num_nodes + 1 + num_links):
            u, v, w = file_data[i].split()
            graph.append([name_to_id[u], name_to_id[v], w])

        # start of Kruskal's
        graph.sort(key=lambda x: x[2])

        # create indirect heap
        parent = [0]
        rank = [0]
        for i in range(1, num_nodes + 1):
            parent.append(i)
            rank.append(0)

        mst = []
        i = 0  # used to iterate through graph
        e = 0  # num of edges in mst
        # while there are still edges left to check
        while e < num_nodes - 1:
            u, v, w = graph[i]
            i += 1
            # check if edge is valid
            u_parent = find(parent, u)
            v_parent = find(parent, v)

            if u_parent != v_parent and valid(u, v, id_to_name, type, assigned_center):
                e += 1
                # add edge to mst
                mst.append([u, v, w])
                # join trees
                union(parent, rank, u_parent, v_parent)

        # sum up edges in mst
        for i in mst:
            edgeWeightSum += int(i[2])

        return edgeWeightSum
