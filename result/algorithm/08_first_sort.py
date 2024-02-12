from sort_data import testcases
import hashlib

def hash4(result: list):
    return hashlib.md5(str(result).encode()).hexdigest()[:4]

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

def main():
    for i, tc in enumerate(testcases):
        print(f'Testcase {i + 1}의 결과: {hash4(qsort(tc))}')

if __name__ == '__main__':
    main()