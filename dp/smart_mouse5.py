
from smart_mouse5_data import testcase_1, testcase_2, testcase_3, testcase_4, testcase_5, testcase_6, testcase_7


def find_min_path(n, t):
    min_time = [float('inf')] * (n + 1)
    previous = [0] * (n + 1)

    min_time[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if min_time[i] > min_time[j] + t[j][i]:
                min_time[i] = min_time[j] + t[j][i]
                previous[i] = j
    path = []
    current = n
    while current != 0:
        path.append(current)
        current = previous[current]
    path.reverse()
    return min_time[n], path


def find_min_time(n, t):
    min_time = [float('inf')] * (n + 1)
    min_time[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            min_time[i] = min(min_time[i], min_time[j] + t[j][i])
    return min_time[n]

def main():
    testcases = [testcase_1, testcase_2, testcase_3, testcase_4, testcase_5, testcase_6, testcase_7]
    for i, tc in enumerate(testcases):
        min_time, path = find_min_path(len(tc) - 1, tc)
        print(f"TC {i + 1} - 최소 이동 시간 : {min_time}")
        path_str = map(str, [0] + path)
        print(f"    최소 이동 경로 : {' -> '.join(path_str)}")
        print()
   

if __name__ == '__main__':
    main()