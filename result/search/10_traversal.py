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

def in_order(root: Species):
    if root == None:
        return []
    result = []
    result += in_order(root.left)
    result.append(root.name)
    result += in_order(root.right)
    return result

def pre_order(root: Species):
    if root == None:
        return []
    result = []
    result.append(root.name)
    result += pre_order(root.left)
    result += pre_order(root.right)
    return result

def post_order(root: Species):
    if root == None:
        return []
    result = []
    result += post_order(root.left)
    result += post_order(root.right)
    result.append(root.name)
    return result


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

def hash4_from_list(arr): 
    return hashlib.md5(str(arr).encode()).hexdigest()[:4]


def main():
    with open("tree_example2.txt", "r") as f:
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
        root, _ = make_tree(tc)
        in_order_list = in_order(root)
        pre_order_list = pre_order(root)
        post_order_list = post_order(root)
        result_1 = hash4_from_list(pre_order_list)
        result_2 = hash4_from_list(post_order_list)
        result_3 = hash4_from_list(in_order_list)
        print(f"Testcase {i + 1}")
        print(f"    함수 1의 결과 : {result_1}")
        print(f"    함수 2의 결과 : {result_2}")
        print(f"    함수 3의 결과 : {result_3}")
        print()

if __name__ == "__main__":
    main()
