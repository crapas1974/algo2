# 그리디 알고리즘으로 최소한의 동전 숫자로 금액을 구성하는 방법을 반환하는 함수
#   n: 금액
#   Return Value : (동전의 최소 개수, 각 동전의 개수를 나타내는 딕셔너리)
def greedy_change(n, coins):
    # 동전의 종류를 내림차순으로 정렬
    coins.sort(reverse=True)

    coin_count = 0
    coin_used = {}

    for coin in coins:
        # 해당 동전으로 얼마나 많이 줄 수 있는지 계산
        if n >= coin:
            num = n // coin
            n -= num * coin
            coin_count += num
            coin_used[coin] = num

    return coin_count, coin_used

# 그리디 알고리즘으로 제한된 동전으로 최소한의 동전 숫자로 금액을 구성하는 방법을 반환하는 함수
#   n: 금액
#   Return Value : (동전의 최소 개수, 각 동전의 개수를 나타내는 딕셔너리)
#                   만약 금액을 만들 수 없다면 (None, None)을 반환
def limited_greedy_change(n, max_coins):

    coins = list(max_coins.keys())
    coins.sort(reverse=True)  # 동전의 종류를 내림차순으로 정렬
    # 각 동전의 최대 사용 가능 개수를 설정


    coin_count = 0
    coin_used = {}

    for coin in coins:
        if n >= coin:
            # 가능한 많이 사용되는 동전의 수와 제한된 동전의 수 중 작은 것을 선택
            num = min(n // coin, max_coins[coin])
            n -= num * coin
            coin_count += num

            # 사용한 동전의 개수를 업데이트
            if coin in coin_used:
                coin_used[coin] += num
            else:
                coin_used[coin] = num
#    if n != 0:  # 더 이상 사용할 수 있는 동전이 없는데 남은 금액이 있는 경우
#        break
    return coin_count, coin_used, n

def dynamic_change(n, coins):
    # 금액에 따른 최소 동전 개수와 동전 조합을 저장할 DP 테이블 초기화
    dp = [(n + 1, []) for _ in range(n + 1)]
    dp[0] = (0, [])

    for a in range(1, n + 1):
        for coin in coins:
            if a - coin >= 0:
                if dp[a - coin][0] + 1 < dp[a][0]:
                    dp[a] = (dp[a - coin][0] + 1, dp[a - coin][1] + [coin])

    if dp[n][0] == n + 1:
        return -1, []
    else:
        # 동전 별 개수 계산
        coin_count = {}
        for coin in dp[n][1]:
            if coin in coin_count:
                coin_count[coin] += 1
            else:
                coin_count[coin] = 1
        return dp[n][0], coin_count
import time

def main():
#    coins = [100, 50, 25, 10, 5, 1]
#    coins = [45, 35, 1]

    # n = 99
    # coin_count, coin_used = greedy_change(n, coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)
    # n = 398
    # coin_count, coin_used = greedy_change(n, coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)
    # n = 399
    # coin_count, coin_used = greedy_change(n, coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)

    # max_coins = {
    #     100: float('inf'),  # 무한대
    #     50: float('inf'),
    #     25: 0,
    #     10: 1,
    #     5: float('inf'),
    #     1: 3
    # }

    # n = 99
    # coin_count, coin_used, remain = limited_greedy_change(n, max_coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)
    # print("남은 금액: ", remain)
    
    # n = 398
    # coin_count, coin_used, remain = limited_greedy_change(n, max_coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)
    # print("남은 금액: ", remain)
    
    # n = 399
    # coin_count, coin_used, remain = limited_greedy_change(n, max_coins)
    # print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    # print("이 때의 각 동전의 개수: ", coin_used)
    # print("남은 금액: ", remain)
    coins = [100, 50, 25, 10, 5, 1]
    n = 75
    coin_count, coin_used = dynamic_change(n, coins)
    print(f"사용 가능한 동전 : {coins}")
    print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    print("이 때의 각 동전의 개수: ", coin_used)
    coins = [35, 25, 1]
    n = 75
    coin_count, coin_used = dynamic_change(n, coins)
    print(f"사용 가능한 동전 : {coins}")
    print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    print("이 때의 각 동전의 개수: ", coin_used)
    coins = [100, 50, 25, 10, 5, 1]
    n = 111
    coin_count, coin_used = dynamic_change(n, coins)
    print(f"사용 가능한 동전 : {coins}")
    print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    print("이 때의 각 동전의 개수: ", coin_used)
    coins = [35, 25, 1]
    n = 111
    coin_count, coin_used = dynamic_change(n, coins)
    print(f"사용 가능한 동전 : {coins}")
    print(f"{n}센트를 거슬러 줄 때 필요한 동전의 최소 개수: {coin_count}")
    print("이 때의 각 동전의 개수: ", coin_used)

    coins = [100, 50, 25, 10, 5, 1]
    n = 999999
    s = time.time()
    coin_count1, coin_used1 = dynamic_change(n, coins)
    e1 = time.time()
    print(e1 - s)
    coin_count2, coin_used2 = greedy_change(n, coins)
    e2 = time.time()
    print(e1 - s, e2 - e1)


if __name__ == "__main__":
    main()