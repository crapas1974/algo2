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

def make_random_seq(size, vocab = None):
    if vocab == None:
        vocab = ['A', 'C', 'G', 'T']
    seq = ''
    for _ in range(size):
        seq += random.choice(vocab)
    return seq

#print(make_random_seq(50))
vocab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(make_random_seq(1000, vocab))
#make_random_graph(200, 10000, 100, 150)
# 52C2
# 100C2 
# 150C2=
for _ in range(1000):
    print(make_random_seq(4))
for _ in range(20):
    for _ in range(10):
        print(make_random_seq(4), "-")
    print("print")