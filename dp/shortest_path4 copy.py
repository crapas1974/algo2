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
    #@execution_time
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
            #print("new turn", distances_from_start)
            updated_distances_from_start = {}       
            for mid in distances_from_start.keys():
                if mid not in updated_distances_from_start:
                    updated_distances_from_start[mid] = distances_from_start[mid]
                else:
                    updated_distances_from_start[mid] = min(updated_distances_from_start[mid], distances_from_start[mid])
                for dst in vertices:
                    #print("check", mid, dst)
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
            #print("updated", updated_distances_from_start, len(updated_distances_from_start))
            #print("old", distances_from_start, len(distances_from_start))
            is_updated = False
            if len(distances_from_start) != len(updated_distances_from_start):
                is_updated = True
            else:
                #print(distances_from_start)
                #print(updated_distances_from_start)
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
        
    def find_longestest_distance2(self, start, end):
        vertices = list(self.vertices.keys())
        distances_from_start = {}
        for (v1, v2), v in self.distance_table.items():
            if v1 == start or v2 == start:
                if v1 == start:
                    distances_from_start[v2] = v
                else:
                    distances_from_start[v1] = v
        while True:
            #print("new turn", distances_from_start)
            updated_distances_from_start = {}       
            for mid in distances_from_start.keys():
                if mid not in updated_distances_from_start:
                    updated_distances_from_start[mid] = distances_from_start[mid]
                else:
                    updated_distances_from_start[mid] = min(updated_distances_from_start[mid], distances_from_start[mid])
                for dst in vertices:
                    #print("check", mid, dst)
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
            #print("updated", updated_distances_from_start, len(updated_distances_from_start))
            #print("old", distances_from_start, len(distances_from_start))
            is_updated = False
            if len(distances_from_start) != len(updated_distances_from_start):
                is_updated = True
            else:
                #print(distances_from_start)
                #print(updated_distances_from_start)
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
        

    #@execution_time
    def find_shortest_path(self, start, end):
        vertices = list(self.vertices.keys())
        vertices.sort()
        distances = {}
        shortest_paths = {}
        for (v1, v2), v in self.distance_table.items():
            key = tuple(sorted([v1, v2]))
            distances[key] = v
            shortest_paths[key] = [[v1, v2]]
        while True:
            updated_distances = {}            
            for i in range(len(vertices)):
                for j in range(i + 1, len(vertices)):
                    v1 = vertices[i]
                    v2 = vertices[j]
                    key = (v1, v2)
                    current_distance = float('inf')
                    current_path = []
                    if key in distances:
                        current_distance = distances[key]
                        current_path = shortest_paths[key]
                    for inter_vertex in vertices:
                        if inter_vertex == v1 or inter_vertex == v2:
                            continue
                        first_half_key = tuple(sorted([v1, inter_vertex]))
                        second_half_key = tuple(sorted([inter_vertex, v2]))
                        if first_half_key in distances and second_half_key in distances:
                            distance_through_inter_vertex = distances[first_half_key] + distances[second_half_key]
                            path_through_inter_vertex = []
                            for path_prev in shortest_paths[first_half_key]:
                                for path_after in shortest_paths[second_half_key]:
                                    composed_path = path_prev[:-1]
                                    if path_prev[0] != v1:
                                        composed_path = path_prev[::-1][:-1]
                                    if path_after[-1] == v2:
                                        composed_path += path_after
                                    else:
                                        composed_path += path_after[::-1]
                                    path_through_inter_vertex.append(composed_path)
                            if distance_through_inter_vertex < current_distance:
                                current_distance = distance_through_inter_vertex
                                current_path = path_through_inter_vertex
                            elif distance_through_inter_vertex == current_distance:
                                for path in path_through_inter_vertex:
                                    if path not in current_path:
                                        current_path.append(path)
                    if current_distance != float('inf'):
                        updated_distances[(key)] = current_distance
                        shortest_paths[key] = current_path
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
        if key not in distances:
            return None, None
        if shortest_paths[key][0][0] == start:
            result_path = shortest_paths[key]
        else:
            result_path = []
            for path in shortest_paths[key]:
                result_path.append(path[::-1])

        return distances[key], result_path


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
        distance, path = lab_map.find_shortest_path('start', 'end')
        #distance2 = lab_map.find_shortest_distance2('start', 'end')
        #if distance != distance2:
        #    print("Wrong!", distance, distance2)
        print(f"Testcase {i + 1} : ", end = '')
        if distance == None:
            print("start에서 시작해 end에 도착할 수 있는 경로가 존재하지 않습니다.")
        else:
            print(f"최단 거리는 {distance}입니다.")
            print(f"    최단 경로를 구하는 함수의 반환값 : {path}")
        #break
        # result = lab_map.find_shortest_path('start', 'end')
        # distance = result[0]
        # if distance == float('inf'):
        #     print(f"Testcase {i + 1}에서 start에서 시작해 end에 도착할 수 있는 경로가 존재하지 않습니다.")
        # else:
        #     print(f"Testcase {i + 1}의 최단 거리는 {distance}입니다.")
        #     print(f"    최단 경로를 구하는 함수의 반환값 : {result}")
        
        print()

if __name__ == "__main__":
    main()  