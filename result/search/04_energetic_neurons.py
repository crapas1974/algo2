from neurons_v import testcases

def find_maxsum_subarray(arr, start = None, end = None):
    if start == None:
        start = 0
    if end == None:
        end = len(arr) - 1
    if start == end:
        return arr[start], [(start, end)]
    mid = (start + end) // 2
    leading_max, leading_max_parts = find_maxsum_subarray(arr, start, mid)
    trailing_max, trailing_max_parts = find_maxsum_subarray(arr, mid + 1, end)
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
        print(f"Testcase {i + 1}")
        max_sum, max_sum_indices = find_maxsum_subarray(tc)

        print(f"    최대 부분 합 : {max_sum}")
        max_sum_indices.sort()
        print(f"    최대 부분 합을 갖는 부분 배열의 시작과 끝 인덱스의 리스트 : {max_sum_indices}")
        print()

if __name__ == "__main__":
    main()
