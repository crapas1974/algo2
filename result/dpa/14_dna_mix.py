import time
def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간 - {end - start} 초")
        return result
    return wrapper

@execute_time
def is_pattern_mixed_topdown_wrapper(in_seq1, in_seq2, out_seq):
    return is_pattern_mixed_topdown(in_seq1, in_seq2, out_seq)

def is_pattern_mixed_topdown(in_seq1, in_seq2, out_seq):
    ins1_len = len(in_seq1)
    ins2_len = len(in_seq2)
    out_len = len(out_seq)
    if (ins1_len == 0) and (ins2_len == 0) and (out_len == 0):
        return True
    if (ins1_len + ins2_len) != out_len:
        return False
    case_in_seq1 = False
    case_in_seq2 = False
    if (ins1_len != 0) and (in_seq1[0] == out_seq[0]):
        case_in_seq1 = is_pattern_mixed_topdown(in_seq1[1:], in_seq2, out_seq[1:])
    if (ins2_len != 0) and (in_seq2[0] == out_seq[0]):
        case_in_seq2 = is_pattern_mixed_topdown(in_seq1, in_seq2[1:], out_seq[1:])

    return case_in_seq1 or case_in_seq2

@execute_time
def is_pattern_mixed_bottomup(in_seq1, in_seq2, out_seq):
   ins1_len = len(in_seq1)
   ins2_len = len(in_seq2)
   out_len = len(out_seq)

   if out_len != ins1_len + ins2_len:
       return False

   mixseq = [[True] * (ins2_len + 1) for _ in range(0, ins1_len + 1)]

   for i in range(1, ins1_len + 1):
       if in_seq1[i - 1] != out_seq[i - 1]:
           mixseq[i][0] = False
       else:
           mixseq[i][0] = mixseq[i - 1][0]

   for j in range(1, ins2_len + 1):
       if in_seq2[j - 1] != out_seq[j - 1]:
           mixseq[0][j] = False
       else:
           mixseq[0][j] = mixseq[0][j - 1]
      
   for i in range(1, ins1_len + 1):
       for j in range(1, ins2_len + 1):
           ll_from_i1 = in_seq1[i - 1]
           ll_from_i2 = in_seq2[j - 1]
           ll_from_out = out_seq[i + j - 1]
           if (ll_from_i1 == ll_from_out) and (ll_from_i2 != ll_from_out):
               mixseq[i][j] = mixseq[i - 1][j]
           elif (ll_from_i1 != ll_from_out) and (ll_from_i2 == ll_from_out):
               mixseq[i][j] = mixseq[i][j - 1]
           elif (ll_from_i1 == ll_from_out) and (ll_from_i2 == ll_from_out):
               mixseq[i][j] = mixseq[i - 1][j] or mixseq[i][j - 1]
           else:
               mixseq[i][j] = False

   return mixseq[ins1_len][ins2_len]


def main():
    testcases = [
        ('CT', 'AG', 'ACTG'), 
        ('CT', 'AG', 'CGAT'), 
        ('', 'CATG', 'CATG'), 
        ('CATG', '', 'CATG'), 
        ('TGACT', 'GAACACG', 'GTAAGACCTACG'), 
        ('AGTACAAAATT', 'TTTAACT', 'TTATAAGCTTACAAAATT'), 
        ('CGTAACTAAA', 'TTCTCAGGC', 'CGTTAACTTCACAAGGCAA'), 
        ('ACCACGGTGAAGATTACTTCAGCACAGGCGACACCATGTCGGACGGGATGATATGTCTCTTTATTGTCCAGGGAGGCAGG', 'GTCGCCGGGCACGAGTAGCCTTACAGTTGCTCTTCCGCTAGATTCAGTCCCGGGCATCGTCTCATATTTGGTTACCATTG', 'AGCCTCAGCCCGGGCAGCGAGGTTGAAGAGATCCTTTACTACAGTTTCGAGCCATCAGGCGACCTTCCACCGACTTAGGTACTGTGCACGGGATAGGTACCCTATGTGCGTCTTTATTGGTCACTCCAGGGGAGTCTGCATCATAGTTGGGTTACCATTG'), 
        ('ATGGCGCAGGGTAGATGGACACGATCCACGCATGGACTGGTACCTAATGTTGCTCGATCGCAACAGCTTCTGGCGCCAAG', 'GTGCCAAAGCCGTTAGTCCCGACACGCTACTACTATACTTGTCGCTTAAGGACTCGGAGGGGTAAATCAAGTTCGGTTTT', 'AGTTGGCGCCGACAAGGAGCCGGTTATGAATGTGGACCCGACACCACGGATCCACTACTCGCAATCTAGGACTACTGGTTACTGTCCTGAATCGTTAAGGATTGCTCTCCGGACGACGGGGCGTAAACAATCAGCATCAATGTGGTCCGCGCGAAGTTTT')
    ]

    for i, tc in enumerate(testcases):
        print(f'Testcase {i + 1}')
        print(f"    하향식 접근법 : ", end = '')
        print(f"        {'정상적으로 생성' if is_pattern_mixed_topdown_wrapper(*tc) else '비정상으로 생성'}")
        print(f"    상향식 접근법 : ", end = '')
        print(f"        {'정상적으로 생성' if is_pattern_mixed_bottomup(*tc) else '비정상으로 생성'}")
        print()

if __name__ == "__main__":
    main()