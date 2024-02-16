class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
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

import hashlib
def hash4_from_list(arr):
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
            elif line[-1] == '-':
                value, _ = line.split(" ")
                root = remove(root, value)
            else:
                value = line
                root = insert(root, value)

if __name__ == '__main__':
    main()