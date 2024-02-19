def min_path_sum_from_left_to_right(n, m, grid):
    min_sum = [[0] * n for _ in range(m)]
    upward_min = [0] * m
    downward_min = [0] * m
    for i in range(n):
        for j in range(m):
            min_sum[j][i] = grid[j][i]
            if i != 0:
                min_sum[j][i] += min_sum[j][i - 1]
        downward_min[0] = min_sum[0][i]
        for j in range(1, m):
            downward_min[j] = min(downward_min[j - 1] + grid[j][i], min_sum[j][i])
        upward_min[m - 1] = min_sum[m - 1][i]
        for j in range(m - 2, -1, -1):
            upward_min[j] = min(upward_min[j + 1] + grid[j][i], min_sum[j][i])
        for j in range(m):
            min_sum[j][i] = min(upward_min[j], downward_min[j])
    return min(min_sum[j][n - 1] for j in range(m))

def min_path_from_left_to_right(n, m, grid):
    min_sum = [[0] * n for _ in range(m)]
    min_path = {}
    upward_min = [0] * m
    upward_min_path = [''] * m
    downward_min = [0] * m
    downward_min_path = [''] * m

    for i in range(n):
        for j in range(m):            
            if i != 0:
                min_sum[j][i] = min_sum[j][i - 1] + grid[j][i]
                min_path[(j, i)] = [path + 'R' for path in min_path[(j, i - 1)]]
            else:
                min_sum[j][i] = grid[j][i]
                min_path[(j, i)] = ['']
        downward_min[0] = min_sum[0][i]
        downward_min_path[0] = min_path[(0, i)]
        for j in range(1, m):
            if downward_min[j - 1] + grid[j][i] < min_sum[j][i]:
                downward_min[j] = downward_min[j - 1] + grid[j][i]
                downward_min_path[j] = [path + 'D' for path in downward_min_path[j - 1]]
            elif downward_min[j - 1] + grid[j][i] > min_sum[j][i]:
                downward_min[j] = min_sum[j][i]
                downward_min_path[j] = min_path[(j, i)]
            else:
                downward_min[j] = min_sum[j][i]
                downward_min_path[j] = [path + 'D' for path in downward_min_path[j - 1]] + min_path[(j, i)]
        upward_min[m - 1] = min_sum[m - 1][i]
        upward_min_path[m - 1] = min_path[(m - 1, i)]
        for j in range(m - 2, -1, -1):
            if upward_min[j + 1] + grid[j][i] < min_sum[j][i]:
                upward_min[j] = upward_min[j + 1] + grid[j][i]
                upward_min_path[j] = [path + 'U' for path in upward_min_path[j + 1]]
            elif upward_min[j + 1] + grid[j][i] > min_sum[j][i]:
                upward_min[j] = min_sum[j][i]
                upward_min_path[j] = min_path[(j, i)]
            else:
                upward_min[j] = min_sum[j][i]
                upward_min_path[j] = [path + 'U' for path in upward_min_path[j + 1]] + min_path[(j, i)]
        for j in range(m):
            if upward_min[j] < downward_min[j]:
                min_sum[j][i] = upward_min[j]
                min_path[(j, i)] = upward_min_path[j]
            elif upward_min[j] > downward_min[j]:
                min_sum[j][i] = downward_min[j]
                min_path[(j, i)] = downward_min_path[j]
            else:
                min_sum[j][i] = upward_min[j]
                min_path[(j, i)] = list(set(upward_min_path[j] + downward_min_path[j]))
    
    min_val = float('inf')
    result_paths = []
    for j in range(m):
        if min_sum[j][n - 1] < min_val:
            min_val = min_sum[j][n - 1]            
            result_paths = []
            for path in min_path[(j, n - 1)]:
                result_paths.append((j + 1, path))
        elif min_sum[j][n - 1] == min_val:
            for path in min_path[(j, n - 1)]:
                result_paths.append((j + 1, path))
    return min_val, result_paths

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
    testcases = load_test_data("./neurostinix_in_grid_2.txt")
    for i, tc in enumerate(testcases):
        n, m, grid = tc
        print(f"Testcases {i + 1}: {n} X {m}")
        min_ps_lr = min_path_sum_from_left_to_right(n, m, grid)
        print(f"    최소 비용 경로의 비용 (좌우) : {min_ps_lr}")
        
        min_ps_lr, min_path = min_path_from_left_to_right(n, m, grid)
        print(f"    최소 비용 경로의 비용 (좌우) : {min_ps_lr}")
        print(f"    최소 경로 (좌우)")
        for j, (end_cell, path) in enumerate(min_path):
            print(f"      경로 {j + 1}는 ({n}, {end_cell})에서 종료되며, 경로는 {path}입니다.")
        print()

if __name__ == "__main__":
    main()