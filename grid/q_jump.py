def elec_alive_probability_td(n, k, i, j, memo=None):
   # 메모이제이션 딕셔너리 초기화
   if memo == None:
       memo = {}
      
   # 모든 경우의 점프 방식
   moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

   # 그리드 밖으로 나간 경우
   if i < 0 or i >= n or j < 0 or j >= n:
       return 0

   # 마지막 점프이면 그리드 안에 있으므로 확률 1 반환
   if k == 0:
       return 1

   # 메모이제이션된 결과가 있는지 확인
   if (i, j, k) in memo:
       return memo[(i, j, k)]

   prob = 0
   # 가능한 모든 점프에 대해 확률 계산
   for m_i, m_j in moves:
       prob += elec_alive_probability_td(n, k - 1, i + m_i, j + m_j, memo) / 8.0

   # 결과를 메모하고 반환
   memo[(i, j, k)] = prob
   return prob
def elec_alive_probability_bu(n, m, k, i, j):
   # 전자의 이동 방향 정의 - 키는 가중치, 값은 해당 가중치의 이동 방향
   directions = {}
   directions[4] = [(2, 1), (1, 2)]
   directions[2] = [(2, -1), (-2, 1), (1, -2), (-1, 2)]
   directions[1] = [(-2, -1), (-1, -2)]
   # 총 경우를 구하기 위해, 전체 개수를 가중치를 기준으로 곱해서 더한다.
   weight_sum = sum([weight * len(direction) for weight, direction in directions.items()])

   # 확률 배열을 생성하고 초기화한다.
   prob = [[0 for _ in range(m)] for _ in range(n)]
   prob[i][j] = 1  # 시작 위치의 확률은 1

   # k번 퀀텀 점프
   for _ in range(k):
       # 점프 이후의 확률을 저장할 배열
       prob_next = [[0 for _ in range(m)] for _ in range(n)]

       # 모든 위치에 대해
       for i in range(n):
           for j in range(m):
               # 각 확률별 가중치에 대해
               for weight, directions_for_weight in directions.items():
                   # 해당 가중치의 이동 방향에 대해
                   for m_i, m_j in directions_for_weight:
                       next_i, next_j = i + m_i, j + m_j
                       # 그리드 내에 있는 경우 확률을 업데이트 한다.
                       # 가중치 만큼 더하고 가중치 기준의 전체 경우의 수로 나눈다.
                       if 0 <= next_i < n and 0 <= next_j < m:
                           prob_next[next_i][next_j] += prob[i][j] * weight / weight_sum

       # 현재 그리드 밖에 있는 확률                   
       out_grid_prob = 1 - sum(sum(row) for row in prob)
       # 그리드 밖에 있는 전자는 0.1의 확률로 초기 위치(i, j)로 복귀한다.
       prob_next[i][j] += out_grid_prob * 0.1
       # 점프 이후의 확률 배열 계산이 끝난 후, 다음 단계를 위해 현재 배열로 업데이트
       prob = prob_next

   # k번의 퀀텀 점프를 계산한 후, 그리드의 모든 셀의 확률을 더한다.
   return sum(sum(row) for row in prob)

def main():
    TC1 = (3, 2, 0, 0)
    TC2 = (3, 2, 1, 1)
    TC3 = (20, 50, 11, 13)
    TC4 = (1, 10, 0, 0)
    TC5 = (39, 800, 20, 20)

    testcases = [TC1, TC2, TC3, TC4, TC5]
    for i, tc in enumerate(testcases):
        print(f'TC{i + 1} : ', end="")
        print(elec_alive_probability_td(*tc))

    TC1 = (3, 3, 2, 0, 0)
    TC2 = (3, 3, 2, 1, 1)
    TC3 = (20, 25, 50, 11, 13)
    TC4 = (1, 1, 10, 0, 0)
    TC5 = (21, 31, 10, 0, 0)
    TC6 = (21, 31, 10, 11, 16)
    TC7 = (21, 31, 10, 20, 30)
    TC8 = (21, 31, 3000, 0, 0)
    TC9 = (21, 31, 3000, 11, 16)
    TC10 = (21, 31, 3000, 20, 30)
    testcases = [TC1, TC2, TC3, TC4, TC5, TC6, TC7, TC8, TC9, TC10]
    for i, tc in enumerate(testcases):
        print(f'TC{i + 1} : ', end="")
        print(elec_alive_probability_bu(*tc))
        
if __name__ == '__main__':
    main()