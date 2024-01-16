import time, random

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def max_subarray_sum_bu(array):
    # dp 배열 초기화
    n = len(array)
    dp = [0] * n
    dp[0] = array[0]


    # 배열을 순회하며 dp 값을 계산
    for i in range(1, n):
        # 현재 항목을 마지막으로 하는 부분 배열의 최대 합을 계산
        if dp[i - 1] <= 0:
            dp[i] = array[i]
        else:
            dp[i] = dp[i - 1] + array[i]
    # dp[]의 최대값을 반환
    return max(dp)

@execute_time
def max_subarray_sum_bf(array):
    max_sum = array[0]  # 가장 큰 합을 저장하는 변수, 배열의 첫 번째 요소로 초기화
    n = len(array)
    for start in range(n):  # 모든 시작점에 대해
        for end in range(start, n):  # 시작점부터 배열의 끝까지의 모든 끝점에 대해
            current_sum = sum(array[start:end+1])  # 현재 부분 수열의 합을 계산
            max_sum = max(max_sum, current_sum)  # 최대값을 업데이트
    return max_sum

@execute_time
def max_subarray_sum_td_wrapper(array):
    return max_subarray_sum_td(array, 0, len(array) - 1, {})


def max_subarray_sum_td(array, i, j, memo=None):
    if memo == None:
        memo = {}
    if i > j:  # i == j일 때까지 동작 (원소가 하나인 부분 배열)
        return float('-inf')  # 음의 무한대 반환
    if (i, j) in memo:
        return memo[(i, j)]
    # 현재 부분 배열의 합을 계산
    current_sum = sum(array[i: j + 1])

    # 다음 세 가지 경우를 고려하여 최대 합을 찾음:
    # 1. 현재 부분 배열을 포함하는 경우
    # 2. 현재 부분 배열의 첫 번째를 제외하는 경우
    # 3. 현재 부분 배열의 마지막을 제외하는 경우
    include_current = current_sum
    exclude_first = max_subarray_sum_td(array, i + 1, j, memo)
    exclude_last = max_subarray_sum_td(array, i, j - 1, memo)


    # 세 경우 중 최대값 반환
    memo[(i, j)] = max(include_current, exclude_first, exclude_last)
    return memo[(i, j)]

def max_subarray_sum_and_subarray(array):
    # dp 배열 초기화
    max_start_index = [0]
    max_end_index = [0]
    max_subarray_sum = array[0]
    dp_start_index = 0
    n = len(array)
    dp = [0] * n
    dp[0] = array[0]

    # 배열을 순회하며 dp 값을 계산
    for i in range(1, n):
        # 현재 항목을 마지막으로 하는 부분 배열의 최대 합을 계산
        if dp[i - 1] <= 0:
            dp[i] = array[i]
            dp_start_index = i
        else:
            dp[i] = dp[i - 1] + array[i]
        if dp[i] == max_subarray_sum:	
            max_start_index.append(dp_start_index)
            max_end_index.append(i)
        elif dp[i] > max_subarray_sum:
            max_subarray_sum = dp[i]
            max_start_index = [dp_start_index]
            max_end_index = [i]
    
    # dp[]의 최대값을 반환
    array_max_subarray_sum = None
    if max_subarray_sum > 0:
        array_max_subarray_sum = []
        for i in range(len(max_start_index)):
            array_max_subarray_sum.append(array[max_start_index[i]: max_end_index[i] + 1])
    return max_subarray_sum, array_max_subarray_sum

def max_subarray_sum_bonus(array):
    n = len(array)
    # dp[i]의 역할을 하는 변수
    max_now = array[0]
    # 지금까지의 최대값을 저장하는 변수
    max_sofar = array[0]
    # 배열을 순회하며 max_now를 갱신
    for i in range(1, n):
        # 현재 항목을 마지막으로 하는 부분 배열의 최대 합을 계산
        if max_now <= 0:
            max_now = array[i]
        else:
            max_now += array[i]
        # 최대값 갱신
        max_sofar = max(max_sofar, max_now)
    # dp[]의 최대값에 해당하는 max_sofar를 반환
    return max_sofar

