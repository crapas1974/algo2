import sys
sys.setrecursionlimit(1000000)

def count(n):
    if n == 0:
        return 0
    count(n - 1)
    print(n)

def count_reverse(n):
    if n == 0:
        return 0
    print(n)
    count_reverse(n - 1)

def main():
    print("정방향 출력")
    count(10)
    print("역방향 출력")    
    count_reverse(10)
    print("큰 수가 입력 되었을 때")
    count(10000)

if __name__ == "__main__":
    main()

