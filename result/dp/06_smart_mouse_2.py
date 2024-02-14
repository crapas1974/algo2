from smart_mouse_2_tc import testcases
import time

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
    for i, tc in enumerate(testcases):
        print(f"Testcase {i + 1}")
        n = len(tc) - 1
        print(f"    최소 이동 시간 : {find_min_time_wrapper(0, n, tc)}")
        print()


if __name__ == '__main__':
    main()