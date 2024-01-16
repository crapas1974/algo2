import time
import random

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 수행 시간 - {end - start} 초")
        return result
    return wrapper

@execute_time
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    for i in range(4):
        testcase = [random.randint(1, 100) for _ in range(10 ** (i + 1))]
        print(f"testcase {i + 1} :", end=" ")
        bubble_sort(testcase)

if __name__ == '__main__':
    main()