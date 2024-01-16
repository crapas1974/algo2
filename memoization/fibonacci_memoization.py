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
def fibonacci_wrapper(n):
    return fibonacci_memoization(n)

def fibonacci_memoization(n, memo=None):
    if memo == None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0: 
        return None
    elif n == 1: 
        return 1
    elif n == 2: 
        return 1
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
        return memo[n]
    
def main():
    testcase = [5, 10, 15, 20, 25, 30, 35, 40, 100]
    for n in testcase:
        print(f"n = {n}")
        print(f"결과 : {fibonacci_wrapper(n)}")

if __name__ == '__main__':
    main()
