class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def value_and_structure(root, init=True):
    if root == None:
        return
    result = str(root.key)
    if root.left == None and root.right == None:
        return result
    result += "("
    if root.left == None:
        result += ","
    else:
        result += value_and_structure(root.left, False) + ","
    if root.right == None:
        result += ")"
    else:
        result += value_and_structure(root.right, False) + ")"
    if init:
        print(result)
    return result

def inorder_list(root):
    if root == None:
        return []
    return inorder_list(root.left) + [root.key] + inorder_list(root.right)

def get_every_balance(root):
    if root == None:
        return []
    return get_every_balance(root.left) + [get_balance(root)] + get_every_balance(root.right)


def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def rotate_right(y):
    print("~~", y.key)
    x = y.left
    print("~~~", x.key)

    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    if not node:
        return AVLTreeNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    update_height(node)

    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return rotate_right(node)

    if balance < -1 and key > node.right.key:
        return rotate_left(node)

    if balance > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    if balance < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def remove(node, key):
    if not node:
        return node

    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        if not node.left or not node.right:
            temp = node.left if node.left else node.right
            if not temp:
                temp = node
                node = None
            else:
                node = temp
        else:
            temp = minValueNode(node.right)
            node.key = temp.key
            node.right = remove(node.right, temp.key)

    if not node:
        return node

    update_height(node)

    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return rotate_right(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return rotate_left(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def is_in_tree(root, key):
    if root == None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return is_in_tree(root.left, key)
    return is_in_tree(root.right, key)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

import hashlib
def hash4(input):
    if not isinstance(input, str):
        input = str(input)
    return hashlib.sha256(input.encode()).hexdigest()[:4]

def main():
    root = None
    with open("well_made_tree_data.txt", "r") as f:
        while True:
            line = f.readline().strip()
            #print(">>>", line)
            if not line:
                break
            if line[:4] == 'TTAC':
                print(value_and_structure(root))
            if line == "init":
                root = None
            elif line == "print":
                sorted_list = inorder_list(root)
                print(hash4(sorted_list))
                balance_list = get_every_balance(root)
                print(''.join([str(balance) for balance in balance_list]))            
                tree_str = value_and_structure(root)
                print(hash4(tree_str))
            elif line == "print_list":
                sorted_list = inorder_list(root)
                print(hash4(sorted_list))
#                print(hash4_from_list(inorder_list(root)))
            elif line == "print_balance":
                balance_list = get_every_balance(root)
                print(''.join([str(balance) for balance in balance_list]))            
            elif line == "print_tree":
                tree_str = value_and_structure(root)
                print(hash4(tree_str))
            elif line[-1] == '-':
                value, _ = line.split(" ")
                root = remove(root, value)
            elif line[-1] == '?':
                value, _ = line.split(" ")
                print(is_in_tree(root, value))
            else:
                value = line
                root = insert(root, value)

    # root = None
    # root = insert(root, 5)
    # root = insert(root, 4)
    # root = insert(root, 3)
    # root = insert(root, 2)
    # root = insert(root, 1)
    # root = insert(root, 10)
    # root = insert(root, 11)
    # print_tree(root)
    # root = insert(root, 12)
    # root = insert(root, 13)
    # root = insert(root, 14)
    # print_tree(root)
    # root = insert(root, 15)
    print_tree(root)

if __name__ == '__main__':
    main()