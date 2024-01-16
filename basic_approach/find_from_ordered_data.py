def find_index(arr, k, start, end):
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return find_index(arr, k, start, mid - 1)
    else:
        return find_index(arr, k, mid + 1, end)

def line_into_int_or_str(line):
    line = line.strip()
    if line.isdigit():
        return int(line)
    else:
        return line

def main():
    testcases = []
    with open("sorted_list.txt", "r") as f:
        lines = f.readlines()
    
    start_lines = []
    end_lines = []
    for i in range(len(lines)):
        if lines[i][:8] == "testcase":
            start_lines.append(i)
            if i != 0:
                end_lines.append(i - 1)
    end_lines.append(len(lines) - 1)
    tc_num = 0
    for i in range(len(start_lines)):
        tc_num += 1
        start = start_lines[i]
        end = end_lines[i]
        k = line_into_int_or_str(lines[start + 1])
        arr = []
        for j in range(start + 2, end + 1):
            arr.append(line_into_int_or_str(lines[j]))
        result = find_index(arr, k, 0, len(arr) - 1)
        print(f"testcase {tc_num} result : {result}")
    
    for i, (tc, k, size) in enumerate(testcases):
        print(f"testcase {i + 1}: {find_index(tc, k, 0, size - 1)}")


if __name__ == "__main__":
    main()