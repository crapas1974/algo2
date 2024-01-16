
def cut_sequence(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    arr_length = len(arr)
    for i in range(1, arr_length):
        head = arr[:i]
        tail = arr[i:]
        print(arr, head, tail)
        tail_cut = cut_sequence(tail)
        for t in tail_cut:
            print("$$", head, t)
            result.append([head + t])
    result.append([arr])
    return result


def generate_partitions(lst):
    """ Generate all partitions of a list while maintaining the original order. """

    def recurse(current, remaining):
        if not remaining:
            result.append(current)
            return
        print("rmn", remaining)
        head, *tail = remaining
        recurse(current + [[head]], tail)  # Start a new sublist with the head
        if current:
            recurse(current[:-1] + [current[-1] + [head]], tail)  # Add head to the last sublist

    result = []
    recurse([], lst)
    return result

def p2(arr, prefix_list = None, result = None):
    if prefix_list == None:
        prefix_list = []
    if result == None:
        result = []
    if not arr:
        result.append(prefix_list)
        return result
    head = arr[0]
    tail = arr[1:]
    p2(tail, prefix_list + [[head]], result)
    if prefix_list:
        p2(tail, prefix_list[:-1] + [prefix_list[-1] + [head]], result)
    return result
import hashlib
def hash4(input):    
    return hashlib.sha256(input.encode()).hexdigest()[:4]

def c2h4(arr):
    arr.sort()
    result = ''
    for mid_list in arr:
        result += '_'
        for inner_list in mid_list:
            result += '='
            for element in inner_list:
                if isinstance(element, int):
                    result += chr((element % 26) + 65) + ','
                else:
                    result += element + ','
    return hash4(result)


# Test the function with the example [1, 2, 3]
#test_list = [1, 2, 3]
#partitions = generate_partitions(test_list)
#partitions

# get all list of partitions of given list
def partitioning(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    arr_length = len(arr)
    for i in range(1, arr_length):
        head = arr[:i]
        tail = arr[i:]
        print("ht", arr, head, tail)
        tail_cut = partitioning(tail)
        print("tc", tail_cut)
        for t in tail_cut:
            result.append([head, t])
    result.append([arr])

    return result



import random
def make_random_sequences(min_length, max_length, size):
    arr = []
    for i in range(size):
        arr.append(''.join(random.choice('ACGT') for _ in range(random.randint(min_length, max_length))))
    return arr

def main():
    testcases = [
        [1],
        ['C'],
        [1, 1],
        [1, 2, 3],
        [1, 1, 1],
        ['C', 'T', 'A'],
        ['C', 'T', 'A', 'G'],
        [1, 1, 1, 1],
        ['C', 'T', 'A', 'G', 'T'],
        [23, 24, 25, 26, 27],
        ['CT', 'AG', 'TG', 'GC', 'CA', 'AT'],

    ]
    testcases.append(make_random_sequences(1, 3, 10))
    testcases.append(make_random_sequences(1, 10, 5))
    print(testcases)
#     #s = ['C', 'T', 'A', 'G', 'T']
#     #s = ['C', 'T', 'A', 'G']
#     #seq = 'CTAG'
#     #s = ['C', 'T', 'A']
#     s = [1, 2, 3]
#     #s = ['C', 'T']
#     print("--")
#     #ps = cut_sequence(s)
#     #for p in ps:
#     #    print(p)
# #    print(cut_sequence(s))
#     print(generate_partitions(s))
#     #print("~", partitioning(s))
#     #print("!", p2(s))
#     result2 = p2(s)
#     print("~~", result2)
#     result2 = p2(s)
#     for p in result2:
#         print(p)
#     print(make_result_simple_hash(result2))
#     t1 = [[[1], [2], [3]], [[1], [2, 3]], [[1, 2], [3]], [[1, 2, 3]]]
#     t2 = [[[1, 2, 3]], [[1], [2], [3]], [[1], [2, 3]], [[1, 2], [3]]]
#     h1 = make_result_simple_hash(t1)
#     h2 = make_result_simple_hash(t2)
#     print(h1)
#     print(h2)
    
    for tc in testcases:
        result = p2(tc)
        cnt = {}
        for r in result:
            for inner_list in r:
                if inner_list not in cnt:
                    cnt[inner_list] = 0
                cnt[inner_list] += 1
        print(result)
#        for r in result:
#            print(r)
        print(c2h4(result))
        print(cnt)
if __name__ == "__main__":
    main()