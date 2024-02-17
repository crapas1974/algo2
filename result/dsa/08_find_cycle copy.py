class Graph:
    def __init__(self):
        self.vertices = {}


    def add_edge(self, start, end):
        if start not in self.vertices:
            self.vertices[start] = []
        if end not in self.vertices:
            self.vertices[end] = []
        self.vertices[start].append(end)

    def remove_edge(self, start, end):
        if start in self.vertices:
            if end in self.vertices[start]:
                self.vertices[start].remove(end)                

    def edge_vertex_count(self):
        v_count = 0
        e_count = 0
        for vertex, neighbors in self.vertices.items():
            v_count += 1
            e_count += len(neighbors)
        return v_count, e_count

    def find_cycle2(self):
#        vertices_cnt = len(self.vertices)
        visited = {}
        #rec_stack = None
        for vertex in self.vertices:
            visited[vertex] = False
            #rec_stack[vertex] = False

        for vertex in self.vertices:
            #print(f"check {vertex}")
            #print(f"    visited : {visited}")
            #print(f"    rec_stack : {rec_stack}")
            if not visited[vertex]:
                if self._find_cycle2(vertex, visited):
                    #print(f"   True visited : {visited}")
                    #print(f"   True rec_stack : {rec_stack}")
                    return True
        return False

    def _find_cycle2(self, vertex, visited, rec_stack = None):
        if rec_stack == None:
            rec_stack = {}
            for vertex in self.vertices:
                rec_stack[vertex] = False
        visited[vertex] = True
        rec_stack[vertex] = True

        for neighbour in self.vertices[vertex]:
            if not visited[neighbour]:
                if self._find_cycle2(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[vertex] = False
        return False
        
    
    def find_cycle(self):
#        vertices_cnt = len(self.vertices)
        visited = {}
        rec_stack = {}
        for vertex in self.vertices:
            visited[vertex] = False
            rec_stack[vertex] = False

        for vertex in self.vertices:
            #print(f"check {vertex}")
            #print(f"    visited : {visited}")
            #print(f"    rec_stack : {rec_stack}")
            if not visited[vertex]:
                if self._find_cycle(vertex, visited, rec_stack):
                    #print(f"   True visited : {visited}")
                    #print(f"   True rec_stack : {rec_stack}")
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
    
    def find_cycle_node(self):
        visited = {}
        rec_stack = {}
#        in_cycle = []
        for vertex in self.vertices:
            visited[vertex] = False
            rec_stack[vertex] = False

        for vertex in self.vertices:
#            print(f"check {vertex}")
#            print(f"    visited : {visited}")
            print(f"    rec_stack : {rec_stack}")
            if not visited[vertex]:
                self._find_cycle_node(vertex, visited, rec_stack)
#                if self._find_cycle_node(vertex, visited, rec_stack):
#                    print(f"   True visited : {visited}")
#                    print(f"   True rec_stack : {rec_stack}")
#                    return True
        print(f"   True   visited : {visited}")
        print(f"   True rec_stack : {rec_stack}")

                
        return False

    def _find_cycle_node(self, vertex, visited, rec_stack = None):
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
    

    def print_edges(self, filewrite=False):
        if not filewrite:
            for vertex, neighbors in self.vertices.items():
                for neighbor in neighbors:
                    print(f"{vertex} {neighbor}")
        else:
            with open("tc.txt", "w") as f:
                f.write("Testcase\n")
                for vertex, neighbors in self.vertices.items():
                    for neighbor in neighbors:
                        f.write(f"{vertex} {neighbor}\n")
                f.write("End Testcase\n")

    def count_cycles(self):
        count = 0
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, vertex)
                elif neighbor != parent:
                    nonlocal count
                    count += 1

        for vertex in self.vertices:
            if vertex not in visited:
                dfs(vertex, None)

        return count

    def find_cycle_count(self):
        visited = {}
        rec_stack = {}
        cycle_count = 0

        for vertex in self.vertices:
            visited[vertex] = False
            rec_stack[vertex] = False

        for vertex in self.vertices:
            if not visited[vertex]:
                cycle_detected = self._find_cycle_count(vertex, visited, rec_stack)
                cycle_count += cycle_detected[0]
        return cycle_count

    def _find_cycle_count(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True
        cycle_detected = [0]

        for neighbour in self.vertices[vertex]:
            if not visited[neighbour]:
                result = self._find_cycle_count(neighbour, visited, rec_stack)
                cycle_detected[0] += result[0]
            elif rec_stack[neighbour]:
                cycle_detected[0] += 1

        rec_stack[vertex] = False
        return cycle_detected
    
    def find_longest_cycle(self):
        max_length = [0]  # 리스트를 사용하여 참조를 통한 업데이트 가능

        def dfs(vertex, visited, start, length):
            visited.add(vertex)
            for neighbour in self.vertices.get(vertex, []):
                if neighbour == start:  # 사이클을 찾음
                    max_length[0] = max(max_length[0], length + 1)
                elif neighbour not in visited:
                    dfs(neighbour, visited, start, length + 1)
            visited.remove(vertex)

        for start_vertex in self.vertices:
            dfs(start_vertex, set(), start_vertex, 0)

        return max_length[0]
    
    def remove_non_cycle_vertices(self):
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

    def remove_non_cycle_vertices_old2(self):
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



            # for start, ends in self.vertices.items():
            #     if start in remove:
            #         del self.vertices[start]
            #         continue
            #     for end in ends:
            #         if end in remove:
            #             self.vertices[start].remove(end)
        #return self

        # vertices = list(self.vertices.keys())
        # for v, n in self.vertices.items():
        #     for vertex in n:
        #         if vertex not in vertices_reverse:
        #             vertices_reverse[vertex] = []
        #         vertices_reverse[vertex].append(v)
        # while True:
        #     remove = []
        #     for start, ends in vertices:
        #         for end in ends:
        #             if len(vertices_reverse[end]) == 0:   # n에서 나가는게 없어
        #                 remove.append(n)
        #     for v, neighbors in vertices_reverse:
        #         for n in neighbors:
        #             if len(vertices[n]) == 0:
        #                 remove.append(n)

        #                 vertices.remove(n)
        #                 removed = True

        

    
    # def remove_non_cycle_vertices(self):
    #     visited = {}
    #     rec_stack = {}
    #     for vertex in self.vertices:
    #         visited[vertex] = False
    #         rec_stack[vertex] = False
    #     for vertex in self.vertices:
    #         if not visited[vertex]:
    #             self._remove_non_cycle_vertices(vertex, visited, rec_stack)
    #     return self
    
    # def _remove_non_cycle_vertices(self, vertex, visited, rec_stack):
    #     visited[vertex] = True
    #     rec_stack[vertex] = True
    #     for neighbour in self.vertices[vertex]:
    #         if not visited[neighbour]:
    #             self._remove_non_cycle_vertices(neighbour, visited, rec_stack)
    #         elif rec_stack[neighbour]:
    #             self.remove_edge(vertex, neighbour)
    #     rec_stack[vertex] = False
    #     return False
    


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



import random
def choose_random_vname(vertex_cnt, length, voca = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']):
    vnames = []
    while len(vnames) < vertex_cnt:
        vname = ''.join(random.choices(voca, k = length))
        if vname not in vnames:
            vnames.append(vname)
            print(f"ADd {vname} ")
    return vnames

def make_acyclic_graph(vertex_cnt):
    if vertex_cnt <= 26:
        vertex_name_length = 1
    elif vertex_cnt <= 676:
        vertex_name_length = 2
    else:
        vertex_name_length = 3

    vertex_names = choose_random_vname(vertex_cnt, vertex_name_length)
    edges = []
    for v1 in vertex_names:
        for v2 in vertex_names:
            edges.append((v1, v2))
    checked_cnt = 0
    random.shuffle(edges)
    g = Graph()
    i = 0
    for edge in edges:
        i += 1
        if i % 10000 == 0:
            print(f"Add {i}th edge")
        g.add_edge(*edge)
        if g.find_cycle():
            g.remove_edge(*edge)
            checked_cnt += 1
        if checked_cnt == 2000:
            break
    # i = 0
    # while g.find_cycle():
    #     if i % 100000 == 0:
    #         print(f"Remove {i}th edge")
    #     g.remove_edge(*edges[i])
    #     i += 1
    return g

def make_random_graph(vertex_cnt, edge_cnt):
    if vertex_cnt <= 26:
        vertex_name_length = 1
    elif vertex_cnt <= 676:
        vertex_name_length = 2
    else:
        vertex_name_length = 3

    vertex_names = choose_random_vname(vertex_cnt, vertex_name_length)
    edges = []
    while len(edges) < edge_cnt:
        v1 = random.choice(vertex_names)
        v2 = random.choice(vertex_names)
        if (v1, v2) not in edges and (v2, v1) not in edges:
            edges.append((v1, v2))
    g = build_graph(edges)
    return g


def main():
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = build_graph(tc)
        #g.print_edges()
        print(f"Testcase {i + 1} : {'O' if g.find_cycle() else 'X'}")
        print(f"Testcase {i + 1} : {'O' if g.find_cycle2() else 'X'}")
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