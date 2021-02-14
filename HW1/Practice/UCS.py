import time
from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.V_org = vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        if w == 1:
            self.graph[u].append(v)
        elif w == 2:
            '''split all edges of weight 2 into two 
            edges of weight 1 each.  The intermediate 
            vertex number is maximum vertex number + 1, 
            that is V.'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V = self.V + 1
        elif w == 3:
            '''split all edges of weight 3 into three 
            edges of weight 1 each.  The intermediate 
            vertices number is maximum vertex number + 1, and 
            maximum vertex number + 2; that is V and V + 1'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(self.V + 1)
            self.graph[self.V + 1].append(v)
            self.V = self.V + 2

    # To print the shortest path stored in parent[]
    def print_path(self, parent, j, m, n):
        Path_len = 1
        if parent[j] == -1 and j < self.V_org:  # Base Case : If j is source
            print('(' + str(j // n) + ',' + str(j % m) + ')')
            return 0  # when parent[-1] then path length = 0
        l = self.print_path(parent, parent[j], m, n)

        # increment path length
        Path_len = l + Path_len

        # print node only if its less than original node length.
        # i.e do not print any new node that has been added later
        if j < self.V_org:
            print('(' + str(j // n) + ',' + str(j % m) + ')')

        return Path_len

    '''This function mainly does BFS and prints the 
       shortest path from src to dest. It is assumed 
       that weight of every edge is 1'''

    def uniform_cost_search(self, src, dest, m, n):

        # Mark all the vertices as not visited
        # Initialize parent[] and visited[]
        visited = [False] * self.V
        parent = [-1] * self.V

        # Create a queue for BFS
        queue = [src]

        # Mark the source node as visited and enqueue it
        visited[src] = True

        while queue:

            # Dequeue a vertex from queue
            s = queue.pop(0)

            # if s = dest then print the path and return
            if s == dest:
                return self.print_path(parent, s, m, n)

            # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s


# Driver code
def main():
    # Read the input file
    with open('Environment.txt', 'r') as file:
        mat = [[int(float(num)) for num in line.split(',')] for line in file]

    # Get the dimensions
    m = mat.__len__()
    n = mat[0].__len__()

    # Construct the corresponding graph
    # while still respecting the boundaries
    graph = Graph(m * n)
    for i in range(m):
        for j in range(n):
            if i - 1 >= 0 and mat[i - 1][j] != 1:
                graph.add_edge(((i * n) + j), ((i - 1) * n) + j, 2)
            if i + 1 < m and mat[i + 1][j] != 1:
                graph.add_edge(((i * n) + j), ((i + 1) * n) + j, 3)
            if j - 1 >= 0 and mat[i][j - 1] != 1:
                graph.add_edge(((i * n) + j), ((i * n) + (j - 1)), 1)
            if j + 1 < n and mat[i][j + 1] != 1:
                graph.add_edge(((i * n) + j), ((i * n) + (j + 1)), 1)

    # Set the start timestamp
    start_time = time.time()

    # Part A: (0,0) --- (23,24)
    print('------------ Part A ------------')
    cost = graph.uniform_cost_search(((0 * n) + 0), ((23 * n) + 24), m, n)
    print('Minimum Cost:', cost)

    # Set the end timestamp
    end_time = time.time()

    # Measure execution time
    print('Execution Time:', (end_time - start_time) * 1000, 'Milliseconds')

    # Set the start timestamp
    start_time = time.time()

    # Part B: (17,1) --- (17,29)
    print('------------ Part B ------------')
    cost = graph.uniform_cost_search(((17 * n) + 1), ((17 * n) + 29), m, n)
    print('Minimum Cost:', cost)

    # Set the end timestamp
    end_time = time.time()

    # Measure execution time
    print('Execution Time:', (end_time - start_time) * 1000, 'Milliseconds')


if __name__ == '__main__':
    main()
