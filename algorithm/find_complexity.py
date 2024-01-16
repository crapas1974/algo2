def sigma(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return sigma(n - 1) + n

def max_number1(arr, size):
    result = 0
    for i in range(size):
        if arr[i] > result:
            result = arr[i]
    return result

def max_number2(arr, start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    leading_max = max_number2(arr, start, mid)
    trailing_max = max_number2(arr, mid + 1, end)
    if leading_max > trailing_max:
        return leading_max
    else:
        return trailing_max

def max_number3(arr, start, end):
    if start == end:
        return arr[start]
    if start + 1 == end:
        return arr[start] if arr[start] > arr[end] else arr[end]
    mid = (start + end) // 2
    leading_max = max_number3(arr, start, mid)
    trailing_max = max_number3(arr, mid + 1, end)
    if leading_max > trailing_max:
        return leading_max
    else:
        return trailing_max
    
def find_number1(arr, size, k):    
    for i in range(size):
        if arr[i] > k:
            return -1
        if arr[i] == k:
            return i
    return -1    

def find_number2(arr, start, end, k):
    if start == end:
        if arr[start] == k:
            return start
        else:
            return -1
    mid = (start + end) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return find_number2(arr, start, mid, k)
    else:
        return find_number2(arr, mid + 1, end, k)

import random

def make_distinct_random_list(size):
    arr = [5000]
    while len(arr) < size:
        num = random.randint(1, 10000)
        if num not in arr:
            arr.append(num)
    return arr

def test_c(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * test_c(n // 2) + 1
    else:
        return test_c((n + 1) // 2) + test_c((n - 1) // 2) + 1
def main():
    print("sigma(512)의 결과 :", sigma(512))
    size1 = 512
    arr1 = make_distinct_random_list(size1)
    size2 = 511
    arr2 = make_distinct_random_list(size2)

    arr1_sorted = sorted(arr1)
    arr2_sorted = sorted(arr2)
    print("길이 512의 리스트에서의 최댓값")
    print("    max_number1의 결과 :", max_number1(arr1, size1))
    print("    max_number2의 결과 :", max_number2(arr1, 0, size1 - 1))
    print("    max_number3의 결과 :", max_number3(arr1, 0, size1 - 1))
    print("정렬된 길이 512의 리스트에서 5000의 인덱스 번호")
    print("    find_number1의 결과 :", find_number1(arr1_sorted, size1, 5000))
    print("    find_number2의 결과 :", find_number2(arr1_sorted, 0, size1 - 1, 5000))

    print("길이 511의 리스트에서의 최댓값")
    print("    max_number1의 결과 :", max_number1(arr2, size2))
    print("    max_number2의 결과 :", max_number2(arr2, 0, size2 - 1))
    print("    max_number3의 결과 :", max_number3(arr2, 0, size2 - 1))
    print("정렬된 길이 511의 리스트에서 5000의 인덱스 번호")
    print("    find_number1의 결과 :", find_number1(arr2_sorted, size2, 5000))
    print("    find_number2의 결과 :", find_number2(arr2_sorted, 0, size2 - 1, 5000))

if __name__ == '__main__':
    main()