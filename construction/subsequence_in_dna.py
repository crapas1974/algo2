def dna_lcsb_sequence_bu(word1, word2):
    # 행렬 초기화
    lcsb = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    max_length = 0
    end_of_lcsb = []


    # 각 문자열에 대해 첫 글자부터 마지막 글자까지 반복
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # 일치하는 경우, 대각선 방향 작은 문제의 결과에서 1을 더함
            if word1[i - 1] == word2[j - 1]:
                lcsb[i][j] = lcsb[i - 1][j - 1] + 1
                # 최대 길이와 이 때 최장 공통 문자열의 끝 위치를 추가하거나, 갱신한다.
                if lcsb[i][j] == max_length:                   
                    end_of_lcsb.append(i)
                elif lcsb[i][j] > max_length:
                    max_length = lcsb[i][j]
                    end_of_lcsb = [i]
            else:
                lcsb[i][j] = 0  # 일치하지 않는 경우, 0으로 설정


    # 최장 공통 부분 문자열 추출
    lcsb_strs = []
    for end in end_of_lcsb:
        # 공통 부분 문자열이 중복되는 경우 저장하지 않는다.
        lcsb_str = word1[end - max_length:end]
        if lcsb_str not in lcsb_strs:
            lcsb_strs.append(lcsb_str)

    return lcsb_strs

def dna_lcs_td(word1, word2, memo = None):
    # 메모이제이션 딕셔너리 초기화
    if memo == None:
        memo = {}
    # 종료조건 : 두 문자열 중 빈 문자열이 있으면 0을 반환
    if word1 == '' or word2 == '':
        return 0
    # 메모이제이션 되어 있는 결과는 그대로 사용
    if (word1, word2) in memo:
        return memo[(word1, word2)]
    # 마지막 글자가 같을 때는 재귀 호출한 결과에 1을 더한다.
    if word1[-1] == word2[-1]:
        memo[(word1, word2)] = 1 + dna_lcs_td(word1[:-1], word2[:-1], memo)
    else:
        # 마지막 글자가 다르면 각 글자에서 마지막 글자를 뺀 양쪽의 경우를 재귀호출 하고 결과 중 최대값을 사용한다.
        memo[(word1, word2)] = max(dna_lcs_td(word1[:-1], word2, memo), dna_lcs_td(word1, word2[:-1], memo))


    return memo[(word1, word2)]

def dna_lcs_bu(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)
    # LCS를 저장할 배열을 생성한다.
    lcs = [[0] * (word2_length + 1) for _ in range(word1_length + 1)]
    # 두 문자열의 첫 번째 글자부터 한 글자씩 추가하면서 LCS를 계산한다.
    for i in range(word1_length):
        for j in range(word2_length):
            if word1[i] == word2[j]:    # 추가 후 마지막 글자가 같을 때
                lcs[i + 1][j + 1] = lcs[i][j] + 1
            else:                       # 추가 후 마지막 글자가 다를 때
                lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])


    return lcs[word1_length][word2_length]


def dna_lcs_sequence_bu(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)
    # LCS를 저장할 배열을 생성한다.
    lcs = [[0] * (word2_length + 1) for _ in range(word1_length + 1)]
    # 두 문자열의 첫 번째 글자부터 한 글자씩 추가하면서 LCS를 계산한다.
    for i in range(word1_length):
        for j in range(word2_length):
            if word1[i] == word2[j]:    # 추가 후 마지막 글자가 같을 때
                lcs[i + 1][j + 1] = lcs[i][j] + 1
            else:                       # 추가 후 마지막 글자가 다를 때
                lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])




    # lcs 배열을 역순으로 추적한다.
    lcs_str = ''
    i = len(word1)
    j = len(word2)
    while True:   
        # 둘 중 하나의 문자열이 비거나 lcs[i][j] = 0이면 종료   
        if i == 0 or j == 0 or lcs[i][j] == 0:
            break
        # 두 문자열의 마지막 글자를 빼도 값이 같다면 양쪽 글자 모두 LCS포함되지 않는다.
        if lcs[i][j] == lcs[i - 1][j - 1]:
            i -= 1
            j -= 1
        # 두 문자열의 마지막 글자 중 하나가 LCS이 되는 상황이므로, 같은 문자열이 될 때까지 이동한다.
        elif lcs[i][j] == lcs[i - 1][j]:
            i -= 1
        elif lcs[i][j] == lcs[i][j - 1]:
            j -= 1
        # 두 문자열의 마지막 글자가 같은 상황 - LCS의 앞 부분에 해당 글자를 추가한다.
        else:
            lcs_str = word1[i - 1] + lcs_str
            i -= 1
            j -= 1
    return lcs[word1_length][word2_length], lcs_str

