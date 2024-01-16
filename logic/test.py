import time
import random

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 수행 시간 - {end - start} 초")
        return result
    return wrapper

def distance(arr):
    max = -1
    count = 0
    idx = []
    for i, (n1, n2) in enumerate(arr):                
        xor_result = n1 ^ n2
        count = bin(xor_result).count('1')
        if count > max:
            max = count
            idx = [i + 1]
        elif count == max:
            idx.append(i + 1)
    return idx, max

@execute_time
def distance3(arr):
    max = -1
    count = 0
    idx = []
    for i, (n1, n2) in enumerate(arr):                
        xor_result = n1 ^ n2
        count = 0
        while xor_result > 0:
            if xor_result % 2 == 1:
                count += 1
            xor_result //= 2
#        count = bin(xor_result).count('1')
        if count > max:
            max = count
            idx = [i + 1]
        elif count == max:
            idx.append(i + 1)
    return idx, max

@execute_time

def distance2(arr):
    max = -1
    idx = []
    
    for i, (n1, n2) in enumerate(arr):
        count = 0
        while n1 > 0 or n2 > 0:
            if n1 % 2 != n2 % 2:
                count += 1
            n1 //= 2
            n2 //= 2
        if count > max:
            max = count
            idx = [i + 1]
        elif count == max:
            idx.append(i + 1)
    return idx, max

def make_test_list(size):
    arr = []
    for i in range(size):
        n1 = random.randint(0, 1023)
        n2 = random.randint(0, 2 ** 20 - 1)
        # n1 = random.randint(0, 1023)
        # n2 = random.randint(0, 1023)
        arr.append((n1, n2))
    return arr

def main():
    with open("new_chemical_test.txt", "r") as f:
        lines = f.readlines()
        testcases = []
        tc1 = []
        for i in range(5):
            tc1.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc1)
        tc2 = []
        for i in range(5, 1005):
            tc2.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc2)
        tc3 = []
        for i in range(1005, 11005):
            tc3.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc3)

#    tc1 = [(26, 13), (173, 205), (17, 142), (123, 13), (154, 77)]
#    tc2 = make_test_list(1000)
#    tc3 = make_test_list(10000)
#    testcases = [tc1, tc2, tc3]
#    for tc in testcases:
#        for n1, n2 in tc:
#            print(f"{n1},{n2}")
    for i, tc in enumerate(testcases):        
        idx, _ = distance(tc)
        print(f"testcase {i + 1}의 결과 : {sum(idx)}")
    # testcase_i = []
    # for i in range(10000):
    #     n1 = random.randint(1, 1023)
    #     n2 = random.randint(1, 1023)
    #     testcase_i.append((n1, n2))

    # print(n1, n2)
    # print(distance1(n1, n2))
    # print(distance2(n1, n2))

if __name__ == '__main__':
    main()