class Device:
    def __init__(self, model_name: str):
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
    list1_head = make_list_with_size(1000, 'A')
    cur = list1_head
    cycle_start1 = None
    for i in range(500):
        if i == 50:
            cycle_start1 = cur
        cur = cur.next
    cur.next = cycle_start1

    list2_head = make_list_with_size(1000, 'B')
    cycle_start2 = None

    list3_head = make_list_with_size(1000, 'C')
    cycle_start3 = list3_head

    cur = list3_head
    while cur.next:
        cur = cur.next
    cur.next = list3_head
    
    cycle1, before1 = find_cycle(list1_head)
    cycle2, before2 = find_cycle(list2_head)
    cycle3, before3 = find_cycle(list3_head)

    head4 = Device('D0')
    head4.next = head4
    cycle4, before4 = find_cycle(head4)
    
    if cycle1:
        print(cycle1.model_name)
        print(cycle_start1.model_name)
        print(before1.model_name)
    else:
        print("no cycle")
    if cycle2:
        print(cycle2.model_name)
        print(cycle_start2.model_name)
        print(before2.model_name)
    else:
        print("no cycle")
    if cycle3:
        print(cycle3.model_name)
        print(cycle_start3.model_name)
        print(before3.model_name)
    else:
        print("no cycle")

    print(cycle4.model_name)
    print(before4.model_name)


    # cycle = find_cycle(head)
    # cycle2 = find_cycle(head2)
    # cycle3 = find_cycle(head3)
    # print(head3.model_name)
    # print(cycle3.model_name)
    # print(cycle3.next.model_name)
    # print(head3.model_name)
    # print(cycle)
    # print(last.next)
    # print(cycle3)
    # print(last3.next)
    
    #list1_json = make_json_from_list(head)
    #print(list1_json)
    # lists = [head, head2, head3]
    # with open('data.pickle', 'wb') as f:
    #     pickle.dump(lists, f)
    # with open('data.pickle', 'rb') as f:
    #     lists2 = pickle.load(f)
    # print(lists[0].model_name)
    # print(lists[1].model_name)
    # print(lists[2].model_name)
    # print(lists2[0].model_name)
    # print(lists2[1].model_name)
    # print(lists2[2].model_name)





if __name__ == "__main__":
    main()
