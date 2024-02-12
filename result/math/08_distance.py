def distance(arr):
    max = -1
    count = 0
    idx = []
    for i, (n1, n2) in enumerate(arr):                
        xor_result = n1 ^ n2
        count = bin(xor_result).count('1')
        if count > max:
            max = count
            idx = [i + 1]
        elif count == max:
            idx.append(i + 1)
    return idx, max

def main():
    with open("new_chemical_test.txt", "r") as f:
        lines = f.readlines()
        testcases = []
        tc1 = []
        for i in range(5):
            tc1.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc1)
        tc2 = []
        for i in range(5, 1005):
            tc2.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc2)
        tc3 = []
        for i in range(1005, 11005):
            tc3.append(tuple(map(int, lines[i].split(','))))
        testcases.append(tc3)

    for i, tc in enumerate(testcases):        
        idx, _ = distance(tc)        
        print(f"testcase {i + 1}의 결과 : {idx}")

if __name__ == '__main__':
    main()