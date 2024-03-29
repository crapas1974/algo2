import time

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper
@execute_time
def dna_break_bf_wrapper(sequence, patterns):
    return dna_break_bf(sequence, patterns)
def dna_break_bf(sequence, patterns):
    for pattern in patterns:
        # 종료조건 1 : 염기서열 문자열이 주어진 패턴 중 하나인 경우 (True)
        if pattern == sequence:
            return True
        if pattern == sequence[:len(pattern)]:
            # 패턴을 제외한 나머지 부분을 재귀호출한다.
            result = dna_break_bf(sequence[len(pattern):], patterns)
            if result:
                return True
    # 종료조건 2 : 염기서열 문자열이 주어진 패턴 중 하나로 시작하지 않는 경우 (False)
    return False
@execute_time
def dna_break_bu(sequence, patterns):
    sequence_length = len(sequence)
    # 각 위치에서의 분리 가능 여부를 저장하는 배열
    # 초기값은 모두 False
    dp = [False] * (sequence_length + 1)
    dp[0] = True
    for i in range(1, sequence_length + 1):
        for j in range(i):
            if dp[j] and sequence[j:i] in patterns:
                dp[i] = True
                break
    return dp[sequence_length]

def dna_break_and_broken(sequence, patterns):
    # 결과를 저장할 배열
    results = []
    for pattern in patterns:
        # 종료조건 1 : 염기서열 문자열이 주어진 패턴 중 하나인 경우 - [pattern]을 반환한다.
        if pattern == sequence:
            return [pattern]
        if pattern == sequence[:len(pattern)]:
            # 패턴을 제외한 나머지 부분을 재귀호출한다.
            results_after = dna_break_and_broken(sequence[len(pattern):], patterns)
            # 반환 결과는 빈 배열 (실패인 경우) 또는 나머지 부분을 패턴으로 쪼갠 결과들의 목록이다.
            # 빈 배열이 아닌 경우, 현재 패턴과 나머지 부분의 결과의 각각을 합쳐서 현재의 결과 목록에 추가한다.
            # 모든 결과를 찾아야 하므로, 참인 경우에도 바로 반환하지 않고, 계속해서 탐색한다.
            for result_after in results_after:
                results.append(pattern + " " + result_after)
    # 종료조건 2 : 염기서열 문자열이 주어진 패턴 중 하나로 시작하지 않는 경우 - []를 반환한다.    
    return results


