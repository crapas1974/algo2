def filtering_n_by_3(n):
    if n == 1:
        return 0
    if n == 2:
        return 3
    
    dp = [0] * (n + 1)    
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2

    return dp[n]

def main():
    for n in range(1, 21):
        print(f"{n} X 3 크기의 배양기에서 가능한 실험 설정의 수 : {filtering_n_by_3(n)}")

if __name__ == '__main__':
    main()