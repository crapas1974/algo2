import random

class VirusMutations:
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0
        self.edge_count = 0

    def add_process(self, before, after):
        if before not in self.vertices:
            self.vertices[before] = []
            self.vertex_count += 1
        if after not in self.vertices:
            self.vertices[after] = []
            self.vertex_count += 1
        self.vertices[before].append(after)
        self.edge_count += 1

    def edge_count_in_graph(self):
        return self.edge_count
    
    def vertex_count_in_graph(self):
        return self.vertex_count
    
    def final_mutation_list(self, start, result=None):
        if result == None:
            result = []
        if start not in self.vertices:
            return result
        for vertex in self.vertices[start]:
            if vertex not in result:
                result.append(vertex)
                self.final_mutation_list(vertex, result)
        return result
    
    def print_graph(self):
        print("Testcase")
        edge_list = []
        for vertex in self.vertices:
            for edge in self.vertices[vertex]:
                edge_list.append((vertex, edge))
        random.shuffle(edge_list)
        for edge in edge_list:
            print(f"{edge[0]},{edge[1]}")


import hashlib
def hash4_from_list(input):
    input.sort()    
    return hashlib.md5(','.join(input).encode()).hexdigest()[:4]

def main():
    testcases = []
    with open('virus_mutation_data.txt', 'r') as f:
        lines = f.readlines()
    tc = None   
    for line in lines:
        if line[:8] == 'Testcase':
            if tc != None:
                testcases.append(tc)
            tc = []
        else:
            segments = line.strip().split(',')
            if len(segments) == 2 and segments[0] != segments[1]:
                tc.append((segments[0], segments[1]))
    
    if tc != None:
        testcases.append(tc)

    print("----- 방향성이 있는 경우 -----")
    for i, tc in enumerate(testcases):
        print("Testcase", i + 1)
        vc = VirusMutations()
        for before, after in tc:
            vc.add_process(before, after)
        print(f"    꼭짓점의 수 : {vc.vertex_count_in_graph()}")
        print(f"    변의 수 : {vc.edge_count_in_graph()}")
        virus_from_start = vc.final_mutation_list('start')
        print(f"    start에서 도달 가능한 변이 바이러스의 수 : {len(virus_from_start)}")
        print(f"    start에서 도달 가능한 변이 바이러스 목록의 간이 해시값 : {hash4_from_list(virus_from_start)}")
        print()

    print("----- 방향성이 없는 경우 -----")
    for i, tc in enumerate(testcases):
        print("Testcase", i + 1)
        vc = VirusMutations()
        for before, after in tc:
            vc.add_process(before, after)
            vc.add_process(after, before)
        virus_from_start = vc.final_mutation_list('start')
        print(f"    start에서 도달 가능한 변이 바이러스의 수 : {len(virus_from_start)}")
        print(f"    start에서 도달 가능한 변이 바이러스 목록의 간이 해시값 : {hash4_from_list(virus_from_start)}")
        print()    


    


if __name__ == "__main__":
    main()