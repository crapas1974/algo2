
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

def main():
    head_a = add_node_last(None, 'A1')
    head_a = add_node_last(head_a, 'A2')
    head_a = add_node_last(head_a, 'A3')
    head_a = add_node_last(head_a, 'A4')
    head_a = add_node_last(head_a, 'A3')
    head_a = add_node_first(head_a, 'A0')
    head_a = add_node(head_a, 'A3', 'A8')
    print(nodes_in_list(head_a))
    print(nodes_in_list(reverse(head_a)))
    head_b = add_node_last(None, 'B1')
    head_b = add_node_last(head_b, 'B2')
    head_b = add_node_last(head_b, 'B3')
    head_b = add_node_last(head_b, 'B4')
    head_b = add_node_last(head_b, 'BR')
    head_b = add_node_last(head_b, 'BR')
    head_b = add_node_last(head_b, 'B5')
    head_b = add_node_last(head_b, 'B6')
    head_b = add_node_last(head_b, 'BR')
    head_b = add_node_first(head_b, 'BR')
    head_b = add_node_first(head_b, 'BR')
    head_b = add_node_first(head_b, 'BR')
    print(nodes_in_list(head_b))
    head_b = remove_models(head_b, 'BR')
    print(nodes_in_list(reverse(head_b)))
    print(nodes_in_list(head_b))
    head_c = add_node_last(None, 'C1')
    head_c = remove_first(head_c)
    head_c = add_node_first(head_c, 'C2')
    head_c = remove_last(head_c)
    head_c = add_node_first(head_c, 'C3')
    head_c = add_node_first(head_c, 'C4')
    head_c = remove_first(head_c)
    head_c = add_node_first(head_c, 'C5')
    head_c = add_node_first(head_c, 'C6')
    head_c = remove_last(head_c)
    head_c = add_node_first(head_c, 'C7')
    head_c = add_node_first(head_c, 'C8')
    head_c_3 = node_at(head_c, 2)
    print(nodes_in_list(head_c))
    print(nodes_in_list(head_c_3))
    print(nodes_in_list(reverse(head_c_3)))
    head_d = add_node_first(None, 'D1')
    for _ in range(10):
        head_d = add_node_first(head_d, 'D1')
    for _ in range(10):
        head_d = remove_first(head_d)
    print(nodes_in_list(head_d))
    for _ in range(10):
        head_d = remove_first(head_d)
    print(nodes_in_list(head_d))

if __name__ == '__main__':
    main()

