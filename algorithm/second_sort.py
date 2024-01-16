def msort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = msort(arr[:mid])
    right = msort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) or right_index < len(right):
        if left_index >= len(left):
            merged.append(right[right_index])
            right_index += 1
        elif right_index >= len(right):
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    return merged

import hashlib
def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]

import random
def make_number_list(min, max, size):
    arr = []
    for i in range(size):
        arr.append(random.randint(min, max))
    return arr

def make_sequence_list(min_length, max_length, size):
    arr = []
    for i in range(size):
        arr.append(''.join(random.choice('ACGT') for _ in range(random.randint(min_length, max_length))))
    return arr

def make_number_testcases():
    testcases = []
    testcases.append([3, 2, 1, 5, 4])
    testcases.append([1])
    testcases.append([1, 1, 1, 1, 1])
    testcases.append([1, 2, 3, 4, 5])
    testcases.append([5, 4, 3, 2, 1])
    testcases.append(make_number_list(10000, 20000, 20))
    testcases.append(make_number_list(-100, 100, 30))
    testcases.append(make_number_list(1, 100, 100))

    with open('testcase1.txt', 'w') as f:
        for i, tc in enumerate(testcases):
            f.write(f'testcase {i + 1}\n{len(tc)}\n')
            for i, n in enumerate(tc):
                f.write(str(n) + '\n')

def make_sequence_testcases():
    testcases = []
    testcases.append(['CTCAT', 'TACAG', 'GACT', 'TAGGC', 'ATCTA'])
    testcases.append(['CATG'])
    testcases.append(['CATG', 'CATG', 'CATG', 'CATG', 'CATG'])
    testcases.append(['ATCTA', 'CTCAT', 'GACT', 'TACAG', 'TAGGC'])
    testcases.append(['TAGGC', 'TACAG', 'GACT', 'CTCAT', 'ATCTA'])
    testcases.append(make_sequence_list(10, 40, 20))
    testcases.append(make_sequence_list(1, 60, 30))
    testcases.append(make_sequence_list(10, 80, 100))

    with open('testcase2.txt', 'w') as f:
        for i, tc in enumerate(testcases):
            f.write(f'testcase {i + 1}\n{len(tc)}\n')
            for i, n in enumerate(tc):
                f.write(str(n) + '\n')

def main():
    print("숫자 리스트")
    with open('testcase1.txt', 'r') as f:
        number_list = []
        i = 0
        line = f.readline()
        while True:
            if not line or line[0:8] == 'testcase':
                if i == 0:
                    i += 1
                    line = f.readline()
                else:
                    print(f"testcase {i}")
                    sorted_list = msort(number_list)
                    result = ''
                    for n in sorted_list:
                        result += str(n % 10)
                    print(f"    계산한 간이 해시 값 : {hash4(result)}")
                    number_list = []
                    i += 1
                    line = f.readline()
                if not line:
                    break
                
            else:
                number_list.append(int(line.strip()))
            line = f.readline()

    print("\n유전자 시퀀스 리스트")
    with open('testcase2.txt', 'r') as f:
        sequence_list = []
        i = 0
        line = f.readline()
        while True:
            if not line or line[0:8] == 'testcase':
                if i == 0:
                    i += 1
                    line = f.readline()
                else:
                    print(f"testcase {i}")
                    sorted_list = msort(sequence_list)
                    result = ''
                    for sequence in sorted_list:
                        result += sequence[0]
                    print(f"    계산한 간이 해시 값 : {hash4(result)}")
                    sequence_list = []
                    i += 1
                    line = f.readline()
                if not line:
                    break
                
            else:
                sequence_list.append(line.strip())
            line = f.readline()




if __name__ == '__main__':
    main()