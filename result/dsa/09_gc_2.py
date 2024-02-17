class MatrixGraph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.visited = [False] * len(adj_matrix)

    def dfs(self, vertex):
        self.visited[vertex] = True
        for neighbor in range(len(self.adj_matrix[vertex])):
            if self.adj_matrix[vertex][neighbor] == 1 and not self.visited[neighbor]:
                self.dfs(neighbor)

    def count_connected_components(self):
        count = 0
        for vertex in range(len(self.adj_matrix)):
            if not self.visited[vertex]:
                self.dfs(vertex)
                count += 1
        return count


def datafile_into_testcase():
    with open("group_count.txt", "r") as f:
        lines = f.readlines()
    startlines = []
    endlines = []
    for i, line in enumerate(lines):
        if line.startswith("Testcase"):
            startlines.append(i + 1)
        if line.startswith("End Testcase"):
            endlines.append(i - 1)
    testcases = []
    for i in range(len(startlines)):
        edges = []
        for j in range(startlines[i], endlines[i] + 1):
            edge = tuple(lines[j].strip().split(" "))
            edges.append(edge)
        testcases.append(edges)
    return testcases

tc = datafile_into_testcase()
print(len(tc))
print(tc[0])
print(tc[1])

# # Example usage
# adj_matrix = [
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0]
# ]

# graph = Graph(adj_matrix)
# num_components = graph.count_connected_components()
# print("Number of connected components:", num_components)