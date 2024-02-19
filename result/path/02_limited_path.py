def path_count_bottom_up(m, n, blocks):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for block in blocks:        
        dp[block[0] - 1][block[1] - 1] = -1
    
    for i in range(1, m):
        if dp[i][0] == 0:
            dp[i][0] = dp[i - 1][0]
    for j in range(1, n):
        if dp[0][j] == 0:
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j] if dp[i - 1][j] != -1 else 0
                dp[i][j] += dp[i][j - 1] if dp[i][j - 1] != -1 else 0
    return dp[m - 1][n - 1]

def count_and_path_bottom_up(m, n, blocks):
    dp  = [[0] * n for _ in range(m)]
    paths = [[None] * n for _ in range(m)]
    dp[0][0] = 1
    paths[0][0] = ['']
    for block in blocks:
        dp[block[0] - 1][block[1] - 1] = -1
        paths[block[0] - 1][block[1] - 1] = []
    for i in range(m):
        if dp[i][0] == 0:
            dp[i][0] = dp[i - 1][0]
            if dp[i][0] != -1:
                paths[i][0] = ['R' * i]
            else:
                paths[i][0] = []
    for j in range(n):
        if dp[0][j] == 0:
            dp[0][j] = dp[0][j - 1]
            if dp[0][j] != -1:
                paths[0][j] = ['D' * j]
            else:
                paths[0][j] = []
    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j] == 0:
                up_path = []
                left_path = []
                if dp[i - 1][j] != -1:
                    dp[i][j] = dp[i - 1][j]
                    left_path = [path + 'R' for path in paths[i - 1][j]]
                if dp[i][j - 1] != -1:
                    dp[i][j] += dp[i][j - 1]
                    up_path = [path + 'D' for path in paths[i][j - 1]]
                paths[i][j] = left_path + up_path
                if dp[i][j] == 0:
                    dp[i][j] = -1
                    paths[i][j] = []
    return dp[m - 1][n - 1], paths[m - 1][n - 1]

def path_count_top_down(m, n, blocks, memo = None):
    if memo == None:
        memo = {}
        memo[(1, 1)] = 1
        for block in blocks:
            memo[block] = 0
    if (m, n) in memo:
        return memo[(m, n)]
    count = 0    

    if m != 1:
        count += path_count_top_down(m - 1, n, blocks, memo)
    if n != 1:
        count += path_count_top_down(m, n - 1, blocks, memo)
    memo[(m, n)] = count
    return memo[(m, n)]

def count_and_path_top_down(m, n, blocks, memo = None):
    if memo == None:
        memo = {}
        memo[(1, 1)] = (1, [''])
        for block in blocks:
            memo[block] = (0, None)
    if (m, n) in memo:
        return memo[(m, n)]
    paths = []
    count = 0
    if m != 1:
        left_count, left_paths = count_and_path_top_down(m - 1, n, blocks, memo)        
        if left_paths != None:
            paths += [left_path + 'R' for left_path in left_paths]
            count += left_count
    if n != 1:
        up_count, up_paths = count_and_path_top_down(m, n - 1, blocks, memo)
        if up_paths != None:
            paths += [up_path + 'D' for up_path in up_paths]
            count += up_count

    memo[(m, n)] = (count, paths)
    return memo[(m, n)]


def main():
    testcases = [
        (4, 4, [(2, 3), (3, 2)]),
        (6, 4, [(2, 4), (5, 3)]),
        (4, 4, [(1, 1)]),
        (5, 4, [(2, 4), (5, 3)]),
        (9, 7, [(1, 6), (4, 1)]),
        (9, 7, [(2, 2), (2, 4), (2, 7), (3, 3), (3, 6), (4, 4), (5, 2), (6, 2), (6, 4), (7, 2), (7, 5), (8, 4), (8, 6)]),
        (300, 300, [(1, 1)]),
        (100, 150, [(28, 21), (31, 97), (86, 87), (69, 20), (34, 21), (47, 103), (72, 26), (16, 147), (43, 138), (73, 95), (32, 97), (1, 149), (72, 104), (92, 71), (41, 128), (81, 61), (94, 143), (73, 128), (3, 137), (5, 24), (12, 89), (5, 106), (23, 14), (60, 119), (92, 89), (65, 25), (78, 64), (83, 62), (3, 147), (17, 4)])
    ]

    for i, (m, n, blocks) in enumerate(testcases):
        block_length = len(blocks)
        print(f"Testcase {i + 1} : {block_length}개의 셀이 차단된 {m} x {n} 그리드에서의 경로 수(상향식) : {path_count_bottom_up(m, n, blocks)}")
        print(f"Testcase {i + 1} : {block_length}개의 셀이 차단된 {m} x {n} 그리드에서의 경로 수(하향식) : {path_count_top_down(m, n, blocks)}")
        print()

    testcases = [
        (4, 4, [(2, 3), (3, 2)]),
        (6, 4, [(2, 4), (5, 3)]),
        (4, 4, [(1, 1)]),
        (5, 4, [(2, 4), (5, 3)]),
        (9, 7, [(2, 2), (2, 4), (2, 7), (3, 3), (3, 6), (4, 4), (5, 2), (6, 2), (6, 4), (7, 2), (7, 5), (8, 4), (8, 6)]),

    ]
    for i, (m, n, blocks) in enumerate(testcases):
        block_length = len(blocks)
        print(f"Testcase {i + 1} : {block_length}개의 셀이 차단된 {m} x {n} 그리드")
        bottom_up_count, bottom_up_paths = count_and_path_bottom_up(m, n, blocks)
        top_down_count, top_down_paths = count_and_path_top_down(m, n, blocks)
        bottom_up_paths.sort()
        top_down_paths.sort()
        if bottom_up_paths != top_down_paths:
            print("Wrone!!!")
            exit(-1)
        print(f"    경로 수(상향식) : {bottom_up_count}")
        print(f"    경로 수(하향식) : {top_down_count}")
        print(f"    경로 목록(상향식) : {bottom_up_paths}")
        print(f"    경로 목록(하향식) : {top_down_paths}")
        print()

if __name__ == '__main__':
    main()