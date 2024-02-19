def max_path_sum_topdown(i, j, grid, memo = None):
    if memo == None:
        memo = {}
        i = i - 1
        j = j - 1

    if (i, j) in memo:
        return memo[(i, j)]
  
    height = len(grid)
    width = len(grid[0])
    if i >= width or j >= height:
        return - float('inf')
    if i < 0 or j < 0:
        return - float('inf')
    if i == 0 and j == 0:
        return grid[0][0]    
    if i == 0:
        memo[(0, j)] = grid[j][0] + max_path_sum_topdown(0, j - 1, grid, memo)
    if j == 0:
        memo[(i, 0)] = grid[0][i] + max_path_sum_topdown(i - 1, 0, grid, memo)

    memo[(i, j)] = grid[j][i] + max(max_path_sum_topdown(i - 1, j, grid, memo),          
                                    max_path_sum_topdown(i, j - 1, grid, memo))
    return memo[(i, j)]

def max_path_sum_bottomup(n, m, grid):
    mps = [[0] * n for _ in range(m)]
    move = {}

    mps[0][0] = grid[0][0]
    move[(0, 0)] = ['']
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0: 
                mps[j][0] = mps[j - 1][0] + grid[j][0]
                move[(j, 0)] = [move[(j - 1, 0)][0] + 'D']
            elif j == 0:
                mps[0][i] = mps[0][i - 1] + grid[0][i]
                move[(0, i)] = [move[(0, i - 1)][0] + 'R']
            else:
                move[(j, i)] = []                
                if mps[j - 1][i] >= mps[j][i - 1]:
                    mps[j][i] = mps[j - 1][i] + grid[j][i]                    
                    for path in move[(j - 1, i)]:
                        move[(j, i)].append(path + 'D')
                if mps[j - 1][i] <= mps[j][i - 1]:
                    mps[j][i] = mps[j][i - 1] + grid[j][i]
                    for path in move[(j, i - 1)]:
                        move[(j, i)].append(path + 'R')
    
    return mps[m - 1][n - 1], move[(m - 1, n - 1)]

def load_test_data(filename):
    testcase = []
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_segments = line.split(',')
            try:
                n = int(line_segments[0])
                m = int(line_segments[1])
                if len(line_segments) != n * m + 2:
                    print("Invalid test data")
                    break
                grid = [[0] * n for _ in range(m)]
                for i in range(n * m):
                    grid[i // n][i % n] = int(line_segments[i + 2])
            except ValueError:
                print("Invalid test data")
                break
            testcase.append((n, m, grid))
    return testcase

def main():
    testcases = load_test_data("./neurostinix_in_grid.txt")
    for i, tc in enumerate(testcases):
        n, m, grid = tc
        print(f"Testcases {i + 1}: {n} X {m}")
        max_ps_topdown = max_path_sum_topdown(n, m, grid)
        print(f"    최대 비용 경로의 비용 (하향식) : {max_ps_topdown}")
        max_ps_bottomup, path = max_path_sum_bottomup(n, m, grid)
        path.sort()
        path_len = len(path)
        print(f"    최대 비용 경로의 비용 (상향식) : {max_ps_bottomup}")
        print(f"    최대 비용 경로의 개수 : {path_len}")
        print(f"    오름차순 정렬 상위 10개 까지의 경로: {path[:10]}")
        print()

if __name__ == "__main__":
    main()