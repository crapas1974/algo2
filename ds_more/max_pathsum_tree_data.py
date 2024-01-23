class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_binary_tree(input_str):
    if not input_str:
        return None
    values = input_str.split(",")
    root = BTreeNode(int(values[0]))
    queue = [root]
    index = 1
    while index < len(values):
        node = queue.pop(0)
        left_value = values[index]
        index += 1
        if left_value != "n":
            node.left = BTreeNode(int(left_value))
            queue.append(node.left)
        if index < len(values):
            right_value = values[index]
            index += 1
            if right_value != "n":
                node.right = BTreeNode(int(right_value))
                queue.append(node.right)


    return root

def insert_by_value(node, data):
    if data >= node.data:
        if node.right == None:
            node.right = BTreeNode(data)
        else:
            insert_by_value(node.right, data)
    else:
        if node.left == None:
            node.left = BTreeNode(data)
        else:
            insert_by_value(node.left, data)



def get_testcases():
    test1 = "-1,3,6,1,0,2,-8"
    test2 = "-100, 1, 1, 1, 1, 1, 1"
    test3 = "68,13,80,n,45,74,80,23,48,n,76,n,n,n,31,n,58,n,n,n,37,51,n,36"
    test4 = "-32,-44,-30,-63,-44,-31,-13,-68,-63,n,n,n,n,-17,n,-96,-64,n,-59,n,n,-97,-90"
    test5 = "-37,-80,52,-87,-59,-25,67,-96,n,-67,-44,-34,42,66,77,n,n,-76,n,-50,-40,n,n,31,n,n,n,68,98,n,n,-51,-47,-43,n,-4,37,n,75,81,n,n,n,n,n,n,n,n,25,n,n,n,n,n,89,n,25"
    test6 = "3,-1,3,-3,0,n,3,n,-2,-1,0,n,3,-3,-2,n,-1,n,2,n,3,n,-3,n,-2,n,n,1,2,n,n,n,-3,n,-2,0,1,n,2,n,-3,n,-2,n,0,n,1,n,2,n,-3,n,-2,n,0,n,1,n,2,n,-3,n,-2,n,0,n,1,n,2,n,-3,n,-2,n,0,n,n,n,2,n,n,n,n,n,n,n,2,n,2"
    test7 = "1,-98,100,-99,-48,76,n,n,n,-82,-12,25,84,-84,-81,-43,-6,21,71,n,93,-98,n,n,-63,-46,-39,n,-2,19,21,25,72,92,n,n,-88,-74,n,n,n,n,-26,n,-2,15,n,n,n,n,43,n,n,n,n,-90,n,-77,-66,n,-17,n,n,3,18,33,45,n,n,n,-77,n,n,n,n,2,n,n,n,26,37,n,51,n,-76,n,n,n,32,33,42,n,51,n,n,29,n,n,33,n,n,n,53,n,n,n,33,n,66,n,35,57,n,n,n,n,64,62"
    test8 = "0,-58,22,-66,-1,14,62,-67,-64,-39,-1,8,18,38,67,-75,-67,-66,-60,-40,-28,n,-1,7,10,17,20,32,44,64,76,-93,-69,n,-67,n,-66,-63,-59,-53,-40,-31,-27,n,-1,6,7,9,11,15,17,19,20,29,33,42,60,63,64,75,80,-98,-90,-75,-69,n,n,n,-66,-64,-61,-60,-59,-54,-47,n,-40,-36,-30,-28,-8,n,-1,5,6,n,n,8,9,10,12,14,15,n,17,18,19,n,20,27,29,32,34,39,42,51,60,62,63,n,65,72,75,78,97,-99,-95,-91,-88,n,-73,n,-68,n,-65,n,-64,-63,-61,n,-60,n,-59,-55,-54,-50,-43,n,-40,-37,-34,-31,-29,n,-28,-17,-5,n,-1,4,5,n,n,n,8,n,9,n,10,11,12,n,14,n,16,n,n,n,18,n,19,n,21,24,28,n,30,n,32,33,34,38,40,n,43,48,51,n,60,n,62,n,63,64,66,71,72,n,75,76,79,92,98,-100,-99,-96,-94,-93,-91,-90,-84,-75,-73,-69,-68,-66,-65,n,n,n,-62,n,-61,n,-60,n,-59,-58,n,n,-54,-52,-50,-45,-42,n,-40,-39,-37,-36,-32,n,-31,-30,-29,n,n,-25,-11,-6,-5,n,-1,3,4,n,5,n,n,n,9,n,10,n,11,n,12,n,14,15,n,n,18,n,n,n,21,22,25,27,28,29,30,n,32,n,33,n,35,n,38,39,41,42,43,44,48,n,52,n,61,n,n,n,63,n,64,65,66,69,71,n,73,n,75,n,77,78,79,86,95,97,100,n,-100,n,-99,-97,-96,-95,-94,n,-93,n,-91,n,-89,-88,-79,n,-75,n,-71,n,-69,n,-68,n,-66,n,-65,-63,-62,n,-61,n,n,n,n,n,-56,n,-54,-53,-51,n,-50,-46,-45,-43,-41,n,-40,n,-39,n,-37,n,-36,-34,-32,n,-31,n,-30,n,-29,-26,-25,-12,-9,-7,-6,n,-4,n,-1,0,3,n,4,n,5,n,9,n,10,n,11,n,13,n,14,n,15,n,18,n,21,n,22,24,25,n,27,n,28,n,29,n,31,n,32,n,33,34,37,n,38,n,39,40,41,n,42,n,43,n,47,n,48,51,56,60,61,n,63,n,64,n,65,n,66,67,70,n,71,72,74,n,n,76,77,n,78,n,79,85,88,92,96,n,97,99,100,n,-100,n,-99,-98,-97,n,-96,n,-95,n,-94,n,-93,n,-91,n,-89,n,-88,-80,-78,n,-74,-72,-71,n,-69,n,-68,n,-66,n,n,n,-63,n,-62,n,-61,-58,-56,n,-54,n,-53,-52,-51,n,-48,-47,-46,n,-45,n,-43,-42,-41,n,-40,n,-38,n,-37,n,-35,n,-33,n,n,n,n,n,-30,n,-29,-27,-26,n,-25,-14,-12,-10,-9,-8,-7,n,n,-5,-3,n,n,n,0,n,3,n,4,n,5,n,n,n,10,n,11,n,13,n,14,n,15,n,n,n,n,n,22,n,24,n,25,n,27,n,n,n,29,30,31,n,n,n,33,n,34,36,37,n,38,n,39,n,40,n,41,n,n,n,43,46,47,n,50,n,51,54,59,n,60,n,61,n,n,n,64,n,65,n,66,n,67,69,70,n,71,n,72,73,74,n,n,n,77,n,78,n,79,82,85,86,90,n,92,95,96,n,97,98,99,n,100,n,-100,n,n,n,n,n,-97,n,-96,n,-95,n,-94,n,-92,n,-91,n,-89,n,-88,-81,-80,-79,-78,n,-74,n,-72,n,-70,n,n,n,-68,n,n,n,-63,n,-62,n,n,n,-57,n,-56,n,-54,n,-53,n,-52,n,-51,-49,-48,n,n,n,-46,n,-45,n,-43,n,-42,n,-41,n,-40,-39,-38,n,-37,-36,-35,-34,-33,n,-30,n,-29,n,-27,n,-26,n,-20,-15,-14,n,-12,-11,-10,n,-9,n,-8,n,-7,n,-5,-4,-2,n,2,n,3,n,n,n,n,n,n,n,n,n,n,n,14,n,15,n,23,n,24,n,25,n,27,n,29,n,30,n,31,n,33,n,34,35,36,n,37,n,n,n,39,n,40,n,41,n,43,44,46,n,47,49,50,n,51,53,54,57,59,n,60,n,61,n,64,n,n,n,n,n,67,n,69,n,70,n,71,n,72,n,73,n,74,n,77,n,78,n,79,80,82,n,85,n,86,89,91,n,92,n,95,n,96,n,97,n,98,n,99,n,100,n,-100,n,-97,n,-96,n,n,n,n,-93,-92,n,-91,n,n,n,-87,-84,-81,n,-80,n,-79,n,-77,n,-74,n,-72,-71,-70,n,n,n,-63,n,-62,-58,-57,n,n,n,-54,n,-53,n,-52,n,n,-50,-49,n,-48,n,-46,n,-44,n,-43,n,-42,n,n,n,-40,n,-39,n,-38,n,-37,n,-36,n,-35,n,-34,n,n,n,-30,n,-29,n,-27,n,-26,-22,-20,-16,-15,n,-13,n,-12,n,-11,n,-10,n,-9,n,-8,n,-7,n,n,n,-4,-3,-2,0,2,n,3,n,14,n,n,22,23,n,24,n,26,n,n,n,29,n,30,n,31,n,33,n,34,n,35,n,36,n,37,n,39,n,40,n,41,n,43,n,44,n,46,n,47,48,49,n,50,n,51,52,53,n,54,56,58,n,59,n,60,n,61,n,n,n,68,n,69,n,70,n,n,n,72,n,73,n,74,n,77,n,n,n,79,n,80,n,84,n,85,n,87,88,89,90,91,n,92,n,95,n,96,n,n,n,98,n,99,n,100,n,n,n,-97,n,-96,n,n,n,-92,n,n,-88,-85,n,-83,n,-81,n,-80,n,-79,-78,-77,n,-74,n,n,n,-71,n,-70,n,-63,n,n,n,-58,n,-57,n,-54,n,n,n,n,n,-50,n,-49,n,-48,n,-46,-45,n,n,-43,n,-42,n,-40,n,n,n,n,n,-37,n,-36,n,n,n,-34,n,-30,n,-29,n,n,n,-26,-25,-21,n,-19,-17,-16,n,-15,-14,-13,n,-12,n,-11,n,-10,n,-9,n,-8,n,n,n,-4,n,-3,n,-2,n,0,n,n,n,n,n,n,n,22,n,23,n,24,25,26,n,n,n,30,n,31,n,n,n,n,n,35,n,36,n,37,n,39,n,n,n,41,n,43,n,44,n,46,n,47,n,48,n,49,n,50,n,51,n,52,n,53,n,55,n,56,57,58,n,n,n,n,n,61,67,68,n,69,n,70,n,72,n,73,n,n,n,n,n,n,n,81,83,84,n,85,86,87,n,88,n,89,n,90,n,n,n,94,n,95,n,n,n,98,n,99,n,100,n,n,n,-96,n,-92,n,n,-86,-85,-84,-83,n,-81,n,-80,n,-79,n,-78,n,-76,n,-74,n,-71,n,-70,n,-63,n,-58,n,-57,n,-54,n,-50,n,-49,n,-48,n,n,n,n,n,n,n,-42,n,n,n,-37,n,n,n,n,n,n,n,-29,n,n,n,-24,-22,-21,-20,-18,n,-17,n,-16,n,-15,n,n,n,-13,n,-12,n,n,n,-10,n,-9,n,-8,n,n,n,-3,n,-2,n,1,n,22,n,23,n,24,n,25,n,n,n,30,n,n,n,35,n,36,n,37,n,39,n,n,n,n,n,45,n,46,n,n,n,48,n,n,n,50,n,51,n,52,n,53,54,55,n,56,n,n,n,58,n,n,n,67,n,68,n,n,n,70,n,n,n,n,80,81,82,83,n,84,n,n,n,86,n,n,n,n,n,n,n,90,92,94,n,95,n,n,n,99,n,100,n,n,n,-92,-87,n,n,-85,n,-84,n,-82,n,-81,n,-80,n,-79,n,-78,-77,-76,n,n,n,-71,n,n,n,-63,n,-58,n,n,n,n,n,-50,n,n,n,-48,n,-42,n,n,n,-29,-25,-24,n,-22,n,-21,n,-20,-19,-18,n,-17,n,n,n,-15,n,n,n,-12,n,-10,n,-9,n,-8,n,-3,n,-2,0,1,n,22,n,23,n,24,n,25,n,n,n,n,n,n,n,37,n,39,n,45,n,46,n,48,n,n,n,n,n,52,n,53,n,n,n,55,n,56,n,58,n,67,n,68,n,70,n,80,n,81,n,82,n,83,n,84,n,86,n,n,n,93,n,94,n,95,n,n,n,n,n,n,n,-87,n,n,n,-84,-83,-82,n,-81,n,-80,n,-79,n,-78,n,-77,n,-76,n,n,n,n,n,-58,n,n,n,-48,n,n,n,n,n,-25,n,-24,n,-22,n,-21,n,n,n,n,n,-18,n,-17,n,n,n,-12,n,-10,n,-9,n,n,n,-3,n,-2,n,0,n,1,n,n,n,23,n,n,n,n,n,37,n,n,n,n,n,n,n,48,n,n,n,n,n,55,n,56,n,58,n,67,n,n,n,70,n,80,n,81,n,82,n,n,n,84,n,86,92,n,n,94,n,n,n,-87,n,-84,n,n,n,-82,n,-81,n,n,n,-79,n,-78,n,-77,n,-76,n,n,n,-48,n,-25,n,-23,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,-3,n,-2,n,n,n,1,n,n,n,n,n,n,n,55,n,n,n,n,n,67,n,n,n,80,n,81,n,82,n,84,n,86,n,92,n,94,n,n,n,-84,n,-82,n,n,n,-79,n,-78,n,-77,n,n,n,n,n,-25,-24,-23,n,-3,n,-2,n,n,n,55,n,67,n,n,n,n,n,n,n,84,n,86,n,92,n,94,n,n,n,n,n,-79,n,-78,n,n,n,n,n,-24,n,n,n,-3,n,n,n,n,n,67,n,84,n,86,n,92,n,n,n,n,n,-78,n,-24,n,n,n,n,n,84,n,n,n,92"
    testcases_data = [test1, test2, test3, test4, test5, test6, test7, test8]
    testcases = []
    for test_data in testcases_data:
        testcases.append(build_binary_tree(test_data))
    return testcases
