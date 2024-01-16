import math
import time
def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 수행 시간 - {end - start} 초")
        return result
    return wrapper

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

#@execute_time
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


def factorization_special(n):
    if n <= 0:
        return []    
    if n % 2 == 0:
        return [2] + factorization_special(n // 2)

    a = math.ceil(math.sqrt(n))
    b_square = a * a - n
    b = int(math.sqrt(b_square))
    while b * b != b_square:
        a += 1
        b_square = a * a - n
        b = int(math.sqrt(b_square))
    small_factor = a - b
    large_factor = a + b
    if small_factor == 1:
        return [n]
    return factorization_special(small_factor) + factorization_special(large_factor)

def main():
    start = 1000
    end = 10000
    result = 0
    for i in range(start, end + 1):
        factors = factorization(i)
        factors.sort()
        #print(factors)
        base = ''
        upper = ''
        before = -1
        before_upper = 0
        for j in factors:
            if before != j:
                if before != -1:
                    base += str(before)
                    upper += str(before_upper)
                before = j
                before_upper = 1
                #print(before)
            else:
                before_upper += 1
        base += str(before)
        upper += str(before_upper)
        result += int(base + upper)
        #print(f"{i}, {base}, {upper}, {base + upper}")
    print(f"{start} 이상 {end} 이하의 정수를 소인수 분해 한 결과를 사용해서 만든 수를 모두 더하면 {result}입니다.")
        #print(f"{i} = {factors}")
    
    for i in range(1, 20 ,2):
        n = 100000000 + i
        small_divisor, large_divisor = find_closest_divisors(n)
        print(f"{n}을 두 수의 곱셈으로 나타낼 때 가장 가까운 두 조합은 {small_divisor}와 {large_divisor}이며, 그 차이는 {large_divisor - small_divisor}입니다.")

if __name__ == '__main__':
    main()
# 예시 사용

# #start = 1000000000
# #end = 1000001000
# start = 100000
# end = 110000
# #end = start + 2
# fast_time = 0
# slow_time = 0
# factor_list = []
# time_list = []
# for i in range(start, end):    
#     m = 1
#     start_time = time.time()
#     fl_fast = factorization(i)
#     fast_time += time.time() - start_time
#     fl_fast.sort()
#     start_time = time.time()
#     fl_slow = factorization_slow(i)
#     slow_time += time.time() - start_time
#     fl_slow.sort()
#     if fl_fast != fl_slow:
#         print(i)
#         break
#     #print(f" {i - start}, {slow_time - fast_time}")
#     factor_list.append((fl_fast, slow_time - fast_time, slow_time, fast_time, i))

#    time_list.append(slow_time - fast_time)
    #print(fl_fast)


# print("---")
# factor_list.sort(key=lambda x: x[1])
# print(factor_list[0])
# print(factor_list[1])
# print(factor_list[-2])
# print(factor_list[-1])
# x_sum = 0
# sl_sl = 0
# for factor in factor_list:
#     x_sum += factor[1]
#     if factor[2] > factor[3]:
#         sl_sl += 1
# print(x_sum)
# print(sl_sl)
# print(f"fast_time: {fast_time}")
# print(f"slow_time: {slow_time}")
#     for j in fl:
#         m *= j
#     if m != i:
#         print(i)
#         break
# n = 9999973 * 9999991 * 9999971
# factors = factorization_wrapper(n)
# print(factors)
# factors = factorization_slow(n)
# print(factors)

#n = 2 ** 50 + 1
#factors = factorization(n)
#print(factors)

# pl = prime_numbers_fast(1000)[-4:]
# p_m = []
# for p1 in pl:
#     for p2 in pl:
#         for p3 in pl:
#             for p4 in pl:
#                 p_m.append(p1 * p2 * p3 * p4)



# # pl = prime_numbers_fast(10000000)[-10:]
# # p_m = []
# # for p1 in pl:
# #     for p2 in pl:
# #         p_m.append(p1 * p2)

# p_m = list(set(p_m))
# print(len(p_m))
# time1 = 0
# time2 = 0
# for p in p_m:
#     start_time = time.time()
#     factorization(p)
#     time1_gap = time.time() - start_time
#     time1 += time1_gap
#     start_time = time.time()
#     factorization_special(p)
#     time2_gap = time.time() - start_time
#     time2 += time2_gap
#     print(p, time1_gap, time2_gap)

# print(time1)
# print(time2)

# # print(2 * 2 * 3 * 5 * 7 * 7)
# # fl = factorization(2 * 2 * 3 * 5 * 7 * 7)
# # print(fl)