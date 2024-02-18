class Graph:
    def __init__(self, number_of_vertices, edges):
        self.costs = [[float('inf')] * (number_of_vertices) for _ in range(number_of_vertices)]
        for i in range(number_of_vertices):
            self.costs[i][i] = 0
        for edge in edges:
            start, end, cost = edge
            self.costs[start - 1][end - 1] = cost
            self.costs[end - 1][start - 1] = cost
        self.number_of_vertices = number_of_vertices

    def min_connecting_costs(self):
        dp = []
        for x in self.costs:
            dp.append(x.copy())        
        for k in range(self.number_of_vertices):
            for i in range(self.number_of_vertices):
                for j in range(self.number_of_vertices):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        result = ','.join([','.join(map(str, x)) for x in dp]).replace('inf', 'X')
        return result
    
    def min_connecting_costs_and_path(self, neuron1, neuron2):
        dp = []
        for x in self.costs:
            dp.append(x.copy())
        next_in_shortest_path = [[-1 if self.costs[i][j] == float('inf') else j for j in range(self.number_of_vertices)] for i in range(self.number_of_vertices)]
        for k in range(self.number_of_vertices):
            for i in range(self.number_of_vertices):
                for j in range(self.number_of_vertices):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        next_in_shortest_path[i][j] = next_in_shortest_path[i][k]
        result = ','.join([','.join(map(str, x)) for x in dp]).replace('inf', 'X')

        connecting_cost_n1_to_n2 = dp[neuron1 - 1][neuron2 - 1]
        connecting_cost_n_to_1 = dp[self.number_of_vertices - 1][0]
        if connecting_cost_n1_to_n2 == float('inf'):
            connecting_cost_n1_to_n2 = -1
            path_n1_to_n2 = []
        else:
            path_n1_to_n2 = self._make_path(next_in_shortest_path, neuron1, neuron2)
        
        if connecting_cost_n_to_1 == float('inf'):
            connecting_cost_n_to_1 = -1
            path_n_to_1 = []
        else:
            path_n_to_1 = self._make_path(next_in_shortest_path, self.number_of_vertices, 1)

        return result, connecting_cost_n1_to_n2, path_n1_to_n2, connecting_cost_n_to_1, path_n_to_1

    def _make_path(self, next_in_shortest_path, start, end):
        path = [start]
        while start != end:
            start = next_in_shortest_path[start - 1][end - 1] + 1
            path.append(start)
        return path
    
def datafile_into_testcase():
    with open("artificial_neuron_data_2.txt", "r") as f:
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
        testcases.append((number_of_neurons[i], edges))    
    return testcases

import hashlib
def hash4(input):
    return hashlib.sha256(str(input).encode()).hexdigest()[:4]

def main():
    bonus = False
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = Graph(*tc)
        # 두 신경 세포 쌍의 최소 연결 비용만 출력하는 본 문제의 경우
        if not bonus:
            connecting_cost = g.min_connecting_costs()
            print(f"Testcase {i + 1}의 연결 비용은 {hash4(connecting_cost)}입니다.")
        # 두 신경 세포 쌍의 최소 연결 비용과 지정된 쌍의 연결 방법을 출력하는 보너스 과제의 경우
        else:
            connecting_cost, cost_2_4, path_2_4, cost_n_1, path_n_1 = g.min_connecting_costs_and_path(2, 4)
            print(f"Testcase {i + 1}의 연결 비용은 {hash4(connecting_cost)}입니다.")
            if cost_2_4 != -1:
                print(f"    이 그래프에서 최소의 비용으로 2번 세포와 4번 세포를 연결할 때의 최소 비용은 {cost_2_4}이며, 이 때의 연결은 다음 세포를 차례대로 연결한 것입니다.\n    {path_2_4}")
            else:
                print(f"    이 그래프에서 2번 세포와 4번 세포를 연결할 수 없습니다.")
            if cost_n_1 != -1:
                print(f"    이 그래프에서 최소의 비용으로 N번 세포와 1번 세포를 연결할 때의 최소 비용은 {cost_n_1}이며, 이 때의 연결은 다음 세포를 차례대로 연결한 것입니다.\n    {path_n_1}")
            else:
                print(f"    이 그래프에서 N번 세포와 1번 세포를 연결할 수 없습니다.")
        print()

if __name__ == "__main__":
    main()
