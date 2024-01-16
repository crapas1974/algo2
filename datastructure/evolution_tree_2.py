class Species:
    def __init__(self, name, gene_list=None):
        self.name = name
        self.gene_list = gene_list
        self.childs = []

def add_species(parent, name, gene_list=None):
    child_species = Species(name, gene_list)
    parent.childs.append(child_species)
    return child_species

def make_gene_list(node):
    if node.gene_list:
#        print("1", node.name, node.gene_list)
        return node.gene_list
    if len(node.childs) == 0:        
        return None
    gene_list = None
    can_make_gene_list = True
    for child in node.childs:
        # 자식 노드의 gene_list가 없으면 재귀 호출로 자식 노드이 gene_list를 구성한다.
        if child.gene_list == None:
            child.gene_list = make_gene_list(child)
        # 구성한 후에도 자식 노드의 gene_list가 None이면 해당 노드의 gene_list를 구성할 수 없다.
        # 단 전체 자식들의 gene_list를 구성해야 하므로 재귀 호출은 반복한다.
        if child.gene_list == None:
            can_make_gene_list = False
            continue

        if gene_list == None:
            gene_list = child.gene_list
        else:
            gene_list = list(set(gene_list) & set(child.gene_list))
    if can_make_gene_list:
        node.gene_list = gene_list
    #print(node.name, node.gene_list)
    return node.gene_list
# def make_sample_tree(imported):
#     root = None
#     for imported_line in imported:
#         nodes = imported_line.strip().split('|')
#         for node in nodes:
#             node_name, node_position, *gene_list = node.split(',')
#             if gene_list == []:
#                 gene_list = None
#             if node_position == '':
#                 root = Species(node_name, gene_list)
#             else:
#                 for 

            #print(node_name, node_location, gene_list)

def make_tree_description(node, position = 'r'):
    description = position + ',' + node.name + ','
    description += str(len(node.childs)) + ','
    if node.gene_list:
        for gene in node.gene_list:
            description += str(gene) + ','
    description += '\n'
    if len(node.childs) == 0:
        return description
    #description += '('
    for i, child in enumerate(node.childs):
        description += make_tree_description(child, position + str(i))
#    description = description[:-1]
#    description += ')'
    return description

def generate_tree(description):
    root = None
    parent = None
    node_descriptions = description.split('\n')
    for node_description in node_descriptions:
        if node_description == '':
            continue
        node_description = node_description[:-1]
        #print("--", node_description)
        node_segment = node_description.split(',')
        node_position = node_segment[0]
        node_name = node_segment[1]
        child_count = int(node_segment[2])
        if len(node_segment) > 3:
            gene_list = node_segment[3:]
            gene_list = list(map(int, gene_list))
        else:
            gene_list = None
        node = Species(node_name, gene_list)
        if node_position == 'r':
            root = node
        else:
            parent = root
            for i in range(1, len(node_position) - 1):
                parent = parent.childs[int(node_position[i])]
            parent.childs.append(node)
    return root

import random

def generate_random_tree(max_depth, currend_depth = 0):
    # make random name with 5 letters
    name = ''
    for i in range(5):
        name += chr(random.randint(65, 90))
    has_child = random.randint(0, 1)
    has_child = 1
    if has_child == 0 or currend_depth == max_depth:
        gene_count = random.randint(20, 25)
        #gene_count = 80
        gene_list = set()
        for i in range(gene_count):
            gene_list.add(random.randint(1, 20))
        gene_list = list(gene_list)
        return Species(name, gene_list)
    num_child = random.randint(1, 3)
    node = Species(name)
    for _ in range(num_child):
        node.childs.append(generate_random_tree(max_depth, currend_depth + 1))
    return node


    # make random child number




    #for i in range(int(child_count)):


# def generate_tree(description):
#     print("DI", description)
#     tree_segment = description.split(',')
#     node_name = tree_segment[0]
#     gene_list = tree_segment[1:]
#     last_index = -1
#     for i, gene in enumerate(gene_list):
#         if gene[0] == '(':
#             last_index = i
#             break
#     if last_index != -1:
#         gene_list = gene_list[:last_index]
#     if len(gene_list) == 0:
#         gene_list = None
#     node = Species(node_name, gene_list)

