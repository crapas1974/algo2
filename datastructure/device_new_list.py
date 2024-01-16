
class Device:
    def __init__(self, model_name):
        self.model_name = model_name
        self.next = None
        self.before = None

def add_node_first(head: Device, model_name: str) -> Device:    
    new_node = Device(model_name)
    if head == None:
        return new_node
    head.before = new_node
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
            new_node.before = cur
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
            new_node.before = cur
            cur.next = new_node
            if new_node.next != None:
                new_node.next.before = new_node
            break
        if cur.next == None:
            cur.next = new_node
            new_node.before = cur
            break
        cur = cur.next
    return head

def remove_first(head: Device) -> Device:
    if head == None:
        return None
    if head.next == None:
        return None
    head.next.before = None
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
            if cur.next != None:
                cur.next.before = cur
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

def before_node(after_node: Device) -> Device:
    if after_node == None:
        return None
    return after_node.before

def remove_node(target: Device) -> (bool, Device):
    if target == None:
        return False, None
    if target.before == None:
        if target.next == None:
            return True, None
        target.next.before = None
        return True, target.next
    if target.next == None:
        target.before.next = None
        return False, None
    target.before.next = target.next
    target.next.before = target.before
    return False, None

def reverse_all(node: Device) -> Device:
    head = Device(node.model_name)
    cur = node.next
    while cur != None:
        head = add_node_first(head, cur.model_name)
        cur = cur.next
    cur = node.before
    while cur != None:
        head = add_node_last(head, cur.model_name)
        cur = cur.before
    return head

import hashlib

def hash4(input: str) -> str:
    return hashlib.md5(input.encode()).hexdigest()[:4]



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
    head = add_node_last(None, 'Z1')
    _, head = remove_node(head)
    result.append(nodes_in_list(head))
    head = add_node_last(None, 'Z1')
    head = add_node_last(head, 'Z2')
    head = add_node_last(head, 'Z3')
    head = add_node_last(head, 'Z4')
    _, head = remove_node(head)
    result.append(nodes_in_list(head))
    head = add_node_last(None, 'Z1')
    head = add_node_last(head, 'Z2')
    head = add_node_last(head, 'Z3')
    head = add_node_last(head, 'Z4')
    will_remove_node = node_at(head, 2)
    remove_node(will_remove_node)
    result.append(nodes_in_list(head))
    will_remove_node = node_at(head, 2)
    remove_node(will_remove_node)
    result.append(nodes_in_list(head))
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
    new_head = before_node(node_at(head, 99))
    result.append(nodes_in_list(reverse(new_head)))
    
    for result in result:
        print(hash4(result), result[:20])   

    head = add_node_last(None, 'M1')
    head = add_node_last(head, 'M2')
    head = add_node_last(head, 'M3')
    head = add_node_last(head, 'M4')
    head = add_node_last(head, 'M5')
    node3 = node_at(head, 2)
    print(nodes_in_list(reverse_all(node3)))
    print(nodes_in_list(head))

if __name__ == '__main__':
    main()

