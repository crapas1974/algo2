def get_grid_value(i, j, grid):
    if i < 0 or j < 0:
        return 0
    if i >= len(grid[0]) or j >= len(grid):
        return 0
    return grid[j][i]

def max_stimulation(n, m, init_stimulation, grid):
    # 흥분도 변화량을 저장하는 grid of stimulation 배열을 생성한다.
    grid_st = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            grid_st[j][i] = get_grid_value(i - 1, j, grid) + get_grid_value(i + 1, j, grid) + \
                            get_grid_value(i, j - 1, grid) + get_grid_value(i, j + 1, grid) - \
                            4 * grid[j][i]
                
    # 최대흥분도합을 저장할 배열
    # - 셀 (i, j)의 최대경로합은 mps[j][i]에 저장한다.
    max_ps = [[0] * n for _ in range(m)]
    min_ps = [[0] * n for _ in range(m)]



    # 초기값 설정
    max_ps[0][0] = min_ps[0][0] = max(grid_st[0][0] + init_stimulation, 0)    
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:      # 가장 왼쪽 열
                max_ps[j][0] = min_ps[j][0] = max_ps[j - 1][0] + grid_st[j][0]
            elif j == 0:    # 가장 위쪽 행
                max_ps[0][i] = min_ps[0][i] = max_ps[0][i - 1] + grid_st[0][i]
            else: 
                max_ps[j][i] = max(max_ps[j - 1][i], max_ps[j][i - 1]) + grid_st[j][i]
                min_ps[j][i] = min(min_ps[j - 1][i], min_ps[j][i - 1]) + grid_st[j][i]
            # 각 셀에서의 바이러스 흥분도는 0 이하로 내려갈 수 없다.
            max_ps[j][i] = max(max_ps[j][i], 0)
            min_ps[j][i] = max(min_ps[j][i], 0)


    # 순간 최대 흥분도는 각 셀에서의 최대 흥분도 중 최대값이다.
    max_stimulation = max([max(row) for row in max_ps])
    min_stimulation = min([min(row) for row in min_ps])


    return max_stimulation, min_stimulation


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
                init_stimulation = int(line_segments[2])
                if len(line_segments) != n * m + 3:
                    print("Invalid test data")
                    break
                grid = [[0] * n for _ in range(m)]
                for i in range(n * m):
                    grid[i // n][i % n] = int(line_segments[i + 3])
            except ValueError:
                print("Invalid test data")
                break
            testcase.append((n, m, init_stimulation, grid))
    return testcase

def main():
    testcases = load_test_data("./neurostinix_in_grid_4.txt")
    for i, tc in enumerate(testcases):
        n, m, init_stimulation, grid = tc        
        max_ps, min_ps = max_stimulation(n, m, init_stimulation, grid)
        print(f"Testcases {i + 1}: 최대 흥분도는 {max_ps}이며 최소 흥분도는 {min_ps} 입니다.")
       
        print()

if __name__ == "__main__":
    main()