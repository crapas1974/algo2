class Device:
    def __init__(self, model_name: str, next=None):
        self.model_name = model_name
        self.next = next

def detect_cycle_start(head):
    if not head or not head.next:
        return None

    # 순환 감지
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 순환 감지
            break

    if not fast or not fast.next:
        return None  # 순환 없음

    # 순환 시작점 찾기
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # 순환 시작 노드

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

def node_at(head: Device, idx: int) -> Device:
    cur = head
    for _ in range(idx):
        cur = cur.next
    return cur
# # 예제 리스트 생성
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = head.next  # 순환 생성: 2에서 시작

# # 순환 시작 노드 찾기
# cycle_start = detect_cycle_start(head)
# if cycle_start:
#     print(f"Cycle starts at node with value: {cycle_start.value}")
# else:
#     print("No cycle found")
def make_random_list(size: int) -> Device:
    head = None
    for i in range(size):
#        head = add_node_last(head, random.choice(['A', 'B', 'C', 'D']))
        head = add_node_last(head, f"{i}")
    return head


def main():
    head = make_random_list(1000)
    node_500 = node_at(head, 500)
    last = node_500
    node_50 = node_at(head, 50)    
    node_500.next = node_50
    cycle_start = node_50
    print("---1")
    print(head.model_name)
    print(last.model_name)
    print(cycle_start.model_name)
    detected_cycle_start = detect_cycle_start(head)
    print(detected_cycle_start.model_name)
    print("---2")

    head2 = make_random_list(1000)
    last2 = node_at(head2, 999)
    print(head2.model_name)
    print(last2.model_name)

    print("---3")
    head3 = make_random_list(2000)
    last3 = node_at(head3, 1999)
    last3.next = head3
    cycle_start3 = head3
    detected_cycle_start3 = detect_cycle_start(head3)
    print(head3.model_name)
    print(last3.model_name)
    print(cycle_start3.model_name)
    print(detected_cycle_start3.model_name)

if __name__ == '__main__':
    main()