# #    i = 0
#     child_start = description.find('(') + 1
#     child_end = -1
#     child_descriptions = ''
#     if child_start != 0:
#         child_end = description.rfind(')')
#         child_descriptions = description[child_start:child_end]
#     child_description_list = child_descriptions.split('|')
#     print("D", child_description_list, len(child_description_list))
#     #for child_description in child_description_list:
#     #    child = generate_tree(child_description)
#     #    node.childs.append(child)
#     return node




    # for c in description:
    #     if c == '(':
    #         child_start = i
    #         break
    #     i += 1
    # if child_start != -1:
    #     child_end = description.rfind(')')
    #     child_description = description[child_start+1:child_end]
    #     child_description = child_description.split('|')
    #     for child in child_description:
    #         generate_tree(child)



def main():
    with open("evolution_tree_testcase.txt", "r") as f:
        tree_description = ''
        testcase_line = f.readline()
        while True:
            line = f.readline()            
            if not line or line[0] == 't' or line.strip == '':
                root = generate_tree(tree_description)
                print(testcase_line.strip())
                print("  ", make_gene_list(root))
                if not line or line.strip == '':
                    break
                else:
                    testcase_line = line
                    tree_description = ''
            else:
                tree_description += line




#     root = Species('P1')
#     root.childs.append(Species('C1', [1, 2, 3, 4, 5]))
#     root.childs.append(Species('C2', [1, 3, 5, 6, 7]))
#     desc1 = make_tree_description(root)
#     print(desc1)
#     print(make_gene_list(root))

#     root = Species('A0')
#     add_species(root, 'B0')
#     add_species(root, 'B1')
#     add_species(root.childs[0], 'C0', [1, 2, 3, 4, 5])
#     add_species(root.childs[0], 'C1', [1, 3, 5, 7, 9])
#     add_species(root.childs[1], 'C2', [2, 3, 5, 6, 7])
#     add_species(root.childs[1], 'C3', [3, 4, 5, 7, 8])
#     desc1 = make_tree_description(root)
# #    print(make_gene_list(root))
#     print(desc1)
#     root_copy = generate_tree(desc1)
# #    print("rcpy name : ", root_copy.name)
#     print("---")
#     print(make_tree_description(root_copy))

#     print("---")
#     print(make_gene_list(root))
#     print(make_gene_list(root_copy))
#     for i in range(100000):
#         print(i)

#         root = generate_random_tree(3)
#         desc = make_tree_description(root)
# #        print(desc)
# #        print("-----")
#         root_copy = generate_tree(desc)
#         l1 = make_gene_list(root)
#         l2 = make_gene_list(root_copy)
#         if l1 != l2:
#             print("ERROR")
#             print(desc)
#             print(l1)
#             print(l2)
#             break
#         print("Case")
#         print(desc)
#         r2 = generate_tree(desc)
#         make_gene_list(r2)

#         print(l1)
#         break

#         if len(desc.split('\n')) > 0 and l1 != None:
#             print("Case")
#             print(desc)
#             print(l1)
#             break




















    # root = Species('A0')
    # add_species(root, 'B0')
    # add_species(root, 'B1')
    # add_species(root, 'B2')
    # add_species(root.childs[0], 'C0', [1, 2, 3, 32, 48, 64]) 
    # add_species(root.childs[0], 'C1')
    # add_species(root.childs[0], 'C2', [32, 35, 48, 49, 64]) 
    # add_species(root.childs[1], 'C3', [32, 36, 40, 44, 48])
    # add_species(root.childs[1], 'C4', [32, 35, 38, 41, 44, 48]) 
    # add_species(root.childs[1], 'C5', [32, 37, 42, 44, 47, 48])
    # add_species(root.childs[2], 'C6', [16, 32, 48]) 
    # add_species(root.childs[2], 'C7', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48])
    # add_species(root.childs[2], 'C8') 
    # add_species(root.childs[0].childs[1], 'D0', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])
    # add_species(root.childs[0].childs[1], 'D1', [32, 33, 36, 37, 40, 42, 48, 64])
    # add_species(root.childs[2].childs[2], 'D2', [16, 32, 48, 64, 80])
    # add_species(root.childs[2].childs[2], 'D3', [8, 16, 24, 32, 40, 48, 56, 64, 72])
    # desc2 = make_tree_description(root)
    # root_copy = generate_tree(desc2)
    # desc2_cpy = make_tree_description(root_copy)
    # print("---")
    # print(desc2)
    # print("---")
    # print(desc2_cpy)
    # print("---")
    # print(make_gene_list(root))
    # print(make_gene_list(root_copy))


#    print(make_gene_list(root))
#    print(desc2)

    # with open("evolution_tree_testcase.txt", "r") as f:
    #     imported = []
    #     while True:
    #         line = f.readline()
    #         if not line: break
    #         imported.append(line)
    #     make_sample_tree(imported)

if __name__ == '__main__':
    main()
        