def main():
    # patterns = ['CTAG', 'GCC', 'CTA']
    # test1 = "CTAG"
    # test2 = "GCCCTACTAG"
    # test3 = "CCCCCCCCCC"
    # test4 = "GTTTCAGGGA"
    # test5 = "CTAGCTAGCC"
    # test6 = "CTACTAGCTAGCC"
    # test7 = "ACCAGAGTCTCTCCTCTTAC"
    # test8 = "GCCCTACTAGCCCTAGCTAGCCCTAGGCCCTAGCCCTAGCCGCCGCCCTACTAGCCCTACTA"
    # test9 = "GCCCTAGCTAGCTAGCCGCCGCCCTACTACTAGCCGCCGCCTAGCCGCCCTACTACTAGGCCCTAG"
    # test10 = "CTAGCTACTACTAGCTAGCTAGCTAGCTAGCTACTAGCTACTAGCTAGCCCTAGCTACTAGCTAGCTAGCTAGCTAGGCCGCCCTAGCTAGGCCGCCCTAGCTAGCTAGGCCGCCCTAGCTAGGCCGCCCTAGCTAGCTAGCTACTAGCTACTAGCTAGCCGCCCTAGCCCTACTAG"
    # test11 = "GCCCTAGCTACTAGCTAGCTAGCCGCCCTACTAGGCCGCCCTACTACTAGGCCGCCGCCCTAGCTAGGCCGCCCTACTAGCTACTAGCTAGCTACTAGCTACTAGCTACTAGGCCGCCCTACTAGGCCCTACTAGGCCCTAGCCGCCCTAGCTAGGCCGCCCTACTAGGCCCTACTACTAGGCCCTAGCTACTAGCTAGGCCCTAGGCCGCCCTAGGCCCTACTACTACTAGCCGCCGCCCTACTAGGCCCTACTACTAGCCCTAGGCCCTAGCTAGCTACTAGCCGCCCTAGCTAGGCCGCCGCCGCCCTAGGCCGCCCTAGCCGCCCTACTACTACTACTAGCTACTACTAGCTAGCTACTAGCTACTAGGCCGCCGCCGCCCTACTAGGCCCTACTAGCTACTAGCCCTACTACTACTACTAGCCGCCGCCCTAGCTAGCCGCCCTAGGCCCTACTACTACTAGCCGCCCTAGGCCCTACTAGCCCTAGGCCCTAGCCCTAGCTAGCCCTAGCTAGCTAGCCGCCCTACTACTAGCTACTAGCTAGCTAGCTAGGCCCTAGCTAGGCCGCCGCCCTAGGCCCTACTAGCTAGCCGCCCTACTAGGCCGCCCTAGCTAGCCCTAGCCCTAGCCGCCCTAGCTAGCTACTAGCCCTACTAGCTAGCTAGCCCTACTAGCTACTAGCTAGCCCTACTACTAGCCCTACTAGCTACTACTAGCCCTAGGCCCTAGGCCCTAGCTACTACTAGGCCGCCGCCCTACTAGCCGCCGCCCTAGGCCCTACTACTAGGCCGCCGCCCTAGCTAGCCCTAGGCCCTAGCTAGGCCCTAGCCCTACTAGGCCCTAGCTAGCTAGCTAGGCCGCCCTAGCTAGCTAGCCGCCGCCGCCCTAGCCCTAGGCCCTAGCTAGCCGCCGCCCTAGCCCTAGCCGCCCTACTAGCTAGCTACTACTAGCTAGCTACTAGCTACTAGCTAGCCCTAGCCCTAGGCCGCCGCCGCCCTAGCCCTACTACTACTAGCCCTAGGCCCTACTAGCTAGGCCGCCCTAGCCCTAGCTAGCTAGCTAGCTACTACTAGGCCCTAGCTAGCCCTAGGCCGCCCTACTAGCTAGCTACTAGCTAGCTAGCTAGCCGCCCTAGGCCGCCCTAGCCCTAGGCCGCCGCCCTACTACTAGCCCTACTACTAGCTACTAGCTAGCTACTAGCTAGCTAGGCCCTACTAGCTACTAGCCCTAGCTAGCTAGCCCTAGCTAGGCCCTAGCCCTACTAGCCGCCCTAGCCGCCCTACTAGGCCGCCCTAGCTACTAGCTAGCTACTACTAGCCCTAGCCGCCGCCGCCCTACTAGCTAGGCCGCCGCCGCCCTAGCTAGCCCTACTAGCTAGCTAGCTAGCTAGCTAGGCCGCCCTAGCTAGCCCTACTAGCTACTAGGCCCTAGCTACTAGCCCTAGGCCCTACTACTAGCTACTAGCTAGCCCTACTAGCTAGCTAGCCCTAGCTACTAGGCCCTACTAGCTAGCTAGCCCTACTAGCTAGCTACTAGCCCTAGCTAGCTACTAGCCCTAGGCCGCCGCCCTAGCCCTAGCTACTAGCTAGCTAGCTACTAGCTAGCTAGCTAGCCCTACTACTACTAGCCGCCCTAGCTACTACTACTAGCCCTAGCTAGCTAGCCCTACTACTACTAGCTAGCCCTACTAGCTAGCCGCCCTAGCTAGCTAGCTACTAGCCCTACTAGCCCTACTACTAGCTACTAGGCCCTAGGCCGCCCTAGCCCTAGGCCCTACTAGCTACTACTAGCTAGCTAGGCCGCCCTACTACTACTACTAGCTACTACTAGCTAGCTAGCCGCCCTAGCTAGGCCGCCGCCCTAGCTAGCTAGCTAGCTAGCTAGCTACTAGCTAGCTACTAGCTACTAGCCCTAGCTAGCTAGCTAGCTACTAGCTACTAGCTACTAGCCCTAGCCCTAGGCCGCCGCCGCCCTAGCTAGGCCCTAGCTAGCCGCCCTACTAGGCCCTAGCTAGCTACTAGGCCGCCGCCCTACTAGCTAGGCCGCCCTACTAGGCCCTAGCCCTACTAGCTACTAGCCGCCCTACTAGGCCCTAGCTAGCTACTAGCTACTACTAGCCGCCCTAGCCCTAGCTACTAGCTAGCCCTACTACTAGCTAGCTACTAGCTACTAGCCCTACTACTAGCCCTAGCTACTAGGCCCTAGCCGCCCTAGCCCTACTAGGCCGCCCTACTACTAGCCGCCCTACTAGGCCCTAGCTAGCTACTAGCTAGCCCTACTACTAGCTACTAGGCCCTAGCTACTAGCCCTAGCTACTAGCTAGCTAGGCCCTAGCTAGCTAGCTAGCTACTAGCTACTAGCTAGCTAGGCCCTACTAGCTACTAGGCCCTAGCTAGCCGCCCTAGCTAGCTAGCCCTAGCTAGGCCGCCGCCGCCCTACTAGCTACTACTAGCTAGCCGCCCTACTAGCCCTAGCTACTACTAGCTAGGCCGCCCTAGGCCCTACTAGCCCTAGCCCTACTAGCTAGGCCGCCCTAGGCCCTACTACTAGGCCGCCGCCCTACTAGCTAGCTAGCTAGCTAGCCCTACTAGGCCCTAGCCCTAGGCCCTACTACTAGCTAGCTACTACTAGGCCCTAGGCCCTACTAGCTAGCTACTAGCTAGGCCCTAGCTAGCTAGGCCCTAGCTACTAGCCGCCCTAGCTAGCTAGCCCTACTAGGCCCTAGGCCGCCCTACTAGCTAGCCGCCGCCCTAGGCCGCCCTAGCTACTAGCTAGCCGCCCTAGCTAGCTAGCCCTACTAGGCCCTAGCTAGCTAGCTAGGCCCTACTACTACTAGCCCTAGCTAGGCCCTACTAGCTACTAGCTACTAGGCCCTAGCCCTAGGCCGCCCTAGCTACTACTACTAGCCCTAGCTAGGCCCTAGCTAGCTAGCTACTACTAGCCGCCCTACTAGCCCGATTAGCTACTAGGCCGCCCTACTAGCTAGCTAGCTACTAGCTAG"
    # testcases = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11]

    patterns = ['CT', 'TA', 'AG', 'CTT', 'AAG']
    test1 = "CTTAAG"
    test2 = "GCCCTACTAGCCCTAGCTAGCCCTAGGCCCTAGCCCTAGCCGCCGCCCTACTAGCCCTACTA"
    test3 = "AGCTCTTAAAGAAGTATAAGCTTCTCTTCTCTTCTTAAGTAAGCTCTTACTCTTAAGCTAGAGAGAGAG"
    testcases = [test1, test2, test3]

    for i, testcase in enumerate(testcases):
        print(f"TC {i + 1}을 자른 결과 : {dna_break_and_broken(testcase, patterns)}")
        print()
              
              
              

if __name__ == '__main__':
    main()