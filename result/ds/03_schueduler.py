from collections import deque
import hashlib

class Queue:
    def __init__(self):
        self.queue = []

    # 시간 복잡도 : O(1)
    def push(self, item):
        self.queue.append(item)

    # 시간 복잡도 : O(n)
    def pop(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def q2str(self):
        return ''.join(job for job, _ in self.queue)        

def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]

def manage_job_with_qclass(job_list, minute_per_cycle):
    job_segment = job_list.strip().split(',')
    job_startings = {}
    for i in range(len(job_segment) // 3):
        name = job_segment[i * 3]
        start = int(job_segment[i * 3 + 1])
        cycle = int(job_segment[i * 3 + 2])
        if start not in job_startings:
            job_startings[start] = []
        job_startings[start].append((name, cycle))
    job_waiting = Queue()
    total_cycle = 0
    result = ''
    while True:        
        if total_cycle in job_startings:
            for job in job_startings[total_cycle]:
                job_waiting.push(job)
        if job_waiting.size() == 0:
            break
        job = job_waiting.pop()
        cycle_remain = job[1] - 1
        if cycle_remain > 0:
            job_waiting.push((job[0], cycle_remain))
        result += job_waiting.q2str()
        total_cycle += 1
    return total_cycle * minute_per_cycle, result


def manage_job(job_list, minute_per_cycle):
    job_segment = job_list.strip().split(',')
    job_startings = {}
    for i in range(len(job_segment) // 3):
        name = job_segment[i * 3]
        start = int(job_segment[i * 3 + 1])
        cycle = int(job_segment[i * 3 + 2])
        if start not in job_startings:
            job_startings[start] = []
        job_startings[start].append((name, cycle))
    job_waiting = deque()
    total_cycle = 0
    result = ''
    while True:        
        if total_cycle in job_startings:
            for job in job_startings[total_cycle]:
                job_waiting.append(job)
        if len(job_waiting) == 0:
            break
        job = job_waiting.popleft()
        cycle_remain = job[1] - 1
        if cycle_remain > 0:
            job_waiting.append((job[0], cycle_remain))
        result += ''.join(job_in_waitinglist[0] for job_in_waitinglist in job_waiting)
        total_cycle += 1
    return total_cycle * minute_per_cycle, result

def main():
    with open('scheduler_testcases.txt', 'r') as f:
        i = 0
        while True:
            tcline = f.readline()
            if not tcline or len(tcline.strip()) == 0:
                break
            caseline = f.readline()
            t, w = manage_job(caseline.strip(), 10)
            # Queue class를 사용해서 구현한 함수
            # t, w = manage_job_with_qclass(caseline.strip(), 10)
            print(tcline.strip())
            print(f"    최초의 휴식 시간은 {t}분 후 입니다.")
            print(f"    각 사이클의 대기열을 이어붙인 결과의 간이 해시 값은 {hash4(w)} 입니다.")
            print()


if __name__ == '__main__':
    main()