def main():
    TC1 = [1, 2, 3, 4, 5]
    TC2 = [-2, -3, 1, -6, -3]
    TC3 = [0, 0, 0, 0, 0]
    TC4 = [-1, -2, -3, -4, -5]
    TC5 = [7, -9, -2, -6, 4, 6, 3, 7, 6, 7, -6, -1]
    TC6 = [-2, 2, 0, 0, 1, 1, -4, 7, 8, 4, 5, 1, 0, -3, -1, -10, -8, -4, -8, -2, 1, -8, -10, -6, -6, -4, 0, -1, -2, -10, 4, -5, -4, -8, 4, 3, -3, 8, -10, -9, 8, -5, 3, -9, -8, 0, 9, -4, 2, 7, -4, 8, -10, 0, 8, -10, 4, -3, 5, 6, -9, 7, 6, 8, 5, 9, 8, 0, 1, 4, 6, 1, -4, -2, -8, 7, 5, 7, -1, 4, -2, -7, -6, -10, -9, -8, -10, -3, 9, 4, 6, 4, 8, 3, 4, 8, -2, -3, -3, 10, 0, -4, 6, -2, 4, -10, -5, -7, 2, -8, -8, -1, -1, 3, -5, 2, 8, -8, -6, -7, -3, 9, 5, 6, -5, 2, -2, -10, -8, 10, -4, 0, 5, -6, 7, 10, -7, 6, 0, 3, 2, -2, 10, -8, 5, -10, 2, 0, 8, 2, 7, 4, -3, -6, 2, -8, -6, -10, -10, 4, -6, 2, -3, 5, 7, 2, -7, -9, 1, -3, -10, 7, 8, -3, -6, 7, 2, 5, -4, 0, 8, 8, 10, -9, 10, -7, -7, -4, 0, 0, -9, -10, -6, 5, -7, -1, -1, -8, 6, -2, 0, -4, 3, -2, 7, 3, 2, 4, 9, -10, 7, 9, -8, -7, -4, 3, 10, 5, -5, -9, 4, 7, 4, -8, -3, 0, 2, 6, -9, -3, -7, -5, -3, 5, -5, -2, 8, 2, 6, -7, -8, -9, -3, -3, 4, -5, -1, -5, -7, -4, -10, -9, -4, 5, -1, -7, -8, -8, -3, -9, -6, -1, -7, -8, -2, -10, 9, -4, -5, -10, -7, -7, 6, -8, 8, 10, -7, 0, 6, 6, -3, 7, -3, 4, 6, -2, -9, 4, 7, 0, -3, -2, 3, -9, 6, 2, 0, -5, -9, -2, -6, 3, -8, 4, 1, 2, -2, -5, -6, 7, -7, -7, 7, 5, 5, 8, 8, 4, -9, 3, 6, 6, 9, 2, -8, 1, 9, -1, 3, -7, 0, -5, -1, -10, -4, 0, -8, 4, 8, -7, -10, -6, 3, 4, 6, -8, -4, -4, -6, -7, -1, 6, -6, -4, -8, 2, -5, 0, 5, 1, 8, -1, -3, -4, -8, 9, 8, -4, -6, 4, 10, 7, 1, -5, 9, 2, 7, -3, -2, -3, -10, -3, 4, -5, -6, -10, 2, 6, 2, 5, -4, 3, -9, -6, -6, 7, -8, -9, 1, -10, -2, -6, -8, -3, -8, -3, -8, 7, -9, -8, -6, -10, -4, -6, 9, 0, 3, -10, 3, -7, 1, -6, -2, -7, 9, 7, 4, -3, -10, -10, 0, 0, -1, 0, 0, 3, -8, 1, 9, 1, -3, 2, 6, -9, -4, 6, -9, 8, -2, 3, 4, 2, -10, 0, 2, 5, 10, -2, -4, -6, -6, 3, -9, 3, 9, 9, 6, -1, 10, -6, -6, -9, 1, 2, 4, 1, -5, 3, 0, -9, 10, -3, 7, 6, 8, -6, -6, -2, -8, 7, -5, 8, -2, -6, -8, 7, 5, 1, -2, 9, 9, -7, 4, -10, -5, 1, -10, -2, -8, -6, -9, -8, -10, 6, -8, 7, -2, -4, -9, -4, -10, -10, -3, 3, -2, -10, 8, -8, 9, -3, -8, 8, -2, 3, -10, 1, 4, 1, -1, 5, -7, 4, 7, 1, -8, 9, -10, -8, 4, -9, 4, 2, 3, -9, 9, -3, -5, 7, -4, -8, -10, -7, -4, -8, 5, 4, 2, 0, 8, -2, -6, -2, 2, -5, -7, 6, -8, -5, 0, 10, -10, 5, 3, -4, 3, 8, -8, -7, -9, 1, -1, -10, -6, -6, 4, 10, 0, 7, 5, 10, 6, 5, -6, -9, -5, 5, -7, -10, -5, -1, -10, 6, 10, -7, -8, -6, 2, -7, 3, -1, -5, 8, -5, 8, -6, 10, 8, 5, -10, 0, -8, 8, -8, 2, -7, 5, 9, -9, -4, 4, 1, -5, 5, 6, -7, 10, 10, -1, 2, -2, -5, 2, 9, 8, -7, -6, -6, 2, -10, 9, 9, 1, 3, 8, 1, -3, -1, 5, -7, -6, 7, -4, 5, 4, 9, 8, 10, -4, -6, -10, -4, 5, 6, 7, 10, -9, 10, 2, -8, -10, 3, -9, -9, -10, 4, -4, 9, -9, -2, -4, 1, -6, 5, 10, -2, 8, -1, -9, 3, -4, 9, -5, 7, 3, 5, 9, -2, -2, -10, -4, 2, -3, 1, -6, -4, 7, -1, 0, -3, 1, -8, -7, 0, 3, -2, -9, -3, 8, 8, 0, -3, 8, -5, 7, -5, 5, 2, 8, 9, -4, -9, 9, -1, -9, 0, -9, 10, -1, 0, -2, -1, 0, 8, 7, -4, 10, -4, 3, 10, 4, 10, -6, 7, -2, -9, -4, 4, 9, 8, 0, -6, 5, 7, -3, -6, 8, -10, -6, 3, 5, 0, -6, 8, 8, -4, -9, 6, 7, -5, 5, 10, 10, -3, 4, -5, 3, 2, 6, 10, -7, -4, -5, 6, -10, 6, -6, -3, -6, -8, 6, -4, -1, 5, -1, -10, -8, -6, 5, -7, -1, -8, 6, 3, 8, -3, -8, 10, 1, 6, -7, 8, -6, -2, 0, -10, -10, -7, -2, -2, -10, -6, -5, 5, -10, -7, 8, -10, 9, -1, -4, -7, 1, 1, 1, 5, 9, -10, 6, -2, 5, 1, -3, -5, 9, -7, 5, 9, 10, 3, -7, -3, 7, -7, -6, 0, 5, -4, -10, 4, -5, 9, -8, -8, 5, -8, -4, 0, 9, 10, -5, -5, 10, 6, 5, -8, 4, -5, -10, -3, 6, -5, -6, -4, -2, -1, 8, -3, 10, -6, 8, 8, -9, 1, -8, -5, -6, 10, -7, -2, -5, -8, 7, -10, -7, 2, 7, 6, 0, -10, 4, 3, 9, 6, 3, -9, 10, -10, -5, 10, 3, 3, 10, 4, 9, 3, -3, 7, 6, -10, 1, -9, 3, -7, -6, -4, 7, -5, 9, 5, 4, -10, 9, -1, -3, 1, -10, -4, -7, -8, -1, 10, 2, 9, 8, 9, 9]
    TC7 = [-5, 1, 5, -6, 5, 3, 6, -2, 3, -10, -4, -7, -6, 1, -1, 0, 4, 7, 9, -7, -7, 10, 5, -9, -7, -5, 1, 6, -1, 6, -7, -7, 0, -8, -4, 3, 9, 4, 2, 3, -3, -10, -6, -4, -2, -6, -10, -8, -6, 3]
    testcases = [TC1, TC2, TC3, TC4, TC5, TC6, TC7]

    for i, testcase in enumerate(testcases):
    #    print("완전 탐색법")
    #    print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_bf(testcase)}")
    #    print("하향식 다이나믹 프로그래밍")
    #    print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_td_wrapper(testcase)}")
#        print("상향식 다이나믹 프로그래밍")
#        print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_bu(testcase)}")
        sum, subarray = max_subarray_sum_and_subarray(testcase)

        print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {sum}")
        print(f"TC {i + 1}에서 가장 큰 부분 배열 : {subarray}")

        print(f"TC {i + 1}에서 공간 복잡도가 O(1)인 구현의 결과 - 가장 큰 부분 배열의 합 : {max_subarray_sum_bonus(testcase)}")        

        print()
    
    # print("길이 2000인 배열에서의 결과")

    # arr_length = 2000
    # test = [random.randint(-10, 10) for _ in range(arr_length)]
    # print("완전 탐색법")
    # print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_bf(test)}")
    # print("상향식 다이나믹 프로그래밍")
    # print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_bu(test)}")

    # print()
    # print("길이 10000인 배열에서의 결과")

    # arr_length = 10000
    # test = [random.randint(-10, 10) for _ in range(arr_length)]
    # print("상향식 다이나믹 프로그래밍")
    # print(f"TC {i + 1}에서 가장 큰 부분 배열의 합 : {max_subarray_sum_bu(test)}")

if __name__ == '__main__':
    main()