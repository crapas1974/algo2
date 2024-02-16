from max_pathsum_tree_data import get_testcases

def absorbing_max_path(node, path = "@"):
    if node == None:
        return 0, [], -float('inf'), ([], [])
    max_left_path_sum, max_leftmost_node, left_max_so_far, left_max_path_ends = absorbing_max_path(node.left, path + "l")

    max_right_path_sum, max_rightmost_node, right_max_so_far, right_max_path_ends = absorbing_max_path(node.right, path + "r")

    if max_left_path_sum <= 0 and max_right_path_sum <= 0:
        current_oneway_path_sum = node.data
        current_oneway_path_end = [path]
    elif max_left_path_sum == max_right_path_sum:
        current_oneway_path_sum = node.data + max_left_path_sum
        current_oneway_path_end = max_leftmost_node + max_rightmost_node
    elif max_left_path_sum > max_right_path_sum:
        current_oneway_path_sum = node.data + max_left_path_sum
        current_oneway_path_end = max_leftmost_node
    else:
        current_oneway_path_sum = node.data + max_right_path_sum
        current_oneway_path_end = max_rightmost_node

    current_max_so_far = node.data
    current_max_path_ends = [([path], [path])]
    if max_left_path_sum <= 0 and max_right_path_sum > 0:
        current_max_so_far += max_right_path_sum
        current_max_path_ends = [([path], max_rightmost_node)]

    elif max_left_path_sum > 0 and max_right_path_sum <= 0:
        current_max_so_far += max_left_path_sum
        current_max_path_ends = [(max_leftmost_node, [path])]

    elif max_left_path_sum > 0 and max_right_path_sum > 0:
        current_max_so_far += max_left_path_sum + max_right_path_sum
        current_max_path_ends = [(max_leftmost_node, max_rightmost_node)]        

    if current_max_so_far > left_max_so_far and current_max_so_far > right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends
    elif current_max_so_far == left_max_so_far and left_max_so_far > right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + left_max_path_ends
    elif current_max_so_far == right_max_so_far and right_max_so_far > left_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + right_max_path_ends
    elif current_max_so_far == left_max_so_far and left_max_so_far == right_max_so_far:
        max_path_sum_under_node = current_max_so_far
        max_path_ends = current_max_path_ends + left_max_path_ends + right_max_path_ends
    elif left_max_so_far == right_max_so_far and left_max_so_far > current_max_so_far:
        max_path_sum_under_node = left_max_so_far
        max_path_ends = left_max_path_ends + right_max_path_ends
    elif left_max_so_far > right_max_so_far and left_max_so_far > current_max_so_far:
        max_path_sum_under_node = left_max_so_far
        max_path_ends = left_max_path_ends
    elif right_max_so_far > left_max_so_far and right_max_so_far > current_max_so_far:
        max_path_sum_under_node = right_max_so_far
        max_path_ends = right_max_path_ends

    return current_oneway_path_sum, current_oneway_path_end, max_path_sum_under_node, max_path_ends

def main():
    testcases = get_testcases()
    for i, testcase_root in enumerate(testcases):
        result = []
        _, _, max_path_sum, max_path_ends = absorbing_max_path(testcase_root)
        for starts, ends in max_path_ends:
            for start in starts:
                for end in ends:
                    result.append((start, end))

        print(f"Testcase {i + 1}")
        print(f"    최대 경로합: {max_path_sum}")
        print(f"    최대 경로합 경로의 양 끝 노드 : {result}")
        print()

if __name__ == '__main__':
    main()
