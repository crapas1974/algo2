class Species:
    def __init__(self, name):
        self.name = name
        self.children = []

def add_child(species_name: str, parent: Species) -> Species:
    new_species = Species(species_name)
    if parent != None:
        parent.children.append(new_species)
    return new_species

def node_with_name(species_name: str, node: Species) -> Species:
    if node == None:
        return None
    if node.name == species_name:
        return node
    for child in node.children:
        result = node_with_name(species_name, child)
        if result != None:
            return result
    return None

def level_of_children(node: Species) -> int:
    if node == None:
        return None
    if len(node.children) == 0:
        return 0
    level_of_direct_children = []
    for child in node.children:
        level_of_direct_children.append(level_of_children(child))
    return max(level_of_direct_children) + 1

def descendant_all(node: Species) -> list[str]:
    if node == None:
        return []
    result = [node.name]
    for child in node.children:
        result += descendant_all(child)
    return result

def farthest_children_name_and_level(node: Species) -> (list[str], int):
    if node == None:
        return None, None
    result = [node.name]
    max_level = 0
    for child in node.children:
        child_names, child_level = farthest_children_name_and_level(child)
        if child_level > max_level:
            max_level = child_level
            result = child_names
        elif child_level == max_level:
            result += child_names
    return result, max_level + 1

def farthest_children_name(node: Species) -> list[str]:
    return farthest_children_name_and_level(node)[0]

def is_descendant(species_name: str, node: Species) -> bool:
    if node == None:
        return False
    if node.name == species_name:
        return True
    for child in node.children:
        if is_descendant(species_name, child):
            return True
    return False

def main():
    root1 = add_child('A0', None)
    add_child('A1', root1)
    add_child('A2', root1)
    add_child('A3', root1)
    add_child('A4', root1.children[0])
    add_child('A5', root1.children[0])
    add_child('A6', root1.children[0])
    add_child('A7', root1.children[1])
    add_child('A8', root1.children[2])
    add_child('A9', root1.children[2])
    add_child('A10', root1.children[0].children[0])
    add_child('A11', root1.children[0].children[0])
    add_child('A12', root1.children[0].children[1])
    add_child('A13', root1.children[2].children[1])
    add_child('A14', root1.children[0].children[1].children[0])
    add_child('A15', root1.children[0].children[1].children[0].children[0])
    add_child('A16', root1.children[0].children[1].children[0].children[0])

    root2 = add_child('A0', None)
    add_child('A1', root2)
    add_child('A2', root2)
    add_child('A3', root2.children[1])
    add_child('A4', root2.children[1])
    add_child('A5', root2.children[1].children[1])
    add_child('A6', root2.children[1].children[1])
    add_child('A7', root2.children[1].children[1].children[1])
    add_child('A8', root2.children[1].children[1].children[1])
    add_child('A9', root2.children[1].children[1].children[1].children[1])
    add_child('A10', root2.children[1].children[1].children[1].children[1])

    root3 = add_child('A0', None)
    add_child('A1', root3)
    add_child('A2', root3)
    add_child('A3', root3)
    add_child('A4', root3)
    add_child('A5', root3)
    add_child('A6', root3)
    add_child('A7', root3)
    add_child('A8', root3)
    add_child('A9', root3)
    
    root4 = add_child('A0', None)
    add_child('A1', root4)
    add_child('A2', root4.children[0])
    add_child('A3', root4.children[0].children[0])
    add_child('A4', root4.children[0].children[0].children[0])
    add_child('A5', root4.children[0].children[0].children[0].children[0])
    add_child('A6', root4.children[0].children[0].children[0].children[0].children[0])
    add_child('A7', root4.children[0].children[0].children[0].children[0].children[0].children[0])
    add_child('A8', root4.children[0].children[0].children[0].children[0].children[0].children[0].children[0])
    add_child('A9', root4.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0])



    testcases = [root1, root2, root3, root4]

    for i, tc in enumerate(testcases):
        print(f"계통도 {i + 1}")
        print(f"    트리의 높이 : {level_of_children(tc)}")
        print(f"    최상위 조상으로부터 진화의 단계가 가장 먼 자손(들)의 이름 : {', '.join(farthest_children_name(tc))}")
        max_height_child_name = []
        max_height = -1
        for child in tc.children:
            height_of_child = level_of_children(child)
            if height_of_child > max_height:
                max_height = height_of_child
                max_height_child_name = [child.name]
            elif height_of_child == max_height:
                max_height_child_name.append(child.name)
        max_height_child_name_str = ', '.join(max_height_child_name)        
        if max_height == -1:
            print(f"    최상위 조상의 자식이 없습니다.")
        else:
            print(f"    최상위 조상의 자식 중 가장 진화 단계가 긴 자손을 가진 자식(들)의 이름 : {max_height_child_name_str}")
        decendant_names = ', '.join(descendant_all(tc))
        print(f"    계통도 내 모든 생물(들)의 이름 : {decendant_names}")
        has_decentent_A12 = is_descendant('A12', tc)
        if has_decentent_A12:
            print(f"    A12는 계통도 내에 있습니다.")
        else:
            print(f"    A12는 계통도 내에 없습니다.")
        node_A5 = node_with_name('A5', tc)
        print(f"    A5 생물종을 루트로 하는 서브트리의 높이 : {level_of_children(node_A5)}")
        print()

if __name__ == '__main__':
    main()
        
    


    
    
        
