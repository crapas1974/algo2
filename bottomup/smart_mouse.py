import time
import random
import sys
sys.setrecursionlimit(10000)

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

def sm_min_time_memoization(i, j, t, memo=None):
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
            min_time = min(min_time, sm_min_time_memoization(i, k, t, memo) + sm_min_time_memoization(k, j, t, memo))
        memo[(i, j)] = min_time            
        return min_time
    except IndexError:
        return None

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper


# n번 지점까지의 최소 시간을 구하는 함수
@execute_time
def sm_min_time_bu(n, t):
    # 각 지점까지의 최소 시간을 저장하는 배열
    min_time = [float('inf')] * (n + 1)
    min_time[0] = 0
    # 1번 지점부터 n번 지점까지의 최소 시간을 차례로 계산한다.
    for i in range(1, n + 1):
        for j in range(i):
            # i번 지점 까지의 최적 경로가 j번 지점을 지나는 경우 
            # min_time[i]를 갱신한다.
            min_time[i] = min(min_time[i], min_time[j] + t[j][i])
    return min_time[n]

@execute_time
def sm_min_time_memoization_wrapper(i, j, t):
    return sm_min_time_memoization(i, j, t)

def main():

    # t = [[0, 4, 8, 14, 19], [-1, 0, 5, 11, 16], [-1, -1, 0, 5, 8], [-1, -1, -1, 0, 4], [-1, -1, -1, -1, 0]]
    # n = len(t) - 1
    # print(f"최소 이동 시간 : {sm_min_time_bu(n, t)}")
    #t = make_maze(1000)
    n = 200
    t = make_maze(n)
    print(t)
    print(f"상향식 접근법으로 계산한 최소 이동 시간 : {sm_min_time_bu(n, t)}")
    print(f"하향식 접근법으로 계산한 최소 이동 시간 : {sm_min_time_memoization_wrapper(0, n, t)}")

if __name__ == '__main__':
    main()