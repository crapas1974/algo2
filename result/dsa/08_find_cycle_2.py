class Graph:
    def __init__(self):
        #self.vertices = vertices
        #self.adj = {v: [] for v in range(vertices)}
        self.vertices = {}        

    def add_edge(self, start, end):
        if start not in self.vertices:
            self.vertices[start] = []
        if end not in self.vertices:
            self.vertices[end] = []
        self.vertices[start].append(end)

    def find_cycle(self):
#        vertices_cnt = len(self.vertices)
        visited = {}
        rec_stack = {}
        for vertex in self.vertices:
            visited[vertex] = False
            rec_stack[vertex] = False

        for vertex in self.vertices:
            if not visited[vertex]:
                if self._find_cycle(vertex, visited, rec_stack):
                    return True
        return False

    def _find_cycle(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbour in self.vertices[vertex]:
            if not visited[neighbour]:
                if self._find_cycle(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[vertex] = False
        return False

    # def _find_cycle(self, node, visited, rec_stack):
    #     visited[node] = True
    #     rec_stack[node] = True

    #     for neighbour in self.adj[node]:
    #         if not visited[neighbour]:
    #             if self._find_cycle(neighbour, visited, rec_stack):
    #                 return True
    #         elif rec_stack[neighbour]:
    #             return True

    #     rec_stack[node] = False
    #     return False
    
def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    print(g.find_cycle())
    print(g.vertices)

if __name__ == '__main__':
    main()