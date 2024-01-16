def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be integer")
    if n < 1:        
        raise ValueError("Input must be positive integer")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sigma(n):
    if not isinstance(n, int):
        raise TypeError("Input must be integer")
    if n == 1:
        return 1
    if n < 1:
        raise ValueError("Input must be positive integer")
    return n + sigma(n - 1)
    
def main():
    testcase = [10, 15, 20, 25, 30, 0.5, 0, -1]
    for n in testcase:
        try:
            print(f"n = {n}일 때")
            fib_result = fibonacci(n)
            sig_result = sigma(n)
            print(f"  1에서 n까지의 합 : {sig_result}")
            print(f"  피보나치 수열의 일반항 : {fib_result}")
        except TypeError as e:
            print(f"  예외 발생 : {e}")
        except ValueError as e:
            print(f"  예외 발생 : {e}")
            
if __name__ == "__main__":
    main()