from collections import deque

def expand_path_sum(n, m, grid, i, j, min_sum, queue_check):
    changed = False
    if i > 0:
        if min_sum[j][i - 1] > min_sum[j][i] + grid[j][i - 1]:
            min_sum[j][i - 1] = min_sum[j][i] + grid[j][i - 1]
            queue_check.append((i - 1, j))
            changed = True
    if i < n - 1:
        if min_sum[j][i + 1] > min_sum[j][i] + grid[j][i + 1]:
            min_sum[j][i + 1] = min_sum[j][i] + grid[j][i + 1]
            queue_check.append((i + 1, j))
            changed = True        
    if j > 0:
        if min_sum[j - 1][i] > min_sum[j][i] + grid[j - 1][i]:
            min_sum[j - 1][i] = min_sum[j][i] + grid[j - 1][i]
            queue_check.append((i, j - 1))
            changed = True
    if j < m - 1:
        if min_sum[j + 1][i] > min_sum[j][i] + grid[j + 1][i]:
            min_sum[j + 1][i] = min_sum[j][i] + grid[j + 1][i]
            queue_check.append((i, j + 1))
            changed = True
    return changed

def min_free_path_sum(n, m, grid, start, end):    
    s_x = start[0] - 1
    s_y = start[1] - 1
    e_x = end[0] - 1
    e_y = end[1] - 1
    queue_check = deque([(s_x, s_y)])
    min_sum = [[float('inf')] * n for _ in range(m)]    
    min_sum[s_y][s_x] = grid[s_y][s_x]
    while queue_check:
        i, j = queue_check.popleft()
        expand_path_sum(n, m, grid, i, j, min_sum, queue_check)
    return min_sum[e_y][e_x]

def coor_to_directions(path):
    result = ''
    for i in range(len(path) - 1):
        before = path[i]
        after = path[i + 1]
        if before[0] < after[0]:
            result += 'R'
        elif before[0] > after[0]:
            result += 'L'
        elif before[1] < after[1]:
            result += 'D'
        elif before[1] > after[1]:
            result += 'U'
    return result

def find_path(start, end, min_sum, grid):
    if start == end:
        return [[start]]
    i, j = end
    paths = []
    before_min_sum = min_sum[j][i] - grid[j][i]
    if i > 0 and min_sum[j][i - 1] == before_min_sum:
        paths += find_path(start, (i - 1, j), min_sum, grid)
    if i < len(min_sum[0]) - 1 and min_sum[j][i + 1] == before_min_sum:
        paths += find_path(start, (i + 1, j), min_sum, grid)
    if j > 0 and min_sum[j - 1][i] == before_min_sum:
        paths += find_path(start, (i, j - 1), min_sum, grid)
    if j < len(min_sum) - 1 and min_sum[j + 1][i] == before_min_sum:
        paths += find_path(start, (i, j + 1), min_sum, grid)
    for i in range(len(paths)):
        paths[i].append(end)
    return paths

def expand_path(n, m, grid, i, j, min_sum, queue_check, min_path_before):
    changed = False
    if i > 0: 
        if min_sum[j][i - 1] > min_sum[j][i] + grid[j][i - 1]:
            min_sum[j][i - 1] = min_sum[j][i] + grid[j][i - 1]
            queue_check.append((i - 1, j))
            min_path_before[j][i - 1] = 'R'
            changed = True
    if i < n - 1: 
        if min_sum[j][i + 1] > min_sum[j][i] + grid[j][i + 1]:
            min_sum[j][i + 1] = min_sum[j][i] + grid[j][i + 1]
            queue_check.append((i + 1, j))
            min_path_before[j][i - 1] = 'L'
            changed = True        
    if j > 0: 
        if min_sum[j - 1][i] > min_sum[j][i] + grid[j - 1][i]:
            min_sum[j - 1][i] = min_sum[j][i] + grid[j - 1][i]
            queue_check.append((i, j - 1))
            min_path_before[j][i - 1] = 'D'
            changed = True
    if j < m - 1:
        if min_sum[j + 1][i] > min_sum[j][i] + grid[j + 1][i]:
            min_sum[j + 1][i] = min_sum[j][i] + grid[j + 1][i]
            queue_check.append((i, j + 1))
            min_path_before[j][i - 1] = 'U'
            changed = True
    return changed

def min_free_path(n, m, grid, start, end):
    s_x = start[0] - 1
    s_y = start[1] - 1
    e_x = end[0] - 1
    e_y = end[1] - 1
    queue_check = deque([(s_x, s_y)])
    min_sum = [[float('inf')] * n for _ in range(m)]
    min_path_before = [[''] * n for _ in range(m)]
    min_sum[s_y][s_x] = grid[s_y][s_x]
    while queue_check:
        i, j = queue_check.popleft()
        expand_path(n, m, grid, i, j, min_sum, queue_check, min_path_before)
    moves = []
    paths = find_path((start[0] - 1, start[1] - 1), (end[0] - 1, end[1] - 1), min_sum, grid)
    for path in paths:
        moves.append(coor_to_directions(path))
    return min_sum[e_y][e_x], moves

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
                s_x = int(line_segments[2])
                s_y = int(line_segments[3])
                e_x = int(line_segments[4])
                e_y = int(line_segments[5])
                if len(line_segments) != n * m + 6:
                    print("Invalid test data")
                    break
                grid = [[0] * n for _ in range(m)]
                for i in range(n * m):
                    grid[i // n][i % n] = int(line_segments[i + 6])
            except ValueError:
                print("Invalid test data")
                break
            testcase.append((n, m, (s_x, s_y), (e_x, e_y), grid))
    return testcase

def main():
    testcases = load_test_data("./neurostinix_in_grid_3.txt")
    for i, tc in enumerate(testcases):
        n, m, start, end, grid = tc
        print(f"Testcases {i + 1}: {n} X {m}")
        min_ps = min_free_path_sum(n, m, grid, start, end)
        print(f"    최소 경로 합 : {min_ps}")
        min_ps, paths = min_free_path(n, m, grid, start, end)
        print(f"    최소 경로 : ")
        for j, path in enumerate(paths):
            print(f"      경로 {j + 1} : {path}")
        print()

if __name__ == "__main__":
    main()
