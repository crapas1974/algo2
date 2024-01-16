import random

def make_distance(i, j):
    distance = 0
    for x in range(j - i):
        distance += random.randint(-1, 1) + 3
    return distance

def make_maze(n):
    maze = []
    for i in range(n + 1):
        ith_line = []
        for j in range(n + 1):
            if i > j:
                ith_line.append(-1)
            elif i == j:
                ith_line.append(0)
            else:
                ith_line.append(make_distance(i, j))
        maze.append(ith_line)
    return maze

def main():
    n = 5
    maze = make_maze(n)
    print(maze)

if __name__ == '__main__':
    main()