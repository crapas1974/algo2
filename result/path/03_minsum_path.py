def min_path_sum_bottomup(n, m, grid):
    mps = [[0] * n for _ in range(m)]
    move = [[0] * n for _ in range(m)]

    mps[0][0] = grid[0][0]
    move[0][0] = ''
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                mps[j][0] = mps[j - 1][0] + grid[j][0]
                move[j][0] = 'D'
            elif j == 0:
                mps[0][i] = mps[0][i - 1] + grid[0][i]
                move[0][i] = 'R'
            else:
                if mps[j - 1][i] < mps[j][i - 1]:
                    move[j][i] = 'D'
                    mps[j][i] = mps[j - 1][i] + grid[j][i]
                else:                            
                    move[j][i] = 'R'           
                    mps[j][i] = mps[j][i - 1] + grid[j][i]
    
    move_str = ''
    i = n - 1
    j = m - 1
    while True:
        move_str = move[j][i] + move_str
        if i == 0 and j == 0:
            break       
        if move[j][i] == 'D':
            j -= 1
        else:                
            i -= 1
    
    return mps[m - 1][n - 1], move_str


def min_path_sum_topdown(i, j, grid, memo = None):
    if memo == None:
        memo = {}
        i = i - 1
        j = j - 1

    if (i, j) in memo:
        return memo[(i, j)]
    
    height = len(grid)
    width = len(grid[0])
    if i >= width or j >= height:
        return float('inf')
    if i < 0 or j < 0:
        return float('inf')
    
    if i == 0 and j == 0:
        return grid[0][0]

    if i == 0:
        memo[(0, j)] = grid[j][0] + min_path_sum_topdown(0, j - 1, grid, memo)
    if j == 0:
        memo[(i, 0)] = grid[0][i] + min_path_sum_topdown(i - 1, 0, grid, memo)

    memo[(i, j)] = grid[j][i] + min(min_path_sum_topdown(i - 1, j, grid, memo),          
                                    min_path_sum_topdown(i, j - 1, grid, memo))
    return memo[(i, j)]

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
        min_ps_topdown = min_path_sum_topdown(n, m, grid)
        print(f"    최소 비용 경로의 비용 (하향식) : {min_ps_topdown}")
        min_ps_bottomup, path = min_path_sum_bottomup(n, m, grid)
        print(f"    최소 비용 경로의 비용 (상향식) : {min_ps_bottomup}")
        print(f"    최소 비용 경로 : {path}")
        print()

if __name__ == "__main__":
    main()