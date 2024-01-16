import time
from maze_test_data import make_maze

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def mt_wrapper(i, j, t):
    return sm_min_time_memoization(i, j, t)

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

def main():
    for i in range(5):
        n = (i + 1) * 4
        print(f"n = {n}인 경우")
        t = make_maze(n)
        print(f"최소 이동 시간 : {mt_wrapper(0, n, t)}")

if __name__ == '__main__':
    main()