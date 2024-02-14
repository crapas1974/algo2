def fossil_num_case_and_case(value_list, target_value):
    cases = [[] for _ in range(target_value + 1)]
    cases[0] = [[]]  
    for value in value_list:
        for n in range(value, target_value + 1):
            for prev_case in cases[n - value]:
                new_case = prev_case + [value]
                cases[n].append(new_case)
    return len(cases[target_value]), cases[target_value]

def main():
    TC1 = (501, [34, 47, 55])
    TC2 = (4, [1, 2])
    TC3 = (5, [1, 2, 3])
    TC4 = (25, [3, 4, 5, 6])
    testcases = [TC1, TC2, TC3, TC4]

    print("모든 경우의 수와 경우의 수 목록")
    for i, testcase in enumerate(testcases):
        num_case, cases = fossil_num_case_and_case(testcase[1], testcase[0])
        print(f"    TC {i + 1}에서 생성할 수 있는 반입 목록의 수 : {num_case}")
        print(f"    TC {i + 1}에서 생성할 수 있는 반입 목록 : {sorted(cases)}")


if __name__ == '__main__':
    main()