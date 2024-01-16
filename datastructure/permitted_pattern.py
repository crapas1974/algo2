# pattern[0] : length
# pattern[1] : list of number for false purine
#              for example : pattern[2] = [1, 3] and length = 4
#              checking pattern 'XOXO' for checking O
# 0123 -> 2^(4 - 1), 2^(4 - 2), 2^(4 - 3), 2^(4 - 4)
# 2^(length 0 - 1), 2^(length - 1 - 1)
def by_bm(inputs, pattern):
    input_len = pattern[0]    
    mask = 0   
    for number in pattern[1]:
        mask += 2 ** (input_len - 1 - number)

    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        result = input_pattern & mask
        if result != 0:
            not_permitted_list.append(i)
    return not_permitted_list

def by_matching(inputs, pattern):
    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        n = inputs[i]
        jari = 0
        while n > 0:
            if n % 2 == 1:
                if pattern[0] - jari - 1 in pattern[1]:
                    not_permitted_list.append(i)
                    break
            n //= 2
            jari += 1
    return not_permitted_list
def by_bm3(inputs, pattern):
    input_len = pattern[0]    
    mask = pattern[1]
    # mask = 0   
    # for number in pattern[1]:
    #     mask += 2 ** (input_len - 1 - number)

    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        result = input_pattern & mask
        if result != 0:
            not_permitted_list.append(i)
    return not_permitted_list

def by_matching3(inputs, pattern):
    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        n = inputs[i]
        m = pattern[1]
        jari = 0
        while n > 0:
            if n % 2 == m % 2:
                not_permitted_list.append(i)
                break
            n //= 2
            m //= 2
            jari += 1
    return not_permitted_list



def by_bm2(inputs, pattern):
    input_len = pattern[0]    
    mask = 0   
    for c in pattern[1]:
        mask += 2 ** (input_len - 1 - int(c))
    #print(mask)

#    for number in pattern[1]:
#        mask += 2 ** (input_len - 1 - number)

    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        n = int(input_pattern, 2)
        result = n & mask
        if result != 0:
            not_permitted_list.append(i)
    return not_permitted_list

def by_matching2(inputs, pattern):
    not_permitted_list = []
    for i, input_pattern in enumerate(inputs):
        for i in range(len(input_pattern)):
            if input_pattern[i] == '1' and i in pattern[1]:
                not_permitted_list.append(i)
                break
        # n = inputs[i]
        # jari = 0
        # while n > 0:
        #     if n % 2 == 1:
        #         if pattern[0] - jari - 1 in pattern[1]:
        #             not_permitted_list.append(i)
        #             break
        #     n //= 2
        #     jari += 1
    return not_permitted_list


import random
def make_data(num_of_input, length):
    inputs = []
    for _ in range(num_of_input):
        inputs.append(random.randint(0, 2 ** length - 1))
    pattern = list(set([random.randint(0, length - 1) for _ in range(length // 2)]))
    return inputs, (length, pattern)

def make_data2(num_of_input, length):
    inputs = []
    for _ in range(num_of_input):
        input_pattern = ''
        for _ in range(length):
            input_pattern += str(random.randint(0, 1))
        inputs.append(input_pattern)
    pattern = ''
    for _ in range(length):
        pattern += str(random.randint(0, 1))
    return inputs, (length, pattern)

def make_data3(num_of_input, length):
    pattern = ''
    for _ in range(length):
        pattern += str(random.randint(0, 1))
    inputs = []
    for _ in range(num_of_input):
        input_pattern = pattern[:-1] + str(random.randint(0, 1))
        inputs.append(input_pattern)
    return inputs, (length, pattern)

def make_data4(num_of_input, length):
    inputs = []
    for _ in range(num_of_input):
        inputs.append(random.randint(0, 2 ** length - 1))
    
    pattern = random.randint(0, 2 ** length - 1)
    return inputs, (length, pattern)

import time
def main():
    inputs, pattern = make_data(10000, 100)
#    print(inputs)
#    print(pattern)

#    inputs = [i for i in range(16)]
#    pattern = (4, [2])
    start = time.time()
    r1 = by_bm(inputs, pattern)
    e1 = time.time()
    r2 = by_matching(inputs, pattern)
    e2 = time.time()
    print(e1 - start, e2 - e1)

    if r1 != r2:
        print("ERROR")

    # for i in range(16):
    #     print(f"{i:2} : {i:04b}")
if __name__ == '__main__':
    main()