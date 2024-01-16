def way2go_blocking_td(n, m, blockings, memo = None):
    if memo == None:
        memo = {}
        memo[(1, 1)] = 1
    # (n, m)이 차단된 경우 - n, m 부터 재귀 호출하므로 이 구현의 원점은 (1, 1)이다.
    if (n - 1, m - 1) in blockings:
        return 0
   
    if (n, m) in memo:
        return memo[(n, m)]


    if n < 1 or m < 1:
        return 0
    else:
        memo[(n, m)] = way2go_blocking_td(n - 1, m, blockings, memo) + way2go_blocking_td(n, m - 1, blockings, memo)
        return memo[(n, m)]
    

def way2go_blocking_bu(n, m, blockings):
    if (0, 0) in blockings:
        return 0
    way2go_cnt = [[0 for _ in range(m)] for _ in range(n)]
    way2go_cnt[0][0] = 1


    for i in range(n):
        for j in range(m):
            # (i, j)가 차단된 경우
            if (i, j) in blockings:
                continue
            if i > 0:
                way2go_cnt[i][j] += way2go_cnt[i - 1][j]
            if j > 0:
                way2go_cnt[i][j] += way2go_cnt[i][j - 1]


    return way2go_cnt[n - 1][m - 1]


def main():
    TC1 = (6, 4, [(1, 3), (4, 2)])
    TC2 = (100, 150, [(28, 21), (31, 97), (86, 87), (69, 20), (34, 21), (47, 103), (72, 26), (16, 147), (43, 138), (73, 95), (32, 97), (0, 149), (72, 104), (92, 71), (41, 128), (81, 61), (94, 143), (73, 128), (3, 137), (5, 24), (12, 89), (5, 106), (23, 14), (60, 119), (92, 89), (65, 25), (78, 64), (83, 62), (3, 147), (17, 4)])
    TC3 = (9, 7, [(0, 5), (3, 0)])
    TC4 = (300, 300, [(0, 0)])

    testcases = [TC1, TC2, TC3, TC4]
    for i, (n, m, t) in enumerate(testcases):
        print(f"TC {i + 1} : ")
        print(f"하향식 접근법의 결과 : {way2go_blocking_td(n, m, t)}")
        print(f"상향식 접근법의 결과 : {way2go_blocking_bu(n, m, t)}")

if __name__ == '__main__':
    main()
