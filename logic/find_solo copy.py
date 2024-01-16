def find_solo(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

def find_solo2(arr):
    temp = []
    for i in arr:
        if i in temp:
            temp.remove(i)
        else:
            temp.append(i)
    return temp[0]

def make_sample_list(size):
    arr = []
    for i in range((size + 1) // 2):
        random_number = random.randint(1, 100000)
        arr.append(random_number)
        arr.append(random_number)
    random.shuffle(arr)
    removed = arr.pop()
    return arr, removed
import random
def main():
    n = 999999
    arr, removed = make_sample_list(n)
    solo = find_solo(arr)
    print(f"리스트에서 찾은 외로운 숫자는 {solo}이며, 이는 예상대로 {removed}입니다.")
    solo2 = find_solo2(arr)
    print(solo2)
    # print(solo)
    # solo2 = find_solo2(arr)
    # print(solo2)
if __name__ == '__main__':
    main()