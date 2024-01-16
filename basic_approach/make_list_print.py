import random

def make_int_list(min, max, size, is_sort = False):
    arr = []
    for _ in range(size):
        arr.append(random.randint(min, max))
    
    sum_arr = sum(arr)
    avg = sum_arr / size
    if is_sort:
        arr.sort()
    print(f"리스트의 합은 {sum_arr}이고, 평균은 {avg}입니다.")
    print(f" 리스트 ")
    print(arr)

def make_ctag_list(min_length, max_length, min_size, max_size, is_sort = False):
    arr = []
    for _ in range(random.randint(min_size, max_size)):
        arr.append(''.join(random.choice('ACGT') for _ in range(random.randint(min_length, max_length))))
    if is_sort:
        arr.sort()
    print(f"리스트의 길이는 {len(arr)}입니다.")
    print(f"리스트 ")
    print(arr)

def make_tuple_for_meeting_list(size):
    startings = []
    endings = []
    for _ in range(size):
        hour = random.randint(9, 17)
        minute = random.randint(0, 5)
        startings.append(hour + minute / 10)
        while True:
            ending_hour = random.randint(9, 18)
            ending_minute = random.randint(0, 5)
            ending_time = ending_hour + ending_minute / 10
            if ending_time > 18:
                ending_time = 18
            if ending_time > startings[-1]:
                endings.append(ending_time)
                break
    print(list(zip(startings, endings)))
        

    
#make_int_list(0, 100, 100, True)
#make_ctag_list(60, 80, 1000, 1000, True)
#make_int_list(-30, 30, 1000)
#make_int_list(-1, 1, 2000)

make_tuple_for_meeting_list(100)

