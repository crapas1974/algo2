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

def convert_tree_bfs(root: Species):   
    if root == None:
        return ''
    result = root.name + ','
    node_for_explore = [root.left, root.right]
    while True:
        next_node_count = 0
        node_for_explore_next = []
        for node in node_for_explore:
            if node == None:
                result += ','
                node_for_explore_next += [None, None]
            else:
                result += node.name + ','
                if node.left != None:
                    node_for_explore_next.append(node.left)
                    next_node_count += 1
                else:
                    node_for_explore_next.append(None)
                if node.right != None:
                    node_for_explore_next.append(node.right)
                    next_node_count += 1
                else:
                    node_for_explore_next.append(None)
        if next_node_count == 0:
            break
        node_for_explore = node_for_explore_next
    while result[-1] == ',':
        result = result[:-1]
    return result

def recover_tree(tree_str: str):
    nodes = tree_str.split(',')
    if len(nodes) == 0:
        return None
    root = Species(nodes[0])
    parent_nodes = [root]
    next_parent_nodes = []
    idx = 1
    while idx < len(nodes):
        if len(parent_nodes) == 0:
            parent_nodes = next_parent_nodes
            next_parent_nodes = []

        parent_node = parent_nodes.pop(0)
        if parent_node == None:
            next_parent_nodes += [None, None]
        else:
            next_child = nodes[idx]
            if next_child != '':
                parent_node.left = Species(next_child)
                next_parent_nodes.append(parent_node.left)            
            else:
                next_parent_nodes.append(None)
            if idx + 1 >= len(nodes):
                break
            next_child = nodes[idx + 1]
            if next_child != '':
                parent_node.right = Species(next_child)
                next_parent_nodes.append(parent_node.right)
            else:
                next_parent_nodes.append(None)
        idx += 2
    return root





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
        tree_description = convert_tree_bfs(root)
        print(f"    BFS 문자열 표현의 간이 해시값 : {hash4(tree_description)}")
        recovered_tree = recover_tree(tree_description)
        recovered_tree_description = convert_tree_bfs(recovered_tree)
        if tree_description == recovered_tree_description:
            print(f"    복원한 트리의 BFS 문자열 표현의 간이 해시값 : {hash4(recovered_tree_description)}")
            print(f"    원래의 트리와 일치합니다.")
        else:
            print(f"    복원한 트리의 BFS 문자열 표현의 간이 해시값 : {hash4(recovered_tree_description)}")
            print(f"    원래의 트리와 일치하지 않습니다.")
        print()

if __name__ == "__main__":
    main()
