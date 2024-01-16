class Species:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def add_child(species_name: str, parent: Species, is_left: bool) -> Species:
    new_species = Species(species_name)
    if parent != None:
        if is_left:
            if parent.left != None:
                return None
            else:
                parent.left = new_species
        else:
            if parent.right != None:
                return None
            else:
                parent.right = new_species
    return new_species

def node_with_name(species_name: str, root) -> Species:
    if root == None:
        return None
    if root.name == species_name:
        return root
    if root.left != None:
        result = node_with_name(species_name, root.left)
        if result != None:
            return result
    if root.right != None:
        result = node_with_name(species_name, root.right)
        if result != None:
            return result
    return None

def ancestor_list(node: Species, root: Species) -> list[str]:
    if node == None or root == None:
        return None
    if node == root:
        return []
    if root.left != None:
        result = ancestor_list(node, root.left)
        if result != None:
            return [root.name] + result
    if root.right != None:
        result = ancestor_list(node, root.right)
        if result != None:
            return [root.name] + result
    return None

def make_tree(nodes: list[(str, str)]):
    print(nodes)
    check_node_location = nodes[0][0]
    # nodes의 각 항목은 (location, 이름)으로 구성되어 있다.

    # nodes를 location의 길이 순으로 정렬한다.
    nodes.sort(key=lambda x: len(x[0]))
    print("Sorted", nodes)

    root = add_child(nodes[0][1], None, True)
    check_node = None
    if check_node_location == 'O':
        check_node = root
    for i in range(1, len(nodes)):        
        location = nodes[i][0]
        name = nodes[i][1]
        #print(location, name)
        parent = root
        discovery_str = ''
        for j in range(1, len(location) - 1):
        #    print("discovery - ", location[j])
            if location[j] == 'l':
                parent = parent.left
                discovery_str += 'l'
            else:
                parent = parent.right
                discovery_str += 'r'
        
        if location[-1] == 'l':
        #    print(f"add node parent {discovery_str} name {parent.name} left")
            added_node = add_child(name, parent, True)
            
        else:
        #    print(f"add node parent {discovery_str} name {parent.name} right")
            added_node = add_child(name, parent, False)
        if location == check_node_location:
            check_node = added_node
    print(root.name, check_node.name)
    return root, check_node
        


import random

def make_random_node_name(length):
    name = ''
    for _ in range(length):
        name += chr(random.randint(97, 122))
    return name

def level_of_children(node: Species) -> int:
    if node == None:
        return None
    if node.left == None and node.right == None:
        return 0
    if node.left == None and node.right != None:
        return level_of_children(node.right) + 1
    if node.left != None and node.right == None:
        return level_of_children(node.left) + 1
    return max(level_of_children(node.left), level_of_children(node.right)) + 1

def descendant_all(node: Species) -> list[str]:
    if node == None:
        return []
    result = [node.name]
    result += descendant_all(node.left)
    result += descendant_all(node.right)
    return result


# def make_random_binary_tree(name_list = None, parent = None):
#     if name_list == None:
#         name_list = []
#     if parent == None:
#         name = make_random_node_name(5)
#         name_list.append(name)
#         parent = add_child(name, None, True)
#     toss = random.randint(1, 10)
#     print(toss)
#     if toss <= 5:
#         parent.left = make_random_binary_tree(name_list, make_random_binary_tree(name_list, parent))
#     toss = random.randint(1, 10)
#     print(toss)
#     if toss <= 5:
#         parent.right = make_random_binary_tree(name_list, make_random_binary_tree(name_list, parent))
#     return parent

def make_random_binary_tree(left_b = 5, right_b = 5, name_list = None, parent = None):
    if name_list == None:
        name_list = []

    if parent == None:
        name = make_random_node_name(5)
        name_list.append(name)
        parent = add_child(name, None, True)
#    ch = random.randint(0, 10000)
    toss = random.randint(1, 10)
#    print(ch, toss)
    if toss <= left_b:
        while True:
            name = make_random_node_name(5)
            if name not in name_list:
                break
        name_list.append(name)
        left_node = add_child(name, parent, True)
        make_random_binary_tree(left_b, right_b, name_list, left_node)
        
    toss = random.randint(1, 10)
#    print(ch, toss)
    if toss <= right_b:
        while True:
            name = make_random_node_name(5)
            if name not in name_list:
                break
        name_list.append(name)
        right_node = add_child(name, parent, False)
        make_random_binary_tree(left_b, right_b, name_list, right_node)

    return parent

