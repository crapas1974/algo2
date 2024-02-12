# make avl binary tree

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def print_tree(root, init=True):
    if root == None:
        return
    result = str(root.value)
    if root.left_child == None and root.right_child == None:
        return result
    result += "("
    if root.left_child == None:
        result += "X,"
    else:
        result += print_tree(root.left_child, False) + ","
    if root.right_child == None:
        result += "X)"
    else:
        result += print_tree(root.right_child, False) + ")"
    if init:
        print(result)
    return result

def insert(node, value):
    if node == None:
        return BSTNode(value)
    if value < node.value:
        node.left_child = insert(node.left_child, value)
    else:
        node.right_child = insert(node.right_child, value)
    return node
    
def tree_height(node):
    if node == None:
        return 0
    left = tree_height(node.left_child)
    right = tree_height(node.right_child)
    #print(left, right)
    return 1 + max(tree_height(node.left_child), tree_height(node.right_child))

def rebalance_tree(root):
    l_height = tree_height(root.left_child)
    r_height = tree_height(root.right_child)
    if l_height > r_height + 1:
        new_root = root.left_child
        if root.left_child.right_child == None:
            new_root.right_child = root
        else:
            parent_node = root
            while new_root.right_child != None:
                parent_node = new_root
                new_root = new_root.right_child
            parent_node.right_child = new_root.left_child
            new_root.left_child = root.left_child
            new_root.right_child = root
        root.left = None
    elif l_height < r_height + 1:
        new_root = root.right_child
        if root.right_child.left_child == None:
            new_root.left_child = root
        else:
            parent_node = root
            while new_root.left_child != None:
                parent_node = new_root
                new_root = new_root.left_child
            parent_node.left_child = new_root.right_child
            new_root.right_child = root.right_child
            new_root.left_child = root
        root.right = None
    return new_root



def main():
#     root = None
#     root = insert(None, 50)
#     root = insert(root, 30)
#     root = insert(root, 20)
#     print(root.value)
# #    root = remove(root, 20)
#  #   root = remove(root, 30)
#     print(root.value)
# #    root = remove(root, 50)
#     print(root.value)
#     insert(root, 40)
#     insert(root, 70)
#     insert(root, 60)
#     insert(root, 80)
#     insert(root, 18)
#     insert(root, 35)
#     insert(root, 61)
#     insert(root, 81)
#     insert(root, 13)
#     insert(root, 19)
#     insert(root, 19)
#     insert(root, 60)

#     print_tree(root)
#     #print(tree_height(root))
#     #print(tree_height(root.left_child))
#     #print(tree_height(root.right_child))
#     #print(tree_height(root.left_child.left_child))
#     #print(tree_height(root.left_child.left_child.left_child))
#     print(tree_height(root.left_child.left_child.right_child))

    root = None
    root = insert(root, 50)
    root = insert(root, 49)    
    root = insert(root, 48)    
    root = insert(root, 47)   
    root = insert(root, 46)    
    print_tree(root)
    root = rebalance_tree(root)
    print_tree(root)


if __name__=="__main__":
    main()

"""
                  50
            30                 70     
       20      40         60        80
  18         35             61         81
13  19                     60
      19
"""