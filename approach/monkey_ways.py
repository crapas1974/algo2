def monkey_get_banana_td(scores, target, ws_memo = None):
    # ws_memo - 메모이제이션 dictionaly로,
    # 호출하지 않을 때가 처음 실행되는 시점으로 초기화한다.
    if ws_memo == None:
        ws_memo = {}
   
    # ws_memo에 있는 경우 재활용한다.
    if target in ws_memo:
        return ws_memo[target]
    result = []


    for score in scores:
        # 종료조건 1 : target과 딱 맞은 행동을 하는 경우 (성공)
        if score == target:
            result.append([score])
        # 종료조건 2 : 선택한 행동이 target보다 점수가 높은 경우
        elif score > target:
            continue
        else:
            # 행동 후 남은 점수에 대해 재귀호출한다.
            subsequences = monkey_get_banana_td(scores, target - score, ws_memo)
            # 결과의 목록 각각에 현재 행동을 앞에 추가한다.
            for subseq in subsequences:
                result.append([score] + subseq)
    # 메모이제이션        
    ws_memo[target] = result
    return result

def monkey_get_banana_bu(scores, target):
    # DP 테이블 초기화: 각 점수에 도달하기 위한 방법을 저장할 리스트
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # 0점에 도달하는 방법은 아무것도 하지 않는 것


    # 1점부터 차례로 올라가면서 각 점수에 대해 가능한 모든 조합을 찾아 DP 테이블에 저장
    for current_score in range(1, target + 1):
        for score in scores:
            # 선택한 행동을 취할 수 있으면
            if score <= current_score:
                # 해당 행동을 취한 후의 점수 (현재 점수에서 행동 점수를 뺀 값)의 목록에
                # 해당 행동의 점수를 앞에 추가하고, 이 목록을 취합한다.
                for sequence in dp[current_score - score]:
                    dp[current_score].append(sequence + [score])


    return dp[target]

def main():
    testcases = [([15, 20], 10), ([1, 2, 3], 6), ([12, 14, 16, 18, 20], 105), ([13, 17, 19], 56)]
    for i, (scores, target) in enumerate(testcases):
        print(f"TC {i + 1} : ")
        print(f"상향식 접근법의 결과 : {monkey_get_banana_bu(scores, target)}")
        print(f"하향식 접근법의 결과 : {monkey_get_banana_td(scores, target)}")

if __name__ == '__main__':
    main()