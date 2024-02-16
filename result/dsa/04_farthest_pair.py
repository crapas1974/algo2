from tree_diameter_data import get_testcases
from collections import deque

def farthest_nodes(root, memo = None):
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
    farthest_child_data = {}
    for i in range(max_level, -1, -1):
        for node in level_dict[i]:
            if node.left == None: 
                left_height = -1
                left_diameter, left_diameter_pair = -1, []
                left_farthest_child_data = [root.data]
            else:                 
                left_height = height[node.left]                
                left_diameter, left_diameter_pair = diameter[node.left]
                left_farthest_child_data = farthest_child_data[node.left]
            if node.right == None:
                right_height = -1
                right_diameter, right_diameter_pair = -1, []
                right_farthest_child_data = [root.data]
            else:                 
                right_height = height[node.right]
                right_diameter, right_diameter_pair = diameter[node.right]
                right_farthest_child_data = farthest_child_data[node.right]

            if left_height > right_height:
                height[node] = 1 + left_height
                farthest_child_data[node] = left_farthest_child_data
            elif left_height < right_height:
                height[node] = 1 + right_height
                farthest_child_data[node] = right_farthest_child_data
            else: 
                height[node] = 1 + left_height
                farthest_child_data[node] = left_farthest_child_data + right_farthest_child_data
           
            if height[node] == 0:
                farthest_child_data[node] = [node.data]

            diameter_current_node = left_height + right_height + 2
            diameter_from_child = max(left_diameter, right_diameter)
           
            if diameter_current_node >= diameter_from_child:
                combi = []                
                for left_data in left_farthest_child_data:
                    for right_data in right_farthest_child_data:
                        combi.append((left_data, right_data))
                if diameter_current_node == left_diameter:
                    combi += left_diameter_pair
                if diameter_current_node == right_diameter:
                    combi += right_diameter_pair
                diameter[node] = (diameter_current_node, combi)
            elif left_diameter > right_diameter:
                diameter[node] = (left_diameter, left_diameter_pair)
            elif left_diameter < right_diameter:
                diameter[node] = (right_diameter, right_diameter_pair)
            else:
                diameter[node] = (left_diameter, left_diameter_pair + right_diameter_pair)
    return diameter[root]



def main():
    testcases = get_testcases()
    for i, tc in enumerate(testcases):
        tree_diameter, furthest_node_pairs = farthest_nodes(tc)
        print(f"Testcase {i + 1}")
        print(f"    트리의 지름 : {tree_diameter}")
        print(f"    가장 먼 노드 쌍 : {furthest_node_pairs}")
        print()

if __name__ == "__main__":
    main()  