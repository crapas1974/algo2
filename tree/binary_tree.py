class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert_child(self, l_or_r, node):
        # insert left child
        if l_or_r == 0:
            # if left child already exists, return False
            if self.left != None:
                return False
            self.left = node
        # insert right child
        elif l_or_r == 1:
            # if right child already exists, return False
            if self.right != None:
                return False
            self.right = node
        else:
            return False
        return True
   
    def delete_child(self, l_or_r):
        # delete left child
        if l_or_r == 0:
            self.left = None
        # delete right child
        elif l_or_r == 1:
            self.right = None
        else:
            return False
        return True
    
    def print_tree(self, end = True):
        # pre-order traversal - 자기 자신을 먼저 출력한다.
        print(self.data, end="")
        # 종료조건 : 양쪽 자식 노드가 모두 없는 경우
        if self.left == None and self.right == None:
            return
        # 자식 노드가 있는 경우
        print("(", end = "")
        # 왼쪽 자식 노드가 있는 경우 왼쪽 자식의 노드로 재귀 호출한다.
        if self.left != None:            
            self.left.print_tree(False)
        print(",", end = "")
        # 오른쪽 자식 노드가 있는 경우 오른쪽 자식 노드로 재귀 호출한다.
        if self.right != None:
            self.right.print_tree(False)
        print(")", end = "")
        # end = True인 경우는 재귀 호출이 아닌 최초 호출이므로 줄바꿈을 한다.
        if end:
            print()

def build_binary_tree(input_str):
    if not input_str:
        return None
    values = input_str.split(",")
    root = BTreeNode(int(values[0]))
    for i in range(1, len(values) - 1):
        insert_by_value(root, int(values[i]))
    return root


def build_binary_tree2(input_str):
    if not input_str:
        return None

    values = input_str.split(",")
    root = BTreeNode(int(values[0]))
    queue = [root]
    index = 1


    while index < len(values):
        node = queue.pop(0)


        left_value = values[index]
        index += 1
        if left_value != "n":
            node.left = BTreeNode(int(left_value))
            queue.append(node.left)


        if index < len(values):
            right_value = values[index]
            index += 1
            if right_value != "n":
                node.right = BTreeNode(int(right_value))
                queue.append(node.right)


    return root

def insert_by_value(node, data):
    if data >= node.data:
        if node.right == None:
            node.right = BTreeNode(data)
        else:
            insert_by_value(node.right, data)
    else:
        if node.left == None:
            node.left = BTreeNode(data)
        else:
            insert_by_value(node.left, data)
