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
def fossil_num_case_bf_wrapper(value_list, target_value):
    return fossil_num_case_bf(value_list, target_value)

def fossil_num_case_bf(value_list, target_value):
    # 종료조건 1 : 목표 가치에 정확히 도달한 경우 (성공)
    if target_value == 0:
        return 1
    # 종료조건 2 : 가치는 남았으나, 더 이상 반입할 화석이 종류가 없는 경우 (실패)
    if len(value_list) == 0:
        return 0
    # 종료조건 3 : 목표 가치를 초과한 경우 (실패)
    if target_value < 0:
        return 0
    result = 0
    # 가치 배열의 첫 번째 항목을 0개부터 가치를 초과하지 않는 수 만큼 반입하고,
    # 남은 가치 배열과, 남은 목표 가치를 사용해 재귀호출한다.
    for i in range(target_value // value_list[0] + 1):
        # 성공의 경우 반환되는 1을 더한다.
        result += fossil_num_case_bf(value_list[1:], target_value - value_list[0] * i)
    return result

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
    # 메모의 키로 (value_list의 길이, target_value)의 튜플을 사용한다.
    # 메모에 있는 값이면, 메모를 사용한다.
    if (len(value_list), target_value) in memo:
        return memo[(len(value_list), target_value)]
    result = 0
    for i in range(target_value // value_list[0] + 1):
        result += fossil_num_case_td(value_list[1:], target_value - value_list[0] * i, memo)
    # 메모에 결과를 저장한다.
    memo[(len(value_list), target_value)] = result
    return result

@execute_time
def fossil_num_case_bu(value_list, target_value):
    # 각 가치에 대한 경우의 수를 저장하는 배열
    # 0으로 초기화하고, 
    # num_case[0]만 1로 초기화한다. 아무것도 반입하지 않는 한 가지 경우가 존재한다.
    num_case = [0] * (target_value + 1)
    num_case[0] = 1  

    # 모든 종류의 화석에 대해서 반복
    for value in value_list:
        # 현재 화석의 가치부터 목표 가치까지 반복
        for n in range(value, target_value + 1):
            # 현재 가치 n을 만들 수 있는 방법의 개수를 이전 가치의 경우를 수를 더해 구한다.
            num_case[n] += num_case[n - value]
    return num_case[target_value]

def fossil_num_case_and_case(value_list, target_value):
    # 각 가치에 대한 모든 경우의 목록을 저장하는 배열
    # 빈 리스트로 초기화하고,
    # num_case[0]만 1로 초기화한다. 아무것도 반입하지 않는 한 가지 경우가 존재한다.
    cases = [[] for _ in range(target_value + 1)]
    cases[0] = [[]]  
    # 모든 종류의 화석에 대해서 반복
    for value in value_list:
        # 현재 화석의 가치부터 목표 가치까지 반복
        for n in range(value, target_value + 1):
            # n - value를 만들 수 있는 모든 경우에 대해서,
            # 현재 화석의 가치를 추가한 새로운 경우를 생성한다.
            # (n - value)가 가능하지 않다면, 빈 리스트가 반환되므로
            # 루프 안으로 들어가지 않는다.
            for prev_case in cases[n - value]:
                # 현재 화석의 가치를 추가한 새로운 경우  
                new_case = prev_case + [value]
                # 새롭게 생성된 경우를 목록 배열에 추가
                cases[n].append(new_case)
    return len(cases[target_value]), cases[target_value]

def main():
    testcases = []
    # testcases.append((501, [34, 47, 55]))
    # testcases.append((8, [2, 2]))
    # testcases.append((99, [3, 4, 5, 6]))
    # testcases.append((590, [2, 6, 9, 3, 10]))
    # testcases.append((500, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # testcases.append((1000, [1, 2, 3, 4, 5]))
    testcases.append((501, [34, 47, 55]))
    testcases.append((5, [1, 2, 3]))
    testcases.append((25, [3, 4, 5, 6]))

    print("모든 경우의 수와 경우의 수 목록")
    for i, testcase in enumerate(testcases):
        num_case, cases = fossil_num_case_and_case(testcase[1], testcase[0])
        print(f"  TC {i + 1}에서 생성할 수 있는 반입 목록의 수 : {num_case}")

        print(f"  TC {i + 1}에서 생성할 수 있는 반입 목록 : {cases}")

    # print("상향식 다이나믹 프로그래밍")
    # for i, testcase in enumerate(testcases):
    #     print(f"  TC {i + 1}에서 생성할 수 있는 반입 목록의 경우의 수 : {fossil_num_case_bu(testcase[1], testcase[0])}")


if __name__ == '__main__':
    main()