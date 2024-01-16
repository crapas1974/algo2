# make every combination from vocaborary without duplication and recursion
def build_combination(vocaborary):
    vocaborary = list(set(vocaborary))
    result = []
    for i in range(1 << len(vocaborary)):
        temp = []
        for j in range(len(vocaborary)):
            if i & (1 << j):
                temp.append(vocaborary[j])
        result.append(temp)
    return result

def build_combination_with_recursion(vocaborary):
    vocaborary = list(set(vocaborary))
    result = []
    def recursion(idx, temp):
        if idx == len(vocaborary):
            result.append(temp)
            return
        recursion(idx + 1, temp + [vocaborary[idx]])
        recursion(idx + 1, temp)
    recursion(0, [])
    return result





# make every permutation from vocaborary without duplication and recursion
def build_permutation(voacaborary):
    voacaborary = list(set(voacaborary))
    result = []
    def recursion(idx, temp):
        if idx == len(voacaborary):
            result.append(temp)
            return
        for i in range(idx, len(voacaborary)):
            voacaborary[idx], voacaborary[i] = voacaborary[i], voacaborary[idx]
            recursion(idx + 1, temp + [voacaborary[idx]])
            voacaborary[idx], voacaborary[i] = voacaborary[i], voacaborary[idx]
    recursion(0, [])
    return result

# make every permutation from vocaborary without duplication and with recursion
def build_permutation_with_recursion(voacaborary):
    voacaborary = list(set(voacaborary))
    result = []
    def recursion(idx, temp):
        if idx == len(voacaborary):
            result.append(temp)
            return
        recursion(idx + 1, temp + [voacaborary[idx]])
        for i in range(idx + 1, len(voacaborary)):
            voacaborary[idx], voacaborary[i] = voacaborary[i], voacaborary[idx]
            recursion(idx + 1, temp + [voacaborary[idx]])
            voacaborary[idx], voacaborary[i] = voacaborary[i], voacaborary[idx]
    recursion(0, [])
    return result

def main():
    vocaborary = ['C', 'T', 'A', 'G']
    result1 = build_combination(vocaborary)
    print(result1)
    result2 = build_combination_with_recursion(vocaborary)
    print(result2)
    result1.sort()
    result2.sort()

    result3 = build_permutation(vocaborary)
    result4 = build_permutation_with_recursion(vocaborary)

    print("R3 -> ", result3)
    print("R4 -> ", result4)

    print(result1 == result2)


if __name__ == '__main__':
    main()
