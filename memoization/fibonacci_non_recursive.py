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
def fibonacci_non_recursive(n):
    if n <= 0:
        return None
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    fib_n_2 = 1
    fib_n_1 = 1
    for _ in range(3, n + 1):
        fib_n = fib_n_2 + fib_n_1
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
    return fib_n
    
def main():
    testcase = [5, 10, 15, 20, 25, 30, 35, 40, 100]
    for n in testcase:
        print(f"n = {n}")
        print(f"결과 : {fibonacci_non_recursive(n)}")

if __name__ == '__main__':
    main()
