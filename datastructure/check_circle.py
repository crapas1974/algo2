from device_list import add_node_last, Device


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


def main():
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

if __name__ == "__main__":
    main()