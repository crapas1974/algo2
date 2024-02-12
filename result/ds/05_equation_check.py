def is_valid_expression(expression):
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        if char in bracket_mapping:
            if not stack or stack[-1] != bracket_mapping[char]:
                return False
            stack.pop()
        elif char in bracket_mapping.values():
            stack.append(char)

    return not stack

def count_meaningless_brackets(expression):
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    previous_bracket = False
    previous_continuous_bracket = False
    count = 0

    for char in expression:
        if char in bracket_mapping:
            if not stack or stack[-1] != bracket_mapping[char]:
                return False
            if previous_bracket and not previous_continuous_bracket:
                count += 1
                previous_continuous_bracket = True
            stack.pop()
            previous_bracket = True
        else:
            previous_continuous_bracket = False
            previous_bracket = False
            if char in bracket_mapping.values():
                stack.append(char)

    return count

def main():
    with open("tcs_equation_inspecter.txt", "r") as f:
        equation = ''
        testcase = ''
        while True:
            line = f.readline()
            if not line or line[:8] == 'Testcase':
                if equation != '':
                    inspect_result = is_valid_expression(equation)
                    if inspect_result:
                        print(testcase)

                        print('  유효한 수식입니다.')
                        repeated_bracket_pair = count_meaningless_brackets(equation)
                        print('  의미없이 중첩된 괄호 쌍의 수 :', repeated_bracket_pair)
                        print()
                    else:
                        print(testcase)
                        print('  유효하지 않은 수식입니다.\n')
                if not line:
                    break
                testcase = line.strip()
                equation = ''
            else:
                equation += line.strip()

if __name__ == "__main__":
    main()
