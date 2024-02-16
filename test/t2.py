def countWays(n):
    # dp 배열 초기화
    dp = [0] * (n + 1)
    
    # 기본 경우 설정
    dp[0] = 1  # 빈 그리드의 경우
    if n >= 1:
        dp[1] = 0  # 1x3 그리드는 채울 수 없음
    if n >= 2:
        dp[2] = 3  # 2x3 그리드는 3가지 방법으로 채울 수 있음

    # n >= 3 인 경우의 점화식
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2

    return dp[n]

# 예제 사용
n = 8
print(countWays(n))