from wildcard_pattern_data import testcases
def isMatch(sequence, pattern):

    seq_size = len(sequence)
    pat_size = len(pattern)
    dp = [[False] * (pat_size + 1) for _ in range(seq_size + 1)]

    # 빈 문자열끼리의 매칭
    dp[0][0] = True

    # 패턴의 시작 부분이 '*'인 경우 처리
    for j in range(1, pat_size + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, seq_size + 1):
        for j in range(1, pat_size + 1):
            if pattern[j - 1] == '*':
                # '*'가 0개 또는 그 이상의 문자와 매칭될 때
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or sequence[i - 1] == pattern[j - 1]:
                # 일반 문자 또는 '?'와의 매칭
                dp[i][j] = dp[i - 1][j - 1]

    return dp[seq_size][pat_size]


def main():

    for i, tc in enumerate(testcases):
        sequence, pattern = tc
        pattern = '*' + pattern + '*'
        print(f"Testcase {i + 1} : {'포함' if isMatch(sequence, pattern) else '불포함'}")
        print()

if __name__ == '__main__':
    main()