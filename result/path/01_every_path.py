def path_count_bottom_up(m, n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

def count_and_path_bottom_up(m, n):
    dp  = [[0] * n for _ in range(m)]
    paths = [[''] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        dp[i][0] = 1
        paths[i][0] = ['R' * i]
    for j in range(n):
        dp[0][j] = 1
        paths[0][j] = ['D' * j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            paths[i][j] = ['R' + path for path in paths[i - 1][j]] + ['D' + path for path in paths[i][j - 1]]
    return dp[m - 1][n - 1], paths[m - 1][n - 1]

def path_count_top_down(m, n, memo = None):
    if memo == None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 or n == 1:
        return 1
    memo[(m, n)] = path_count_top_down(m - 1, n, memo) + path_count_top_down(m, n - 1, memo)
    return memo[(m, n)]

def count_and_path_top_down(m, n, memo = None):
    if memo == None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        memo[(1, 1)] = (1, [''])
        return memo[(1, 1)]
    paths = []
    count = 0
    if m != 1:
        left_count, left_paths = count_and_path_top_down(m - 1, n, memo)
        paths += ['R' + left_path for left_path in left_paths]
        count += left_count
    if n != 1:
        up_count, up_paths = count_and_path_top_down(m, n - 1, memo)
        paths += ['D' + up_path for up_path in up_paths]
        count += up_count
    memo[(m, n)] = (count, paths)
    return memo[(m, n)]


def main():
    testcases = [(3, 2), (2, 3), (6, 3), (1, 100), (100, 1), (15, 25), (25, 25), (25, 15), (100, 150), (500, 10), (500, 495)]
    for i, (m, n) in enumerate(testcases):
        print(f"Testcase {i + 1} : {m} x {n} 그리드에서의 경로 수(상향식) : {path_count_bottom_up(m, n)}")
        print(f"Testcase {i + 1} : {m} x {n} 그리드에서의 경로 수(하향식) : {path_count_top_down(m, n)}")
        print()
        

    testcases = [(3, 2), (2, 3), (6, 3)]
    for i, (m, n) in enumerate(testcases):
        print(f"Testcase {i + 1} : {m} x {n} 그리드")
        bottom_up_count, bottom_up_paths = count_and_path_bottom_up(m, n)
        top_down_count, top_down_paths = count_and_path_top_down(m, n)
        bottom_up_paths.sort()
        top_down_paths.sort()
        print(f"    경로 수(상향식) : {bottom_up_count}")
        print(f"    경로 수(하향식) : {top_down_count}")
        print(f"    경로 목록(상향식) : {bottom_up_paths}")
        print(f"    경로 목록(하향식) : {top_down_paths}")
        print()

if __name__ == '__main__':
    main()