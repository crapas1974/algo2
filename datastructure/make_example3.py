import random
# 36 * 36 = 1296
def convert_num_to_name(num):
    first = num // 36
    second = num % 36
    if first < 26:
        first = chr(first + ord('A'))
    else:
        first = str(first - 26)
    if second < 26:
        second = chr(second + ord('A'))
    else:
        second = str(second - 26)
    return first + second

def make_virtual_schedule(num_of_job, max_cycle):
    schedule = ''
    for i in range(num_of_job):
        job_name = convert_num_to_name(i)
        start = random.randint(0, max_cycle)
        cycle = random.randint(1, max_cycle - start)
        schedule += job_name + ',' + str(start) + ',' + str(cycle) + ','
    return schedule[:-1]

