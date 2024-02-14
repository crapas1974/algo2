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
def combination_td_wrapper(n, m):
    return combination_td(n, m)
def combination_td(n, m, memo = None):
    if memo == None:
        memo = {}
    if n < 0 or m < 0:
        return None
    if n < m:
        return None
    if (m == 0) or (n == m):
        return 1
    elif (n, m) in memo:
        return memo[(n, m)]
    else:
        memo[(n, m)] = combination_td(n - 1, m, memo) + combination_td(n - 1, m - 1, memo)
        return memo[(n, m)]

@execute_time    
def combination_bu(n, m, comb = {}):
    if n < 0 or m < 0:
        return None
    if n < m:
        return None
    for i in range(0, n + 1):
        for j in range(0, i + 1):
            if j == 0:
                comb[(i, j)] = 1
            elif i == j:
                comb[(i, j)] = 1
            else:
                comb[(i, j)] = comb[(i - 1, j)] + comb[(i - 1, j - 1)]
            if (i == n) and (j == m):
                return comb[(i, j)]
            
def main():
    print("combination(900, 450)의 경우")
    print(f"하향식 접근 방식 : {combination_td_wrapper(900, 450)}")
    print()
    print(f"상향식 접근 방식 : {combination_bu(900, 450)}")
    print()
    print("combination(900, 5)의 경우")    
    print(f"하향식 접근 방식 : {combination_td_wrapper(900, 5)}")
    print()
    print(f"상향식 접근 방식 : {combination_bu(900, 5)}")

if __name__ == '__main__':
    main()