import time
from memory_profiler import profile

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 수행 시간 - {end - start} 초")
        return result
    return wrapper

def prime_numbers_with_segment(start, end, small_primes = None):
    result = []
    if start == 0:
        return prime_numbers(end)
    if small_primes == None:
        small_primes = []
    number_cnt = end - start + 1
    sieve = [True] * (number_cnt)
    for prime in small_primes:
        check_start = (start // prime) * prime
        if check_start < start:
            check_start += prime
        for i in range(check_start, end + 1, prime):
            sieve[i - start] = False
    for i in range(number_cnt):
        if sieve[i] == True:
            result.append(i + start)
    return small_primes + result



# eratostesnes sieve
#@profile
# memory usage 
#   boolean list : 1bit * (n + 1) 
#   prime list : 4byte * k (k : number of prime numbers)
@execute_time
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

#step_size = 1000000
step_size = 1000000
#@profile
def prime_numbers2(n):
    start = 0
    result = []
    while True:
        if start + step_size > n:
            result = prime_numbers_with_segment(start, n, result)
            break
        result = prime_numbers_with_segment(start, start + step_size, result)
        start += step_size
    return result

def prime_numbers_with_segment_new(start, end, primes = None):
    if primes == None:
        primes = []
    if start == 0:
        if end < 2:
            primes == 0
            return        
        sieve = [True] * (end + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(end ** 0.5) + 1):
            if sieve[i] == True:
                for j in range(i + i, end + 1, i):
                    sieve[j] = False
        for i in range(2, end + 1):
            if sieve[i] == True:
                primes.append(i)
        return
    
    number_cnt = end - start + 1
    sieve = [True] * (number_cnt)
    for prime in primes:        
        check_start = (start // prime) * prime
        if check_start < start:
            check_start += prime
        for i in range(check_start, end + 1, prime):
            sieve[i - start] = False
    for i in range(number_cnt):
        if sieve[i] == True:
            primes.append(i + start)

def prime_numbers3(n):
    start = 0
    result = []
    while True:
        if start + step_size > n:
            prime_numbers_with_segment_new(start, n, result)
            break
        prime_numbers_with_segment_new(start, start + step_size, result)
        start += step_size
    return result

def prime_numbers_with_segment(start, end, primes = None):
    if primes == None:
        primes = []
    if start == 0:
        if end < 2:
            primes == 0
            return        
        sieve = [True] * (end + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(end ** 0.5) + 1):
            if sieve[i] == True:
                for j in range(i + i, end + 1, i):
                    sieve[j] = False
        for i in range(2, end + 1):
            if sieve[i] == True:
                primes.append(i)
        return
    
    number_cnt = end - start + 1
    sieve = [True] * (number_cnt)
    for prime in primes:        
        check_start = (start // prime) * prime
        if check_start < start:
            check_start += prime
        for i in range(check_start, end + 1, prime):
            sieve[i - start] = False
    for i in range(number_cnt):
        if sieve[i] == True:
            primes.append(i + start)

import math
@execute_time
def prime_numbers_with_small_memory(n):
    step_size_by_number = int((n) / math.log(n, 2))
    start = 0
    result = []
    while True:
        if start + step_size_by_number > n:
            prime_numbers_with_segment(start, n, result)
            break
        prime_numbers_with_segment(start, start + step_size_by_number - 1, result)
        start += step_size_by_number
        #step_size_in_here *= 2
        
    return result


@execute_time
def prime_numbers_slow(n):
    result = []
    if n < 2:
        return result
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result

import hashlib
def hash4(prime_list: list):
    prime_list.sort()
    print(prime_list)
    return hashlib.sha256(str(prime_list).encode()).hexdigest()[:4]

def main():
    target = 1000
    primes = prime_numbers_fast(target)
    print(f"{target} 이하의 모든 소수는 {len(primes)}개이며, 소수의 합은 {sum(primes)} 입니다.")    
    target = 10000000
#    s1 = time.time()
    primes = prime_numbers_fast(target)    
#    e1 = time.time()
    print(f"{target} 이하의 모든 소수는 {len(primes)}개이며, 소수의 합은 {sum(primes)} 입니다.")    
#    s2 = time.time()
    print("공간 효율적으로 구현한 경우")
    primes = prime_numbers_with_small_memory(target)
#    e2 = time.time()
    print(f"{target} 이하의 모든 소수는 {len(primes)}개이며, 소수의 합은 {sum(primes)} 입니다.")    
    # s3 = time.time()
    # primes = prime_numbers5(target)
    # e3 = time.time()
    # print(f"{target} 이하의 모든 소수는 {len(primes)}개이며, 소수의 합은 {sum(primes)} 입니다.")    
    # print(f"소요 시간 : {e1 - s1} 초")
    # print(f"소요 시간 : {e2 - s2} 초")
    # print(f"소요 시간 : {e3 - s3} 초")

    # print(len(primes))
    # print(hash4(primes))
    # start = time.time()
    # a = prime_numbers2(target)
    # end = time.time()
    # print(f"소요 시간 : {end - start} 초")
    # print(len(a))
    # start = time.time()
    # a = prime_numbers3(target)
    # end = time.time()
    # print(f"소요 시간 : {end - start} 초")
    # print(len(a))
    # #print(a)

    # q = [5, 4, 3, 2, 1]
    # print(hash4(q))
    # a = prime_numbers_with_segment(0, 30)
    # print(a)
    # a = prime_numbers_with_segment(31, 60, a)
    # print(a)
    # a = prime_numbers_with_segment(61, 90, a)
    # print(a)
    # start = time.time()
    # primes = prime_numbers4(target)
    # end = time.time()
    # print(f"소요 시간 : {end - start} 초")
    # print(len(primes))

if __name__ == "__main__":
    main()

