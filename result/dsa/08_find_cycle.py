class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end):
        if start not in self.vertices:
            self.vertices[start] = []
        if end not in self.vertices:
            self.vertices[end] = []
        self.vertices[start].append(end)
    
    # time complexity - O(V + E)
    def find_cycle(self):
        is_visited = {}
        for vertex in self.vertices:
            is_visited[vertex] = False

        for vertex in self.vertices:
            if not is_visited[vertex]:
                if self.check_cycle_dfs(vertex, is_visited):
                    return True
        return False

    def check_cycle_dfs(self, vertex, is_visited, is_valid_current = None):
        if is_valid_current == None:
            is_valid_current = {}
            for init_vertex in self.vertices:
                is_valid_current[init_vertex] = False
        is_visited[vertex] = True
        is_valid_current[vertex] = True

        for neighbour in self.vertices[vertex]:
            if not is_visited[neighbour]:
                if self.check_cycle_dfs(neighbour, is_visited, is_valid_current):
                    return True
            elif is_valid_current[neighbour]:
                return True

        is_valid_current[vertex] = False
        return False

def build_graph(edges):
    g = Graph()
    for edge in edges:
        g.add_edge(*edge)
    return g

def datafile_into_testcase():
    with open("find_cycle_data.txt", "r") as f:
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
            edges.append(tuple(lines[j].strip().split(" ")))
        testcases.append(edges)
    return testcases

def main():
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = build_graph(tc)
        print(f"Testcase {i + 1}의 사이클 : {'O' if g.find_cycle() else 'X'}")
        print()

if __name__ == '__main__':
    main()