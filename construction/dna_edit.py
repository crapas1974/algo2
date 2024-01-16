def dna_edit_cost_td(seq1, seq2, i = 0, j = 0, memo=None):
   # 메모이제이션 딕셔너리 초기화
   if memo is None:
       memo = {}


   # 메모에 저장되어 있는지 확인
   if (i, j) in memo:
       return memo[(i, j)]


   # 종료조건: 두 문자열 중 하나가 비었으면, 남은 문자열의 길이만큼 편집 거리에 추가
   if i == len(seq1):
       return len(seq2) - j
   if j == len(seq2):
       return len(seq1) - i


   # 같은 문자일 경우, 다음 글자로 이동
   if seq1[i] == seq2[j]:
       memo[(i, j)] = dna_edit_cost_td(seq1, seq2, i + 1, j + 1, memo)
       return memo[(i, j)]


   # 삽입, 삭제, 치환 비용 계산
   insert_cost = dna_edit_cost_td(seq1, seq2, i, j+1, memo)
   delete_cost = dna_edit_cost_td(seq1, seq2, i+1, j, memo)
   replace_cost = dna_edit_cost_td(seq1, seq2, i+1, j+1, memo)
   # 세 가지 비용중 최소값에 변형 비용 1을 더한 값을 메모이제이션하고 반환한다.
   memo[(i, j)] = 1 + min(insert_cost, delete_cost, replace_cost)


   return memo[(i, j)]

def dna_edit_cost_bu(seq1, seq2):
    # 두 문자열의 길이
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    # edit_distance 테이블 초기화: 각 셀은 두 문자열의 서브스트링에 대한 편집 거리를 저장
    edit_distance = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    # 초기화: 첫 번째 행과 열 설정
    for i in range(len_seq1 + 1):
        edit_distance[i][0] = i
    for j in range(len_seq2 + 1):
        edit_distance[0][j] = j

    # edit_distance 테이블 채우기
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
								# 문자가 같으면, 왼쪽 대각선 위의 값 가져오기
                edit_distance[i][j] = edit_distance[i - 1][j - 1]  
            else:
                edit_distance[i][j] = 1 + min(edit_distance[i - 1][j],  # 삭제
                                   edit_distance[i][j - 1],    # 삽입
                                   edit_distance[i - 1][j - 1]) # 교체


    # 변형 방법을 작성한다.
    
    i = len_seq1
    j = len_seq2
    path = []
    while i > 0 and j > 0:
        current = edit_distance[i][j]
        if seq1[i - 1] == seq2[j - 1]:   # 마지막 글자가 같아서 변형할 필요가 없는 경우
            i, j = i - 1, j - 1
        elif current == edit_distance[i - 1][j - 1] + 1:    # 치환
            path.append(f"'{seq1[i - 1]}'를 '{seq2[j - 1]}'로 치환")
            i, j = i - 1, j - 1
        elif current == edit_distance[i - 1][j] + 1:        # 삭제
            path.append(f"'{seq1[i - 1]}'를 삭제")
            i -= 1
        elif current == edit_distance[i][j - 1] + 1:        # 삽입
            path.append(f"'{seq2[j - 1]}'를 삽입")
            j -= 1

    while i > 0:
        path.append(f"'{seq1[i - 1]}'를 삭제")      # 앞 부분에 모자라는 만큼 삽입
        i -= 1
    while j > 0:
        path.append(f"'{seq2[j - 1]}'를 삽입")      # 앞 부분에 남는 만큼 삭제
        j -= 1

    return edit_distance[len_seq1][len_seq2], path[::-1] # 집어서 반환


