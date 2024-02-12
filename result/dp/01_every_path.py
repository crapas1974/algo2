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

    def find_all_path(self, start, end, visited = None, paths = None):
        result = []
        is_first_call = False        
        if visited == None:
            visited = []
            is_first_call = True
        if paths == None:
            paths = []

        visited.append(start)
        if start == end:            
            paths.append(visited)
        else:
            for neighbor in self.vertices[start]:
                if neighbor not in visited:
                    self.find_all_path(neighbor, end, visited[:], paths)

        if is_first_call:
            
            for path in paths:
                distance = 0
                for i in range(len(path) - 1):
                    distance_key = (path[i], path[i + 1])
                    if path[i] > path[i + 1]:
                        distance_key = (path[i + 1], path[i])
                    distance += self.distance_table[distance_key]
                result.append((path, distance))
            
        return result


def main():
    with open("dp_tc1.txt", "r") as f:
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

        all_paths = lab_map.find_all_path('start', 'end')
        if all_paths == []:
            print(f"Testcase {i + 1}에서 start에서 시작해 end에 도착할 수 있는 경로가 존재하지 않습니다.")
        else:
            path_count = len(all_paths)
            total_distance = 0
            min_distance = float('inf')
            max_distance = 0
            min_path = []
            max_path = []
            for path, distance in all_paths:
                total_distance += distance
                if distance < min_distance:
                    min_distance = distance
                    min_path = [path]
                elif distance == min_distance:
                    min_path.append(path)
                if distance > max_distance:
                    max_distance = distance
                    max_path = [path]
                elif distance == max_distance:
                    max_path.append(path)
            print(f"Testcase {i + 1}의 모든 경로의 수는 {path_count}이며 최단 거리는 {min_distance}, 최장 거리는 {max_distance}, 평균 거리는 {total_distance // path_count} 입니다.")
            print(f"    최단 거리 경로")
            for path in min_path:
                print(f"        {' -> '.join(path)}")
            print(f"    최장 거리 경로")
            for path in max_path:
                print(f"        {' -> '.join(path)}")
        print()

if __name__ == "__main__":
    main()  