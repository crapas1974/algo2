def remove_rival_recursive(n, k):
    if n == 1:
        return 0 
    else:
        return (remove_rival_recursive(n - 1, k) + k) % n

# 예제: 7명의 사람, 각 단계에서 3번째 사람을 제거
# n = 100000
# k = 1000
# last_person = josephus_recursive(n, k) + 1  # 사람의 위치는 1부터 시작하므로 1을 더함
# print(f"마지막으로 남는 사람의 위치: {last_person}")
def main():
    testcases = [(7, 3), (15, 5), (1, 10), (10, 1), (15, 5), (5, 15), (30, 30), (1000, 1), (1000, 39), (100000, 100), (100000, 333), (100000, 1000)]
    for i, (n, k) in enumerate(testcases):
        last_virus = remove_rival_recursive(n, k) + 1
        print(f"testcase {i + 1}: {last_virus}")

if __name__ == "__main__":
    main()