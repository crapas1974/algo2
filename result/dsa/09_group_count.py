class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = []
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = []
        if vertex2 not in self.vertices[vertex1]:
            self.vertices[vertex1].append(vertex2)
        if vertex1 not in self.vertices[vertex2]:
            self.vertices[vertex2].append(vertex1)

    def count_connected_components(self):
        vertex_list = list(self.vertices.keys())
        is_visited = {vertex: False for vertex in vertex_list}
        count = 0
        for vertex in vertex_list:
            if not is_visited[vertex]:
                self.search_connected_node(vertex, is_visited)
                count += 1
        return count
    
    def search_connected_node(self, v, is_visited):
        is_visited[v] = True
        for i in self.vertices[v]:
            if not is_visited[i]:
                self.search_connected_node(i, is_visited)
    
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

def main():
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = Graph()
        for edge in tc:
            g.add_edge(*edge)
        print(f"Testcase {i + 1}의 그룹 수 : {g.count_connected_components()}")
        print()

if __name__ == "__main__":
    main()
