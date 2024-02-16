def dna_break_and_broken(sequence, patterns):
    results = []
    for pattern in patterns:
        if pattern == sequence:
            return [pattern]
        if pattern == sequence[:len(pattern)]:
            results_after = dna_break_and_broken(sequence[len(pattern):], patterns)
            for result_after in results_after:
                results.append(pattern + " " + result_after)
    return results

def main():
    patterns = ['CTAG', 'GCC', 'CTA', 'GGC', 'CCTA']
    test1 = "CTAG"
    test2 = "CCCCCCCCCC"
    test3 = "CTAGGCCCTA"
    test4 = "CTAGGCCCTAT"
    test5 = "GTTTCAGGGA"
    test6 = "CTAGCTAGCC"
    test7 = "CTACTAGCTAGCC"
    test8 = "ACCAGAGTCTCTCCTCTTAC"
    test9 = "GCCCTACTAGCCCTAGCTAGCCCTAGGCCCTAGCCCTAGCCGCCGCCCTACTAGCCCTACTA"
    test10 = "GCCCTAGCTAGCTAGCCGCCGCCCTACTACTAGCCGCCGCCTAGCCGCCCTACTACTAGGCCCTAG"
    test11 = "CTAGCTACTACTAGCTAGCTAGCTAGCTAGCTACTAGCTACTAGCTAGCCCTAGCTACTAGCTAGCTAGCTAGCTAGGCCGCCCTAGCTAGGCCGCCCTAGCTAGCTAGGCCGCCCTAGCTAGGCCGCCCTAGCTAGCTAGCTACTAGCTACTAGCTAGCCGCCCTAGCCCTACTAG"
    testcases = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11]

    for i, testcase in enumerate(testcases):
        print(f"Testcase {i + 1}")
        result = dna_break_and_broken(testcase, patterns)
        if result == []:
            print("    패턴 만으로 분리할 수 없습니다.")
        else:
            print("    분리된 패턴 목록 ")
            for r in result:
                print(f"        {r.replace(' ', '-')}")

        print()

if __name__ == '__main__':
    main()