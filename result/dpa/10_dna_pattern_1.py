def find_lap(input_seq):
    if not input_seq:
        return ''

    dp = [1] * len(input_seq)
    prev = [-1] * len(input_seq)

    max_len = 0
    max_index = 0

    for i in range(1, len(input_seq)):
        for j in range(i):
            if input_seq[j] <= input_seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_index = i

    longest_ascending_pattern = ''
    while max_index != -1:
        longest_ascending_pattern += input_seq[max_index]
        max_index = prev[max_index]
    return longest_ascending_pattern[::-1]    

def main():

    testcases = [
        'CTAGTACG', 
        'CTAGGTACG', 
        'AAA', 
        'ACGT', 
        'TGCA', 
        'ACTTTTTTTCGGGGGGT', 
        'ACTTTTTCT', 
        'ACTTTTTCGGGT', 
        'ACTTTTTCGGGGGGTTTTTT', 
        'GCCTGCTGGT', 
        'CCCATCTTCCGTCATTATAG', 
        'ACCAAGAAACTGTAATCTCCTTCTTCTCGA', 
        'TCCGTTCGGCATACCCCCCGGCGGGGATATCGAACTGGAG', 
        'GTCCGAGGGGCAAGCAAGCGGGTTGACGCATCCTGAAGCTCTTTCACAGG', 
        'ATGGGTGAAAACCCCCATTAACATAACTGGCGCCGGGAGTTACGAATCTCGTGCTTGAAGAAGGGCAAACTGTTTTACGAGAGGTGGGGACAGACTACCT', 
        'CAATCATCTGGCCTCCAATTAAGACTTTATGCTGCTGCTAGCCAGAAATTTATTGACCACCACGGATGCGACGGCTCGACGCTGATGGTGTGACGTTGCAAAAGCTGGTCTATGGCTTGGTTTAGTGGTGGCCATGGACCCCTCACTCGTAATTTGTAAATGTAATAATAGGCGCCAAATTCAGTGTCTGATGCTGGTTCCCCAGCTGTCTCTTGCAAGTCGGCGCCAATCGTTTTCCACGGAACGACTTGTCTGCGGCCTATGCATCGTTCGCTAGCCAGTTAAATGGCATATGCTAGTTCACCTAACCACTTCAAAGTATCAGCCCAAGGATTTTCACCAGGTAGGGAAATTATTAGGATCGCTAAGCAACCCACTGTCCGATACGACAGCCCGCTGCCAGCGTTTCATTATAGTCTTGGAATACCGTTCCGTTGTTTTCAAACCGTTCCAACCCCCCTGATGCGCCAGCGTCTAGGTTTGTCGGCGCTAGTGGCCACCAGCGCGTGCCATACACGCGGTGTTGGCCTAATCAGTTGCTAAGTACCTAGAACGACAGCTAACCGAAAGAGAAAACATCGAGCTTTTACGTAATTTCTACACTATACGCCCTGGACGACATACTAGTCTGCGTTTGGTCTATATCTATATGTTCACTCCGAAGCTCTCAGATCTGATACAGACACATGAGGGTCTTGTAGCATTCCTAGAGCTTCTATACGCGTGGTTCGCCGGCCAGGATATGGGTCACACGGGTACATTCAACTCCTACTACGAGAGGGGGTGTTTAAACTATCCGTAAAGCCACAGTAATCGAGATTTACCCATAGGCGACCGATCAAATCGTCTATGGACAGAAGTGGCTCCGCCCGCGAAGCTAACATAAGGTCCAATTACATTGTTACCTAAGCTCTTGTACTAAAATCTAGTGATCATAATCCCGGCCCCGTTATCGCCACCATGGCAATATTTGAACGCGCCCTCGTAGAGCTCATAAGGA'
    ]

    for i, tc in enumerate(testcases):
        print(f"Testcase {i + 1}")
        longest_ascending_pattern = find_lap(tc)
        length_of_lap = len(longest_ascending_pattern)
        print(f"    가장 긴 오름차순 부분 순열의 길이 : {length_of_lap}")
        print(f"    가장 긴 오름차순 부분 순열 중 하나 : {longest_ascending_pattern}")
        print()

if __name__ == '__main__':
    main()
