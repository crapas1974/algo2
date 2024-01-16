# solution example for 1-2

def pseudo_sort(arr):
    for i in range(len(arr) - 1):
        # 닥터 J의 아이디어는 가장 큰 원소를 제일 뒤로 보낼 뿐, 모든 원소에 대해서는 정렬을 수행하지 않는다.
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

def correct_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [5, 4, 3, 2, 1]
    arr2 = arr.copy()
    print('input_list : ', arr)
    pseudo_sort(arr)
    print(arr)
    correct_sort(arr2)
    print(arr2)

if __name__ == '__main__':
    main()
