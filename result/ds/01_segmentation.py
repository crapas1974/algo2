def segmentations(arr, prefix_list = None, result = None):
    if prefix_list == None:
        prefix_list = []
    if result == None:
        result = []
    if not arr:
        result.append(prefix_list)
        return result
    head = arr[0]
    tail = arr[1:]
    segmentations(tail, prefix_list + [[head]], result)
    if prefix_list:
        segmentations(tail, prefix_list[:-1] + [prefix_list[-1] + [head]], result)
    return result

import hashlib
def print_result(result: list):
    print(f"    결과 리스트의 항목의 수 : {len(result)}")
    sorted_result = sorted(result)
    hash4_string = hashlib.md5(str(sorted_result).encode()).hexdigest()[:4]
    print(f"    결과 리스트의 간이 해시 값 : {hash4_string}")


def main():
    testcases = [['C', 'T', 'A'], [1, 2, 3], [1, 1, 1], [1], ['C'], [1, 1], ['C', 'T', 'A', 'G'], [1, 1, 1, 1], ['C', 'T', 'A', 'G', 'T'], [23, 24, 25, 26, 27], ['CT', 'AG', 'TG', 'GC', 'CA', 'AT'], ['AT', 'TGA', 'AC', 'TC', 'AGC', 'GGA', 'AA', 'TT', 'TCT', 'G'], ['TTCGTC', 'GCT', 'GTCAGATGC', 'T', 'CGCCAT']]
    
    for i, tc in enumerate(testcases):
        result = segmentations(tc)
        print(f"Testcase {i + 1}의 입력 : {tc}")
        print_result(result)
        print()

if __name__ == "__main__":
    main()