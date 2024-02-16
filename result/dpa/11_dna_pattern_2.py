from wildcard_pattern_data import testcases
def isMatch(sequence, pattern):
    seq_size = len(sequence)
    pat_size = len(pattern)
    dp = [[False] * (pat_size + 1) for _ in range(seq_size + 1)]
    dp[0][0] = True
    for j in range(1, pat_size + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, seq_size + 1):
        for j in range(1, pat_size + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or sequence[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[seq_size][pat_size]


def main():

    for i, tc in enumerate(testcases):
        sequence, pattern = tc
        ast_pattern = '*' + pattern + '*'
        print(f"Testcase {i + 1}")
        print(f"    '{sequence}'에 패턴 '{pattern}'은 {'포함' if isMatch(sequence, ast_pattern) else '불포함'}")
        print()

if __name__ == '__main__':
    main()