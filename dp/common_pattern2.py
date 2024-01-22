def dna_longgest_shared_pattern(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)
    
    dp = [[0] * (word2_length + 1) for _ in range(word1_length + 1)]
    # 두 문자열의 첫 번째 글자부터 한 글자씩 추가하면서 dp를 계산한다.
    for i in range(word1_length):
        for j in range(word2_length):
            if word1[i] == word2[j]:    # 추가 후 마지막 글자가 같을 때
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:                       # 추가 후 마지막 글자가 다를 때
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # dp 배열을 역순으로 추적한다.
    longest_shared_pattern = ''
    i = len(word1)
    j = len(word2)
    while True:   
        # 둘 중 하나의 문자열이 비거나 dp[i][j] = 0이면 종료   
        if i == 0 or j == 0 or dp[i][j] == 0:
            break
        # 두 문자열의 마지막 글자를 빼도 값이 같다면 양쪽 글자 모두 최장 공통부분문자열에 포함되지 않는다.
        if dp[i][j] == dp[i - 1][j - 1]:
            i -= 1
            j -= 1
        # 두 문자열의 마지막 글자 중 하나가 최장 공통부분문자열이 되는 상황이므로, 같은 문자열이 될 때까지 이동한다.
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        # 두 문자열의 마지막 글자가 같은 상황 - 최장 공통부분문자열의 앞 부분에 해당 글자를 추가한다.
        else:
            longest_shared_pattern = word1[i - 1] + longest_shared_pattern
            i -= 1
            j -= 1
    return longest_shared_pattern


def dna_longgest_shared_pattern_length(word1, word2):
    word1_length = len(word1)
    word2_length = len(word2)
    dp = [[0] * (word2_length + 1) for _ in range(word1_length + 1)]
    for i in range(word1_length):
        for j in range(word2_length):
            if word1[i] == word2[j]:    # 추가 후 마지막 글자가 같을 때
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:                       # 추가 후 마지막 글자가 다를 때
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[word1_length][word2_length]



def main():
    testcases = [('CTAC', 'CACG'), ('CCCAGCGTCGAAACCGCTGC', 'ACACGGATGCCTGTTATGAT'), ('CAACCACAAC', 'C'), ('AATGATGCTC', ''), ('TCTCTCATCAACAACGGGGTTGACCAAACGGGCAGTGTGGTGTTCAAAGCCGACTTATAGCCTACATGACTTAGCTTGCTATTACGTTGCATTTCCACGGAAACCCGAAAGCAGGGTCAGAGCCTCGCTGATCCACCCACTAACTATATCGCCCTTCCTCAGTCATGCTCCCGCGCAAAGAGGGGCTCTCAAGGTGTTCGTAGGTTGGCCGCCCTTGTGCTCTGAGGCCTAGTAAGAGGGTATCACGTTGCGCAGCAAGGCAAAGGGGCTACCGTGAACGCAGCTATGGGATGTGCAAAACGTGATGACTAGCGTCGCGTTAGTGCTTCCAGCATAAGTCCGAGCCAGGCCGCCTAGACATGGTTACTGTTGACTTGGTCCCCTTTTGTTAAGGTGCACAATCGACAACGGGTGGTCGGCCATCTCTTGCATAGGTCGGAGTTAAAGGACCGCGAACTGGCCCTCTACGTTTTTGTCACGCGGAGTGGCGCATTAAGATA', 'CCTACTTCTTAAGGCCGGTAGTGAAGTTCACAATATGTGTTTCTACCTATTACCCAAGGTGCGAGGGTTTTGATCGGGTGTGTTTTAGGCCTATTTAACTCCATCCGGCGAGTCACGTGGTCCGCTCATGTAGTGCTTACGGGGATCGGGTGGGGTAATAGTAGCGACGATTGTGCTTAGCCCGAGCGTGAAACTGCCAATATCGATGAACGATCTGAAATACACGTTGAATTGAAGCCGCTAGTGGTTCCATCGAATAGTCCTAGGGATGAATAGATATGGGGTTACAAAGAACCCACGGCTCAGGCTGGACATTAACAGCGAGTCGCTTCTACAGAGGGCGTTCATCAACGCGGGTTTAAGATATCCCATTGGGGTCGTGACGTGTCCTCGCCCAATGCGCGACTCGATCCATACGTAGACTATTACAACGGCGTGGAATCTTAAAATTCGAAGTATCGGGACCGGCGGACGCATGCGTAATTTGTCGCCTCGAGAGG'), ('GGTTCACTGGACACCTATCAAGGGAACTTGTTTCGGTGCTACATGATGTGCACTACTCCTATTACATTCGTTCTTCTTAAGAAACAACAGTGTTGCATGGCTATGACGGCCGTATAACTCCCCAGGTAGCTGAGGCATACAGGCTCGGAGGAGGGTCATGCATCATGTGTTGTCAAACCTGTCGTGTAGACAAGCTCCGGAGAGCGATGAGGTGGGGAAAGGCTAATGAAGGTTCTATTGTTTCTATATGGTGCGCCATAGATCTATGTTTTAGGGTCCGCACTACTCGCATATGCCCACTGGCAGAAATAGCAGGGCTTGCGGGCTAAATTCCCTGCACCGAAAACAGCCATCCCCCAGATCAGTGTCGATCGCACCTGCCAATTATTGACTTTCAGTGGCTAGATCAATCTTCGAAACCAAACATTTGCTACGACGGATCGGAGCTTGTTACTGCACGACAGACGGGGCACACTATGTCGGTTCCTTGCACCTCCGGAGTCAAGGCCTGGAAAATCGCAATTCGGACCGAGATAATATTCGATCGCCTACATAGAATTGAATCGTGATGACATCGTGGACCTTGACGCTACTACTTTA', 'TGGACGTGTGTAGCTTTATCGCCTTTCGACAAAAAAAACTCATTGGTCATGTACGTTCGACTCCTGGGTCACGCTTCATCTTGAGGTTCAAAATTAGTGTAGACCCTCTAGCAACTTCGCACATCTCTCCAGATCGGTTCCTATAAAATATGTGGCTTGGGATGAGGTGAAGCCGGGTGCCGGGTGCATGTGAATACGCTGATAATCCGGAGGGGCTATACCGGCGCAGCTACTCGCCAACGCACTCCTAGTCCCCTTGGGAGTTGAGGGCACCTGACGTGTGGTGACACAGTCGAGGTT')]
    for i, tc in enumerate(testcases):
        word1, word2 = tc
        print(f"Testcase {i + 1}의 가장 긴 공통 부분 문자열 : {dna_longgest_shared_pattern(word1, word2)}")
        print()

if __name__ == '__main__':
    main()