from collections import deque
import random
import hashlib

def hash4(input):
    return hashlib.md5(input.encode()).hexdigest()[:4]

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

# def append_job_circular_queue(job, front, rear, job_waiting, maximum_waiting):
#     next_rear = (rear + 1) % maximum_waiting
#     if next_rear == front:
#         return rear
#     job_waiting[next_rear] = job
#     return next_rear

# def manage_job_with_maximum_waiting(job_list, minute_per_cycle, maximum_waiting):
#     job_segment = job_list.strip().split(',')
#     job_startings = {}
#     for i in range(len(job_segment) // 3):
#         name = job_segment[i * 3]
#         start = int(job_segment[i * 3 + 1])
#         cycle = int(job_segment[i * 3 + 2])
#         if start not in job_startings:
#             job_startings[start] = []
#         job_startings[start].append((name, cycle))
#     job_waiting = [('', -1) for _ in range(maximum_waiting)]
#     front = 0
#     rear = maximum_waiting - 1
#     total_cycle = 0
#     result = ''
#     ignored = 0
#     while True:
#         if total_cycle in job_startings:
#             for job in job_startings[total_cycle]:
#                 next_rear = append_job_circular_queue(job, front, rear, job_waiting, maximum_waiting)
#                 if rear != next_rear:
#                     rear = next_rear
#                 else:
#                     ignored += 1
#         if front == rear:
#             break
#         current_job = job_waiting[front]
#         front = (front + 1) % maximum_waiting
#         cycle_remain = current_job[1] - 1
#         if cycle_remain > 0:
#             rear = append_job_circular_queue((current_job[0], cycle_remain), front, rear, job_waiting, maximum_waiting)
#         if front <= rear:
#             result += ''.join(job_in_waitinglist[0] for job_in_waitinglist in job_waiting[front:rear])
#         else:
#             result += ''.join(job_in_waitinglist[0] for job_in_waitinglist in job_waiting[front:] + job_waiting[:rear])

#         total_cycle += 1
#     return total_cycle * minute_per_cycle, ignored, result


# def convert_num_to_name(num):
#     first = num // 36
#     second = num % 36
#     if first < 26:
#         first = chr(first + ord('A'))
#     else:
#         first = str(first - 26)
#     if second < 26:
#         second = chr(second + ord('A'))
#     else:
#         second = str(second - 26)
#     return first + second

# def make_virtual_schedule(num_of_job, max_cycle):
#     schedule = ''
#     for i in range(num_of_job):
#         job_name = convert_num_to_name(i)
#         start = random.randint(0, max_cycle // num_of_job)
#         cycle = random.randint(1, (max_cycle - start + 1) // num_of_job * 2 + 1)
#         schedule += job_name + ',' + str(start) + ',' + str(cycle) + ','
#     return schedule[:-1]


# schedule = 'A1,0,3,B1,0,1,C1,0,2,D1,3,1'
# print(manage_job(schedule, 10))
# for i in range(100):
#     schedule = make_virtual_schedule(99, 100)
#     schedule = 'ST,1,10,EN,2,5'
#     print(schedule)
#     t, w = manage_job(schedule, 10)
#     print(t)
#     print(w)
#     print(len(w))
def main():
    with open('scheduler_testcases.txt', 'r') as f:
        i = 0
        while True:
            tcline = f.readline()
            if not tcline or len(tcline.strip()) == 0:
                break
            caseline = f.readline()
            t, w = manage_job(caseline.strip(), 1)
            print(tcline.strip())
            print(f"    최초의 휴식 시간은 {t}분 후 입니다.")
            print(f"    각 사이클의 대기열을 이어붙인 결과의 간이 해시 값은 {hash4(w)} 입니다.")
            print()

if __name__ == '__main__':
    main()

