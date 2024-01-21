import time
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

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"    수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def find_min_time_wrapper(i, j, t):
    return find_min_time(i, j, t)

def find_min_time(i, j, t, memo=None):
    if memo == None:
        memo = {}
    if (i, j) in memo:
        return memo[(i, j)]
    try:
        if i == j:
            return 0
        elif i + 1 == j:
            return t[i][j]
        min_time = t[i][j]
        for k in range(i + 1, j):
            min_time = min(min_time, find_min_time(i, k, t, memo) + find_min_time(k, j, t, memo))
        memo[(i, j)] = min_time            
        return min_time
    except IndexError:
        return None

def main():
    for i in range(4):
        n = i * 10 + 20
        print(f"n = {n}인 경우")
        t = make_maze(n)
        print(t)
        print(f"    최소 이동 시간 : {find_min_time_wrapper(0, n, t)}")
        print()
    t = make_maze(100)    
    print(f"testcase_6 = {t}")
    t = make_maze(200)
    print(f"testcase_7 = {t}")
    

if __name__ == '__main__':
    main()