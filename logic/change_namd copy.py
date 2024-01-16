# AB -> A and B -> A*B
# A( -> A and ( -> A*(
#   symbol + (symbol, opening) -> insert *
# 'B -> A' AND B -> A'*B
# '( -> ' AND ( -> '*(
#   ' + (symbol, opening) -> insert *
# )A -> ) and A -> )*A
# )( -> ) and ( -> )*(
#   ) + (symbol, opening) -> insert *

# A+B -> AB+
# A'+B' -> A'B'+
# A+B' -> AB'+
# A'+B -> A'B+
# (A+B)'+C -> AB+'C+
# (A+B)+C' -> AB+C'+

def is_symbol(char):
    return char not in ['+', "'", '(', ')', '*', '@']

def make_logic_eqstack(expression):
    expression = expression.strip().replace(' ', '')
    expression_with_and = ''

    for i in range(len(expression) - 1):
        #print(f"==>", expression[i], expression[i + 1])
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

            
#    print(expression_with_and)
# A + (B + C) -> A + B + C
# (A + B) + C -> A + B + C
# 괄호 오프닝이 있어. 그 안의 연산을 검사해. 괄호 앞에 연산이 있으면 괄호 안에 연산이 같은지 확인해. 같으면 괄호를 없애는거야.


    



# def make_logic_stack(expression):
#     b_operator = ['+']
#     u_operator = ["'"]
#     bracket = ['(', ')']
#     stack = []
    
#     for i in range(len(expression)):
#         if expression[i] == ' ':
#             continue
#         if expression[i] not in b_operator and expression[i] not in u_operator and expression[i] not in bracket:
#             stack.append(expression[i])
#         elif expression[i] in b_operator:
#             stack.append(expression[i])
#         elif expression[i] in u_operator:
#             stack.append(expression[i])
#         elif expression[i] == '(':
#             stack.append(expression[i])
#         elif expression[i] == ')':
#             while stack and stack[-1] != '(':
#                 stack.pop()
#             stack.pop()
#     return stack


# # A+(B*C) -> ABC*+
# # A+(B*C)' -> ABC*'+
# def infix_to_postfix(expression):
#     oper = ["+", "*", "'"]
#     bracket = ['(', ')']
#     insert_and = ''
#     for i in range(len(expression) - 1):
#         if expression[i] == ' ':
#             continue
#         if expression[i] == '+':
#             insert_and += '+'
#             continue

#         elif expression[i + 1] 
#     for char in expression:
#         if char == ' ':
#             continue
#         if char 

# def change_logic_eqstack(expression):
#     stack = []
#     for char in expression:
#         if char == ' ':
#             continue
#         if char not in ['+', "'", '(', ')']:
#             stack.append(char)
#         else:
#             stack.append(char)
#     return stack

# def simplifying_stack(stack):
#     result == []

def simplified_stack(expression):    
    if '(' in expression:
        eq_in_bracket = 'null'
        in_bracket = False
        start = -1
        end = -1
        depth = 0

        for i in range(len(expression)):
            if expression[i] == '(':
                if in_bracket == False:
                    start = i
                    in_bracket = True
