def pseudo_sort(arr: list[str]):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


a =['abc', 'xyz', 'def', 'opq', 'jkl']

pseudo_sort(a)
print(a)