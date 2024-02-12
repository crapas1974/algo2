from sort_data import testcases
import hashlib

def hash4(result: list):
    return hashlib.md5(str(result).encode()).hexdigest()[:4]

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

def main():
    for i, tc in enumerate(testcases):
        print(f'Testcase {i + 1}의 결과: {hash4(msort(tc))}')

if __name__ == '__main__':
    main()