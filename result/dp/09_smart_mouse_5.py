from smart_mouse_4_tc import testcases, get_large_testcase

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
    large_tc = get_large_testcase()
    testcases.append(large_tc)
    for i, tc in enumerate(testcases):
        min_time, path = find_min_path(len(tc) - 1, tc)
        if i != 9:
            print(f"TC {i + 1} - 최소 이동 시간 : {min_time}")
        else:
            print(f"500개의 지점을 가진 미로에서의 최소 이동 시간 : {min_time}")
        path_str = map(str, [0] + path)
        print(f"    최소 이동 경로 : {' -> '.join(path_str)}")
        print()
   

if __name__ == '__main__':
    main()