from collections import deque

def expand_path_sum(n, m, grid, i, j, min_sum, queue_check):
    #print(f"(i, j) = ({i}, {j})")
    #print(min_sum)
    changed = False
    if i > 0:   # 왼쪽 가장자리가 아님
        if min_sum[j][i - 1] > min_sum[j][i] + grid[j][i - 1]:
            min_sum[j][i - 1] = min_sum[j][i] + grid[j][i - 1]
            queue_check.append((i - 1, j))
            #queue_check[i - 1][j] = True
            changed = True
    if i < n - 1:  # 오른쪽 가장자리가 아님
        if min_sum[j][i + 1] > min_sum[j][i] + grid[j][i + 1]:
            min_sum[j][i + 1] = min_sum[j][i] + grid[j][i + 1]
            queue_check.append((i + 1, j))
#            queue_check[i + 1][j] = True
            changed = True        
    if j > 0:   # 위쪽 가장자리가 아님
        if min_sum[j - 1][i] > min_sum[j][i] + grid[j - 1][i]:
            min_sum[j - 1][i] = min_sum[j][i] + grid[j - 1][i]
            queue_check.append((i, j - 1))
#            queue_check[i][j - 1] = True
            changed = True
    if j < m - 1:  # 아래쪽 가장자리가 아님
        #print(i, j)
        #print(min_sum[i][j + 1])
        #print(min_sum[i][j])
        #print(grid[i][j + 1])
        if min_sum[j + 1][i] > min_sum[j][i] + grid[j + 1][i]:
            min_sum[j + 1][i] = min_sum[j][i] + grid[j + 1][i]
            queue_check.append((i, j + 1))
#            queue_check[i][j + 1] = True
            changed = True
    return changed

def min_free_path_sum(n, m, grid, start, end):
    #print(n, m, grid, start, end)    
    s_x = start[0] - 1
    s_y = start[1] - 1
    e_x = end[0] - 1
    e_y = end[1] - 1
    queue_check = deque([(s_x, s_y)])
    min_sum = [[float('inf')] * n for _ in range(m)]
    #print(min_sum)
    min_sum[s_y][s_x] = grid[s_y][s_x]
    while queue_check:
        i, j = queue_check.popleft()
        expand_path_sum(n, m, grid, i, j, min_sum, queue_check)
#        if i == e_x and j == e_y:
#            return min_sum[j][i]
#        if expand_path_sum(n, m, grid, i, j, min_sum, queue_check):
#            queue_check.append((i, j))    
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




def find_path_bak(start, end, min_sum, grid, memo = None):
    print(start, end)
    if memo == None:
        memo = {}
        start = (start[0] - 1, start[1] - 1)
        end = (end[0] - 1, end[1] - 1)
    if start == end:
        return [[start]]
    if end in memo:
        return memo[end]
    i, j = end
    paths = []
    before_min_sum = min_sum[j][i] - grid[j][i]
    if i > 0 and min_sum[j][i - 1] == before_min_sum:
        #print("L", end='')
        # left_paths = find_path(start, (i - 1, j), min_sum, grid, memo)
        # for path in left_paths:
        #     paths.append(path + [end])
        paths += find_path(start, (i - 1, j), min_sum, grid, memo)
    if i < len(min_sum[0]) - 1 and min_sum[j][i + 1] == before_min_sum:
        # print("R", end='')
        # right_paths = find_path(start, (i + 1, j), min_sum, grid, memo)
        # for path in right_paths:
        #     paths.append(path + [end])
        paths += find_path(start, (i + 1, j), min_sum, grid, memo)
    if j > 0 and min_sum[j - 1][i] == before_min_sum:
        # print("U", end='')
        # up_paths = find_path(start, (i, j - 1), min_sum, grid, memo)
        # for path in up_paths:
        #     paths.append(path + [end])
        paths += find_path(start, (i, j - 1), min_sum, grid, memo)
    if j < len(min_sum) - 1 and min_sum[j + 1][i] == before_min_sum:
        # print("D", end='')
        # down_paths = find_path(start, (i, j + 1), min_sum, grid, memo)
        # for path in down_paths:
        #     paths.append(path + [end])
        paths += find_path(start, (i, j + 1), min_sum, grid, memo)
    for i in range(len(paths)):
        paths[i].append(end)
    memo[end] = paths
    return paths



