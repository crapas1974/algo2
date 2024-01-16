
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def catalan_number(n):
    return binomial_coefficient(2 * n, n) // (n + 1)

def pattern_cnt(change_remain, current_level = 0):
    if change_remain == 0:
        return 1
    result_from_minus = 0
    if current_level > 0:
        result_from_minus = pattern_cnt(change_remain, current_level - 1)
        if result_from_minus == -1:
            return -1
    result_from_plus = pattern_cnt(change_remain - 1, current_level + 1)
    if result_from_plus == -1:
        return -1
    return result_from_minus + result_from_plus

def main():
    for i in range(1, 11):
        print(f"n = {i}일 때의 전체 패턴의 개수 : {pattern_cnt(i)}")
    print(f"n = 100일 때의 전체 패턴의 개수 : {catalan_number(100)}")

if __name__ == '__main__':
    main()


