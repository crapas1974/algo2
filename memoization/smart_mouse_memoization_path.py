
def sm_min_time_path_memoization(i, j, t, memo = None, split = None):
    if memo == None:
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
    # split의 초기값은 j (쉬지 않고 가는게 가장 빠른 경우)
    split[(i, j)] = j
    for k in range(i + 1, j):
        min_time_before, _ = sm_min_time_path_memoization(i, k, t, memo, split)
        min_time_after, _ = sm_min_time_path_memoization(k, j, t, memo, split)
        if min_time > min_time_before + min_time_after:
            min_time = min_time_before + min_time_after
            # 들렀다 가는게 더 빠르면, 가장 빠른 k로 업데이트
            split[(i, j)] = k
#        if min_time > sm_min_time_path_memoization(i, k, t, memo, split) + sm_min_time_path_memoization(k, j, t, memo, split):
#            min_time = sm_min_time_path_memoization(i, k, t, memo, split) + sm_min_time_path_memoization(k, j, t, memo, split)
            # 들렀다 가는게 더 빠르면, 가장 빠른 k로 업데이트
#            split[(i, j)] = k
    memo[(i, j)] = min_time
    return min_time, split

def get_path(i, j, split):
    if i == j:
        return []
    if i + 1 == j:
        return [(i, j)]
    k = split[(i, j)]
    if k == j:
        return [(i, j)]
    return get_path(i, k, split) + get_path(k, j, split)

def main():
#    t_4 = [[0, 4, 8, 14, 19], [-1, 0, 5, 11, 16], [-1, -1, 0, 5, 8], [-1, -1, -1, 0, 4], [-1, -1, -1, -1, 0]]
    t_4 = []
    t_20 = [[0, 5, 6, 12, 24, 25, 36, 42, 48, 27, 30, 55, 36, 52, 70, 75, 64, 51, 108, 76, 80], [-1, 0, 5, 6, 15, 20, 30, 30, 21, 40, 45, 40, 33, 60, 39, 70, 60, 80, 51, 72, 76], [-1, -1, 0, 3, 8, 12, 20, 15, 18, 42, 24, 45, 50, 55, 36, 65, 42, 45, 96, 51, 72], [-1, -1, -1, 0, 5, 8, 15, 24, 25, 18, 42, 24, 27, 60, 55, 36, 39, 42, 90, 80, 85], [-1, -1, -1, -1, 0, 4, 8, 12, 12, 30, 24, 28, 48, 27, 30, 44, 48, 52, 70, 90, 48], [-1, -1, -1, -1, -1, 0, 3, 12, 12, 20, 15, 30, 42, 48, 27, 50, 44, 36, 65, 70, 75], [-1, -1, -1, -1, -1, -1, 0, 5, 6, 18, 20, 20, 30, 21, 40, 27, 40, 33, 72, 52, 84], [-1, -1, -1, -1, -1, -1, -1, 0, 5, 10, 15, 16, 20, 24, 42, 24, 54, 30, 44, 48, 39], [-1, -1, -1, -1, -1, -1, -1, -1, 0, 5, 12, 12, 24, 25, 24, 42, 24, 36, 40, 44, 60], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 3, 8, 15, 12, 25, 18, 21, 40, 54, 40, 66], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 4, 12, 9, 16, 30, 36, 35, 32, 36, 30], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 3, 8, 12, 12, 15, 18, 42, 48, 45], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5, 10, 18, 20, 30, 36, 35, 48], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 3, 6, 12, 20, 20, 24, 21], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5, 12, 9, 20, 25, 24], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5, 12, 15, 12, 20], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 6, 8, 12, 16], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 4, 10, 12], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 6, 10], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
    print("t_4의 경우")
    min_time, split = sm_min_time_path_memoization(0, 4, t_4)
    print(f"최소 이동 시간 : {min_time}")
    path = get_path(0, 4, split)
    path_str = "0"
    for (_, end) in path:
        path_str += f", {end}"
    print(f"경로 : {path_str}")
    print("t_20의 경우")
    min_time, split = sm_min_time_path_memoization(0, 20, t_20)
    path = get_path(0, 20, split)
    path_str = "0"
    for (_, end) in path:
        path_str += f", {end}"
    print(f"경로 : {path_str}")

if __name__ == '__main__':
    main()
