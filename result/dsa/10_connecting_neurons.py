class Graph:
    def __init__(self, number_of_vertices, edges):
        self.vertices = [i for i in range(number_of_vertices + 1)]
        self.edges = []
        for edge in edges:
            self.add_edge(edge[2], edge[0], edge[1])
    
    # method find : 경로 압축
    def find(self, vertex):
        if self.vertices[vertex] != vertex:
            self.vertices[vertex] = self.find(self.vertices[vertex])
        return self.vertices[vertex]
    
    # method union : 두 원소를 합치는 연산
    def union(self, neuron1, neuron2):
        neuron1 = self.find(neuron1)
        neuron2 = self.find(neuron2)
        if neuron1 < neuron2:
            self.vertices[neuron2] = neuron1
        else:
            self.vertices[neuron1] = neuron2

    def add_edge(self, start, end, cost):
        self.edges.append((start, end, cost))

    def min_connecting(self):
        self.edges.sort(key=lambda x: x[0])
        result_cost = 0
        result_edges = []
        for edge in self.edges:
            cost, neuron1, neuron2 = edge
            if self.find(neuron1) != self.find(neuron2):
                self.union(neuron1, neuron2)
                result_cost += cost
                result_edges.append((neuron1, neuron2))
        connected = self.is_fully_connected()
        if connected == False:
            return -1, []
        else:
            return result_cost, result_edges
    
    def min_connecting_cost(self):
        self.edges.sort(key=lambda x: x[0])
        result = 0
        for edge in self.edges:
            cost, neuron1, neuron2 = edge
            if self.find(neuron1) != self.find(neuron2):
                self.union(neuron1, neuron2)
                result += cost
        connected = self.is_fully_connected()
        if connected == False:
            return -1
        else:
            return result
    
    def is_fully_connected(self):
        root = self.find(1)
        for vertex in self.vertices[2:]:
            if self.find(vertex) != root:
                return False
        return True
        


def datafile_into_testcase():
    with open("artificial_neuron_data.txt", "r") as f:
        lines = f.readlines()
    start_lines = []
    end_lines = []
    number_of_neurons = []
    for i, line in enumerate(lines):
        if line.startswith("Testcase"):
            _, _, number_of_neuron = line.strip().split(" ")
            number_of_neurons.append(int(number_of_neuron))
            start_lines.append(i + 1)
        if line.startswith("End Testcase"):
            end_lines.append(i - 1)
    testcases = []
    for i in range(len(start_lines)):
        edges = []
        for j in range(start_lines[i], end_lines[i] + 1):
            edge = tuple(map(int, lines[j].strip().split(" ")))
            edges.append((int(edge[0]), int(edge[1]), int(edge[2])))
        #print(edges)
        #print(number_of_neurons[i])
        testcases.append((number_of_neurons[i], edges))
    
    return testcases
    

import random
def make_random_graph_data(vertex_cnt, edge_cnt):
    if edge_cnt > vertex_cnt * (vertex_cnt - 1) // 2:
        raise ValueError("Too many edges")
    edges = []
    for i in range(1, vertex_cnt + 1):
        for j in range(i + 1, vertex_cnt + 1):
            edges.append((random.randint(1, 100), i, j))
    random.shuffle(edges)
    return vertex_cnt, edges[:edge_cnt]

def main():
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = Graph(*tc)
        print(g.vertices)

        connecting_cost, connecting = g.min_connecting()
        if connecting_cost == -1:
            print(f"Testcase {i + 1} : 연결할 수 없습니다.")
        else:
            print(f"Testcase {i + 1} : {connecting_cost}")
            print(f"Testcase {i + 1} : {connecting}")
        print(g.vertices)
        print()
        if i == 4:
            break
    


if __name__ == "__main__":
    main()
# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def kruskal_with_edges(graph, n):
#     parent = [i for i in range(n + 1)]  # 부모 테이블 초기화
#     edges = []
#     result_cost = 0  # 최소 비용
#     result_edges = []  # 선택된 간선 목록

#     # 모든 간선에 대한 정보를 입력 받기
#     for a, b, cost in graph:
#         edges.append((cost, a, b))

#     # 간선을 비용순으로 정렬
#     edges.sort()

#     # 간선을 하나씩 확인하며
#     for edge in edges:
#         cost, a, b = edge
#         # 사이클이 발생하지 않는 경우에만 집합에 포함
#         if find(parent, a) != find(parent, b):
#             union(parent, a, b)
#             result_cost += cost
#             result_edges.append((a, b))  # 선택된 간선 추가

#     return result_cost, result_edges

# # 간선 정보 입력 (a, b, cost)
# graph = [
#     (1, 2, 3),
#     (2, 3, 2),
#     (3, 4, 1),
#     (4, 1, 2),
#     (1, 3, 4),
# #    (2, 4, 1)
# ]

# # 사무실의 수
# n = 4

# # 최소 신장 트리의 비용과 선택된 간선 목록 계산
# cost, selected_edges = kruskal_with_edges(graph, n)

# print("최소 비용:", cost)
# print("선택된 간선 목록:", selected_edges)

