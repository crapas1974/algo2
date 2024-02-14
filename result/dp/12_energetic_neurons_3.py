from neurons_v import testcases

def max_subarray_sum_with_constant_memory(array):
    n = len(array)
    max_now_start_idx = 0
    max_start_idx = 0
    max_end_idx = 0
    max_now = array[0]
    max_sofar = array[0]
    for i in range(1, n):
        if max_now <= 0:
            max_now = array[i]
            max_now_start_idx = i
        else:
            max_now += array[i]
        if max_now > max_sofar:
            max_sofar = max_now
            max_start_idx = max_now_start_idx
            max_end_idx = i
    return max_sofar, max_start_idx, max_end_idx

def main():
    for i, tc in enumerate(testcases):
        print(f"testcase {i + 1}")
        max_sum, max_sum_start_idx, max_sum_end_idx = max_subarray_sum_with_constant_memory(tc)

        print(f"    최대 부분 합 : {max_sum}")
        print(f"    최대 부분 합을 갖는 부분 배열 중 하나의 시작과 끝 인덱스 : {max_sum_start_idx, max_sum_end_idx}")

        print()


if __name__ == "__main__":
    main()
