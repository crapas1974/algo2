import time
def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def fossil_num_case_td_wrapper(value_list, target_value):
    return fossil_num_case_td(value_list, target_value)

def fossil_num_case_td(value_list, target_value, memo=None):
    if memo == None:
        memo = {}
    if target_value == 0:
        return 1
    if len(value_list) == 0:
        return 0
    if target_value < 0:
        return 0
    if (len(value_list), target_value) in memo:
        return memo[(len(value_list), target_value)]
    result = 0
    for i in range(target_value // value_list[0] + 1):
        result += fossil_num_case_td(value_list[1:], target_value - value_list[0] * i, memo)
    memo[(len(value_list), target_value)] = result
    return result

@execute_time
def fossil_num_case_bu(value_list, target_value):
    num_case = [0] * (target_value + 1)
    num_case[0] = 1  

    for value in value_list:
        for n in range(value, target_value + 1):
            num_case[n] += num_case[n - value]
    return num_case[target_value]

def main():
    TC1 = (501, [34, 47, 55])
    TC2 = (8, [2, 2])
    TC3 = (99, [3, 4, 5, 6])
    TC4 = (590, [2, 6, 9, 3, 10])
    TC5 = (500, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    TC6 = (1000, [1, 2, 3, 4, 5])    
    testcases = [TC1, TC2, TC3, TC4, TC5, TC6]

    for i, testcase in enumerate(testcases):
        print(f"Testcase {i + 1}")
        print("    하향식 접근 ", end = "")        
        num_case = fossil_num_case_td_wrapper(testcase[1], testcase[0])
        print(f"    생성할 수 있는 반입 목록의 수 : {num_case}")
        print("    상향식 접근 ", end = "")        
        num_case = fossil_num_case_bu(testcase[1], testcase[0])
        print(f"    생성할 수 있는 반입 목록의 수 : {num_case}")
        print()

if __name__ == '__main__':
    main()