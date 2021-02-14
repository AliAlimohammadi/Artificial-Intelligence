import time
import networkx as nx

# Read the input file
with open('Environment.txt', 'r') as file:
    mat = [[int(float(num)) for num in line.split(',')] for line in file]

# Get the dimensions
m = mat.__len__()
n = mat[0].__len__()


# Generate the a directed graph
G = nx.DiGraph()


# My own heuristic which is a linear polynomial
# based on Manhattan distance heuristic
def heuristic(a, b):
    a = int(a)
    b = int(b)
    (x1, y1) = (a // n, a % m)
    (x2, y2) = (b // n, b % m)
    return abs(x1 - x2) + abs(y1 - y2)


# Construct the corresponding graph
# while still respecting the boundaries
for i in range(m):
    for j in range(n):
        # Move Up (w = 2)
        if i - 1 >= 0 and mat[i - 1][j] != 1:
            G.add_edge(str((i * n) + j), str(((i - 1) * n) + j), weight=2)
        # Move Down (w = 3)
        if i + 1 < m and mat[i + 1][j] != 1:
            G.add_edge(str((i * n) + j), str(((i + 1) * n) + j), weight=3)
        # Move Left (w = 1)
        if j - 1 >= 0 and mat[i][j - 1] != 1:
            G.add_edge(str((i * n) + j), str((i * n) + (j - 1)), weight=1)
        # Move Right (w = 1)
        if j + 1 < n and mat[i][j + 1] != 1:
            G.add_edge(str((i * n) + j), str((i * n) + (j + 1)), weight=1)

# Set the start timestamp
start_time = time.time()

# A* algorithm with the specified heuristic

# Part A: (0,0) --- (23,24)
print('------------ Part A ------------')
path = nx.astar_path(G, str(0 * n + 0), str(23 * n + 24), heuristic)
for cell in path:
    print('(' + str(int(cell) // n) + ',' + str(int(cell) % m) + ')')
print('Minimum Cost:', nx.astar_path_length(G, str(0), str(23 * n + 24), heuristic))

# Set the end timestamp
end_time = time.time()

# Measure execution time
print('Execution Time:', (end_time - start_time) * 1000, 'Milliseconds')

# Set the start timestamp
start_time = time.time()

# Part B: (17,1) --- (17,29)
print('------------ Part B ------------')
path = nx.astar_path(G, str(17 * n + 1), str(17 * n + 29), heuristic)
for cell in path:
    print('(' + str(int(cell) // n) + ',' + str(int(cell) % m) + ')')
print('Minimum Cost:', nx.astar_path_length(G, str(17 * n + 1), str(17 * n + 29), heuristic))

# Set the end timestamp
end_time = time.time()

# Measure execution time
print('Execution Time:', (end_time - start_time) * 1000, 'Milliseconds')
