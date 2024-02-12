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
def hash4(result: list):
    sorted_result = sorted(result)
    print(sorted_result)
    return hashlib.md5(str(result).encode()).hexdigest()[:4]

# def c2h4(arr):
#     arr.sort()

#     result = ''
#     for mid_list in arr:
#         result += '_'
#         for inner_list in mid_list:
#             result += '='
#             for element in inner_list:
#                 if isinstance(element, int):
#                     result += chr((element % 26) + 65) + ','
#                 else:
#                     result += element + ','
#     return hash4(result)

def counts_per_segment(arr):
    segment_count = {}
    for outer_list in arr:
        for inner_list in outer_list:
            inner_list_tuple = tuple(inner_list)
            if inner_list_tuple not in segment_count:
                segment_count[inner_list_tuple] = 0
            segment_count[inner_list_tuple] += 1
    


    segment_count = dict(sorted(segment_count.items(), key=lambda x: x[1], reverse=True))
    return segment_count

def main():
    testcases = [['C', 'T', 'A'], [1, 2, 3], [1, 1, 1], [1], ['C'], [1, 1], ['C', 'T', 'A', 'G'], [1, 1, 1, 1], ['C', 'T', 'A', 'G', 'T'], [23, 24, 25, 26, 27], ['CT', 'AG', 'TG', 'GC', 'CA', 'AT'], ['AT', 'TGA', 'AC', 'TC', 'AGC', 'GGA', 'AA', 'TT', 'TCT', 'G'], ['TTCGTC', 'GCT', 'GTCAGATGC', 'T', 'CGCCAT']]
    
    for i, tc in enumerate(testcases):
        result = segmentations(tc)
        print(f"Testcase {i + 1}의 입력 : {tc}")
        segment_count = counts_per_segment(result)
        for k, v in segment_count.items():
            print(f"    segment {list(k)} : {v}회")

        # print(f"    결과 : {c2h4(result)}")
        # print(result)
        # cnt = {}
        # for outer_list in result:
        #     print(outer_list)
        #     for inner_list in outer_list:
        #         inner_list_tuple = tuple(inner_list)
        #         if inner_list_tuple not in cnt:
        #             cnt[inner_list_tuple] = 0
        #         cnt[inner_list_tuple] += 1
        # print(cnt)



def main_old():
    testcases = [['C', 'T', 'A'], [1, 2, 3], [1, 1, 1], [1], ['C'], [1, 1], ['C', 'T', 'A', 'G'], [1, 1, 1, 1], ['C', 'T', 'A', 'G', 'T'], [23, 24, 25, 26, 27], ['CT', 'AG', 'TG', 'GC', 'CA', 'AT'], ['AT', 'TGA', 'AC', 'TC', 'AGC', 'GGA', 'AA', 'TT', 'TCT', 'G'], ['TTCGTC', 'GCT', 'GTCAGATGC', 'T', 'CGCCAT']]
    
    for i, tc in enumerate(testcases):
        result = segmentations(tc)
        print(f"Testcase {i + 1}의 입력 : {tc}")
        print(f"    결과 : {c2h4(result)}")
        print(result)
        cnt = {}
        for outer_list in result:
            print(outer_list)
            for inner_list in outer_list:
                inner_list_tuple = tuple(inner_list)
                if inner_list_tuple not in cnt:
                    cnt[inner_list_tuple] = 0
                cnt[inner_list_tuple] += 1
        print(cnt)

if __name__ == "__main__":
    main()