# n x m 크기의 그리드
def way2go_td(n, m, memo = None):
    # 메모이제이션을 위한 딕셔너리 초기화.
    if memo == None:
        memo = {}
    # 저장된 값이 있는 경우 계산하지 않고 반환
    if (n, m) in memo:
        return memo[(n, m)]
    # 그리드 밖으로 나간 경우
    if n < 1 or m < 1:
        return 0
    # 가장 윗 줄과 가장 왼쪽 줄은 이동 방법은 1가지 뿐이다.
    if n == 1 or m == 1:
        return 1
    else:
        # 재귀적으로 위쪽과 왼쪽에서 오는 경우를 더한다.
        memo[(n, m)] = way2go_td(n - 1, m, memo) + way2go_td(n, m - 1, memo)
        return memo[(n, m)]
    
def way2go_bu(n, m):
    if n <= 0 or m <= 0:
        return 0
    
    # 경로 수를 계산할 DP 테이블 초기화
    way2go_cnt = [[0] * m for _ in range(n)]
    way2go_cnt[0][0] = 1

    # DP 테이블 채우기 및 경로 생성
    for i in range(n):
        for j in range(m):
            if i > 0:
                # 왼쪽에서 오는 경로의 수를 더한다.
                way2go_cnt[i][j] += way2go_cnt[i - 1][j]
            if j > 0:
                # 위쪽에서 오는 경로의 수를 더한다.
                way2go_cnt[i][j] += way2go_cnt[i][j - 1]

    return way2go_cnt[n - 1][m - 1]


def way2go_way(n, m):
    if n <= 0 or m <= 0:
        return 0, []
    
    # 경로 수를 계산할 DP 테이블 초기화
    way2go_cnt = [[0] * m for _ in range(n)]
    way2go_cnt[0][0] = 1

    # 경로를 저장할 리스트 초기화
    way2go_methods = [[[] for _ in range(m)] for _ in range(n)]
    way2go_methods[0][0] = ['']

    # DP 테이블 채우기 및 경로 생성
    for i in range(n):
        for j in range(m):
            if i > 0:
                # 왼쪽에서 오는 경로의 수를 더한다.
                way2go_cnt[i][j] += way2go_cnt[i - 1][j]
                # 왼쪽에서 오는 경로의 목록에 현재 위치로 이동하기 위한 방법인 "R"을 추가한다.
                way2go_methods[i][j] += [method + "R" for method in way2go_methods[i - 1][j]]                
            if j > 0:
                # 위쪽에서 오는 경로의 수를 더한다.
                way2go_cnt[i][j] += way2go_cnt[i][j - 1]
                # 위쪽에서 오는 경로의 목록에 현재 위치로 이동하기 위한 방법인 "D"을 추가한다.
                way2go_methods[i][j] += [method + "D" for method in way2go_methods[i][j - 1]]

    return way2go_cnt[n - 1][m - 1], way2go_methods[n - 1][m - 1]


def main():
    TC1 = (1, 100)
    TC2 = (100, 1)
    TC3 = (15, 25)
    TC4 = (25, 25)
    TC5 = (25, 15)
    TC6 = (100, 150)
    TC7 = (0, 0)
    TC8 = (-1, 0)
    TC9 = (0, -1)

    testcases = [TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC8, TC9]
    for i, (n, m) in enumerate(testcases):
        print(f"TC {i + 1} : ")
        print(f"하향식 접근법의 결과 : {way2go_td(n, m)}")
        print(f"상향식 접근법의 결과 : {way2go_bu(n, m)}")
    
    print("5X1 그리드 :")
    cnt, methods = way2go_way(5, 1)
    print(f"  이동 방법의 수 : {cnt}")
    print(f"  이동 방법의 목록 : {methods}")

    print("4X5 그리드 :")
    cnt, methods = way2go_way(4, 5)
    print(f"  이동 방법의 수 : {cnt}")
    print(f"  이동 방법의 목록 : {methods}")

if __name__ == '__main__':
    main()