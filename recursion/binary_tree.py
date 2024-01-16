class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(node, lvalue, rvalue):
  if lvalue != None:
    node.left = Node(lvalue)
  if rvalue != None:
    node.right = Node(rvalue)

def in_order(node):
  if node == None:
    return
  in_order(node.left)
  print(node.data, end = '')
  in_order(node.right)
  
def post_order(node):
  if node == None:
    return
  post_order(node.left)
  post_order(node.right)
  print(node.data, end = '')

def pre_order(node):
  if node == None:
    return
  print(node.data, end = '')
  pre_order(node.left)
  pre_order(node.right)

# 보너스 문제
def in_order_list(node):
    if node == None:
        return []
    return in_order_list(node.left) + [node.data] + in_order_list(node.right)

def main():
    root = Node('V')
    insert(root, 'N', 'T')
    insert(root.left, 'I', 'O')
    insert(root.left.left, None, 'N')
    insert(root.right, 'A', 'N')
    insert(root.right.right, 'O', None)
    insert(root.right.right.left, 'I', None)

    pre_order(root)
    print()
    in_order(root)
    print()
    post_order(root)
    print()
    print(in_order_list(root))

if __name__ == '__main__':
    main()