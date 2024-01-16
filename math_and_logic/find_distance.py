def distance(a, b):
    xor_result = a ^ b
    distance = 0
    while xor_result > 0:
        if xor_result & 3:
            distance += 1
        xor_result >>= 2
    return distance

def make_sequence_number(sequence):
    pb_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    number = 0
    for i in range(len(sequence)):
        number <<= 2
        number += pb_dict[sequence[i]]
    return number

def calculate_distance(sequence1, sequence2):
    return distance(make_sequence_number(sequence1), make_sequence_number(sequence2))

# 0 ~ 1 : 1
# 2 ~ 3 : 2
# 4 ~ 7 : 3
# 8 ~ 15 : 4
# given n, find k (if n == 12, k = 4)
# 2 ** k - 1 < n <= 2 ** (k + 1) - 1
# k = log2(n + 1)
def optimized_distance(a, b):
    # Perform XOR between a and b and count the number of 1s in every two bits
    xor_result = a ^ b
    distance = 0
    while xor_result > 0:
        distance += 1
        xor_result &= xor_result - 1
    return distance

    # xor_result = a ^ b
    # return bin(xor_result).count('1')

def optimized_make_sequence_number(sequence):
    pb_dict = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    binary_string = ''.join([pb_dict[nucleotide] for nucleotide in sequence])
    return int(binary_string, 2)

def optimized_calculate_distance(sequence1, sequence2):
    # Make the length of sequences equal by truncating the longer one
    min_length = min(len(sequence1), len(sequence2))
    sequence1 = sequence1[:min_length]
    sequence2 = sequence2[:min_length]

    return optimized_distance(optimized_make_sequence_number(sequence1), optimized_make_sequence_number(sequence2))



# make sequnce : O(n)
# distance : O(n)

def distance_by_pattern(sequence1, sequence2):
    distance = 0
    min_length = min(len(sequence1), len(sequence2))
    for i in range(min_length):
        if sequence1[i] != sequence2[i]:
            distance += 1
    distance += abs(len(sequence1) - len(sequence2))
    return distance
# distance_by_pattern : O(n)
    
import random
import time
def main():
    seq_num = 3
    seq_len = 5
    # make 1000 random sequence of length 50
    sequences = []
    for i in range(seq_num):
        sequences.append(''.join(random.choice('ACGT') for _ in range(seq_len)))
    print(sequences)
    distance1 = []
    distance2 = []
    start = time.time()
    for i in range(seq_num):
        for j in range(seq_num):
            distance1.append(distance_by_pattern(sequences[i], sequences[j]))
    print(time.time() - start)

    s_number = []
    start = time.time()
    for i in range(seq_num):
        s_number.append(make_sequence_number(sequences[i]))    
    for i in range(seq_num):
        for j in range(seq_num):
            distance2.append(distance(s_number[i], s_number[j]))
    print(time.time() - start)

    s_number2 = []
    distance3 = []
    start = time.time()
    for i in range(seq_num):
        s_number2.append(optimized_make_sequence_number(sequences[i]))
    for i in range(seq_num):
        for j in range(seq_num):
            distance3.append(optimized_distance(s_number2[i], s_number2[j]))
    print(time.time() - start)

    for i in range(seq_num):
        if distance3[i] != distance2[i]:
            print("error", i, distance3[i], distance2[i])
            break

    print(s_number)
    print(s_number2)
    print(distance1)
    print(distance3)
    # p1   = 'CTACGGATA'
    # p2_0 = 'ACCGTATGC'
    # p2_1 = 'CTACGGATG'
    # p2_2 = 'CTAGCGATA' 
    # p2_3 = 'CTACCTGTA'

    # p1n = make_sequence_number(p1)
    # p20n = make_sequence_number(p2_0)
    # p21n = make_sequence_number(p2_1)
    # p22n = make_sequence_number(p2_2)
    # p23n = make_sequence_number(p2_3)

    # print(distance(p1n, p20n))
    # print(distance(p1n, p21n))
    # print(distance(p1n, p22n))
    # print(distance(p1n, p23n))

if __name__ == "__main__":
    main()
          

