
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
    return hashlib.sha256(str(input).encode()).hexdigest()[:4]

def tree_to_string(node: Species) -> list[str]:
    if node == None:
        return []
    result = node.name
    if node.left == None:
        result += '_l_'
    else:
        result += tree_to_string(node.left)
    if node.right == None:
        result += '_r_'
    else:
        result += tree_to_string(node.right)
    return result


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
        root, check_node = make_tree(tc)
        ancestor_nodes = ancestor_list(check_node, root)
        #print(ancestor_nodes)
        print(f"Testcase {i+1}")
        print(f"    출력결과 : {hash4(ancestor_nodes)}")
        print()

if __name__ == '__main__':
    main()