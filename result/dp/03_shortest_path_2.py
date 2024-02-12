import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"실행 시간 : {end_time}")
        return result
    return wrapper

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

    # bonus problem solution
    def find_shortest_distance2(self, start, end):
        vertices = list(self.vertices.keys())
        distances_from_start = {}
        for (v1, v2), v in self.distance_table.items():
            if v1 == start or v2 == start:
                if v1 == start:
                    distances_from_start[v2] = v
                else:
                    distances_from_start[v1] = v
        while True:
            updated_distances_from_start = {}       
            for mid in distances_from_start.keys():
                if mid not in updated_distances_from_start:
                    updated_distances_from_start[mid] = distances_from_start[mid]
                else:
                    updated_distances_from_start[mid] = min(updated_distances_from_start[mid], distances_from_start[mid])
                for dst in vertices:
                    distance_mid_dst = self.get_distance(mid, dst)
                    if distance_mid_dst == None:
                        continue
                    distance_start_mid_dst = distances_from_start[mid] + distance_mid_dst
                    current_distance_start_dst = float('inf')
                    if dst in updated_distances_from_start:
                        current_distance_start_dst = updated_distances_from_start[dst]
                    direct_to_dst = float('inf')
                    if dst in distances_from_start:
                        direct_to_dst = distances_from_start[dst]
                    updated_distances_from_start[dst] = min(distance_start_mid_dst, current_distance_start_dst, direct_to_dst)
            is_updated = False
            if len(distances_from_start) != len(updated_distances_from_start):
                is_updated = True
            else:
                for k, v in distances_from_start.items():
                    if v != updated_distances_from_start[k]:
                        is_updated = True
                        break
            if is_updated == False:
                break
            distances_from_start = updated_distances_from_start
        if end in distances_from_start:
            return distances_from_start[end]
        else:
            return None
                
    def find_shortest_distance(self, start, end):
        vertices = list(self.vertices.keys())
        distances = {}
        for (v1, v2), v in self.distance_table.items():
            key = tuple(sorted([v1, v2]))
            distances[key] = v
        while True:
            updated_distances = {}            
            for i in range(len(vertices)):
                for j in range(i + 1, len(vertices)):
                    v1 = vertices[i]
                    v2 = vertices[j]
                    key = tuple(sorted([v1, v2]))
                    current_distance = float('inf')
                    if key in distances:
                        current_distance = distances[key]
                    for inter_vertex in vertices:
                        if inter_vertex == v1 or inter_vertex == v2:
                            continue
                        first_half_key = tuple(sorted([v1, inter_vertex]))
                        second_half_key = tuple(sorted([inter_vertex, v2]))
                        if first_half_key in distances and second_half_key in distances:
                            current_distance = min(current_distance, distances[first_half_key] + distances[second_half_key])
                    if current_distance != float('inf'):
                        updated_distances[(key)] = current_distance
            is_updated = False
            if len(distances) != len(updated_distances):
                is_updated = True
            else:
                for k, v in distances.items():
                    if v != updated_distances[k]:
                        is_updated = True
                        break
            if is_updated == False:
                break
            distances = updated_distances
        key = tuple(sorted([start, end]))        

        if key in distances:
            return distances[key]
        else:
            return None

def main():
    with open("dp_tc3.txt", "r") as f:
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
        distance = lab_map.find_shortest_distance('start', 'end')
        distance2 = lab_map.find_shortest_distance2('start', 'end')
        if distance != distance2:
            print("Wrong!", distance, distance2)
        print(f"Testcase {i + 1} : ", end = '')
        if distance == None:
            print("start에서 시작해 end에 도착할 수 있는 경로가 존재하지 않습니다.")
        else:
            print(f"최단 거리는 {distance}입니다.")        
        
        print()

if __name__ == "__main__":
    main()  