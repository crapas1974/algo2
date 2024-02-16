from max_power_subtree_data import get_testcases

# def show_tree(root):
#     if root == None:
#         return ''
#     if root.left == None and root.right == None:
#         return f"{root.data}"
#     return f"{root.data}({show_tree(root.left)},{show_tree(root.right)})"
def max_power_wrapper(node):
    return max_power(node)[0]

def max_power(node):
    if node == None:
        return 0, -float('inf')
    tree_sum = node.data    
    if node.left != None:
        l_max, l_sum = max_power(node.left)
    else:
        l_max, l_sum = -float('inf'), 0
    if node.right != None:
        r_max, r_sum = max_power(node.right)
    else:
        r_max, r_sum = -float('inf'), 0
    tree_sum += l_sum + r_sum
    return max(tree_sum, l_max, r_max), tree_sum

def main():
    testcases = get_testcases()
    for i, root in enumerate(testcases):
        max_sum_ = max_power_wrapper(root)
        print(f"Testcase {i + 1}")
        #print(f"    트리 : {show_tree(root)}")
        print(f"    합이 최대인 서브트리에 포함된 노드들의 값의 합 : {max_sum_}")
        print()

if __name__ == "__main__":
    main()