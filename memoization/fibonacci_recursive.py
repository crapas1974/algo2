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
    return fibonacci_recursive(n)

def fibonacci_recursive(n):
    if n <= 0: 
        return None
    elif n == 1: 
        return 1
    elif n == 2: 
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
def main():
    testcase = [-1, 0, 5, 10, 15, 20, 25, 30, 35, 40]
    for n in testcase:
        print(f"n = {n}")
        print(f"결과 : {fibonacci_wrapper(n)}")

if __name__ == '__main__':
    main()
