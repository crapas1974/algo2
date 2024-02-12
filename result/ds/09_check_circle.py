class Device:
    def __init__(self, model_name):
        self.model_name = model_name
        self.next = None

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

    testcases = [list1, list2, list3, list4, list5]
    for i, tc in enumerate(testcases):
        
        is_cyclic_list, before_cyclic_list = find_cycle(tc)
        print(f"연결된 리스트 {i + 1} : {'cyclic' if is_cyclic_list else 'non-cyclic'}")
        if is_cyclic_list:
            print(f"    순환 연결한 노드의 모델 이름 : {before_cyclic_list.model_name}")
        print()

if __name__ == "__main__":
    main()