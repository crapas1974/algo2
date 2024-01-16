def find_solo(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

def find_second_solo(xor_result, n):
    return n ^ xor_result

def make_sample_list(size):
    arr = []
    for i in range((size + 1) // 2):
        random_number = random.randint(1, 100000)
        arr.append(random_number)
        arr.append(random_number)
    random.shuffle(arr)
    removed = arr.pop()
    return arr, removed

def make_sample_list2(size):
    arr = []
    for i in range((size + 1) // 2):
        random_number = random.randint(1, 100000)
        arr.append(random_number)
        arr.append(random_number)
    random.shuffle(arr)
    removed1 = arr.pop()
    removed2 = arr.pop()
    return arr, removed1, removed2

import random
def main():
    n = 999999
    arr, removed = make_sample_list(n)
    solo = find_solo(arr)
    print(f"리스트에서 찾은 외로운 숫자는 {solo}이며, 이는 예상대로 {removed}입니다.")

    n = 999998
    arr, removed1, removed2 = make_sample_list2(n)
    xor_result = find_solo(arr)
    solo = find_second_solo(xor_result, removed1)
    print(f"리스트에서 제거한 숫자는 {removed1}과 {removed2}이며, 이 중 {removed1}을 알고 있을 때 찾은 나머지 숫자는 {solo}입니다.")


if __name__ == '__main__':
    main()