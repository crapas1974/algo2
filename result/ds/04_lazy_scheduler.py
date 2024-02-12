import hashlib

def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]

def append_job_circular_queue(job, front, rear, job_waiting, maximum_waiting):
    if (rear + 1) % maximum_waiting == front:
        return front, rear
    if front == -1:
        front = 0
        rear = 0
        job_waiting[rear] = job
    else:
        rear = (rear + 1) % maximum_waiting
        job_waiting[rear] = job
    return front, rear

def pop_job_circular_queue(front, rear, job_waiting, maximum_waiting):
    if front == -1:
        return front, rear, None
    if front == rear:
        return -1, -1, job_waiting[front]
    return (front + 1) % maximum_waiting, rear, job_waiting[front]

def manage_job_with_maximum_waiting(job_list, minute_per_cycle, maximum_waiting):
    job_segment = job_list.strip().split(',')
    job_startings = {}
    for i in range(len(job_segment) // 3):
        name = job_segment[i * 3]
        start = int(job_segment[i * 3 + 1])
        cycle = int(job_segment[i * 3 + 2])
        if start not in job_startings:
            job_startings[start] = []
        job_startings[start].append((name, cycle))
    job_waiting = [('', -1) for _ in range(maximum_waiting)]
    front = -1
    rear = -1
    total_cycle = 0
    result = ''
    ignored = 0
    while True:
        if total_cycle in job_startings:
            for job in job_startings[total_cycle]:
                next_front, next_rear = append_job_circular_queue(job, front, rear, job_waiting, maximum_waiting)
                if rear != next_rear:
                    front = next_front
                    rear = next_rear
                else:
                    ignored += 1
        if front == -1:
            break
        
        front, rear, current_job = pop_job_circular_queue(front, rear, job_waiting, maximum_waiting)
        cycle_remain = current_job[1] - 1        
        if cycle_remain > 0:
            front, rear = append_job_circular_queue((current_job[0], cycle_remain), front, rear, job_waiting, maximum_waiting)
  
        if front <= rear:
            result += ''.join(job_in_waitinglist[0] for job_in_waitinglist in job_waiting[front:rear + 1])
        else:
            result += ''.join(job_in_waitinglist[0] for job_in_waitinglist in job_waiting[front:] + job_waiting[:rear + 1])
        total_cycle += 1
    return total_cycle * minute_per_cycle, ignored, result

def main():
    with open('scheduler_testcases.txt', 'r') as f:
        i = 0
        while True:
            i += 1
            if i == 1:
                maximum_job = 2
            else:
                maximum_job = i
            
            tcline = f.readline()
            if not tcline or len(tcline.strip()) == 0:
                break
            caseline = f.readline()
            t, ignore, w = manage_job_with_maximum_waiting(caseline.strip(), 10, maximum_job)
            print(tcline.strip())
            print(f"    최초의 휴식 시간은 {t}분 후 입니다.")
            print(f"    무시된 작업은 {ignore}개 입니다.")
            print(f"    각 사이클의 대기열을 이어붙인 결과의 간이 해시 값은 {hash4(w)} 입니다.")
            print()
    


if __name__ == '__main__':
    main()
