from correct_sort import correct_sort
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
def correct_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    test_10 = [random.randint(1, 10000) for _ in range(10)] 
    test_100 = [random.randint(1, 10000) for _ in range(100)] 
    test_1000 = [random.randint(1, 10000) for _ in range(1000)] 
    test_10000 = [random.randint(1, 10000) for _ in range(10000)]
    correct_sort(test_10)
    correct_sort(test_100)
    correct_sort(test_1000)
    correct_sort(test_10000)


if __name__ == '__main__':
    main()