class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

def value_and_structure(root, init=True):
    if root == None:
        return
    result = str(root.value)
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
    return inorder_list(root.left) + [root.value] + inorder_list(root.right)

def get_every_balance(root):
    if root == None:
        return []
    return get_every_balance(root.left) + [get_balance(root)] + get_every_balance(root.right)

def get_height(node):
    if not node:
        return -1
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def rotate_right(node):
    left_child = node.left
    node.left = left_child.right
    left_child.right = node
    update_height(node)
    update_height(left_child)
    return left_child

def rotate_left_right(node):
    left_child = node.left
    right_left_child = left_child.right
    node.left = right_left_child.right
    left_child.right = right_left_child.left
    right_left_child.right = node
    right_left_child.left = left_child
    update_height(node)    
    update_height(left_child)
    update_height(right_left_child)
    return right_left_child

def rotate_left(node):
    right_child = node.right
    node.right = right_child.left
    right_child.left = node
    update_height(node)
    update_height(right_child)
    return right_child

def rotate_right_left(node):
    right_child = node.right
    left_right_child = right_child.left
    node.right = left_right_child.left
    right_child.left = left_right_child.right
    left_right_child.left = node
    left_right_child.right = right_child
    update_height(node)
    update_height(right_child)
    update_height(left_right_child)    
    return left_right_child

def balancing(node):
    if not node:
        return node
    update_height(node)
    balance = get_balance(node)
    if balance > 1:
        balance_left = get_balance(node.left)
        if balance_left >= 0:
            node = rotate_right(node)
        else:
            node = rotate_left_right(node)
    if balance < -1:
        balance_right = get_balance(node.right)
        if balance_right <= 0:
            node = rotate_left(node)
        else:
            node = rotate_right_left(node)
    return node

def insert(node, value):
    if not node:
        return AVLTreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    node = balancing(node)
    return node

def remove(node, value):
    if not node:
        return node
    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if not node.left or not node.right:
            temp = node.left if node.left else node.right
            if not temp:
                temp = node
                node = None
            else:
                node = temp
        else:
            min_value_node = get_min_value_node(node.right)
            node.value = min_value_node.value
            node.right = remove(node.right, min_value_node.value)
    if not node:
        return node
    node = balancing(node)
    return node

def is_in_tree(root, value):
    if root == None:
        return False
    if root.value == value:
        return True
    if value < root.value:
        return is_in_tree(root.left, value)
    return is_in_tree(root.right, value)

def get_min_value_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

import hashlib
# balanced_factor : 트리에 포함된 모든 노드의 균형 지수의 리스트
# inorder_list : 트리를 중위 순회한 결과를 담은 리스트
def hash4(balance_factor: list, inorder_list: list):
    for i in balance_factor:
        if i > 1 or i < -1:
            return "Wrong tree created"
    return format(len(inorder_list), '04d') + " " + hashlib.sha256(str(inorder_list).encode()).hexdigest()[:4]

def main():
    root = None
    with open("balanced_tree_data.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line == "init":
                root = None
            elif line == "print":
                sorted_list = inorder_list(root)
                balance_list = get_every_balance(root)
                print(hash4(balance_list, sorted_list))
            elif line[-1] == '-':
                value, _ = line.split(" ")
                root = remove(root, value)
            elif line[-1] == '?':
                value, _ = line.split(" ")
                if is_in_tree(root, value):
                    print(f"[{value}] : 트리에 포함되어 있습니다.")
                else:
                    print(f"[{value}] : 트리에 포함되어 있지 않습니다.")
            else:
                value = line
                root = insert(root, value)

if __name__ == '__main__':
    main()