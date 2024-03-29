class Graph:
    def __init__(self, number_of_vertices, edges):
        self.parents = [i for i in range(number_of_vertices + 1)]
        self.edges = []
        for edge in edges:
            self.add_edge(edge[2], edge[0], edge[1])
    
    def add_edge(self, start, end, cost):
        self.edges.append((start, end, cost))

    def min_connecting(self):
        self.edges.sort(key=lambda x: x[0])
        result_cost = 0
        result_edges = []
        for edge in self.edges:
            cost, neuron1, neuron2 = edge
            if self._find(neuron1) != self._find(neuron2):
                self._union(neuron1, neuron2)
                result_cost += cost
                if neuron1 > neuron2:
                    neuron1, neuron2 = neuron2, neuron1
                result_edges.append((neuron1, neuron2))
        connected = self._is_fully_connected()
        if connected == False:
            return -1, []
        else:
            return result_cost, sorted(result_edges)
    
    def min_connecting_cost(self):
        self.edges.sort(key=lambda x: x[0])
        result = 0
        for edge in self.edges:
            cost, neuron1, neuron2 = edge
            if self._find(neuron1) != self._find(neuron2):
                self._union(neuron1, neuron2)
                result += cost
        connected = self._is_fully_connected()
        if connected == False:
            return -1
        else:
            return result
    
    def _is_fully_connected(self):
        mst_root = self._find(1)
        for parent in self.parents[2:]:
            if self._find(parent) != mst_root:
                return False
        return True

    def _find(self, vertex):
        if self.parents[vertex] != vertex:
            self.parents[vertex] = self._find(self.parents[vertex])
        return self.parents[vertex]
    
    def _union(self, neuron1, neuron2):
        neuron1 = self._find(neuron1)
        neuron2 = self._find(neuron2)
        if neuron1 < neuron2:
            self.parents[neuron2] = neuron1
        else:
            self.parents[neuron1] = neuron2


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
        testcases.append((number_of_neurons[i], edges))
    
    return testcases
    
def main():
    bonus = True
    testcases = datafile_into_testcase()
    for i, tc in enumerate(testcases):
        g = Graph(*tc)
        
        # 최소 연결 비용만 출력하는 본 문제의 경우
        if not bonus:
            connecting_cost = g.min_connecting_cost()
            if connecting_cost == -1:
                print(f"Testcase {i + 1}의 신경 세포는 완전하게 연결할 수 없습니다.")
            else:
                print(f"Testcase {i + 1}의 연결 비용은 {connecting_cost}입니다.")

        # 최소 연결 비용과 연결 방법을 출력하는 보너스 과제의 경우
        else:
            connecting_cost, connecting = g.min_connecting()
            if connecting_cost == -1:
                print(f"Testcase {i + 1}의 신경 세포는 완전하게 연결할 수 없습니다.")
            else:
                print(f"Testcase {i + 1}의 연결 비용은 {connecting_cost}입니다.")
                print(f"    이 그래프에서 최소의 비용으로 연결하기 위해서는 다음 번호의 신경 세포를 연결합니다.\n    {connecting}")
        
        print()
    


if __name__ == "__main__":
    main()