def main():
    testcases = [['CCCAGCGTCGAAACCGCTGC', 'ACACGGATGCCTGTTATGAT'], ['CAACCACAAC', 'C'], ['AATGATGCTC', ''], ['TCTCTCATCAACAACGGGGTTGACCAAACGGGCAGTGTGGTGTTCAAAGCCGACTTATAGCCTACATGACTTAGCTTGCTATTACGTTGCATTTCCACGGAAACCCGAAAGCAGGGTCAGAGCCTCGCTGATCCACCCACTAACTATATCGCCCTTCCTCAGTCATGCTCCCGCGCAAAGAGGGGCTCTCAAGGTGTTCGTAGGTTGGCCGCCCTTGTGCTCTGAGGCCTAGTAAGAGGGTATCACGTTGCGCAGCAAGGCAAAGGGGCTACCGTGAACGCAGCTATGGGATGTGCAAAACGTGATGACTAGCGTCGCGTTAGTGCTTCCAGCATAAGTCCGAGCCAGGCCGCCTAGACATGGTTACTGTTGACTTGGTCCCCTTTTGTTAAGGTGCACAATCGACAACGGGTGGTCGGCCATCTCTTGCATAGGTCGGAGTTAAAGGACCGCGAACTGGCCCTCTACGTTTTTGTCACGCGGAGTGGCGCATTAAGATA', 'CCTACTTCTTAAGGCCGGTAGTGAAGTTCACAATATGTGTTTCTACCTATTACCCAAGGTGCGAGGGTTTTGATCGGGTGTGTTTTAGGCCTATTTAACTCCATCCGGCGAGTCACGTGGTCCGCTCATGTAGTGCTTACGGGGATCGGGTGGGGTAATAGTAGCGACGATTGTGCTTAGCCCGAGCGTGAAACTGCCAATATCGATGAACGATCTGAAATACACGTTGAATTGAAGCCGCTAGTGGTTCCATCGAATAGTCCTAGGGATGAATAGATATGGGGTTACAAAGAACCCACGGCTCAGGCTGGACATTAACAGCGAGTCGCTTCTACAGAGGGCGTTCATCAACGCGGGTTTAAGATATCCCATTGGGGTCGTGACGTGTCCTCGCCCAATGCGCGACTCGATCCATACGTAGACTATTACAACGGCGTGGAATCTTAAAATTCGAAGTATCGGGACCGGCGGACGCATGCGTAATTTGTCGCCTCGAGAGG'], ['GGTTCACTGGACACCTATCAAGGGAACTTGTTTCGGTGCTACATGATGTGCACTACTCCTATTACATTCGTTCTTCTTAAGAAACAACAGTGTTGCATGGCTATGACGGCCGTATAACTCCCCAGGTAGCTGAGGCATACAGGCTCGGAGGAGGGTCATGCATCATGTGTTGTCAAACCTGTCGTGTAGACAAGCTCCGGAGAGCGATGAGGTGGGGAAAGGCTAATGAAGGTTCTATTGTTTCTATATGGTGCGCCATAGATCTATGTTTTAGGGTCCGCACTACTCGCATATGCCCACTGGCAGAAATAGCAGGGCTTGCGGGCTAAATTCCCTGCACCGAAAACAGCCATCCCCCAGATCAGTGTCGATCGCACCTGCCAATTATTGACTTTCAGTGGCTAGATCAATCTTCGAAACCAAACATTTGCTACGACGGATCGGAGCTTGTTACTGCACGACAGACGGGGCACACTATGTCGGTTCCTTGCACCTCCGGAGTCAAGGCCTGGAAAATCGCAATTCGGACCGAGATAATATTCGATCGCCTACATAGAATTGAATCGTGATGACATCGTGGACCTTGACGCTACTACTTTA', 'TGGACGTGTGTAGCTTTATCGCCTTTCGACAAAAAAAACTCATTGGTCATGTACGTTCGACTCCTGGGTCACGCTTCATCTTGAGGTTCAAAATTAGTGTAGACCCTCTAGCAACTTCGCACATCTCTCCAGATCGGTTCCTATAAAATATGTGGCTTGGGATGAGGTGAAGCCGGGTGCCGGGTGCATGTGAATACGCTGATAATCCGGAGGGGCTATACCGGCGCAGCTACTCGCCAACGCACTCCTAGTCCCCTTGGGAGTTGAGGGCACCTGACGTGTGGTGACACAGTCGAGGTT']]
    for i, tc in enumerate(testcases):
        print(f"TC {i + 1} : ")
        # print(f"  가장 긴 공통 부분 순열의 길이 (하향식 접근법) : {dna_lcs_td(*tc)}")
        #print(f"  가장 긴 공통 부분 순열의 길이 (상향식 접근법) : {dna_lcs_bu(*tc)}")
#        dna_lcs_lenagh, dna_lcs = dna_lcs_sequence_bu(*tc)
#        print(f"  가장 긴 공통 부분 순열의 길이 (상향식 접근법) : {dna_lcs_lenagh}")
#        print(f"  가장 긴 공통 부분 순열 (상향식 접근법) : {dna_lcs}")
        dna_lcsb = dna_lcsb_sequence_bu(*tc)
        lcsb_length = 0
        for lcsb in dna_lcsb:
            lcsb_length = max(lcsb_length, len(lcsb))
        print(f"  가장 긴 공통 부분 문자열 (상향식 접근법) : {dna_lcsb}")
        print(f"  가장 긴 공통 부분 문자열의 길이 (상향식 접근법) : {lcsb_length}")        
        print(f"  가장 긴 공통 부분 문자열의 개수 (상향식 접근법) : {len(dna_lcsb)}")

        



if __name__ == "__main__":
    main()