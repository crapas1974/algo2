class Graph:
    def __init__(self):
        self.vertices = {}
        self.distance_table = {}

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = []
        if vertex2 not in self.vertices[vertex1]:
            self.vertices[vertex1].append(vertex2)
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = []
        if vertex1 not in self.vertices[vertex2]:
            self.vertices[vertex2].append(vertex1)
        distance_key = (vertex1, vertex2)
        if vertex1 > vertex2:
            distance_key = (vertex2, vertex1)
        self.distance_table[distance_key] = distance

    def get_distance(self, vertex1, vertex2):
        if (vertex1, vertex2) in self.distance_table:
            return self.distance_table[(vertex1, vertex2)]
        elif (vertex2, vertex1) in self.distance_table:
            return self.distance_table[(vertex2, vertex1)]
        else:
            return None
    
    def find_shortest_distance(self, start, end, visited = None):
        if visited == None:
            visited = [end]
        if start == end:
            return 0
        distance = float('inf')
        min_distance = float('inf')
        for neighbor in self.vertices[end]:
            if neighbor not in visited:
                distance = self.find_shortest_distance(start, neighbor, visited + [neighbor]) + self.get_distance(neighbor, end)
                if distance < min_distance:
                    min_distance = distance
        return min_distance

    def find_shortest_path(self, start, end, visited = None):
        if visited == None:
            visited = [end]
        if start == end:
            return 0, [visited]
        
        distance = float('inf')
        min_distance = float('inf')
        min_path = []
        for neighbor in self.vertices[end]:
            if neighbor not in visited:
                distance, paths = self.find_shortest_path(start, neighbor, [neighbor] + visited)
                
                if distance + self.get_distance(neighbor, end) < min_distance:
                    min_distance = distance + self.get_distance(neighbor, end)
                    min_path = []
                    for path in paths:
                        min_path.append(path)
                elif distance + self.get_distance(neighbor, end) == min_distance:
                    for path in paths:
                        min_path.append(path)
        return (min_distance, min_path)


def main():
    with open("dp_tc2.txt", "r") as f:
        lines = f.readlines()

    case_start_lines = []
    for i, line in enumerate(lines):
        if line.startswith("Testcase"):
            case_start_lines.append(i)
    case_start_lines.append(len(lines))

    for i in range(len(case_start_lines) - 1):                
        lab_map = Graph()
        for j in range(case_start_lines[i] + 1, case_start_lines[i + 1]):
            line = lines[j].strip()
            if line == '':
                continue
            vertex1, vertex2, distance = line.split(' ')
            distance = int(distance)
            lab_map.add_edge(vertex1, vertex2, distance)

        # sd = lab_map.find_shortest_distance('start', 'end')
        # print(sd)
        result = lab_map.find_shortest_path('start', 'end')
        distance = result[0]
        if distance == float('inf'):
            print(f"Testcase {i + 1}에서 start에서 시작해 end에 도착할 수 있는 경로가 존재하지 않습니다.")
        else:
            print(f"Testcase {i + 1}의 최단 거리는 {distance}입니다.")
            print(f"    최단 경로를 구하는 함수의 반환값 : {result}")
        print()

if __name__ == "__main__":
    main()  