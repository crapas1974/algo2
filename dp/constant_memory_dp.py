from constant_memory_dp_data import testcases


def max_subarray_sum_with_constant_memory(array):
    n = len(array)
    # dp[i]의 역할을 하는 변수
    max_now_start_idx = 0
    max_start_idx = 0
    max_end_idx = 0
    max_now = array[0]
    # 지금까지의 최대값을 저장하는 변수
    max_sofar = array[0]
    # 배열을 순회하며 max_now를 갱신
    for i in range(1, n):
        # 현재 항목을 마지막으로 하는 부분 배열의 최대 합을 계산
        if max_now <= 0:
            max_now = array[i]
            max_now_start_idx = i
        else:
            max_now += array[i]
        # 최대값 갱신
        if max_now > max_sofar:
            max_sofar = max_now
            max_start_idx = max_now_start_idx
            max_end_idx = i
#        max_sofar = max(max_sofar, max_now)
    # dp[]의 최대값에 해당하는 max_sofar를 반환
    return max_sofar, max_start_idx, max_end_idx

def find_maxsum_subarray(arr):
    n = len(arr)
    dp = [0] * n
    start_idx = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]
    max_sum_subarray = [(0, 0)]

    for i in range(1, n):
        if dp[i - 1] <= 0:
            dp[i] = arr[i]
            start_idx[i] = i
        else:
            dp[i] = dp[i - 1] + arr[i]
            start_idx[i] = start_idx[i - 1]
        if dp[i] > max_sum:
            max_sum = dp[i]
            max_sum_subarray = [(start_idx[i], i)]
        elif dp[i] == max_sum:
            max_sum_subarray.append((start_idx[i], i))

    return max_sum, max_sum_subarray



def find_maxsum_subarray_td(arr, start = None, end = None):
    if start == None:
        start = 0
    if end == None:
        end = len(arr) - 1
    if start == end:
        return arr[start], [(start, end)]
    mid = (start + end) // 2
    leading_max, leading_max_parts = find_maxsum_subarray_td(arr, start, mid)
    trailing_max, trailing_max_parts = find_maxsum_subarray_td(arr, mid + 1, end)
    forwaring_sum = 0
    backwarding_sum = 0
    
    forwarding_max = float("-inf")
    backwarding_max = float("-inf")
    forwarding_max_indices = []
    backwarding_max_indices = []
    for i in range(mid, start - 1, -1):
        forwaring_sum += arr[i]
        if forwaring_sum > forwarding_max:
            forwarding_max = forwaring_sum
            forwarding_max_indices = [i]
        elif forwaring_sum == forwarding_max:
            forwarding_max_indices.append(i)

    for i in range(mid + 1, end + 1):
        backwarding_sum += arr[i]
        if backwarding_sum > backwarding_max:
            backwarding_max = backwarding_sum
            backwarding_max_indices = [i]
        elif backwarding_sum == backwarding_max:
            backwarding_max_indices.append(i)
    crossing_max = forwarding_max + backwarding_max
    crossing_max_parts = []
    for i in forwarding_max_indices:
        for j in backwarding_max_indices:
            crossing_max_parts.append((i, j))
    sum_dict = {}
    sum_dict[crossing_max] = crossing_max_parts
    if leading_max in sum_dict:
        sum_dict[leading_max] += leading_max_parts
    else:
        sum_dict[leading_max] = leading_max_parts
    if trailing_max in sum_dict:
        sum_dict[trailing_max] += trailing_max_parts
    else:
        sum_dict[trailing_max] = trailing_max_parts
    max_sum = max(crossing_max, leading_max, trailing_max)
    return max_sum, sum_dict[max_sum]
    

def main():
    for i, tc in enumerate(testcases):
        print(f"testcase {i + 1}")
#        start = time.time()
        max_sum, max_sum_start_idx, max_sum_end_idx = max_subarray_sum_with_constant_memory(tc)
#        print("실행 시간 - ", time.time() - start)

        print(f"    최대 부분 합 : {max_sum}")
        print(f"    최대 부분 합을 갖는 부분 배열 중 하나의 시작과 끝 인덱스 : {max_sum_start_idx, max_sum_end_idx}")

        # min_size = float("inf")
        # min_size_subarray = []
        # for start, end in max_sum_indices:
        #     if end - start < min_size:
        #         min_size = end - start
        #         min_size_subarray = [(start, end)]
        #     elif end - start == min_size:
        #         min_size_subarray.append((start, end))
        print()


if __name__ == "__main__":
    main()
