def dna_edit_process(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    dp = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    for i in range(len_seq1 + 1):
        dp[i][0] = i
    for j in range(len_seq2 + 1):
        dp[0][j] = j

    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1],
                                   dp[i - 1][j - 1])

    i = len_seq1
    j = len_seq2
    path = []
    while i > 0 and j > 0:
        current = dp[i][j]
        if seq1[i - 1] == seq2[j - 1]:
            i, j = i - 1, j - 1
        elif current == dp[i - 1][j - 1] + 1:
            path.append(f"{seq2[j - 1]}로 치환")
            i, j = i - 1, j - 1
        elif current == dp[i - 1][j] + 1:
            path.append(f"삭제")
            i -= 1
        elif current == dp[i][j - 1] + 1:
            path.append(f"{seq2[j - 1]}를 삽입")
            j -= 1

    while i > 0:
        path.append(f"삭제")
        i -= 1
    while j > 0:
        path.append(f"{seq2[j - 1]}를 삽입")
        j -= 1

    return dp[len_seq1][len_seq2], path[::-1]


def main():
    testcases = [
        ['CGAAACCG', 'GATGCCTG'],
        ['CCCAGCGTCGAAACCGCTGC', 'ACACGGATGCCTGTTATGAT'],
        ['CAGTCAGT', 'TGGTG'], 
        ['CAACCACAAC', 'C'], 
        ['C', 'CAACCACAAC'], 
        ['CTTA', ''],
        ['', 'CTTA'],
        ['AATGATGCTC', 'CTAGCTTCA']
    ]

    for i, testcase in enumerate(testcases):
        print(f'Testcase {i + 1} :')
        cost, path = dna_edit_process(testcase[0], testcase[1])
        path_str = ' -> '.join(path)
        print(f'  DNA 변형 비용: {cost}')
        print(f'  변형 방법: {path_str}')
        print()

if __name__ == "__main__":
    main()

    
