def check_in_grid(n, m, i, j):
   return 0 <= i < n and 0 <= j < m

def max_move_from(n, m, grid, max_length, i, j):
   moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
   if max_length[j][i] != -1:
       return max_length[j][i]
   max_length[j][i] = 1
   for move in moves:
       next_i = i + move[0]
       next_j = j + move[1]
       if check_in_grid(n, m, next_i, next_j) and grid[next_j][next_i] > grid[j][i]:
           max_length[j][i] = max(max_length[j][i], max_move_from(n, m, grid, max_length, next_i, next_j) + 1)
   return max_length[j][i]

def longest_move(n, m, grid):
   max_length = [[-1] * n for _ in range(m)]
   path_max_length = 0
   for i in range(n):
       for j in range(m):
           path_max_length = max(max_move_from(n, m, grid, max_length, i, j), path_max_length)
   return path_max_length

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
    testcases = load_test_data("./neurostinix_in_grid_5.txt")
    for i, tc in enumerate(testcases):
        n, m, grid = tc
        print(f"Testcase {i + 1} : 최대 이동 거리는 {longest_move(n, m, grid)}입니다.")
        print()

if __name__ == "__main__":
    main()