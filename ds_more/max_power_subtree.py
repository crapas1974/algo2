from max_power_subtree_data import get_testcases

def max_power_yura(node, path = '@'):
    if node == None:
        return 0, -float('inf'), []
    # 현재 노드의 서브트리 합을 현재 노드의 데이터로 초기화한다.
    tree_sum = node.data    
    if node.left != None:
        # 왼쪽 자식 노드가 있으면 재귀 호출한다. 재귀 호출 시 path에 'l'을 추가한다.  
        l_max, l_max_root_nodes, l_sum = max_power_yura(node.left, path + 'l')
    else:
        # 왼쪽 자식 노드가 없으면 왼쪽 서브트리 합은 0,
        # 최대 서브트리 합은 충분히 작은 값을 사용한다.
        l_max, l_max_root_nodes, l_sum = -float('inf'), [], 0
    # 오른쪽 자식 노드는 왼쪽 자식노드와 동일하게 동작한다.
    if node.right != None:
        r_max, r_max_root_nodes, r_sum = max_power_yura(node.right, path + 'r')
    else:
        r_max, r_max_root_nodes, r_sum = -float('inf'), [], 0
    # 현재 노드의 서브트리 합을 계산한다.
    tree_sum += l_sum + r_sum
    # 1. 현재 노드의 서브 트리 합
    # 2. 왼쪽 서브트리의 최대 서브트리 합
    # 3. 오른쪽 서브트리의 최대 서브트리 합
    # 세 값의 최대값을 서브트리 합, 최대 서브트리의 루트의 위치와 목록과 함께 반환한다.
   
    # 양쪽 서브트리의 결과를 우선 취합
    c_max = max(l_max, r_max)
    if l_max > r_max:
        c_max_root_nodes = l_max_root_nodes
    elif l_max < r_max:
        c_max_root_nodes = r_max_root_nodes
    else:
        c_max_root_nodes = l_max_root_nodes + r_max_root_nodes

    if tree_sum > c_max:
        # 현재 트리의 합이 가장 클 때
        current_max = tree_sum
        current_max_root_nodes = [path]
    elif tree_sum < c_max:
        # 자식 노드의 서브트리 합이 더 클때
        current_max = c_max
        current_max_root_nodes = c_max_root_nodes
    else:
        # 같을 때는 최대 서브트리의 루트 목록에 현재 노드를 추가한다.
        current_max = tree_sum
        current_max_root_nodes = [path] + c_max_root_nodes

    return current_max, current_max_root_nodes, tree_sum



def max_power(node):
    if node == None:
        return 0, -float('inf')
    # 현재 노드의 서브트리 합을 현재 노드의 데이터로 초기화한다.
    tree_sum = node.data    
    if node.left != None:
        # 왼쪽 자식 노드가 있으면 재귀 호출한다.  
        l_max, l_sum = max_power(node.left)
    else:
        # 왼쪽 자식 노드가 없으면 왼쪽 서브트리 합은 0,
        # 최대 서브트리 합은 충분히 작은 값을 사용한다.
        l_max, l_sum = -float('inf'), 0
    # 오른쪽 자식 노드는 왼쪽 자식노드와 동일하게 동작한다.
    if node.right != None:
        r_max, r_sum = max_power(node.right)
    else:
        r_max, r_sum = -float('inf'), 0
    # 현재 노드의 서브트리 합을 계산한다.
    tree_sum += l_sum + r_sum
    # 1. 현재 노드의 서브 트리 합
    # 2. 왼쪽 서브트리의 최대 서브트리 합
    # 3. 오른쪽 서브트리의 최대 서브트리 합
    # 세 값의 최대값을 서브트리 합과 함께 반환한다.
    return max(tree_sum, l_max, r_max), tree_sum

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