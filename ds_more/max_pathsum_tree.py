from max_pathsum_tree_data import get_testcases
import itertools
# 주어진 노드에서 시작해서 하향 방향으로의 최대 경로의 합이다.
# 왼쪽 또는 오른쪽 중 한 쪽 방향으로만 하향한다.
# 반환 값은 두 개이다.
#   1. 나에서 시작하고, 하향하는 경로에서의 최대 경로합
#   2. 나를 루트로 하는 서브트리의 최대 경로합
# def absorbing_max(node):
#     if node == None:
#         return 0, -float('inf')
    
#     # 왼쪽 서브트리의 루트에서 시작하는 하향 최대 경로합과, 왼쪽 서브트리의 최대 경로합
#     max_left_path_sum, left_max_so_far = absorbing_max(node.left)

#     # 오른쪽 서브트리의 루트에서 시작하는 하향 최대 경로합과, 오른족 서브트리의 최대 경로합
#     max_right_path_sum, right_max_so_far = absorbing_max(node.right)

#     # 현재 노드에서 시작하는 하향 최대 경로합. 
#     # 왼쪽, 오른쪽, 현재 노드 중 최대값을 선택하며 양쪽 다 음수인 경우 둘 다 선택하지 않는다.
#     current_oneway_path_sum = max(0, max_left_path_sum, max_right_path_sum) + node.data

#     # 현재 노드를 통과하는 최대 경로합
#     # 왼쪽 자식 노드의 하향 최대 경로합, 오른쪽 자식 노드의 하향 최대 경로합이 모두 음수인 경우
#     current_max_so_far = node.data
    
#     if max_left_path_sum <= 0 and max_right_path_sum > 0:
#         # 오른쪽 자식 노드의 하향 최대 경로합만 양수인 경우는 현재 노드에 이를 더한다.
#         current_max_so_far += max_right_path_sum

#     elif max_left_path_sum > 0 and max_right_path_sum <= 0:
#         # 왼쪽 자식 노드의 하향 최대 경로합만 양수인 경우는 현재 노드에 이를 더한다.
#         current_max_so_far += max_left_path_sum

#     elif max_left_path_sum > 0 and max_right_path_sum > 0:
#         # 양쪽 자식 노드의 하향 최대값이 모두 양수이면, 모두 더한다.
#         current_max_so_far += max_left_path_sum + max_right_path_sum

#     # 현재, 그리고 하위 노드들의 최대 경로합 중에서 최대를 선택한다.
#     max_path_sum_under_node = max(left_max_so_far, 
#                                   right_max_so_far, 
#                                   current_max_so_far)

#     return current_oneway_path_sum, max_path_sum_under_node

