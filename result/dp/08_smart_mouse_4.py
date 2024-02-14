import time
import random
#from smart_mouse4_data import testcase_1, testcase_2, testcase_3, testcase_4, testcase_5
from smart_mouse_3_tc import testcases, get_large_testcase

# def make_distance(i, j):
#     distance = 0
#     for x in range(j - i):
#         distance += random.randint(-1, 1) + 3
#     return distance

# def make_maze(room_count):
#     maze = []
#     for i in range(room_count + 1):
#         ith_line = []
#         for j in range(room_count + 1):
#             if i > j:
#                 ith_line.append(-1)
#             elif i == j:
#                 ith_line.append(0)
#             else:
#                 ith_line.append(make_distance(i, j))
#         maze.append(ith_line)
#     return maze

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"    수행 시간: {end - start} 초")
        return result
    return wrapper

# @execute_time
# def find_min_time_td_wrapper(i, j, t):
#     return find_min_td_time(i, j, t)

# def find_mintime_path(i, j, t, memo = None, split = None):
#     is_first_call = False
#     if memo == None:
#         is_first_call = True
#         memo = {}
#     if split == None:
#         split = {}
#     if i == j:
#         return 0, split
#     elif i + 1 == j:
#         return t[i][j], split
#     if (i, j) in memo:
#         return memo[(i, j)], split
#     min_time = t[i][j]
#     split[(i, j)] = j
#     for k in range(i + 1, j):
#         min_time_before, _ = find_mintime_path(i, k, t, memo, split)
#         min_time_after, _ = find_mintime_path(k, j, t, memo, split)
#         if min_time > min_time_before + min_time_after:
#             min_time = min_time_before + min_time_after
#             split[(i, j)] = k
#     memo[(i, j)] = min_time
#     if is_first_call:        
#         return min_time, get_path(i, j, split)
#     else:
#         return min_time, split

# def find_min_time_td(i, j, t, memo=None):
#     if memo == None:
#         memo = {}
#     if (i, j) in memo:
#         return memo[(i, j)]
#     try:
#         if i == j:
#             return 0
#         elif i + 1 == j:
#             return t[i][j]
#         min_time = t[i][j]
#         for k in range(i + 1, j):
#             min_time = min(min_time, find_min_time_td(i, k, t, memo) + find_min_time_td(k, j, t, memo))
#         memo[(i, j)] = min_time            
#         return min_time
#     except IndexError:
#         return None

# def get_path(start, end, split):
#     if start == end:
#         return []
#     if start + 1 == end:
#         return [start, end]
#     mid = split[(start, end)]
#     if mid == end:
#         return [start, end]
    
#     return get_path(start, mid, split)[:-1] + get_path(mid, end, split)

@execute_time
def find_min_time(n, t):
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

def main():
    for i, tc in enumerate(testcases):
        print(f"Testcase {i + 1}")
        n = len(tc) - 1
        print(f"    최소 이동 시간 : {find_min_time(len(tc) - 1, tc)}")
        print()


    # for i, tc in enumerate(testcases):
    #     min_time = find_min_time(len(tc) - 1, tc)
    #     print(f"TC {i + 1} - 최소 이동 시간 : {min_time}")
    #     print()
        # min_time, path = find_mintime_path(0, len(tc) - 1, tc)
        # print(f"TC {i + 1} - 최소 이동 시간 : {min_time}")
        # path_str = map(str, path)
        # print(f"    최소 이동 경로 : {' -> '.join(path_str)}")
        # print()

    print("500개의 지점을 가진 미로에서의 테스트")
    large_tc = get_large_testcase()
    min_time = find_min_time(len(large_tc) - 1, large_tc)
    print(f"    최소 이동 시간 : {min_time}")

if __name__ == '__main__':
    main()