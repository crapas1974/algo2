class MazeGraph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = []
        if vertex2 not in self.vertices[vertex1]:
            self.vertices[vertex1].append(vertex2)
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = []
        if vertex1 not in self.vertices[vertex2]:
            self.vertices[vertex2].append(vertex1)

    def find_route(self, start, end, visited = None):
        if visited == None:
            visited = []
        if start == end:
            return [end]
        visited.append(start)
        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                route_after = self.find_route(neighbor, end, visited)
                if route_after != None:
                    return [start] + route_after
        return None

def main():
    tc1 = [('start', 'bbb'), ('bbb', 'ccc'), ('bbb', 'ddd'), ('ccc', 'aaa'), ('ccc', 'end'), ('end', 'ddd')]
    tc2 = [('start', 'hhh'), ('hhh', 'aaa'), ('aaa', 'ccc'), ('ccc', 'iii'), ('iii', 'kkk'), ('kkk', 'ddd'), ('ddd', 'end'), ('end', 'bbb'), ('bbb', 'fff'), ('fff', 'jjj'), ('jjj', 'ggg'), ('jjj', 'aaa'), ('bbb', 'aaa'), ('ccc', 'bbb'), ('end', 'ccc'), ('end', 'iii'), ('end', 'fff'), ('fff', 'ggg'), ('ggg', 'ddd'), ('ggg', 'start'), ('start', 'jjj'), ('hhh', 'jjj'), ('hhh', 'lll'), ('aaa', 'lll'), ('aaa', 'mmm'), ('mmm', 'eee'), ('eee', 'iii'), ('iii', 'mmm'), ('ccc', 'mmm'), ('mmm', 'lll')]
    tc3 = [('start', 'hhh'), ('hhh', 'jjj'), ('jjj', 'ggg'), ('jjj', 'start'), ('ggg', 'start'), ('ccc', 'mmm'), ('mmm', 'lll'), ('ggg', 'hhh'), ('aaa', 'lll'), ('aaa', 'ccc'), ('eee', 'mmm'), ('iii', 'ccc'), ('iii', 'eee'), ('eee', 'ccc'), ('eee', 'aaa'), ('iii', 'lll'), ('mmm', 'aaa'), ('lll', 'eee'), ('lll', 'ccc'), ('mmm', 'iii'), ('iii', 'aaa'), ('end', 'kkk'), ('kkk', 'ddd'), ('ddd', 'fff'), ('fff', 'bbb'), ('bbb', 'end'), ('end', 'ddd'), ('fff', 'kkk'), ('kkk', 'bbb'), ('ddd', 'bbb'), ('end', 'fff')]
    tc4 = [('bbb', 'end'), ('bbb', 'ccc'), ('ccc', 'iii'), ('iii', 'lll'), ('lll', 'kkk'), ('kkk', 'ddd'), ('ddd', 'fff'), ('fff', 'jjj'), ('jjj', 'ggg'), ('ggg', 'aaa'), ('aaa', 'eee'), ('eee', 'mmm'), ('mmm', 'hhh'), ('hhh', 'start')]
    tc5 = [('lll', 'eee'), ('lll', 'bbb'), ('lll', 'ccc'), ('lll', 'kkk'), ('lll', 'ddd'), ('lll', 'fff'), ('lll', 'ggg'), ('lll', 'jjj'), ('lll', 'aaa'), ('lll', 'start'), ('lll', 'hhh'), ('lll', 'mmm'), ('lll', 'end')]
    tc6 = [('ccc', 'mmm'), ('bbb', 'iii'), ('iii', 'end'), ('iii', 'kkk'), ('jjj', 'kkk'), ('jjj', 'aaa'), ('start', 'hhh'), ('start', 'ggg'), ('start', 'aaa'), ('aaa', 'lll'), ('lll', 'eee'), ('jjj', 'ddd'), ('ddd', 'end'), ('jjj', 'fff')]
    tc7 = [('start', 'aaa'), ('aaa', 'bbb'), ('bbb', 'ccc'), ('ccc', 'ddd'), ('ddd', 'fff'), ('ccc', 'eee'), ('bbb', 'ggg'), ('ggg', 'ccc'), ('ccc', 'ijk'), ('shd', 'eee'), ('eee', 'hjb'), ('hsh', 'kec'), ('seb', 'cra'), ('cra', 'end'), ('ino', 'kec'), ('ino', 'eee'), ('vat', 'hsh'), ('vat', 'ddd'), ('ion', 'ino'), ('seb', 'vat'), ('cat', 'dog'), ('dog', 'pig'), ('pig', 'rat'), ('rat', 'gom'), ('gom', 'pig'), ('pig', 'cat'), ('bbb', 'hjf'), ('aaa', 'bed'), ('ggg', 'poi'), ('ino', 'bhj'), ('vat', 'okj'), ('cra', 'pas'), ('vat', 'dak'), ('seb', 'bes'), ('ddd', 'rnr'), ('dra', 'gon'), ('gon', 'shd'), ('fac', 'eof'), ('eof', 'fla'), ('fla', 'ten'), ('ten', 'fac')]
    testcases = [tc1, tc2, tc3, tc4, tc5, tc6, tc7]
    for i, tc in enumerate(testcases):
        maze = MazeGraph()
        for vertex1, vertex2 in tc:
            maze.add_edge(vertex1, vertex2)
        print(f"testcase {i + 1}")
        route = maze.find_route('start', 'end')
        if route == None:
            print("    탈출할 수 없음")
        else:
            route_in_str = ' -> '.join(route)
            print(f"    탈출 경로 : {route_in_str}")
        print()


if __name__ == '__main__':
    main()
        
