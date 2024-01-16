import time
def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper


import heapq
class WeightedGraph:
    # 초기화 메소드
    #   is_directed: 방향성 여부를 나타내는 boolean 값
    def __init__(self, is_directed=True):
        # 그래프를 표현하는 딕셔너리로 Key는 꼭짓점, Value는 인접한 꼭짓점들의 리스트
        self.vertices = {}
        # 방향성
        self.is_directed = is_directed
        # 변의 수
        self.edge_count = 0
        # 꼭짓점의 수
        self.vertex_count = 0
        # 가중치 룩업 딕셔너리
        #   룩업 딕셔너리는 Key가 (꼭짓점1, 꼭짓점2)인 튜플이고,
        #   Value는 2개 이상의 가중치를 저장할 수 있도록 가중치들의 리스트로 구성된다.
        self.weight_lookup = {}

    # 변을 추가하는 메소드
    #   vertex1 : 변의 한쪽 끝 꼭짓점이며, 방향성 그래프의 경우 시작점을 의미한다.
    #   vertex2 : 변의 다른쪽 끝 꼭짓점이며, 방향성 그래프의 경우 끝점을 의미한다.
    def add_edge(self, vertex1, vertex2, weight):
        # 가중치의 값이 양의 숫자인지 확인
        if weight <= 0:
            print("가중치는 양의 숫자여야 합니다.")
            return False
        # 그래프에 꼭짓점 추가
        self.__add_vertices([vertex1, vertex2])
        # 변 추가
        if self.is_directed:
            # 그래프가 방향성 그래프라면 지정된 순서의 방향의 변만 추가한다.
            # 만약 변이 이미 존재하면 변은 추가하지 않고 가중치 룩업 테이블에만 이를 추가한다.
            if vertex2 not in self.vertices[vertex1]:
                self.vertices[vertex1].append(vertex2)
            # 가중치 추가
            self.__add_weight(vertex1, vertex2, weight)
        else:
            # 그래프가 비방향성 그래프라면 양쪽 방향의 변을 모두 추가한다.
            # 이때 변이 이미 존재하면 변은 추가하지 않고 가중치 룩업 테이블에만 이를 추가한다.
            if vertex2 not in self.vertices[vertex1]:
                self.vertices[vertex1].append(vertex2)
                self.vertices[vertex2].append(vertex1)
            # 가중치 추가
            #   그래프 딕셔너리와 달리 룩업 테이블은 비방향성 그래프에서는
            #   꼭짓점1과 꼭짓점2의 순서와 무관하게 하나만 저장한다.
            self.__add_weight(max(vertex1, vertex2),
                              min(vertex1, vertex2), weight)

        # 방향성 여부에 따라 변을 몇 개 추가했던 간에 실질적으로 변은 1개 추가되었다.
        self.edge_count += 1
        return True

    def __add_weight(self, vertex1, vertex2, weight):
        if (vertex1, vertex2) not in self.weight_lookup:
            self.weight_lookup[(vertex1, vertex2)] = [weight]
        else:
            self.weight_lookup[(vertex1, vertex2)].append(weight)

    # 꼭짓점을 추가하는 Private 메소드
    #   vertices : 추가할 꼭짓점들의 리스트
    #   만약 그래프에 이미 해당 꼭짓점이 존재한다면, 추가하지 않는다.
    def __add_vertices(self, vertices):
        for vertex in vertices:
            if vertex not in self.vertices:
                self.vertex_count += 1
                self.vertices[vertex] = []

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, "->" , end="")
            for adjacent_vertex in self.vertices[vertex]:
                print(f" {adjacent_vertex}{self.weight_lookup[(vertex, adjacent_vertex)]}", end="")
            print()

    # dfs를 사용해 start_vertex에서 end_vertex까지의 모든 경로를 찾는 메소드
    # 현재 경로에서 추가할 수 있는 모든 경로 중 하나를 선택해 재귀 호출한다.
    # 이러한 방식으로 재귀 호출을 하면, 너비보다 깊이를 우선으로 경로를 탐색하게 된다.
    def find_all_path(self, start_vertex, end_vertex, path=None):
        # 탐색을 시작할 때, 즉 path가 None인 경우 현재 지점으로 구성된 경로를 생성한다.
        if path is None:
            path = [start_vertex]

        # 재귀 호출 시점의 시작 지점이 목표 지점과 동일하면 경로가 완성된 것이다.
        if start_vertex == end_vertex:
            return [path]

        results = []
        # 현재 지점에서 이동 가능한 모든 다른 지점에 대해서
        for next in self.vertices[start_vertex]:
            # 다음 탐색할 지점이 이미 지나온 지점이면 해당 경로는 배제한다.
            if next not in path:
                # 다음 탐색 지점의 경로를 만들어 재귀 호출한다.
                result = self.find_all_path(
                    next, end_vertex, path + [next])
                # 재귀 호출의 결과를 취합한다.
                results += result
        return results
    
    def get_weight(self, vertex1, vertex2):
        return min(self.weight_lookup[(vertex1, vertex2)])
    
    def find_fast_best_cost(self, start_vertex):
        # 최단 거리를 저장하는 딕셔너리
        distances = {}
        # 최단 거리를 초기화한다.
        for vertex in self.vertices:
            distances[vertex] = float('inf')
        distances[start_vertex] = 0
        # 아직 방문하지 않은 꼭짓점들의 집합
        unvisited = set(self.vertices.keys())

        # 방문하지 않은 꼭짓점에 대해서
        while unvisited:
            # 최단 거리를 갖는 꼭짓점을 찾는다.
            current_vertex = None
            current_distance = float('inf')
            for vertex in unvisited:
                if distances[vertex] < current_distance:
                    current_distance = distances[vertex]
                    current_vertex = vertex
            # unvisited가 남아 있는 경우에도 current_vertex를 찾지 못한 경우는
            # start_vertex에서 연결되지 않았다는 뜻이다.
            if current_vertex == None:
                break
            # 최단 거리를 갖는 꼭짓점과 인접한 꼭짓점들의 거리를 갱신한다.
            for neighbor_vertex in self.vertices[current_vertex]:
                if neighbor_vertex in unvisited:
                    new_distance = distances[current_vertex] + \
                        self.get_weight(current_vertex, neighbor_vertex)
                    if new_distance < distances[neighbor_vertex]:
                        distances[neighbor_vertex] = new_distance

            # 이번에 방문한 꼭짓점을 unvisited에서 제거한다.
            unvisited.remove(current_vertex)

        return distances
    
    def find_all_path_with_cost(self, start_vertex, end_vertex, path=None, cost=0):
        # 탐색을 시작할 때, 즉 path가 None인 경우 현재 지점으로 구성된 경로를 생성한다.
        if path is None:
            path = [start_vertex]

        # 재귀 호출 시점의 시작 지점이 목표 지점과 동일하면 경로가 완성된 것이다.
        if start_vertex == end_vertex:
            return [(path, cost)]

        results = []
        # 현재 지점에서 이동 가능한 모든 다른 지점에 대해서
        for next in self.vertices[start_vertex]:
            # 다음 탐색할 지점이 이미 지나온 지점이면 해당 경로는 배제한다.
            if next not in path:
                next_cost = cost + min(self.weight_lookup[(start_vertex, next)])
                # 다음 탐색 지점의 경로를 만들어 재귀 호출한다.
                result = self.find_all_path_with_cost(
                    next, end_vertex, path + [next], next_cost)
                # 재귀 호출의 결과를 취합한다.
                results += result
        return results
    
    @execute_time
    def find_fast_best_path(self, start_vertex, end_vertex):
        # 최단 거리를 저장하는 딕셔너리
        distances = {}
        # 최단 경로를 저장하는 딕셔너리
        paths = {}
        # 최단 거리를 초기화한다.
        for vertex in self.vertices:
            distances[vertex] = float('inf')
        distances[start_vertex] = 0
        # 최단 경로를 초기화한다.
        paths[start_vertex] = [start_vertex]
        # 아직 방문하지 않은 꼭짓점들의 집합
        unvisited = set(self.vertices.keys())
        # 최단 거리를 갖는 꼭짓점을 찾는다.
        while unvisited:
            # 최단 거리를 갖는 꼭짓점을 찾는다.
            current_vertex = None
            current_distance = float('inf')
            for vertex in unvisited:
                if distances[vertex] < current_distance:
                    current_distance = distances[vertex]
                    current_vertex = vertex
            # unvisited가 남아 있는 경우에도 current_vertex를 찾지 못한 경우는
            # start_vertex에서 연결되지 않았다는 뜻이다.
            if current_vertex == None:
                break
            # 최단 거리를 갖는 꼭짓점과 인접한 꼭짓점들의 거리를 갱신한다.
            for vertex in self.vertices[current_vertex]:
                if vertex in unvisited:
                    new_distance = distances[current_vertex] + \
                        self.get_weight(current_vertex, vertex)
                    if new_distance < distances[vertex]:
                        distances[vertex] = new_distance
                        paths[vertex] = paths[current_vertex] + [vertex]

            # 이번에 방문한 꼭짓점을 unvisited에서 제거한다.
            unvisited.remove(current_vertex)
        # paths에 end_vertex가 없으면 start_vertex에서 end_vertex로 가는 경로가 없다는 뜻이다.
        if end_vertex not in paths:
            return None, None
        return distances[end_vertex], paths[end_vertex]

    @execute_time
    def find_faster_best_path(self, start_vertex, end_vertex):
        # 시작 노드에서 각 노드까지의 최단 거리를 저장하는 딕셔너리
        distances = {node: float('inf') for node in self.vertices}
        distances[start_vertex] = 0
        
        # 최단 경로를 저장하는 딕셔너리
        paths = {}
        paths[start_vertex] = [start_vertex]
        # 거리가 정해졌지만 방문하지 않은 노드를 저장하는 우선순위 큐
        # 처음에 방문해야 하는 start_vertex를 추가해 초기화한다.
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            # 현재까지의 최단 거리와 노드를 가져옴
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # 현재 노드에서 인접한 노드들을 순회
            for neighbor_vertex in self.vertices[current_vertex]:
                distance = current_distance + self.get_weight(current_vertex, neighbor_vertex)
 
                # 더 짧은 경로를 찾은 경우, 최단 거리를 업데이트하고 우선순위 큐에 추가
                if distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_vertex))
                    paths[neighbor_vertex] = paths[current_vertex] + [neighbor_vertex]
        
        # paths에 end_vertex가 없으면 start_vertex에서 end_vertex로 가는 경로가 없다는 뜻이다.
        if end_vertex not in paths:
            return None, None
        return distances[end_vertex], paths[end_vertex]
    

    def find_best_path(self, start_vertex, end_vertex):
        results = self.find_all_path_with_cost(start_vertex, end_vertex)
        min_cost = float('inf')
        min_path = None
        for path, cost in results:
            if cost < min_cost:
                min_cost = cost
                min_path = path
        return min_cost, min_path


def main():
    graph = WeightedGraph(True)
    graph.add_edge(0, 1, 80)
    graph.add_edge(1, 0, 80)
    graph.add_edge(0, 2, 190)
    graph.add_edge(2, 0, 190)
    graph.add_edge(1, 2, 100)
    graph.add_edge(2, 1, 100)
    graph.add_edge(2, 3, 50)
    graph.add_edge(3, 4, 55)
    graph.add_edge(4, 2, 40)
    graph.print_graph()

if __name__ == "__main__":
    main()