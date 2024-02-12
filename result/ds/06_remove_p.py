def infix_to_postfix(expression):
    oper = ['+', '-', '*']
    bracket = ['(', ')']
    stack = []
    result = []

    for char in expression:
        if char == ' ':
            continue
        if char not in oper and char not in bracket:
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return ''.join(result)

def calculate(patterns, expression):
    stack = []
    oper = ['+', '-', '*']
    for char in expression:
        if char == ' ':
            continue
        if char not in oper:
            stack.append(patterns[char])
        elif char == ' ': 
            continue
        else:
            pattern2 = stack.pop()
            pattern1 = stack.pop()
            if char == '+':
                stack.append(pattern1 + pattern2)
            elif char == '-':
                before_remove = pattern1
                while True:
                    pattern1 = pattern1.replace(pattern2, '')
                    if before_remove == pattern1:
                        break
                    before_remove = pattern1
                stack.append(pattern1)
            elif char == '*':
                result = ''
                for i in range(min(len(pattern1), len(pattern2))):
                    result += pattern1[i] + pattern2[i]
                if len(pattern1) > len(pattern2):
                    result += pattern1[len(pattern2)]
                stack.append(result)
    return stack.pop()

import hashlib
def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]

patterns = {
    'A': 'CT',
    'B': 'GC',
    'C': 'ATT',
    'D': 'GCG',
    'E': 'CCG',
}

def main():
    with open("opf_testcases.txt", "r") as f:
        lines = f.readlines()
    start_lines = []
    end_lines = []
    for line in lines:
        if line[:8] == 'Testcase':
            start_lines.append(lines.index(line) + 1)
            if len(start_lines) > 1:
                end_lines.append(lines.index(line) - 1)
    end_lines.append(len(lines))

    for i, start_line in enumerate(start_lines):
        equation = ''
        for line in lines[start_line:end_lines[i] + 1]:
            equation += line.strip()
        pnr_result = infix_to_postfix(equation)
        calculated_result = calculate(patterns, pnr_result)
        print(f"Testcase {i + 1}의 결과: {hash4(pnr_result)}")
        print(f"유전자 조작 결과 : {calculated_result}")
        print()


if __name__ == "__main__":
    main()
