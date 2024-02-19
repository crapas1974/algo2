# 주어진 셀이 그리드 안에 있는지 확인하는 도우미 함수
def check_in_grid(n, m, i, j):
   return 0 <= i < n and 0 <= j < m


# 주어진 셀에서 시작하는 최대 증가 경로의 길이를 계산하는 함수
# 재귀 호출로 증가하는 인접 셀의 최대 증가 경로 길이를 가지고 와서,
# 그 중 최대값에 1을 더한 값이 현재 셀에서 시작하는 최대 증가 경로의 길이가 된다.
def calculate_max_increaing_path_length(n, m, grid, max_length, i, j):
   moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
   if max_length[j][i] != -1:
       return max_length[j][i]
   # 현재 셀에서 시작하는 최대 증가 경로 길이의 최소값은 1이다. (주변에 증가하는 셀이 없는 경우)
   max_length[j][i] = 1
   # 가능한 이동 방향에 대해서
   for move in moves:
       next_i = i + move[0]
       next_j = j + move[1]
       # 해당 방향이 그리드 내에 포함되고, 해당 셀의 농도가 증가하는 경우
       if check_in_grid(n, m, next_i, next_j) and grid[next_j][next_i] > grid[j][i]:
           # 이러한 인접 셀에서 시작하는 최대 증가 경로의 길이 중 최대값에 1을 더한다.
           max_length[j][i] = max(max_length[j][i], calculate_max_increaing_path_length(n, m, grid, max_length, next_i, next_j) + 1)
   return max_length[j][i]


# 상향식으로 모든 셀의 최대 증가 경로 길이를 계산하는 함수
def longest_incresaing_path(n, m, grid):
   # 각 셀의 최대 증가 경로를 저장하는 배열
   max_length = [[-1] * n for _ in range(m)]
   # 모든 셀 중에서 최대 값을 저장하는 변수
   path_max_length = 0
   # (0, 0)에서 (n - 1, m - 1) 방향으로 계산해 올라간다.
   for i in range(n):
       for j in range(m):
           # 현재 셀에서 시작하는 최대 증가 경로의 길이를 계산하고, 이들의 최대값을 갱신한다.
           path_max_length = max(calculate_max_increaing_path_length(n, m, grid, max_length, i, j), path_max_length)
   return path_max_length


def get_grid_value(i, j, grid):
    if i < 0 or j < 0:
        return 0
    if i >= len(grid[0]) or j >= len(grid):
        return 0
    return grid[j][i]


def max_stimulation(n, m, grid):
   # 흥분도 변화량을 저장하는 grid of stimulation 배열을 생성한다.
   grid_st = [[0] * n for _ in range(m)]
   for i in range(n):
       for j in range(m):
           grid_st[j][i] = get_grid_value(i - 1, j, grid) + get_grid_value(i + 1, j, grid) + \
                           get_grid_value(i, j - 1, grid) + get_grid_value(i, j + 1, grid) - \
                           4 * grid[j][i]
            
   # 최대흥분도합을 저장할 배열
   # - 셀 (i, j)의 최대경로합은 mps[j][i]에 저장한다.
   mps = [[0] * n for _ in range(m)]


   # 초기값 설정
   mps[0][0] = grid_st[0][0]
  
   for i in range(n):
       for j in range(m):
           if i == 0 and j == 0:
               continue
           if i == 0:      # 가장 왼쪽 열
               mps[j][0] = mps[j - 1][0] + grid_st[j][0]
           elif j == 0:    # 가장 위쪽 행
               mps[0][i] = mps[0][i - 1] + grid_st[0][i]
           else: 
               mps[j][i] = max(mps[j - 1][i], mps[j][i - 1]) + grid_st[j][i]
           # 각 셀에서의 바이러스 흥분도는 0 이하로 내려갈 수 없다.
           mps[j][i] = max(mps[j][i], 0)


   # 순간 최대 흥분도는 각 셀에서의 최대 흥분도 중 최대값이다.
   max_stimulation = max([max(row) for row in mps])


   return mps[m - 1][n - 1], max_stimulation


