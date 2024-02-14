from neurons_v import testcases

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
    
def main():
    for i, tc in enumerate(testcases):
        print(f"testcase {i + 1}")
        max_sum, max_sum_indices = find_maxsum_subarray(tc)

        print(f"    최대 부분 합 : {max_sum}")

        min_size = float("inf")
        min_size_subarray = []
        for start, end in max_sum_indices:
            if end - start < min_size:
                min_size = end - start
                min_size_subarray = [(start, end)]
            elif end - start == min_size:
                min_size_subarray.append((start, end))
        print(f"    최대 부분 합을 갖는 부분 배열 중 길이가 가장 짧은 배열의 시작과 끝 인덱스의 리스트 : {min_size_subarray}")
        print()

if __name__ == "__main__":
    main()
