import time

def fast_remainder_of_telomere(n, k, d):
    return fast_modular_of_exponatial(n, 2 ** k, d)

def fast_modular_of_exponatial(n, k, d):
    result = 1    
    n = n % d

    while k > 0:
        if k % 2 == 1:
            result = (result * n) % d
        k = k // 2
        n = (n ** 2) % d
    return result

def remainder_of_telomere(n, k, d):
    return modular_of_exponatial(n, 2 ** k, d)

def modular_of_exponatial(n, k, d):
    result = 1
    for _ in range(k):
        result = (result * n) % d        
    return result


def main():
    testcases = [
        (6, 3, 43),
        (1, 1, 1),
        (1, 20, 1),
        (2, 20, 65535),
        (6, 10, 43),
        (6, 25, 43),
        (23, 19, 17),
        (81, 10, 1039),
        (33, 3, 1000000007),
        (1079, 30, 8887)
    ]
    for i, tc in enumerate(testcases):
        result = remainder_of_telomere(*tc)
        print(f"Testcase {i + 1}의 결과 : {result}")

    print(f"(n, r, k) = (1079, 30, 8887)일 때 빠른 함수의 결과 : {fast_remainder_of_telomere(1079, 30, 8887)}")
    print(f"(n, r, k) = (6, 100, 43)일 때 빠른 함수의 결과 : {fast_remainder_of_telomere(6, 100, 43)}")

if __name__ == '__main__':
    main()