def load_test_data(filename):
    testcase = []
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_segments = line.split(',')
            try:
                # 그리드의 크기
                n = int(line_segments[0])
                m = int(line_segments[1])
                # 데이터 개수 확인
                if len(line_segments) != n * m + 2:
                    print("Invalid test data")
                    break
                # 테스트용 그리드 생성
                grid = [[0] * n for _ in range(m)]
                for i in range(n * m):
                    grid[i // n][i % n] = int(line_segments[i + 2])
            except ValueError:
                # 숫자로 변환할 수 없는 경우
                print("Invalid test data")
                break
            testcase.append((n, m, grid))
    return testcase

def min_path_sum_bu(n, m, grid):
   # 최소경로합을 저장할 배열
   # - 셀 (i, j)의 최소경로합은 mps[j][i]에 저장한다.
   mps = [[0] * n for _ in range(m)]
   # 최소경로합 경로의 마지막 움직임을 저장하는 배열
   # - 셀 (i, j)에 도달하는 마지막 움직임은 move[j][i]에 저장한다.
   move = [[0] * n for _ in range(m)]

   # 초기값 설정
   mps[0][0] = grid[0][0]
   move[0][0] = ''
  
   for i in range(n):
       for j in range(m):
           if i == 0 and j == 0:
               continue
           if i == 0:      # 가장 왼쪽 열
               mps[j][0] = mps[j - 1][0] + grid[j][0]
               move[j][0] = 'D'
           elif j == 0:    # 가장 위쪽 행
               mps[0][i] = mps[0][i - 1] + grid[0][i]
               move[0][i] = 'R'
           else:
               if mps[j - 1][i] < mps[j][i - 1]:   # 아래쪽으로 이동
                   move[j][i] = 'D'
                   mps[j][i] = mps[j - 1][i] + grid[j][i]
               else:                               # 오른쪽으로 이동
                   move[j][i] = 'R'           
                   mps[j][i] = mps[j][i - 1] + grid[j][i]
  
   # 경로를 재구축한다. 목적지에서 시작점으로 추적해 올라간다.
   move_str = ''
   i = n - 1
   j = m - 1
   while True:
       # 역추적이므로, 앞에 이동 방향을 붙인다.
       move_str = move[j][i] + move_str
       # 출발점에 도착하면 종료
       if i == 0 and j == 0:
           break       
       if move[j][i] == 'D':  # 내려온 경우 위쪽으로 이동
           j -= 1
       else:                  # 옆에서 온 경우 오른쪽으로 이동
           i -= 1
  
   return mps[m - 1][n - 1], move_str


def min_path_sum_td(i, j, grid, memo = None):
    # 메모이제이션 딕셔너리 초기화
    if memo == None:
        memo = {}

    # 메모이제이션 된 셀이면 메모값을 반환
    if (i, j) in memo:
        return memo[(i, j)]
    
    height = len(grid)
    width = len(grid[0])
    # 종료 조건 1 : (i, j)가 그리드 밖에 있는 경우 충분히 큰 값을 반환
    if i >= width or j >= height:
        return float('inf')
    if i < 0 or j < 0:
        return float('inf')
    
    # 종료 조건 2 : (0, 0)
    if i == 0 and j == 0:
        return grid[0][0]
    
    # 이 예시 구현은 좌표 (x, y)가 실제로는 grid[y][x]의 값을 의미하는 설정의 구현이다.

    # 가장 자리에 있는 경우 가장 자리의 경우의 재귀 호출
    if i == 0:
        memo[(0, j)] = grid[j][0] + min_path_sum_td(0, j - 1, grid, memo)
    if j == 0:
        memo[(i, 0)] = grid[0][i] + min_path_sum_td(i - 1, 0, grid, memo)

    # 가장 자리가 아닌 경우의 재귀 호출
    memo[(i, j)] = grid[j][i] + min(min_path_sum_td(i - 1, j, grid, memo),          
                                    min_path_sum_td(i, j - 1, grid, memo))
    return memo[(i, j)]

def min_path_sum_td_wrapper(n, m, grid):
    return min_path_sum_td(n - 1, m - 1, grid)

def max_path_sum_td(i, j, grid, memo = None):
   # 메모이제이션 딕셔너리 초기화
   if memo == None:
       memo = {}

   # 메모이제이션 된 셀이면 메모값을 반환
   if (i, j) in memo:
       return memo[(i, j)]
  
   height = len(grid)
   width = len(grid[0])
   # 종료 조건 1 : (i, j)가 그리드 밖에 있는 경우 충분히 작은 값을 반환
   if i >= width or j >= height:
       return -float('inf')
   if i < 0 or j < 0:
       return -float('inf')
  
   # 종료 조건 2 : (0, 0)
   if i == 0 and j == 0:
       return grid[0][0]
  
   # 이 예시 구현은 좌표 (x, y)가 실제로는 grid[y][x]의 값을 의미하는 설정의 구현이다.

   # 가장 자리에 있는 경우 가장 자리의 경우의 재귀 호출
   if i == 0:
       memo[(0, j)] = grid[j][0] + max_path_sum_td(0, j - 1, grid, memo)
   if j == 0:
       memo[(i, 0)] = grid[0][i] + max_path_sum_td(i - 1, 0, grid, memo)

   # 가장 자리가 아닌 경우의 재귀 호출. 취합할 때 최소가 아니라 최대를 사용해 취합한다.
   memo[(i, j)] = grid[j][i] + max(max_path_sum_td(i - 1, j, grid, memo),          
                                   max_path_sum_td(i, j - 1, grid, memo))
   return memo[(i, j)]

def max_path_sum_td_wrapper(n, m, grid):
   return max_path_sum_td(n - 1, m - 1, grid)

def max_path_sum_bu(n, m, grid):
   # 최대경로합을 저장할 배열
   # - 셀 (i, j)의 최대경로합은 mps[j][i]에 저장한다.
   mps = [[0] * n for _ in range(m)]
   # 최대경로합 경로의 마지막 움직임을 저장하는 배열
   # - 셀 (i, j)에 도달하는 마지막 움직임은 move[j][i]에 저장한다.
   move = [[0] * n for _ in range(m)]

   # 초기값 설정
   mps[0][0] = grid[0][0]
   move[0][0] = ''
  
   for i in range(n):
       for j in range(m):
           if i == 0 and j == 0:
               continue
           if i == 0:      # 가장 왼쪽 열
               mps[j][0] = mps[j - 1][0] + grid[j][0]
               move[j][0] = 'D'
           elif j == 0:    # 가장 위쪽 행
               mps[0][i] = mps[0][i - 1] + grid[0][i]
               move[0][i] = 'R'
           else:   # 작은 값이 아닌 큰 값을 사용한다.
               if mps[j - 1][i] > mps[j][i - 1]:   # 아래쪽으로 이동
                   move[j][i] = 'D'
                   mps[j][i] = mps[j - 1][i] + grid[j][i]
               else:                               # 오른쪽으로 이동
                   move[j][i] = 'R'           
                   mps[j][i] = mps[j][i - 1] + grid[j][i]
  
   # 경로를 재구축한다. 목적지에서 시작점으로 추적해 올라간다.
   move_str = ''
   i = n - 1
   j = m - 1
   while True:
       # 역추적이므로, 앞에 이동 방향을 붙인다.
       move_str = move[j][i] + move_str
       # 출발점에 도착하면 종료
       if i == 0 and j == 0:
           break       
       if move[j][i] == 'D':  # 내려온 경우 위쪽으로 이동
           j -= 1
       else:                  # 옆에서 온 경우 오른쪽으로 이동
           i -= 1
  
   return mps[m - 1][n - 1], move_str


def main():
    testcases = load_test_data("./min_path_testcase.txt")
    for i, testcase in enumerate(testcases):
        n, m, grid = testcase
        print("TC {}: {} X {}".format(i + 1, n, m))
        print("최소 경로 합 (하향식):", min_path_sum_td_wrapper(n, m, grid))
        mps, move_str = min_path_sum_bu(n, m, grid)
        print("최소 경로 합 (하향식):", mps)
        print("이동 경로 (하향식):", move_str)

        # print("최소 경로 합 (하향식):", max_path_sum_td_wrapper(n, m, grid))
        # mps, move_str = max_path_sum_bu(n, m, grid)
        # print("최소 경로 합 (상향식):", mps)
        # print("이동 경로 (상향식):", move_str)
        
        # ms_dst, ms_path = max_stimulation(n, m, grid)
        # print("도착 지점에서의 최대 흥분도 : ", ms_dst)
        # print("순간 최대 흥분도 : ", ms_path)

#        print("최대 증가 경로의 길이 : ", longest_incresaing_path(n, m, grid))



if __name__ == "__main__":
    main()