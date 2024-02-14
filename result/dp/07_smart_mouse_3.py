import time
from smart_mouse_2_tc import testcases
from smart_mouse_3_tc import get_large_testcase

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"    수행 시간: {end - start} 초")
        return result
    return wrapper

def find_mintime_path(i, j, t, memo = None, split = None):
    is_first_call = False
    if memo == None:
        is_first_call = True
        memo = {}
    if split == None:
        split = {}
    if i == j:
        return 0, split
    elif i + 1 == j:
        return t[i][j], split
    if (i, j) in memo:
        return memo[(i, j)], split
    min_time = t[i][j]
    split[(i, j)] = j
    for k in range(i + 1, j):
        min_time_before, _ = find_mintime_path(i, k, t, memo, split)
        min_time_after, _ = find_mintime_path(k, j, t, memo, split)
        if min_time > min_time_before + min_time_after:
            min_time = min_time_before + min_time_after
            split[(i, j)] = k
    memo[(i, j)] = min_time
    if is_first_call:        
        return min_time, get_path(i, j, split)
    else:
        return min_time, split

def get_path(start, end, split):
    if start == end:
        return []
    if start + 1 == end:
        return [start, end]
    mid = split[(start, end)]
    if mid == end:
        return [start, end]
    
    return get_path(start, mid, split)[:-1] + get_path(mid, end, split)

def main():
    for i, tc in enumerate(testcases):
        min_time, path = find_mintime_path(0, len(tc) - 1, tc)
        print(f"TC {i + 1} - 최소 이동 시간 : {min_time}")
        path_str = map(str, path)
        print(f"    최소 이동 경로 : {' -> '.join(path_str)}")
        print()
    large_tc = get_large_testcase()
    st = time.time()
    min_time, path = find_mintime_path(0, len(large_tc) - 1, large_tc)
    print(time.time() - st)
    print(f"Large TC - 최소 이동 시간 : {min_time}")
    path_str = map(str, path)

if __name__ == '__main__':
    main()