from find_complexity_tc import testcases

# 재귀 호출을 사용해서 1에서 n까지의 모든 정수의 합을 구하는 함수이다.
# 시간 복잡도는 O(n)이다.
def func1(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return func1(n - 1) + n

# 재귀 호출을 사용하지 않고 arr 리스트의 최대값을 반환한다.
# 시간 복잡도는 O(n)이다.
def func2(arr, size):
    result = 0
    for i in range(size):
        if arr[i] > result:
            result = arr[i]
    return result

# 재귀 호출을 사용해 arr 리스트의 최대값을 반환한다.
# 시간 복잡도는 O(log n)이다.
def func3(arr, start, end):    
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    leading_max = func3(arr, start, mid)
    trailing_max = func3(arr, mid + 1, end)
    if leading_max > trailing_max:
        return leading_max
    else:
        return trailing_max

# 재귀 호출을 사용해 arr 리스트의 최대값을 반환한다.
# 시간 복잡도는 O(log n)이다.
def func4(arr, start, end):    
    if start == end:
        return arr[start]
    if start + 1 == end:
        return arr[start] if arr[start] > arr[end] else arr[end]
    mid = (start + end) // 2
    leading_max = func4(arr, start, mid)
    trailing_max = func4(arr, mid + 1, end)
    if leading_max > trailing_max:
        return leading_max
    else:
        return trailing_max

# 재귀 호출을 사용하지 않고 오름차순으로 정렬된 arr 리스트에서 k의 값의 인덱스를 반환한다.    
# k가 리스트에 없는 경우 -1을 반환한다.
# 시간 복잡도는 O(n)이다.
def func5(arr, size, k):    
    for i in range(size):
        if arr[i] > k:
            return -1
        if arr[i] == k:
            return i
    return -1    

# 재귀 호출을 사용해 오름차순으로 정렬된 arr 리스트에서 k의 값의 인덱스를 반환한다.    
# k가 리스트에 없는 경우 -1을 반환한다.
# 시간 복잡도는 O(log n)이다.
def func6(arr, start, end, k):
    if start == end:
        if arr[start] == k:
            return start
        else:
            return -1
    mid = (start + end) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return func6(arr, start, mid, k)
    else:
        return func6(arr, mid + 1, end, k)

    
def main():

    print(f"func1\n    func(512)의 결과 : {func1(512)}\n")
    arr1 = testcases[0]
    arr2 = testcases[1]
    size1 = len(arr1)
    size2 = len(arr2)
    print("func2")
    print(f"    첫 번째 리스트에서의 결과 : {func2(arr1, size1)}")
    print(f"    두 번째 리스트에서의 결과 : {func2(arr2, size2)}\n")
    print("func3")
    print(f"    첫 번째 리스트에서의 결과 : {func3(arr1, 0, size1 - 1)}")
    print(f"    두 번째 리스트에서의 결과 : {func3(arr2, 0, size2 - 1)}\n")
    print("func4")
    print(f"    첫 번째 리스트에서의 결과 : {func4(arr1, 0, size1 - 1)}")
    print(f"    두 번째 리스트에서의 결과 : {func4(arr2, 0, size2 - 1)}\n")
    arr1.sort()
    arr2.sort()
    print("func5")
    print(f"    첫 번째 리스트에서의 결과 : {func5(arr1, size1, 5000)}")
    print(f"    두 번째 리스트에서의 결과 : {func5(arr2, size2, 5000)}\n")
    print("func6")
    print(f"    첫 번째 리스트에서의 결과 : {func6(arr1, 0, size1 - 1, 5000)}")
    print(f"    두 번째 리스트에서의 결과 : {func6(arr2, 0, size2 - 1, 5000)}\n")

if __name__ == '__main__':
    main()