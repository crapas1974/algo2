from max_power_subtree_data import get_testcases


def max_power(node):
    if node == None:
        return 0, -float('inf')
    # 현재 노드의 서브트리 합을 현재 노드의 데이터로 초기화한다.
    tree_sum = node.data    
    if node.left != None:
        # 왼쪽 자식 노드가 있으면 재귀 호출한다.  
        l_sum, l_max = max_power(node.left)
    else:
        # 왼쪽 자식 노드가 없으면 왼쪽 서브트리 합은 0,
        # 최대 서브트리 합은 충분히 작은 값을 사용한다.
        l_sum, l_max = 0, -float('inf')
    # 오른쪽 자식 노드는 왼쪽 자식노드와 동일하게 동작한다.
    if node.right != None:
        r_sum, r_max = max_power(node.right)
    else:
        r_sum, r_max = 0, -float('inf')
    # 현재 노드의 서브트리 합을 계산한다.
    tree_sum += l_sum + r_sum
    # 1. 현재 노드의 서브 트리 합
    # 2. 왼쪽 서브트리의 최대 서브트리 합
    # 3. 오른쪽 서브트리의 최대 서브트리 합
    # 세 값의 최대값을 서브트리 합과 함께 반환한다.
    return tree_sum, max(tree_sum, l_max, r_max)

def main():
    testcases = get_testcases()
    for i, root in enumerate(testcases):
        print("testcase %d: " % (i + 1), end="")
        _, max_sum = max_power(root)
        print(max_sum)

if __name__ == "__main__":
    main()