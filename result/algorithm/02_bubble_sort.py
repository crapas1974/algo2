import time
import random

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start} 초")
        return result
    return wrapper

@execute_time
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def make_random_list(size: int):
    return [random.randint(1, 100) for _ in range(size)]

def main():
    for i in range(4):
        test_size = 10 ** (i + 1)
        list_for_test = make_random_list(test_size)
        print(f"길이가 {test_size}인 리스트를 버블 정렬하는데 필요한 시간 : ", end="")
        bubble_sort(list_for_test)

if __name__ == '__main__':
    main()