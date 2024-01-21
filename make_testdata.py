import random
def make_random_graph(vertex_cnt, edge_cnt, d_min, d_max):
    vertices = ['start', 'end']    
    for i in range(vertex_cnt - 2):
        # make 5 length random word with lowercase alphabet only
        while True:
            name = ''
            for j in range(5):
                name += chr(ord('a') + random.randint(0, 25))
            if name not in vertices and name not in ['start', 'end']:
                vertices.append(name)
                break
    edges = []
    while True:
        start = random.choice(vertices)
        end = random.choice(vertices)
        if start == end:
            continue
        if start > end:
            start, end = end, start
        if (start, end) not in edges and (start, end) != ('end', 'start'):
            edges.append((start, end))
        if len(edges) == edge_cnt:
            break

    for start, end in edges:
        distance = random.randint(d_min, d_max)
        print(start, end, distance)

make_random_graph(200, 10000, 100, 150)
# 52C2
# 100C2 
# 150C2=