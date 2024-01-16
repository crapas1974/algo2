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
def fibonacci(n):
    # 길이 n인 리스트를 만든다.
    arr = [0] * n
    # 가장 작은 초기 조건은 값이 주어진다.
    arr[0] = 1
    arr[1] = 1
    # 그 이후로는 계산해서 올라가되, 이전에 계산한 결과를 활용한다.
    for i in range(2, n):
        arr[i] = arr[i - 2] + arr[i - 1]
    # 목표한 일반항의 값을 반환한다.
    return arr[n - 1]


def main():
    print("피보나치 수열의 100번째 항의 값 : ", fibonacci(100))

if __name__ == '__main__':
    main()