def main():
    testcases = [['CATC', 'CGGT'], ['CAACCACAAC', 'C'], ['AATGATGCTC', ''], ['CCCAGCGTCGAAACCGCTGC', 'ACACGGATGCCTGTTATGAT'], ['TCTCTCATCAACAACGGGGTTGACCAAACGGGCAGTGTGGTGTTCAAAGCCGACTTATAGCCTACATGACTTAGCTTGCTATTACGTTGCATTTCCACGGAAACCCGAAAGCAGGGTCAGAGCCTCGCTGATCCACCCACTAACTATATCGCCCTTCCTCAGTCATGCTCCCGCGCAAAGAGGGGCTCTCAAGGTGTTCGTAGGTTGGCCGCCC', 'CCTACTTCTTAAGGCCGGTAGTGAAGTTCACAATATGTGTTTCTACCTATTACCCAAGGTGCGAGGGTTTTGATCGGGTGTGTTTTAGGCCTATTTAACTCCATCCGGCGAGTCACGTGGTCCGCTCATGTAGTGCTTACGGGGATCGGGTGGGGTAATAGTAGCGACGATTGTGCTTAGCCCGAGCGTGAAACTGCCAATATCGATGAACGATCTGAAATACACGTTGAATTGAAGCCGCTAGTGGTTCCATCGAATAGTCCTAGGGATGAATAGATATGGGGTTACAAAGAACCCACGGCTCAGGCTGGACATTAACAGCGAGTCGCTTCTACAGAGGGCGTTCATCAACGCGGGTTTAAGATATCCCATTGGGGTCGTGACGTGTCCTCGCCCAATGCGCGACTCGATCCATACGTAGACTATTACAACGGCGTGGAATCTTAAAATTCGAAGTATCGGGACCGGCGGACGCATGCGTAATTTGTCGCCTCGAGAGG'], ['GGTTCACTGGACACCTATCAAGGGAACTTGTTTCGGTGCTACATGATGTGCACTACTCCTATTACATTCGTTCTTCTTAAGAAACAACAGTGTTGCATGGCTATGACGGCCGTATAACTCCCCAGGTAGCTGAGGCATACAGGCTCGGAGGAGGGTCATGCATCATGTGTTGTCAAACCTGTCGTGTAGACAAGCTCCGGAGAGCGATGAGGTGGGGAAAGGCTAATGAAGGTTCTATTGTTTCTATATGGTGCGCCATAGATCTATGTTTTAGGGTCCGCACTACTCGCATATGCCCACTGGCAGAAATAGCAGGGCTTGCGGGCTAAATTCCCTGCACCGAAAACAGCCATCCCCCAGATCAGTGTCGATCGCACCTGCCAATTATTGACTTTCAGTGGCTAGATCAATCTTCGAAACCAAACATTTGCTACGACGGATCGGAGCTTGTTACTGCACGACAGACGGGGCACACTATGTCGGTTCCTTGCACCTCCGGAGTCAAGGCCTGGAAAATCGCAATTCGGACCGAGATAATATTCGATCGCCTACATAGAATTGAATCGTGATGACATCGTGGACCTTGACGCTACTACTTTA', 'TGGACGTGTGTAGCTTTATCGCCTTTCGACAAAAAAAACTCATTGGTCATGTACGTTCGACTCCTGGGTCACGCTTCATCTTGAGGTTCAAAATTAGTGTAGACCCTCTAGCAACTTCGCACATCTCTCCAGATCGGTTCCTATAAAATATGTGGCTTGGGATGAGGTGAAGCCGGGTGCCGGGTGCATGTGAATACGCTGATAATCCGGAGGGGCTATACCGGCGCAGCTACTCGCCAACGCACTCCTAGTCCCCTTGGGAGTTGAGGGCACCTGACGTGTGGTGACACAGTCGAGGTT']]
    for i, testcase in enumerate(testcases):
        print(f'TC {i + 1} :')
        print(f'  DNA 편집 비용: {dna_edit_cost_td(testcase[0], testcase[1])}')

    testcases = [['CATC', 'CGGT'], ['CAACCACAAC', 'C'], ['C', 'CAACCACAAC'], ['AATGATGCTC', ''], ['CCCAGCGTCGAAACCGCTGC', 'ACACGGATGCCTGTTATGAT']]
    for i, testcase in enumerate(testcases):
        print(f'TC {i + 1} :')
        cost, path = dna_edit_cost_bu(testcase[0], testcase[1])
        print(f'  DNA 편집 비용: {cost}')
        print(f'  편집 방법: {path}')
if __name__ == "__main__":
    main()