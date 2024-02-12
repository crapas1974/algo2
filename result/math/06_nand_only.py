def is_symbol(char):
    return char not in ['+', "'", '(', ')', '*', '@']

def make_logic_eqstack(expression):
    expression = expression.strip().replace(' ', '')
    expression_with_and = ''

    for i in range(len(expression) - 1):
        expression_with_and += expression[i]
        if expression[i] == "'" or is_symbol(expression[i]):
            if expression[i + 1] == "(" or is_symbol(expression[i + 1]):
                expression_with_and += '*'
        if expression[i] == ')':
            if expression[i + 1] == '(' or is_symbol(expression[i + 1]):
                expression_with_and += '*'
    expression_with_and += expression[-1]
    stack = []
    result = []
    for char in expression_with_and:
        if char == "'":
            result.append(char)
        elif is_symbol(char):
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
    return result

def calculate_nand(op1, op2):
    if op1 and op2:
        return False
    else:
        return True

def convert_not_to_nand(operand):
    result = f"({operand}@{operand})"
    return result    

def convert_and_to_nand(operand1, operand2):
    result = f"({operand1}@{operand2})@({operand1}@{operand2})"
    return result

def convert_or_to_nand(operand1, operand2):
    result = f"({operand1}@{operand1})@({operand2}@{operand2})"
    return result

def calculate(expression, input_tf: dict):
    st = make_logic_eqstack(expression)
    result = []
    for char in st:
        if char not in ['@']:
            result.append(input_tf[char])
        else:
            operand2 = result.pop()
            operand1 = result.pop()
            result.append(calculate_nand(operand1, operand2))
    return result[0]

def converted_to_nand_only(expression):
    st = make_logic_eqstack(expression)
    changed_result = []

    for char in st:
        if char not in ['+', '*', "'"]:
            changed_result.append(char)
        else:
            if char == "'":
                operand1 = changed_result.pop()
                changed_result.append(convert_not_to_nand(operand1))
            else:
                operand2 = changed_result.pop()
                operand1 = changed_result.pop()
                if char == '+':
                    changed_result.append("(" + convert_or_to_nand(operand1, operand2) + ")")
                elif char == '*':
                    changed_result.append("(" + convert_and_to_nand(operand1, operand2) + ")")
    return changed_result[0]

def format_tf_head(str):
    result = ''
    for c in str:
        if c == '0':
            result += "F "
        elif c == '1':
            result += "T "
        else: 
            result += c + " "
    return result

def main():
    testcase = [
        "AB",
        "A(B'+C)",
        "AB'+C",
        "A'",
        "A+B",
        "A'A",
        "A'+A",
        "A'B'",
        "A+B'*C",
        "(AB)(CD)",
        "(A+B)C(D+B)",
        "(A'B')'",
        "(A'+B)''+(CD'(B'+A')')'",
        "(A+B)(C+D)(A+C)(B+D)+(AD)",
    ]
    
    for i in range(len(testcase)):
        print("Testcase", i + 1)
        print(f"    입력 - {testcase[i]}")
        converted_result = converted_to_nand_only(testcase[i])
        print(f"    변환 결과 - {converted_result}")
        variables = []
        for c in testcase[i]:
            if c not in ["'", "+", "(", ")"] and c not in variables:
                variables.append(c)
        tf_case_num = 2 ** len(variables)
        print("    진리표")
        print("        " + " ".join(variables) + " 결과")
        for j in range(tf_case_num):
            j_bin_str = bin(j)[2:]
            j_bin_str = '0' * (len(variables) - len(j_bin_str)) + j_bin_str
            input_tf = {}
            for k in range(len(variables)):
                input_tf[variables[k]] = bool(int(j_bin_str[k]))
            nand_only_result = calculate(converted_result, input_tf)
            row_head = format_tf_head(j_bin_str)
            print(f"        {row_head}{'T' if nand_only_result else 'F'}")
        print()


if __name__ == "__main__":
    main()

