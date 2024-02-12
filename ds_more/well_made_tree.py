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
    
def inorder_list(root):
    if root == None:
        return []
    return inorder_list(root.left_child) + [root.value] + inorder_list(root.right_child)

def insert(node, value):
    if node == None:
        return BSTNode(value)
    if value < node.value:
        node.left_child = insert(node.left_child, value)
    else:
        node.right_child = insert(node.right_child, value)
    return node

def remove(root, value):
    if root == None:
        return None
    if value < root.value:
        root.left_child = remove(root.left_child, value)
    elif value > root.value:
        root.right_child = remove(root.right_child, value)
    else:
        if root.left_child == None:
            return root.right_child
        if root.right_child == None:
            return root.left_child
        temp = root.right_child
        while temp.left_child != None:
            temp = temp.left_child
        root.value = temp.value
        root.right_child = remove(root.right_child, temp.value)
    return root



# def insert(root, value):
#     if root == None:
#         return BSTNode(value)
#     if value < root.value:
#         insert(root.left_child, value)
#         return root
#     else:
#         insert(root.right_child, value)
#         return root

#def remove(root, value):
import hashlib

def hash4_from_list(arr):
    # print(arr)
    # if len(arr) == 0:
    #     return ""
    # convert_str = ''
    # # check arr[0] is string type
    # if isinstance(arr[0], str):
    #     convert_str = ''.join(arr)
    # elif isinstance(arr[0], (int)):
    #     sum = 0
    #     for i, n in enumerate(arr):
    #         sum += (n % (i + 1))
    #     convert_str = str(sum)
    # else:
    #     convert_str = str(arr)
    # print(convert_str)
    
    # return hashlib.sha256(convert_str.encode()).hexdigest()[:8]
    return hashlib.sha256(str(arr).encode()).hexdigest()[:4]

def main():
    root = None
    with open("well_made_tree_data.txt", "r") as f:
        
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line == "init":
                root = None
            elif line == "print":
                print(hash4_from_list(inorder_list(root)))
#                print(inorder_list(root))
            elif line[-1] == '-':
                value, _ = line.split(" ")
                root = remove(root, value)
            else:
                value = line
                root = insert(root, value)
    # root = None
    # root = insert(None, 50)
    # root = insert(root, 30)
    # root = insert(root, 20)
    # print(root.value)
    # root = remove(root, 20)
    # root = remove(root, 30)
    # print(root.value)
    # root = remove(root, 50)
    # print(root.value)
    # insert(root, 40)
    # insert(root, 70)
    # insert(root, 60)
    # insert(root, 80)
    # insert(root, 18)
    # insert(root, 35)
    # insert(root, 61)
    # insert(root, 81)
    # insert(root, 13)
    # insert(root, 19)
    # insert(root, 19)
    # insert(root, 60)

    # print_tree(root)
    # print(inorder_list(root))
    # remove(root, 19)
    # remove(root, 19)
    # remove(root, 60)
    # remove(root, 60)
    # remove(root, 60)
    # remove(root, 50)
    # remove(root, 13)
    # remove(root, 18)
    # print_tree(root)
    # print(inorder_list(root))
    
"""
          50
    30            70
  20    40    60    80
 18    35       61    81
13 19
"""

if __name__ == '__main__':
    main()