def tree_to_list(node, current = None):
    if current == None:
        current = 'O'
    result = [(current, node.name)]
    if node.left != None:
        result += tree_to_list(node.left, current + 'l')
    if node.right != None:
        result += tree_to_list(node.right, current + 'r')
    return result
        


def main():
    tree_data = []
    with open("tree_example.txt", "r") as f:
        lines = f.readlines()

    line_length = len(lines)
    testcases = []
    testcase = []
    for line in lines:
        if line[:8] == 'Testcase':
            if testcase != []:
                testcases.append(testcase)
                testcase = []
        else:
            testcase.append(line.strip().split(','))
    testcases.append(testcase)

    for i, tc in enumerate(testcases):
        root, check_node = make_tree(tc)
        print(f"root - {root.name}, check_node - {check_node.name}")
        ancestor_nodes = ancestor_list(check_node, root)
        print(descendant_all(root))
        print(f"Testcase {i+1}")
        print(f"    모든 조상들의 목록 : {ancestor_nodes}")
        print()


    # for line in lines:


    #     tc_num = 0
    #     while True:            
    #         line = f.readline()
    #         if not line or line[:8] == 'Testcase':
    #             if tc_num != 0:
    #                 print("Testcase", tc_num")
    #                 root, check_node = make_tree(tree_data)
    #                 ancestor_nodes = ancestor_list(check_node, root)
    #                 print(f"    모든 조상들의 목록 : {ancestor_nodes}")

    #             if tc_num == 0:
    #                 tc_num += 1
    #             else 
    #             print("Testcase", tc_num)
    #             root, check_node = make_tree(tree_data)
    #             ancestor_nodes = ancestor_list(check_node, root)
    #             print(f"    모든 조상들의 목록 : {ancestor_nodes}")
    #             if not line:
    #                 break
    #             else:
    #                 tree_data = []
    #                 tc_num += 1
    #         else:
    #             tree_data.append(line.strip().split(','))
    #         line = f.readline()

            


#     testcases = []

#     nodes = []
#     nodes.append(('Ol', 'a0'))
#     nodes.append(('O', 'b0'))
#     testcases.append(nodes)     #1
    

#     nodes = []
#     nodes.append(('O', 'a0'))
#     nodes.append(('Ol', 'b0'))
#     nodes.append(('Or', 'b1'))
#     nodes.append(('Oll', 'c0'))
#     nodes.append(('olr', 'c1'))
#     nodes.append(('Orl', 'c2'))
#     nodes.append(('Orr', 'c3'))    
#     testcases.append(nodes[:])  #2
#     random.shuffle(nodes)
#     testcases.append(nodes)     #3


#     nodes = []
#     nodes.append(('Olll', 'd0'))
#     nodes.append(('O', 'a0'))
#     nodes.append(('Ol', 'b0'))
#     nodes.append(('Oll', 'c0'))
#     nodes.append(('Ollll', 'e0'))
#     testcases.append(nodes)  #4

#     nodes = []
#     nodes.append(('Orrrr', 'e0'))
#     nodes.append(('O', 'a0'))
#     nodes.append(('Or', 'b0'))
#     nodes.append(('Orr', 'c0'))
#     nodes.append(('Orrr', 'd0'))
#     testcases.append(nodes)  #5

#     nodes = []
#     nodes.append(('Olrllr', 'f0'))
#     nodes.append(('Olrll', 'e0'))
#     nodes.append(('Olrl', 'd0'))
#     nodes.append(('Olr', 'c0'))
#     nodes.append(('Ol', 'b0'))
#     nodes.append(('O', 'a0'))
#     testcases.append(nodes)  #5
    
#     rt = make_random_binary_tree(5, 5)
#     tree_list = tree_to_list(rt)
#     tree__list_copy = tree_list[:]
#     random.shuffle(tree__list_copy)
#     testcases.append(tree__list_copy)
    

    
    
    

#     for i, tc in enumerate(testcases):
#         print(f"Testcase {i+1}")
#         for j, node_line in enumerate(tc):
#             print(f"{node_line[0]},{node_line[1]}")
# #        make_tree(tc)
# #        print()


    # # r2 = make_random_binary_tree()
    # # print(descendant_all(r2))
    # # print(level_of_children(r2))
    # # print(tree_to_list(r2))
    # r7 = make_random_binary_tree(5, 5)
    # tr7 = tree_to_list(r7)
    # tr7_s = tr7[:]
    # random.shuffle(tr7_s)
    # print(tr7)
    # print("---")
    # print(tr7_s)
    # print()
    # for i, node_line in enumerate(tr7_s):
    #     print(f"{node_line[0]},{node_line[1]}")

    

if __name__ == '__main__':
    main()