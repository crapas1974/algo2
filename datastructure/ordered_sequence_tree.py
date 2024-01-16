class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.left = None
        self.right = None

def add_sequence(parent, sequence):
    if sequence < parent.sequence:
        if parent.left == None:
            parent.left = Sequence(sequence)
            return True
        else:
            return add_sequence(parent.left, sequence)
    elif sequence > parent.sequence:
        if parent.right == None:
            parent.right = Sequence(sequence)
            return True
        else:
            return add_sequence(parent.right, sequence)
    else:
        return False
    
def make_tree_structure(node):
    structure = 'O'
    if node.left or node.right:
        structure += '('
        if node.left:
            structure += make_tree_structure(node.left)
        else:
            structure += 'X'
        structure += ','
        if node.right:
            structure += make_tree_structure(node.right)
        else:
            structure += 'X'
        structure += ')'
    return structure

import random
def make_random_sequence(number,max_length):
    sequence = []
    for i in range(number):
        length = random.randint(1,max_length)
        sequence.append(''.join(random.choice('ACGT') for _ in range(length)))
    return sequence
import hashlib
def hash8(string):
    return hashlib.sha256(string.encode()).hexdigest()[:8]

def main():
    testcases = [
        ['CT'],
        ['CT', 'AC', 'GC', 'GA', 'GT'],
        ['CT', 'AC', 'CT', 'GC', 'CT', 'AC', 'GA', 'GC', 'GT'],
    ]
    for _ in range(17):
        testcases.append(make_random_sequence(random.randint(1,1000), random.randint(1,10)))
    for i, testcase in enumerate(testcases):
        print("testcase", i + 1)
        print(','.join(testcase))
    
    for k, testcase in enumerate(testcases):
        print("testcase", k + 1)
        ignored = 0
        root = Sequence(testcase[0])
        for i in range(1, len(testcase)):
            result = add_sequence(root, testcase[i])
            if result == False:
                ignored += 1
        print("  추가되지 못한 유전자 패턴의 수 :", ignored)        
        print("  트리 구조의 간이 해시 값 : ", hash8(make_tree_structure(root)))
        print(make_tree_structure(root))
#        print(make_tree_structure(root))

    # root = Sequence("CT")
    # add_sequence(root, "AC")
    # add_sequence(root, "GC")
    # add_sequence(root, "GA")
    # add_sequence(root, "GT")
    # #add_sequence(root, "CTGGG")
    # #add_sequence(root, "CTGGGG")
    # #add_sequence(root, "CTGGAG")
    # #add_sequence(root, "ATGGAG")

    # print(make_tree_structure(root))

if __name__ == "__main__":
    main()