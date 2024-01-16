import random

def make_example(length, max_depth):
    brackets = ''
    stack = []
    bracket_mapping = {'(': ')', '[': ']', '{': '}'}
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    while True:
        if len(stack) == max_depth:
            is_increase = False
        elif len(stack) == 0:
            is_increase = True
        else:
            is_increase = random.randint(0, 1)
        if not is_increase:
            brackets += bracket_mapping[stack[-1]]
            stack.pop()
        else:
            added_bracket = '('
#            added_bracket = random.choice(['(', '[', '{'])
            brackets += added_bracket
            stack.append(added_bracket)
        if len(stack) == 0 and len(brackets) > length:
            break
#    print(brackets)
    equations = ''
    at = 0
    current = 0
    while True:
        next = random.randint(1, 5)
#        print(at, len(brackets), current, next)
        if next == 5 and at == len(brackets) and current != 2:
            break

        if not is_valid(current, next):
            continue
        if current == 0:
            if next == 2 or next == 4:
                continue
        if at == len(brackets):
            if next == 3 or next == 4:
                continue

        if next == 3 and brackets[at] not in opening:
            continue
        if next == 4 and brackets[at] not in closing:
            continue
        
        if next == 1:
            equations += chr(random.randint(0, 4) + 65)
        elif next == 2:
            equations += random.choice(['+', '-', '*'])
        elif at == len(brackets):
            if next == 5:
                break
        elif next == 3:
            equations += brackets[at]
            at += 1
        elif next == 4:
            if equations[-2] in opening and bracket_mapping[equations[-2]] == brackets[at]:
                continue
            equations += brackets[at]
            at += 1
        current = next
#        if at == len(brackets) and next == 5:
#            break
#        print(equations)
    return equations

def is_valid(cur, next):
    if cur == 0:    # init
        return next == 1 or next == 3
    elif cur == 1:  # number
        return next == 2 or next == 4
    elif cur == 2:  # sign
        return next == 1 or next == 3
    elif cur == 3:  # opening
        return next == 1 or next == 3
    elif cur == 4:  # closing
        return next == 2 or next == 4
if __name__ == '__main__':
    tcs = [
        (1, 1),
        (5, 3),
        (10, 5),
        (50, 10),
        (50, 1),
        (100, 10),
        (200, 10),
        (500, 20),
        (500, 20),
        (500, 30),
        (500, 1),
        (500, 1),
        (1000, 10),
        (1000, 20),
        (1000, 30),
        (1000, 40),
        (10000, 10),
        (10000, 20)
    ]
 
    for i, tc in enumerate(tcs):
        result = make_example(*tc)
        print("testcase", i + 3)
        at = 0
        while True:
            print(result[at: at + 80])
            at += 80
            if at >= len(result):
                break


    # result = make_example(10000, 5)
    # print(len(result), result)

# init : 0
# 1 : 숫자
# 2 : 부호
# 3 : 오프닝
# 4 : 클로징

# 처음에는 숫자 또는 오프닝이 온다.
# 부호 다음에는 숫자 또는 오프닝이 온다.
# 부호 다음에는 부호와 클로징이 오지 않는다.
# 숫자 다음에는 클로징 또는 부호가 온다.
# 숫자 다음에는 숫자와 오프닝이 오지 않는다.
# 오프닝 다음에는 숫자 또는 오프닝이 온다.
# 오프닝 다음에는 부호와 클로징이 오지 않는다.
# 클로징 다음에는 부호 또는 클로징이 온다.
# 클로징 다음에는 숫자와 오프닝이 오지 않는다.
