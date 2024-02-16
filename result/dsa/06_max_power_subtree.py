from max_power_subtree_data import get_testcases

def max_power_yura(node, path = '@'):
    if node == None:
        return 0, -float('inf'), []
    tree_sum = node.data    
    if node.left != None:
        l_max, l_max_root_nodes, l_sum = max_power_yura(node.left, path + 'l')
    else:
        l_max, l_max_root_nodes, l_sum = -float('inf'), [], 0
    if node.right != None:
        r_max, r_max_root_nodes, r_sum = max_power_yura(node.right, path + 'r')
    else:
        r_max, r_max_root_nodes, r_sum = -float('inf'), [], 0
    tree_sum += l_sum + r_sum
    c_max = max(l_max, r_max)
    if l_max > r_max:
        c_max_root_nodes = l_max_root_nodes
    elif l_max < r_max:
        c_max_root_nodes = r_max_root_nodes
    else:
        c_max_root_nodes = l_max_root_nodes + r_max_root_nodes

    if tree_sum > c_max:
        current_max = tree_sum
        current_max_root_nodes = [path]
    elif tree_sum < c_max:
        current_max = c_max
        current_max_root_nodes = c_max_root_nodes
    else:
        current_max = tree_sum
        current_max_root_nodes = [path] + c_max_root_nodes

    return current_max, current_max_root_nodes, tree_sum

def main():
    testcases = get_testcases()
    for i, root in enumerate(testcases):
        max_sum, max_power_root, _ = max_power_yura(root)
        print(f"Testcase {i + 1}")
        print(f"    합이 최대인 서브트리에 포함된 노드들의 값의 합 : {max_sum}")
        print(f"    값이 최대가 되는 서브트리의 루트 노드 : {max_power_root}")        
        print()

if __name__ == "__main__":
    main()