#                    print("start : ", start)
                depth += 1
                
            elif expression[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i
                    eq_in_bracket = expression[start + 1: end]
                    in_bracket = False
#                    print("end : ", end)
                    print("IN->", eq_in_bracket)
#                    break
        #    print(expression[i], depth)
        
#        print(start, end)
#        in_bracket = expression[start + 1:end]
#        print(in_bracket)
    

        print("No bracket")
    
# def analysis_eq(expression):
#     expression = expression.strip().replace(' ', '')
#     expression_with_and = ''

#     for i in range(len(expression) - 1):
#         #print(f"==>", expression[i], expression[i + 1])
#         expression_with_and += expression[i]
#         if expression[i] == "'" or is_symbol(expression[i]):
#             if expression[i + 1] == "(" or is_symbol(expression[i + 1]):
#                 expression_with_and += '*'
#         if expression[i] == ')':
#             if expression[i + 1] == '(' or is_symbol(expression[i + 1]):
#                 expression_with_and += '*'
#     expression_with_and += expression[-1]
#     expression = expression_with_and
#     depth = 0
#     bracket_stack = []
#     for c in expression:
#         if c == '(':
#             depth += 1

def calculate_nand(op1, op2):
    if op1 and op2:
        return False
    else:
        return True

def change_not_to_nand(operand):
    #print("change not to nand", operand)
    result = f"({operand}@{operand})"
    #print("result", result)
    return result    

def change_and_to_nand(operand1, operand2):
    #print("change and to nand", operand1, operand2)
    result = f"({operand1}@{operand2})@({operand1}@{operand2})"
    #print("result", result)
    return result

def change_or_to_nand(operand1, operand2):
    #print("change or to nand", operand1, operand2)
    result = f"({operand1}@{operand1})@({operand2}@{operand2})"
    #print("result", result)
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

def calculate_temp(expression, input_tf: dict):
    st = make_logic_eqstack(expression)
    result = []
    for char in st:
        if char not in ['+', '*', "'"]:
            result.append(input_tf[char])
        else:
            if char == "'":
                operand1 = result.pop()
                result.append(not operand1)
            else:
                operand2 = result.pop()
                operand1 = result.pop()
                if char == '+':
                    result.append(operand1 or operand2)
                elif char == '*':
                    result.append(operand1 and operand2)
    return result[0]

def change_to_nand(expression):
    st = make_logic_eqstack(expression)
    #st = st[::-1]
    changed_result = []

    #print(st)
    for char in st:
        if char not in ['+', '*', "'"]:
            changed_result.append(char)
        else:
            if char == "'":
                operand1 = changed_result.pop()
                changed_result.append(change_not_to_nand(operand1))
            else:
                operand2 = changed_result.pop()
                operand1 = changed_result.pop()
                if char == '+':
                    changed_result.append("(" + change_or_to_nand(operand1, operand2) + ")")
                elif char == '*':
                    changed_result.append("(" + change_and_to_nand(operand1, operand2) + ")")
    return changed_result[0]
    # while len(st) > 1:
    #     print("cur stack", st)
    #     operand1 = st.pop()
    #     next = st.pop()
    #     if next == "'":
    #         st.append(change_not_to_nand(operand1))
    #     else:
    #         operand2 = next
    #         operation = st.pop()
    #         print(f"op1 : {operand1}, op2 : {operand2}, op : {operation}")
    #         if operation == '+':
    #             st.append(change_or_to_nand(operand1, operand2))
    #         elif operation == '*':
    #             st.append(change_and_to_nand(operand1, operand2))
    #         elif operation == "'":
    #             st.append(change_not_to_nand(operand2))
    #             st.append(operand1)
    # return st.pop()

            
    # operand1 = st.pop()
    # operand2 = st.pop()
    # operation = st.pop()

    # expression = expression.strip().replace(' ', '')

def format_tf_head(str):
    #print(str)
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
        "A'",
        "AB",
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




        # "AB",       # AB*
        # "A'B'",     # A'B'*
        # "(AB)(CD)", # AB*CD** => ABCD*
        # "(A+B)C(D+E)",       # AB+C*DE+* => AB+CDE+*
        # "(A'B')'",          # A'B'*'
        # "(A'+B)''+(CD'(E'+F')')'", # A'B+''CD'*E'F'+'*'+ => A'B'+''CD'E'F'+'*'+
        # "(A+B)(C+D)(E+F)(G+H)+(IH)", #(A+B)*(C+D)*(E+F)*(G+H)+(I*H)", # AB+CD+*EF+*GH+*IH*+ -> AB+CD+EF+GH*IH*+
        # "(A+B)(C+D)(E+F)",
        # #   ['*', (
        # #       ['*', (
        # #           ['+', ('A', 'B')], 
        # #           ['+', ('C', 'D')]
        # #       )], 
        # #       ['+', ('E', 'F')]
        # #   )]
        # #   
        
        # #  

        # "A'A",          # A'A*
        # "(AB(CD(EF)))", # AB*CD*EF***
        # "AB(C+D)EF"
    
    for i in range(len(testcase)):
        print("testcase", i + 1)
        print(f"    입력 - {testcase[i]}")
        changed_result = change_to_nand(testcase[i])
        print(f"    변환 결과 - {changed_result}")
        variables = []
        for c in testcase[i]:
            if c not in ["'", "+", "(", ")"] and c not in variables:
                variables.append(c)
        tf_case_num = 2 ** len(variables)
        print("    진리표")
        print("        " + " ".join(variables) + " 결과")
        for j in range(tf_case_num):
            # change j to binary (string)
            j_bin_str = bin(j)[2:]
            j_bin_str = '0' * (len(variables) - len(j_bin_str)) + j_bin_str
            #print(tf_case_num, j, j_bin_str)
            input_tf = {}
            for k in range(len(variables)):
                input_tf[variables[k]] = bool(int(j_bin_str[k]))
            #print(input_tf)
            nand_only_result = calculate(changed_result, input_tf)
#            mixed_result = calculate_temp(testcase[i], input_tf)
            #print("j_bin_str", j_bin_str)
            #print("nand_only_result", nand_only_result)
            row_head = format_tf_head(j_bin_str)
            print(f"        {row_head}{'T' if nand_only_result else 'F'}")
#            if nand_only_result != mixed_result:
#                print(f"Error: {nand_only_result} != {mixed_result}")
#                exit(-1)
        # st = make_logic_eqstack(testcase[i])
        # print(st)
        # print(f"---\n{testcase[i]}")
        # simplified_stack(testcase[i])
    # test = 'A+B'
    # print(make_logic_stack(test))
    # test = "'A"
    # print(make_logic_stack(test))
    # test = "A'"
    # print(make_logic_stack(test))
    
    # logic_eq = "A + B * (C + D)"
    # print(change_logic_eqstack(logic_eq))
        print()


if __name__ == "__main__":
    main()

