class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def print_tree(root, init=True):
    if root == None:
        return
    result = str(root.key)
    if root.left == None and root.right == None:
        return result
    result += "("
    if root.left == None:
        result += "X,"
    else:
        result += print_tree(root.left, False) + ","
    if root.right == None:
        result += "X)"
    else:
        result += print_tree(root.right, False) + ")"
    if init:
        print(result)
    return result


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
    x = y.left
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

def delete(node, key):
    if not node:
        return node

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
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
            node.right = delete(node.right, temp.key)

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

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def main():
    root = None
    root = insert(root, 5)
    root = insert(root, 4)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 1)
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