class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end):
        if start not in self.vertices:
            self.vertices[start] = []
        if end not in self.vertices:
            self.vertices[end] = []
        self.vertices[start].append(end)
    
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
    
    def find_cycle_old(self):
        visited = {}
        rec_stack = {}
        for vertex in self.vertices:
            visited[vertex] = False
            rec_stack[vertex] = False

        for vertex in self.vertices:
            if not visited[vertex]:
                if self._find_cycle_old(vertex, visited, rec_stack):
                    return True
        return False

    def _find_cycle_old(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbour in self.vertices[vertex]:
            if not visited[neighbour]:
                if self._find_cycle_old(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[vertex] = False
        return False
    

    def remove_non_cycle_vertices_old(self):
        vertices = list(self.vertices.keys())
        i = 0
        while True:
            print(i, "th loop")
            i += 1
            is_start_edge = {v: False for v in vertices}
            is_end_edge = {v: False for v in vertices}
            for start, ends in self.vertices.items():
                for end in ends:
                    is_start_edge[start] = True
                    is_end_edge[end] = True
            remove = []
            print(is_start_edge)
            print(is_end_edge)
            for vertex in vertices:                
                if not is_start_edge[vertex] or not is_end_edge[vertex]:
                    remove.append(vertex)
            if len(remove) == 0:
                break

            for vertex in vertices:
                if vertex in remove:
                    del self.vertices[vertex]
                    continue
                ends = self.vertices[vertex]
                for end in ends:
                    if end in remove:
                        self.vertices[vertex].remove(end)
            for remove_vertex in remove:
                vertices.remove(remove_vertex)


    


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
        #g.print_edges()
        #print(f"Testcase {i + 1} : {'있음' if g.find_cycle() else '없음'}")
        #print(f"Testcase {i + 1} : {'있음' if g.find_cycle_2() else '없음'}")
        print(f"Testcase {i + 1}의 사이클 : {'O' if g.find_cycle() else 'X'}")
 #       print(f"Testcase {i + 1}의 사이클 : {'O' if g.find_cycle_old() else 'X'}")
#
        print()
#        if i == 8:
#            break

        #print(g.find_cycle_count())
#        print(f"{g.find_cycle()}")
        #print(g.edge_vertex_count())
#        if i < 10:
#            print(g.find_cycle_node())
        #     print(g.find_longest_cycle())
        #     #if i == 6 or i == 2:
        #     print(g.edge_vertex_count())
        #     g.remove_non_cycle_vertices()
        #     print(g.edge_vertex_count())
        #     print(g.vertices)

#        print(g.)
        



if __name__ == '__main__':#
    main()