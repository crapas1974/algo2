import math

def find_closest_divisors(n):
    a = math.ceil(math.sqrt(n))
    b_square = a * a - n
    b = int(math.sqrt(b_square))
    while b * b != b_square:
        a += 1
        b_square = a * a - n
        b = int(math.sqrt(b_square))
    small_divisor = a - b
    large_divisor = a + b
    return small_divisor, large_divisor

def prime_numbers_fast(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i] == True]

def factorization(n):
    upper_bound = int(math.sqrt(n))
    primes = prime_numbers_fast(upper_bound)
    result = []
    for prime in primes:
        while n % prime == 0:
            result.append(prime)
            n //= prime
    if n != 1:
        result.append(n)
    return result

def make_factor_sum(start, end):
    result = 0
    for i in range(start, end + 1):
        factors = factorization(i)
        factors.sort()
        before = -1
        cnt = 0
        sub_result = ''
        for f in factors:
            if before == f:
                cnt += 1
            else:
                if before != -1:
                    sub_result += str(before) + str(cnt)
                before = f
                cnt = 1
        sub_result += str(before) + str(cnt)
        result += int(sub_result)
    return result

def main():
    start = 1000 
    end = 10000
    result = make_factor_sum(start, end)
    print(f"{start} 이상 {end} 이하의 정수를 소인수 분해 한 결과를 사용해서 만든 수를 모두 더하면 {result}입니다.")
    
    for i in range(1, 20 ,2):
        n = 100000000 + i
        small_divisor, large_divisor = find_closest_divisors(n)
        print(f"{n}을 두 수의 곱셈으로 나타낼 때 가장 가까운 두 조합은 {small_divisor}와 {large_divisor}이며, 그 차이는 {large_divisor - small_divisor}입니다.")

if __name__ == '__main__':
    main()
