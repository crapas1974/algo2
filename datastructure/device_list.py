
class Device:
    def __init__(self, model_name):
        self.model_name = model_name
        self.next = None

def add_node_first(head: Device, model_name: str) -> Device:    
    new_node = Device(model_name)
    new_node.next = head
    return new_node

def add_node_last(head: Device, model_name: str) -> Device:
    new_node = Device(model_name)
    if head == None:
        return new_node
    
    cur = head
    while True:
        if cur.next == None:
            cur.next = new_node
            break
        cur = cur.next
    return head

def add_node(head: Device, model_before: str, model_name: str) -> Device:
    new_node = Device(model_name)
    if head == None:
        return new_node
    cur = head
    while True:
        if cur.model_name == model_before:
            new_node.next = cur.next
            cur.next = new_node
            break
        if cur.next == None:
            cur.next = new_node
            break
        cur = cur.next
    return head

def remove_first(head: Device) -> Device:
    if head == None:
        return None
    return head.next

def remove_last(head: Device) -> Device:
    if head == None:
        return None
    if head.next == None:
        return None
    cur = head
    while True:
        if cur.next.next == None:
            cur.next = None
            break
        cur = cur.next
    return head

def remove_models(head: Device, model_name: str) -> Device:
    if head == None:
        return None
    while head.model_name == model_name:
        head = head.next
        if head == None:
            return None
    cur = head
    while True:
        if cur.next == None:
            break
        if cur.next.model_name == model_name:
            cur.next = cur.next.next
            continue
        cur = cur.next
    return head

def node_at(head: Device, location: int) -> Device:
    if head == None:
        return None
    if location == 0:
        return head
    cur = head
    for _ in range(location):
        if cur.next == None:
            return None
        cur = cur.next
    return cur

def nodes_in_list(head: Device) -> str:
    result = ''
    cur = head
    while cur != None:
        result += cur.model_name
        cur = cur.next
    return result

def reverse(head: Device) -> Device:
    if head == None:
        return None
    if head.next == None:
        return Device(head.model_name)
    reverse_head = None
    while head != None:
        reverse_head = add_node_first(reverse_head, head.model_name)
        head = head.next
    return reverse_head

import hashlib

def hash4(input: str) -> str:
    return hashlib.md5(input.encode()).hexdigest()[:4]


def make_list_with_size(size: int, prefix: str) -> Device:
    head = None
    for i in range(size):
        head = add_node_last(head, f"{prefix}{i}")
    return head

def find_cycle(head: Device) -> Device:
    slow = fast = head
    while True:
        if slow.next == None or fast.next == None or fast.next.next == None:
            return None, None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = head
    before = None
    while True:
        if slow == fast:
            break
        before = fast
        slow = slow.next
        
        fast = fast.next
    if before == None:
        cur = head
        while cur.next != head:
            cur = cur.next
        before = cur
    return slow, before


def main2():
    list1 = make_list_with_size(1000, 'A')
    list2 = make_list_with_size(1000, 'B')
    list3 = make_list_with_size(5001, 'C')
    list4 = make_list_with_size(1000, 'D')
    list5 = make_list_with_size(5001, 'E')

    cur = list1
    circular_linked_node = None    
    i = 0
    while True:
        if i == 50:
            circular_linked_node = cur
        if cur.next == None:
            break
        cur = cur.next
        i += 1
    cur.next = circular_linked_node

    cur = list3
    circular_linked_node = None    
    i = 0
    while True:
        if i == 50:
            circular_linked_node = cur
        if cur.next == None:
            break
        cur = cur.next
        i += 1
    cur.next = circular_linked_node

    cur = list4
    while True:
        if cur.next == None:
            break
        cur = cur.next
    cur.next = list4

    cur = list5
    while True:
        if cur.next == None:
            break
        cur = cur.next
    cur.next = list5


    is_cyclic_list1, before_cyclic_list1 = find_cycle(list1)
    is_cyclic_list2, before_cyclic_list2 = find_cycle(list2)
    is_cyclic_list3, before_cyclic_list3 = find_cycle(list3)
    is_cyclic_list4, before_cyclic_list4 = find_cycle(list4)
    is_cyclic_list5, before_cyclic_list5 = find_cycle(list5)

    print("list1 : ", 'cyclic' if is_cyclic_list1 else 'non-cyclic')
    if is_cyclic_list1:
        print("    순환 연결한 노드의 모델 이름 :", before_cyclic_list1.model_name)
    print("list2 : ", 'cyclic' if is_cyclic_list2 else 'non-cyclic')
    if is_cyclic_list2:
        print("    순환 연결한 노드의 모델 이름 :", before_cyclic_list2.model_name)
    print("list3 : ", 'cyclic' if is_cyclic_list3 else 'non-cyclic')
    if is_cyclic_list3:
        print("    순환 연결한 노드의 모델 이름 :", before_cyclic_list3.model_name)
    print("list4 : ", 'cyclic' if is_cyclic_list4 else 'non-cyclic')
    if is_cyclic_list4:
        print("    순환 연결한 노드의 모델 이름 :", before_cyclic_list4.model_name)
    print("list5 : ", 'cyclic' if is_cyclic_list5 else 'non-cyclic')
    if is_cyclic_list5:
        print("    순환 연결한 노드의 모델 이름 :", before_cyclic_list5.model_name)


def main():
    result = []
    head = add_node_last(None, 'A1')
    head = add_node_last(head, 'A2')
    head = add_node_last(head, 'A3')
    head = add_node_last(head, 'A4')
    head = add_node_last(head, 'A3')
    head = add_node_first(head, 'A6')
    head = add_node_last(head, 'A7')
    head = add_node(head, 'A3', 'A8')
    result.append(nodes_in_list(head))
    result.append(nodes_in_list(reverse(head)))
    head = add_node_last(None, 'B1')
    head = add_node_last(head, 'B2')
    head = add_node_last(head, 'B3')
    head = add_node_last(head, 'B4')
    head = add_node_last(head, 'BR')
    head = add_node_last(head, 'BR')
    head = add_node_last(head, 'B5')
    head = add_node_last(head, 'B6')
    head = add_node_first(head, 'BR')
    head = add_node_first(head, 'BR')
    head = add_node_first(head, 'BR')
    head = add_node_last(head, 'BR')
    head = add_node_last(head, 'BR')
    head = add_node_last(head, 'BR')
    head = remove_models(head, 'BR')
    result.append(nodes_in_list(head))
    result.append(nodes_in_list(reverse(head)))
    head = add_node_last(None, 'C1')
    head = remove_first(head)
    head = add_node_first(head, 'C2')
    head = remove_last(head)
    head = add_node_first(head, 'C3')
    head = add_node_first(head, 'C4')
    head = remove_first(head)
    head = add_node_first(head, 'C5')
    head = add_node_first(head, 'C6')
    head = remove_last(head)
    head = add_node_first(head, 'C7')
    head = add_node_first(head, 'C8')
    node = node_at(head, 2)
    result.append(nodes_in_list(node))
    result.append(nodes_in_list(reverse(node)))
    head = None
    for i in range(10000):
        model_name = 'D' + str(i % 987)
        head = add_node_first(head, model_name)
    head = add_node_last(node_at(head, 5), 'DN')
    result.append(nodes_in_list(reverse(head)))
    result.append(nodes_in_list(head))
    head = remove_models(head, 'D0')
    result.append(nodes_in_list(reverse(head)))
    result.append(nodes_in_list(head))
    for result in result:
        print(hash4(result), result[:20])   

if __name__ == '__main__':
    main()