# 주어진 노드에서 시작해서 하향 방향으로의 최대 경로의 합이다.
# 왼쪽 또는 오른쪽 중 한 쪽 방향으로만 하향한다.
# 반환 값은 두 개이다.
#   1. 나에서 시작하고, 하향하는 경로에서의 최대 경로합
#   2. 나에서 시작하고, 하향하는 경로에서의 반대쪽 끝 노드의 값
#   3. 나를 루트로 하는 서브트리의 최대 경로합
#   4. 나를 루트로 하는 서브트리의 최대 경로합을 만드는 경로의 조합
def absorbing_max_path(node, path = ''):
    # 기저조건
    if node == None:
        return 0, [], -float('inf'), ([], [])
    # 왼쪽 서브트리의 루트에서 시작하는 하향 최대 경로합과, 왼쪽 서브트리의 최대 경로합
    max_left_path_sum, max_leftmost_node, left_max_so_far, left_max_path_ends = absorbing_max_path(node.left, path + "l")

    # 오른쪽 서브트리의 루트에서 시작하는 하향 최대 경로합과, 오른족 서브트리의 최대 경로합
    max_right_path_sum, max_rightmost_node, right_max_so_far, right_max_path_ends = absorbing_max_path(node.right, path + "r")

    # 현재 노드에서 시작하는 하향 최대 경로합. 
    # 왼쪽, 오른쪽, 현재 노드 중 최대값을 선택하며 양쪽 다 음수인 경우 둘 다 선택하지 않는다.
    # 각 조건에 맞는 햐향 경로의 끝 노드를 선택한다.
    if max_left_path_sum <= 0 and max_right_path_sum <= 0:
        current_oneway_path_sum = node.data
        current_oneway_path_end = [node.data]
    elif max_left_path_sum == max_right_path_sum:
        current_oneway_path_sum = node.data + max_left_path_sum
        current_oneway_path_end = max_leftmost_node + max_rightmost_node
    elif max_left_path_sum > max_right_path_sum:
        current_oneway_path_sum = node.data + max_left_path_sum
        current_oneway_path_end = max_leftmost_node
    else:
        current_oneway_path_sum = node.data + max_right_path_sum
        current_oneway_path_end = max_rightmost_node

    # 현재 노드를 통과하는 최대 경로합
    # 왼쪽 자식 노드의 하향 최대 경로합, 오른쪽 자식 노드의 하향 최대 경로합이 모두 음수인 경우
    # 현재 노드를 통과하는 최대 경로합 경로의, 조건에 맞는 양 끝 노드의 조합도 구한다.
    current_max_so_far = node.data
    current_max_path_ends = [([node.data], [node.data])]
    if max_left_path_sum <= 0 and max_right_path_sum > 0:
        # 오른쪽 자식 노드의 하향 최대 경로합만 양수인 경우는 현재 노드에 이를 더한다.
        current_max_so_far += max_right_path_sum
        current_max_path_ends = [([node.data], max_rightmost_node)]

    elif max_left_path_sum > 0 and max_right_path_sum <= 0:
        # 왼쪽 자식 노드의 하향 최대 경로합만 양수인 경우는 현재 노드에 이를 더한다.
        current_max_so_far += max_left_path_sum
        current_max_path_ends = [(max_leftmost_node, [node.data])]

    elif max_left_path_sum > 0 and max_right_path_sum > 0:
        # 양쪽 자식 노드의 하향 최대값이 모두 양수이면, 모두 더한다.
        current_max_so_far += max_left_path_sum + max_right_path_sum
        current_max_path_ends = [(max_leftmost_node, max_rightmost_node)]

    # 현재, 그리고 하위 노드들의 최대 경로합 중에서 최대를 선택한다.
    # 각 경우의 양 끝 노드의 조합도 구한다.
    # 만약, 동점 최대 경로가 둘 이상 있는 경우, 각각의 케이스를 케이스는 취합한다.
    
    # 현재 노드를 지나는 경로가 최대경로합 경로인 경우
    if current_max_so_far > left_max_so_far and current_max_so_far > right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends
    # 현재 노드를 지나는 경로가 최대 경로합이며, 왼쪽 서브트리에도 같은 값의 최대 경로합 경로가 있는 경우
    elif current_max_so_far == left_max_so_far and left_max_so_far > right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + left_max_path_ends
    # 현재 노드를 지나는 경로가 최대 경로합이며, 오른쪽 서브트리에도 같은 값의 최대 경로합 경로가 있는 경우
    elif current_max_so_far == right_max_so_far and right_max_so_far > left_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + right_max_path_ends
    # 현재 노드를 지나는 경로가 최대 경로합이며, 양쪽 서브트리에도 같은 값의 최대 경로합 경로가 있는 경우
    elif current_max_so_far == left_max_so_far and left_max_so_far == right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + left_max_path_ends + right_max_path_ends
    # 양쪽 서브트리에만 같은 크기의 최대 경로합 경로가 모두 있는 경우
    elif left_max_so_far == right_max_so_far and left_max_so_far > current_max_so_far:
        max_path_sum_under_node = left_max_so_far
        max_path_ends = left_max_path_ends + right_max_path_ends
    # 왼쪽 서브트리에만 최대 경로합 경로가 있는 경우
    elif left_max_so_far > right_max_so_far and left_max_so_far > current_max_so_far:
        max_path_sum_under_node = left_max_so_far
        max_path_ends = left_max_path_ends
    # 오른족 서브트리에만 최대 경로합 경로가 있는 경우
    elif right_max_so_far > left_max_so_far and right_max_so_far > current_max_so_far:
        max_path_sum_under_node = right_max_so_far
        max_path_ends = right_max_path_ends

    # 반환 - 현재 노드에서 시작하는 하향하는 최대 경로합, 이 때의 반대쪽 노드 리스트, 현재 노드를 루트로 하는 서브트리에서 최대 경로합, 현재 노드를 루트로 하는 서브트리에서 최대 경로합 경로의 양 끝 노드 조합
    return current_oneway_path_sum, current_oneway_path_end, max_path_sum_under_node, max_path_ends

def main():
    testcases = get_testcases()
    for i, testcase_root in enumerate(testcases):
        result = []
        _, _, max_path_sum, max_path_ends = absorbing_max_path(testcase_root)
        for path in max_path_ends:
            combinations = list(itertools.product(*path))
            result += combinations

        print(f"Testcase {i + 1}")
        print(f"    최대 경로합: {max_path_sum}")
        print(f"    최대 경로합 경로의 양 끝 노드의 값 : {result}")
        print()

if __name__ == '__main__':
    main()
