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

    def find_shortest_distance(self, start, end, visited = None, memo = None):
        vertices = list(self.vertices.keys())
        distance = {}
        for (v1, v2), v in self.distance_table.items():
            if v1 < v2:
                distance[(v1, v2)] = v
            else:
                distance[(v2, v1)] = v
#            distance[k] = v

        # for vertex in self.vertices:
        #     distance[vertex] = float('inf')

        while True:
            current_distance = {}            
            for i in range(len(vertices)):
                for j in range(i + 1, len(vertices)):
                    v1 = vertices[i]
                    v2 = vertices[j]                    
                    #distance_v1_v2 = float('inf')
                                    
                    distance_v1_v2 = self.get_distance(v1, v2)
                    if distance_v1_v2 == None:
                        distance_v1_v2 = float('inf')
#                    print(v1, v2, distance_v1_v2)    
                    # if (v1, v2) in self.distance_table:
                    #     distance_v1_v2 = self.get_distance(v1, v2)

                    for inter_vertex in vertices:
                        if inter_vertex == v1 or inter_vertex == v2:
                            continue
                        else:
                            distance1 = None
                            if (v1, inter_vertex) in distance:
                                distance1 = distance[(v1, inter_vertex)]
                            elif (inter_vertex, v1) in distance:
                                distance1 = distance[(inter_vertex, v1)]
                            distance2 = None
                            if (inter_vertex, v2) in distance:
                                distance2 = distance[(inter_vertex, v2)]
                            elif (v2, inter_vertex) in distance:
                                distance2 = distance[(v2, inter_vertex)]

                            # distance_1 = self.get_distance(v1, inter_vertex)
                            # distance_2 = self.get_distance(inter_vertex, v2)
                            if distance1 != None and distance2 != None:
                                #print(" mid : ", inter_vertex, distance_v1_v2, distance1, distance2)
                                distance_v1_v2 = min(distance_v1_v2, distance1 + distance2)
                    if distance != float('inf'):
                        if v1 < v2:
                            current_distance[(v1, v2)] = distance_v1_v2
                        else:
                            current_distance[(v2, v1)] = distance_v1_v2
            is_updated = False
            if len(distance) != len(current_distance):
                is_updated = True
            else:
                for k, v in distance.items():
                    if v != current_distance[k]:
                        is_updated = True
                        break
            if is_updated == False:
                break
            distance = current_distance
        
#        print(distance)
        print("result")
        if ('start', 'end') in distance:
            print(distance[('start', 'end')])
        else:
            print(distance[('end', 'start')])
        
                  
        #print(distance[('end', 'start')])


        print()
#        print(self.get_distance('start', 'end'))

            # if len(distance) == len(current_distance):
            #     for k, v in distance.items():
            #         if k in current_distance and 

            #         distance[(v1, v2)] = distance
            #         #(v1, x), (x, v2)

            # current_distance = {}
            # for k, v in distance.items():




        # if visited == None:
        #     visited = [end]
        # if memo == None:
        #     memo = {}
        # if start == end:
        #     return 0
        # if (start, end) in memo:
        #     return memo[(start, end)]
        # distance = float('inf')
        # min_distance = float('inf')
        # for neighbor in self.vertices[end]:
        #     if neighbor not in visited:
        #         distance = self.find_shortest_distance(start, neighbor, visited + [neighbor], memo) + self.get_distance(neighbor, end)
        #         if distance < min_distance:
        #             min_distance = distance
        # #memo[(start, end)] = min_distance
        
        # return min_distance
    


    # def find_shortest_distance(self, start, end, visited=None, memo=None):
    #     if visited is None:
    #         visited = [end]
    #     if memo is None:
    #         memo = {}
    #     if start == end:
    #         return 0
    #     if (start, end) in memo:
    #         return memo[(start, end)]
    #     distance = float('inf')
    #     min_distance = float('inf')
    #     for neighbor in self.vertices[end]:
    #         if neighbor not in visited:
    #             distance = self.find_shortest_distance(start, neighbor, visited + [neighbor], memo) + self.get_distance(neighbor, end)
    #             if distance < min_distance:
    #                 min_distance = distance
    #     memo[(start, end)] = min_distance
    #     return min_distance
    
    # def find_shortest_distance(self, start, end, visited = None):
    #     if visited == None:
    #         visited = []
    #     if start == end:
    #         return 0
    #     distance = float('inf')
    #     min_distance = float('inf')
    #     for neighbor in self.vertices[end]:
    #         if neighbor not in visited:
    #             distance = self.find_shortest_distance(start, neighbor, visited + [neighbor]) + self.get_distance(neighbor, end)
    #             if distance < min_distance:
    #                 min_distance = distance
    #     return min_distance

    def find_shortest_path(self, start, end, visited = None, memo = None):
        if memo == None:
            memo = {}    
        if visited == None:
            visited = [end]
        if start == end:
            return 0, [visited]
        if (start, end) in memo:
            return memo[(start, end)]
        
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
        #memo[(start, end)] = (min_distance, min_path)
        return (min_distance, min_path)
#        return (min_distance, min_path)


def main():
    with open("dp_tc2.txt", "r") as f:
        lines = f.readlines()

    case_start_lines = []
    for i, line in enumerate(lines):
        if line.startswith("Testcase"):
            case_start_lines.append(i)
    case_start_lines.append(len(lines))

    for i in range(len(case_start_lines) - 1):                
        print(f"TC {i + 1}")
        lab_map = Graph()
        for j in range(case_start_lines[i] + 1, case_start_lines[i + 1]):
            line = lines[j].strip()
            if line == '':
                continue
            vertex1, vertex2, distance = line.split(' ')
            distance = int(distance)
            lab_map.add_edge(vertex1, vertex2, distance)
        sd = lab_map.find_shortest_distance('start', 'end')
        print(sd)
        
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