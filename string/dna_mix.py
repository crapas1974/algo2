import time
def execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"수행 시간: {end - start} 초")
        return result
    return wrapper

@execute_time
def is_pattern_mixed_td_wrapper(in_seq1, in_seq2, out_seq):
    return is_pattern_mixed_td(in_seq1, in_seq2, out_seq)

def is_pattern_mixed_td(in_seq1, in_seq2, out_seq):
    ins1_len = len(in_seq1)
    ins2_len = len(in_seq2)
    out_len = len(out_seq)
 
    # 만약 모든 문자열이 빈 문자열인 경우
    if (ins1_len == 0) and (ins2_len == 0) and (out_len == 0):
        return True
    # A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
    if (ins1_len + ins2_len) != out_len:
        return False
    case_in_seq1 = False
    case_in_seq2 = False
    # A의 첫글자와 C의 첫글자가 같은 경우
    if (ins1_len != 0) and (in_seq1[0] == out_seq[0]):
        case_in_seq1 = is_pattern_mixed_td(in_seq1[1:], in_seq2, out_seq[1:])
    # B의 첫글자와 C의 첫글자가 같은 경우
    if (ins2_len != 0) and (in_seq2[0] == out_seq[0]):
        case_in_seq2 = is_pattern_mixed_td(in_seq1, in_seq2[1:], out_seq[1:])

    return case_in_seq1 or case_in_seq2

@execute_time
def is_pattern_mixed_bu(in_seq1, in_seq2, out_seq):
   # 두 입력 시퀀스와 출력 시퀀스의 길이
   ins1_len = len(in_seq1)
   ins2_len = len(in_seq2)
   out_len = len(out_seq)

   # A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
   if out_len != ins1_len + ins2_len:
       return False

   # 시퀀스1의 i번째 글자까지의 부분 문자열과
   # 시퀀스2의 j번째 글자까지의 부분 문자열을 사용해
   # 조합된 시퀀스의 i + j 번째 글자 까지의 부분 문자열을
   # 조합할 수 있는지의 여부를 저장하는 2차원 배열
   mixseq = [[True] * (ins2_len + 1) for _ in range(0, ins1_len + 1)]

   # 첫번째 열을 채운다. 시퀀스1와 조합된 글자와 같을 때 까지는 T, 그 뒤로는 F
   for i in range(1, ins1_len + 1):
       if in_seq1[i - 1] != out_seq[i - 1]:
           mixseq[i][0] = False
       else:
           mixseq[i][0] = mixseq[i - 1][0]

   # 첫번째 행을 채운다. 시퀀스2와 조합된 글자와 같을 때 까지는 T, 그 뒤로는 F
   for j in range(1, ins2_len + 1):
       if in_seq2[j - 1] != out_seq[j - 1]:
           mixseq[0][j] = False
       else:
           mixseq[0][j] = mixseq[0][j - 1]
      
   # 나머지 셀을 채운다.
   # lc_from_i1/i2 는 last letter from in_seq1/in_seq2를 의미하며
   # ll_from_out은 last letter from out_seq를 의미한다.
   for i in range(1, ins1_len + 1):
       for j in range(1, ins2_len + 1):
           # i, j, i + j 번째 각각의 현재 글자들
           ll_from_i1 = in_seq1[i - 1]
           ll_from_i2 = in_seq2[j - 1]
           ll_from_out = out_seq[i + j - 1]
           # 조합 시퀀스의 현재 글자가 시퀀스 1의 현재 글자와만 같을 때
           # -> 조합 시퀀스와 시퀀스 1의 글자를 제외했을 때의 결과와 동일
           if (ll_from_i1 == ll_from_out) and (ll_from_i2 != ll_from_out):
               mixseq[i][j] = mixseq[i - 1][j]
           # 조합 시퀀스의 현재 글자가 시퀀스 2의 현재 글자와만 같을 때
           # -> 조합 시퀀스와 시퀀스 2의 글자를 제외했을 때의 결과와 동일
           elif (ll_from_i1 != ll_from_out) and (ll_from_i2 == ll_from_out):
               mixseq[i][j] = mixseq[i][j - 1]
           # 세 시퀀스의 현재 글자가 모두 같을 때 -> 모두 제외 했을 때의 결과와 동일
           elif (ll_from_i1 == ll_from_out) and (ll_from_i2 == ll_from_out):
               mixseq[i][j] = mixseq[i - 1][j] or mixseq[i][j - 1]
           else:
               mixseq[i][j] = False

   return mixseq[ins1_len][ins2_len]


def main():
    testcases = [('', 'CATG', 'CATG'), ('CATG', '', 'CATG'), ('TGACT', 'GAACACG', 'GTAAGACCTACG'), ('AGTACAAAATT', 'TTTAACT', 'TTATAAGCTTACAAAATT'), ('CGTAACTAAA', 'TTCTCAGGC', 'CGTTAACTTCACAAGGCAA'), ('ACCACGGTGAAGATTACTTCAGCACAGGCGACACCATGTCGGACGGGATGATATGTCTCTTTATTGTCCAGGGAGGCAGG', 'GTCGCCGGGCACGAGTAGCCTTACAGTTGCTCTTCCGCTAGATTCAGTCCCGGGCATCGTCTCATATTTGGTTACCATTG', 'AGCCTCAGCCCGGGCAGCGAGGTTGAAGAGATCCTTTACTACAGTTTCGAGCCATCAGGCGACCTTCCACCGACTTAGGTACTGTGCACGGGATAGGTACCCTATGTGCGTCTTTATTGGTCACTCCAGGGGAGTCTGCATCATAGTTGGGTTACCATTG'), ('ATGGCGCAGGGTAGATGGACACGATCCACGCATGGACTGGTACCTAATGTTGCTCGATCGCAACAGCTTCTGGCGCCAAG', 'GTGCCAAAGCCGTTAGTCCCGACACGCTACTACTATACTTGTCGCTTAAGGACTCGGAGGGGTAAATCAAGTTCGGTTTT', 'AGTTGGCGCCGACAAGGAGCCGGTTATGAATGTGGACCCGACACCACGGATCCACTACTCGCAATCTAGGACTACTGGTTACTGTCCTGAATCGTTAAGGATTGCTCTCCGGACGACGGGGCGTAAACAATCAGCATCAATGTGGTCCGCGCGAAGTTTT')]

    for i, tc in enumerate(testcases):
        print(f'TC {i + 1} : {is_pattern_mixed_td_wrapper(*tc)}')
        print(f'TC {i + 1} : {is_pattern_mixed_bu(*tc)}')


if __name__ == "__main__":
    main()