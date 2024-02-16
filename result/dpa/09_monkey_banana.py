def monkey_get_banana_td(scores, target, ws_memo = None):
    if ws_memo == None:
        ws_memo = {}
   
    if target in ws_memo:
        return ws_memo[target]
    result = []


    for score in scores:
        if score == target:
            result.append([scores.index(score)])
        elif score > target:
            continue
        else:
            subsequences = monkey_get_banana_td(scores, target - score, ws_memo)
            for subseq in subsequences:
                result.append([scores.index(score)] + subseq)
    ws_memo[target] = result
    return result

def monkey_get_banana_bu(scores, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for current_score in range(1, target + 1):        
        for score in scores:
            if score <= current_score:
                for sequence in dp[current_score - score]:
                    dp[current_score].append(sequence + [(score, scores.index(score))])
    result = []
    for sequence in dp[target]:
        result.append([score[1] for score in sequence])

    return result

def main():
    testcases = [([10, 20], 30), ([40, 20], 90), ([15, 20], 10), ([1, 2, 3], 6), ([12, 14, 16, 18, 20], 105), ([13, 17, 19], 56), ([101, 107, 109], 533)]
    for i, (scores, target) in enumerate(testcases):
        print(f"TC {i + 1} : ")
        bottomup_result = monkey_get_banana_bu(scores, target)
        print(f"    상향식 접근법의 결과 : {sorted(bottomup_result)}")
        
        topdown_result = monkey_get_banana_td(scores, target)
        print(f"    하향식 접근법의 결과 : {sorted(topdown_result)}")

if __name__ == '__main__':
    main()