def expand_path(n, m, grid, i, j, min_sum, queue_check, min_path_before):
    #print(f"(i, j) = ({i}, {j})")
    #print(min_sum)
    changed = False
    if i > 0:   # 왼쪽 가장자리가 아님
        if min_sum[j][i - 1] > min_sum[j][i] + grid[j][i - 1]:
            min_sum[j][i - 1] = min_sum[j][i] + grid[j][i - 1]
            queue_check.append((i - 1, j))
            min_path_before[j][i - 1] = 'R'
            #queue_check[i - 1][j] = True
            changed = True
    if i < n - 1:  # 오른쪽 가장자리가 아님
        if min_sum[j][i + 1] > min_sum[j][i] + grid[j][i + 1]:
            min_sum[j][i + 1] = min_sum[j][i] + grid[j][i + 1]
            queue_check.append((i + 1, j))
            min_path_before[j][i - 1] = 'L'
#            queue_check[i + 1][j] = True
            changed = True        
    if j > 0:   # 위쪽 가장자리가 아님
        if min_sum[j - 1][i] > min_sum[j][i] + grid[j - 1][i]:
            min_sum[j - 1][i] = min_sum[j][i] + grid[j - 1][i]
            queue_check.append((i, j - 1))
            min_path_before[j][i - 1] = 'D'
#            queue_check[i][j - 1] = True
            changed = True
    if j < m - 1:  # 아래쪽 가장자리가 아님
        #print(i, j)
        #print(min_sum[i][j + 1])
        #print(min_sum[i][j])
        #print(grid[i][j + 1])
        if min_sum[j + 1][i] > min_sum[j][i] + grid[j + 1][i]:
            min_sum[j + 1][i] = min_sum[j][i] + grid[j + 1][i]
            queue_check.append((i, j + 1))
            min_path_before[j][i - 1] = 'U'
#            queue_check[i][j + 1] = True
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
    #print(min_sum)
    min_sum[s_y][s_x] = grid[s_y][s_x]
    while queue_check:
        i, j = queue_check.popleft()
        expand_path(n, m, grid, i, j, min_sum, queue_check, min_path_before)
#        if i == e_x and j == e_y:
#            return min_sum[j][i]
#        if expand_path_sum(n, m, grid, i, j, min_sum, queue_check):
#            queue_check.append((i, j))
    print(min_path_before)
    print(min_sum)
    moves = []
    paths = find_path((start[0] - 1, start[1] - 1), (end[0] - 1, end[1] - 1), min_sum, grid)
    
    for path in paths:
        print(path)
        moves.append(coor_to_directions(path))

    return min_sum[e_y][e_x], moves







# def min_path_sum(matrix, start, end):
#     print(matrix, start, end)
#     # 시작점과 종료점 설정
#     i, j = start[0] - 1, start[1] - 1
#     k, l = end[0] - 1, end[1] - 1
    
#     # 매트릭스의 행과 열의 수
#     n, m = len(matrix), len(matrix[0])
    
#     # 방문한 셀을 추적하는 배열
#     visited = [[False for _ in range(m)] for _ in range(n)]
    
#     # BFS를 위한 큐, (x좌표, y좌표, 현재까지의 경로합)을 저장
#     queue = deque([(i, j, matrix[i][j])])
#     visited[i][j] = True
    
#     # BFS 실행
#     while queue:
#         x, y, path_sum = queue.popleft()
        
#         # 목표점에 도달한 경우
#         if x == k and y == l:
#             return path_sum
        
#         # 상하좌우 이동
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy
            
#             # 매트릭스 범위 내에 있고, 아직 방문하지 않은 셀인지 확인
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny, path_sum + matrix[nx][ny]))
    
#     # 목표점에 도달할 수 없는 경우
#     return -1

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
        #min_ps = min_free_path_sum(n, m, grid, start, end)
        min_ps, paths = min_free_path(n, m, grid, start, end)
        print(i + 1, min_ps)
        print(paths)
        print()
        break

if __name__ == "__main__":
    main()


# # 매트릭스 예시
# matrix = [
#     [1, 3, 1],
#     [1, 5, 1],
#     [4, 2, 1]
# ]

# # 시작점과 목표점
# start = (0, 0)
# end = (2, 2)

# # 최소 경로합 계산
# print(min_path_sum(matrix, start, end))
