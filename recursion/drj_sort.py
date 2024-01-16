import time
import random

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def drj_sort_1_wrapper(arr):
    return drj_sort_1(arr)

@execute_time
def drj_sort_2_wrapper(arr):
    return drj_sort_2(arr)

def drj_sort_2(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = drj_sort_2(arr[:mid])
    right = drj_sort_2(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def drj_sort_1(arr):
    # 기본 단계: 원소의 수가 0 또는 1이면 이미 정렬되어 있음
    if len(arr) <= 1:
        return arr
		
    pivot = arr[len(arr) // 2]  # 피벗을 중간 요소로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 요소들
    middle = [x for x in arr if x == pivot]  # 피벗과 동일한 요소들
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소들

    return drj_sort_1(left) + middle + drj_sort_1(right)

def main():
    # arr = [5, 4, 3, 2, 1]
    # print('input_list : ', arr)
    # print('drj_sort_1 : ', drj_sort_1(arr))
    # print('drj_sort_2 : ', drj_sort_2(arr))
    test_10 = [random.randint(1, 10000) for _ in range(10)]
    test_100 = [random.randint(1, 10000) for _ in range(100)]
    test_1000 = [random.randint(1, 10000) for _ in range(1000)]
    test_10000 = [random.randint(1, 10000) for _ in range(10000)]
    test_100000 = [random.randint(1, 10000) for _ in range(100000)]
    test_1000000 = [random.randint(1, 10000) for _ in range(1000000)]
    testcases = [test_10, test_100, test_1000, test_10000, test_100000, test_1000000]
    for i in range(len(testcases)):
        print(f"test size : {len(testcases[i])}")
        drj_sort_1_wrapper(testcases[i])
        drj_sort_2_wrapper(testcases[i])


if __name__ == '__main__':
    main()