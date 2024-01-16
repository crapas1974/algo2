class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    ptr = head
    print("linked-list의 내용 : ", end = '')
    while ptr is not None:
        print(ptr.data, end = ' ')
        ptr = ptr.next
    print()

def insert_front(head, data):
    node = Node(data)
    node.next = head
    head = node
    return head

def insert_back(head, data):
    node = Node(data)
    if head is None:
        head = node
        return head
    else:
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = node
        return head
   
def delete_front(head):
    if head is None:
        return None
    else:
        head = head.next
        return head
   
def delete_back(head):
    if head is None:
        return None
    elif head.next is None:
        return None
    else:
        ptr = head
        while ptr.next.next is not None:
            ptr = ptr.next
        ptr.next = None
        return head
# 값이 k인 노드를 찾아서, 해당되는 모든 노드를 삭제한다. 재귀적으로 구현한다.
def delete_node(node, k):
    if node is None:
        return None
    elif node.data == k:
        return delete_node(node.next, k)
    else:
        node.next = delete_node(node.next, k)
        return node
# 재귀적으로 거꾸로 방향의 리스트를 만든다.
def reverse(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        ptr = head
        while ptr.next.next is not None:
            ptr = ptr.next
        new_head = ptr.next
        ptr.next = None
        new_head.next = reverse(head)
        return new_head

def main2():
    head = insert_front(None, 'a')
    head = insert_back(head, 'b')
    head = insert_back(head, 'c')
    head = insert_back(head, 'd')
    head = insert_back(head, 'e')
    head = insert_back(head, 'd')
    head = insert_back(head, 'c')
    head = insert_back(head, 'b')
    head = insert_back(head, 'a')
    head = delete_node(head, 'c')
    print_list(head)
    head = insert_front(None, 'a')
    head = insert_back(head, 'b')
    head = insert_back(head, 'c')
    head = insert_back(head, 'd')
    head = insert_back(head, 'e')
    head = reverse(head)
    print_list(head)

def main():
    # 1의 값을 가지는 노드를 삽입 (리스트를 처음 생성)
    head = insert_front(None, 1)
    print_list(head)    # 1
    # 2의 값을 가지는 노드를 삽입 (리스트의 가장 앞에 삽입)
    head = insert_front(head, 2)
    # 3의 값을 가지는 노드를 삽입 (리스트의 가장 앞에 삽입)
    head = insert_front(head, 3)
    print_list(head)    # 3 2 1
    # 4의 값을 가지는 노드를 삽입 (리스트의 가장 뒤에 삽입)
    head = insert_back(head, 4)
    print_list(head)    # 3 2 1 4
    # 리스트의 가장 앞 노드를 삭제
    head = delete_front(head)
    print_list(head)    # 2 1 4
    # 리스트의 가장 뒤 노드를 삭제
    head = delete_back(head)
    print_list(head)    # 2 1
    # 리스트의 가장 앞 노드를 삭제
    head = delete_front(head)
    # 리스트의 가장 뒤 노드를 삭제
    head = delete_back(head)
    print_list(head)    # 2 1
    # 리스트의 가장 앞 노드를 삭제
    head = delete_front(head)
    print_list(head)    # 2 1

if __name__ == "__main__":
    main2()