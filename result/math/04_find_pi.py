import random

def pi_simulation(n):
    cnt = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            cnt += 1
    return 4 * cnt / n

def integral_simulation(n, func):
    start = 0
    end = 1
    sum = 0
    for _ in range(n):
        x = random.uniform(start, end)
        sum += func(x)
    return (end - start) * sum / n

import math
def main():
    end = 7
    func1 = lambda x: x ** 2
    func2 = lambda x: math.e ** x
    for i in range(1, end + 1):
        print(f"{10 ** i}번 반복한 시뮬레이션에서 pi의 근사값 : {pi_simulation(10 ** i)}")
        print(f"{10 ** i}번 반복한 시뮬레이션에서 y = x^2의 0에서 1사이의 정적분 값의 근사값 : {integral_simulation(10 ** i, func1)}")
        print(f"{10 ** i}번 반복한 시뮬레이션에서 y = e^x의 0에서 1사이의 정적분 값의 근사값 : {integral_simulation(10 ** i, func2)}")

if __name__ == '__main__':
    main()