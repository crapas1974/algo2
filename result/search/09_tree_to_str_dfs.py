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

def convert_tree_dfs(root: Species):   
    if root == None:
        return ''
    result = root.name
    if root.left == None and root.right == None:
        return result
    if root.left != None:
        result += '(' + convert_tree_dfs(root.left) + ','
    else:
        result += '(,'
    if root.right != None:
        result += convert_tree_dfs(root.right) + ')'
    else:
        result += ')'
    return result

def recover_tree(tree_str: str):
    if tree_str == '':
        return None
    if '(' not in tree_str:
        return Species(tree_str)
    depth = 0
    p_start = -1
    comma_at = -1
    p_end = -1
    idx = 0
    while True:
        if tree_str[idx] == '(':
            if depth == 0:
                p_start = idx
            depth += 1
        elif tree_str[idx] == ',':
            if depth == 1:
                comma_at = idx
        elif tree_str[idx] == ')':
            depth -= 1
            if depth == 0:
                p_end = idx
                break
        idx += 1
    left = tree_str[p_start + 1:comma_at]
    right = tree_str[comma_at + 1:p_end]
    node = Species(tree_str[:p_start])
    if left != '':
        node.left = recover_tree(left)
    if right != '':
        node.right = recover_tree(right)
    return node

def make_tree(nodes: list[(str, str)]):
    check_node_location = nodes[0][0]
    nodes.sort(key=lambda x: len(x[0]))

    root = add_child(nodes[0][1], None, True)
    check_node = None
    if check_node_location == 'O':
        check_node = root
    for i in range(1, len(nodes)):
        location = nodes[i][0]
        name = nodes[i][1]
        parent = root
        discovery_str = ''
        for j in range(1, len(location) - 1):
            if location[j] == 'l':
                parent = parent.left
                discovery_str += 'l'
            else:
                parent = parent.right
                discovery_str += 'r'

        if location[-1] == 'l':
            added_node = add_child(name, parent, True)

        else:
            added_node = add_child(name, parent, False)
        if location == check_node_location:
            check_node = added_node
    return root, check_node


import hashlib

def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]


def main():
    with open("tree_example.txt", "r") as f:
        lines = f.readlines()

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
        print(f"Testcase {i+1}")
        root, _ = make_tree(tc)
        tree_description = convert_tree_dfs(root)
        print(f"    BFS 문자열 표현의 간이 해시값 : {hash4(tree_description)}")
        recovered_tree = recover_tree(tree_description)
        recovered_tree_description = convert_tree_dfs(recovered_tree)
        if tree_description == recovered_tree_description:
           print(f"    복원한 트리의 BFS 문자열 표현의 간이 해시값 : {hash4(recovered_tree_description)}")
           print(f"    원래의 트리와 일치합니다.")
        else:
           print(f"    복원한 트리의 BFS 문자열 표현의 간이 해시값 : {hash4(recovered_tree_description)}")
           print(f"    원래의 트리와 일치하지 않습니다.")
        print()

if __name__ == "__main__":
    main()
