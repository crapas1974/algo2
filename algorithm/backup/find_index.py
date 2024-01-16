# 이 함수의 시간 복잡도는 O(log n)이다.

def find_index(target, arr):
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11]
    target = -1
    result = find_index(target, arr)
    print("1st result : ", end='')
    if result == -1:
        print(f"cannot find item value {target}")
    else:
        print(f'{result}')
    arr = [1, 2, 3, 5, 18, 20, 22]
    target = 20
    result = find_index(target, arr)
    print("2nd result : ", end='')
    if result == -1:
        print(f"cannot find item value {target}")
    else:
        print(f'{result}')

if __name__ == '__main__':
    main()