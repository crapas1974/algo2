import time

def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"    실행 시간: {time.time() - start} sec")
        return result
    return wrapper

def remove_rival_list(n, k):
    virus = [True] * n
    count = n
    cur = 0
    while count > 1:
        i = 0
        while i < k:
            if virus[cur]:
                i += 1
            cur = (cur + 1) % n
        virus[(cur - 1) % n] = False
        count -= 1
    for i in range(n):
        if virus[i]:
            return i + 1


def remove_rival_recursive(n, k):
    if n == 1:
        return 0
    else:
        return (remove_rival_recursive(n - 1, k) + k) % n

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_circular_linked_list(n):
    head = Node(1)
    prev = head
    for i in range(2, n + 1):
        new_node = Node(i)
        prev.next = new_node
        prev = new_node
    prev.next = head  # 마지막 노드가 첫 번째 노드를 가리키도록 설정
    return head

@execute_time
def remove_rival_fast(n, k):
    if k == 1:
        return n
    head = create_circular_linked_list(n)
    prev = None
    curr = head

    while curr.next != curr:
        for _ in range(k - 1):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr = curr.next

    return curr.data


def main():
    testcases = [(7, 3), (15, 5), (1, 10), (10, 1), (15, 5), (5, 15), (30, 30), (1000, 1), (1000, 39), (100000, 100), (100000, 333), (100000, 1000)]
    for i, (n, k) in enumerate(testcases):
        print(f"Testcase {i + 1}")
        last_virus = remove_rival_fast(n, k)
        print(f"    winner : {last_virus}")
        print()

if __name__ == "__main__":
    main()