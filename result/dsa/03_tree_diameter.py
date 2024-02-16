from tree_diameter_data import get_testcases
from collections import deque

def height(node, memo):
    if node in memo:
        return memo[node]
    if node == None:
        return -1
    memo[node] = 1 + max(height(node.left, memo), height(node.right, memo))
    return memo[node]


def tree_diameter_topdown(node, memo = None):
    if memo == None:
        memo = {}
    if node == None:
        return 0
    left_diameter = tree_diameter_topdown(node.left, memo)
    right_diameter = tree_diameter_topdown(node.right, memo)
    return max(height(node.left, memo) + height(node.right, memo) + 2,
                left_diameter,
                right_diameter)

def tree_diameter_bottomup(root, memo = None):
    if not root:
        return {}
    level_dict = {}
    queue = deque([(root, 0)])  
    max_level = 0
    while queue:
        node, level = queue.popleft()
        if level not in level_dict:
            level_dict[level] = []
            max_level = level
        level_dict[level].append(node)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    diameter = {}
    height = {}
    for i in range(max_level, -1, -1):
        for node in level_dict[i]:
            if node.left == None:
                left_height = -1
                left_diameter = -1
            else:                
                left_height = height[node.left]                
                left_diameter = diameter[node.left]
            if node.right == None: 
                right_height = -1
                right_diameter = -1
            else:                  
                right_height = height[node.right]
                right_diameter = diameter[node.right]

            height[node] = 1 + max(left_height, right_height)
            diameter[node] = max(left_height + right_height + 2,
                                    left_diameter,
                                    right_diameter)
    return diameter[root]

def main():
    testcases = get_testcases()
    for i, tc in enumerate(testcases):
        print(f"Testcase {i + 1}")
        print(f"    트리의 지름 (상향식) : {tree_diameter_bottomup(tc)}")
        print(f"    트리의 지름 (하향식) : {tree_diameter_topdown(tc)}")
        print()

if __name__ == "__main__":
    main()  