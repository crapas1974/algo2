def qsort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    pivot_count = 1
    
    for i in range(1, len(arr)):        
        if arr[i] < pivot:            
            left.append(arr[i])
        elif arr[i] > pivot:            
            right.append(arr[i])
        else:            
            pivot_count += 1
    return qsort(left) + [pivot] * pivot_count + qsort(right)

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

import random, time

def main():
    for i in range(5):
        list = []
        for _ in range(10 ** (i + 2)):
            list.append(random.randint(1, 10000))
        
        qsort_start = time.time()
        qsort(list)
        qsort_end = time.time()
        m_sort_start = time.time()
        msort(list)
        m_sort_end = time.time()
        print(f"길이가 {10 ** (i + 2)}인 리스트 정렬에 걸린 시간")
        print(f"    퀵 정렬: {qsort_end - qsort_start}초")
        print(f"    병합 정렬: {m_sort_end - m_sort_start}초")
        print()

if __name__ == "__main__":
    main()
