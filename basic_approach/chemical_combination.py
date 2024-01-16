import time


def chemical_combination(chemicals, target_amount, current_combinations = None, current_idx = 0):
    if current_combinations == None:
        current_combinations = []
    if target_amount == 0:
        return current_combinations
    if target_amount < 0:
        return None
    if current_idx == len(chemicals):
        return None
    result = []
    
    current_chemical = chemicals[current_idx]
    if current_chemical == target_amount:
        result.append(current_combinations + [current_idx])
    elif current_chemical < target_amount:
        result_with_current = chemical_combination(chemicals, target_amount - current_chemical, current_combinations + [current_idx], current_idx + 1)
        if result_with_current != None:
            result += result_with_current
    result_without_current = chemical_combination(chemicals, target_amount, current_combinations, current_idx + 1)
    if result_without_current != None:
        result += result_without_current
    return result

import random


def main():
    tc1 = ([1, 2, 3, 4, 5], 5)
    tc2 = ([1, 2, 3, 4, 5], 6)
    tc3 = ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 6)
    tc4 = ([1, 2, 3, 4, 5], 15)
    tc5 = ([1, 2, 3, 4, 5], 16)
    tc6 = ([5, 3, 5, 6, 3, 5, 3, 3, 6, 6, 3, 4, 5, 4, 4, 6, 5, 6, 5, 6, 3, 5, 5, 3, 3, 5, 4, 4, 5, 5], 20)
    tc7 = ([20, 18, 18, 15, 11, 14, 15, 11, 16, 18, 18, 15, 12, 15, 11, 20, 17, 16, 18, 20, 13, 13, 20, 18, 12, 14, 17, 11, 10, 13, 17, 19, 14, 15, 16, 19, 13, 18, 20, 17, 18, 11, 16, 19, 16, 14, 18, 17, 19, 14, 19, 12, 16, 16, 15, 17, 15, 10, 17, 15, 20, 10, 20, 17, 11, 18, 19, 15, 18, 20, 19, 18, 14, 18, 14, 14, 10, 20, 14, 19, 15, 20, 10, 11, 11, 11, 12, 15, 20, 13, 18, 10, 10, 19, 12, 16, 14, 20, 10, 18], 40)
    tc8 = ([20, 18, 18, 15, 11, 14, 15, 11, 16, 18, 18, 15, 12, 15, 11, 20, 17, 16, 18, 20, 13, 13, 20, 18, 12, 14, 17, 11, 10, 13, 17, 19, 14, 15, 16, 19, 13, 18, 20, 17, 18, 11, 16, 19, 16, 14, 18, 17, 19, 14, 19, 12, 16, 16, 15, 17, 15, 10, 17, 15, 20, 10, 20, 17, 11, 18, 19, 15, 18, 20, 19, 18, 14, 18, 14, 14, 10, 20, 14, 19, 15, 20, 10, 11, 11, 11, 12, 15, 20, 13, 18, 10, 10, 19, 12, 16, 14, 20, 10, 18], 60)
    
    tc9 = ([2481, 8036, 3389, 3790, 1044, 4305, 4907, 5996, 3004, 6500, 9786, 6862, 7324, 1150, 8408, 8334, 7769, 3037, 2345, 1126, 4308, 9188, 2480, 7235, 5217, 3103, 7233, 5720, 5271, 2273, 8331, 2292, 8739, 1733, 9435, 1924, 3320, 5345, 1882, 4347, 8143, 5551, 9293, 8634, 1585, 7123, 7119, 8689, 2786, 1729, 1734, 9367, 4808, 188, 1857, 7509, 2708, 7546, 6561, 3511, 6187, 6927, 5803, 6529, 4065, 9270, 5555, 4860, 6915, 3287, 3093, 8325, 2572, 9825, 994, 9806, 8642, 3831, 3411], 10005)
    tc10 = ([[4224, 2041, 1569, 8560, 9851, 5415, 6248, 1357, 6937, 2822, 3464, 7678, 3209, 657, 5501, 738, 223, 471, 4389, 1648, 1973, 6075, 9541, 341, 308, 174, 7478, 5547, 770, 9271, 6213, 6488, 7256, 5624, 281, 8023, 8185, 6738, 624, 8544, 7372, 564, 1367, 5879, 278, 9189, 3304, 5705, 4936, 6785, 9983, 7050, 6214, 7025, 7313, 8274, 3167, 271, 9306, 7421, 9549, 3684, 7470, 9244, 6777, 1663, 3463, 1669, 8575, 5044, 4105, 5520, 8797, 9588, 2981, 9806, 7911, 4315, 1533, 7284, 9412, 2675, 2242, 1478, 6462, 2964, 1187, 3002, 3840, 1314, 9641, 1093, 7458, 5014, 6746, 4487, 3686, 7536, 7211, 2992, 4625, 1888, 3512, 7846, 1085, 2032, 3463, 1339, 3146, 5946, 8545, 3850, 6284, 7175, 4946, 3891, 3696, 5901, 3769, 7254, 6134, 2548, 2954, 8147, 1863, 8697, 1114, 4628, 1113, 6924, 2244, 7082, 9041, 9684, 3257, 9028, 4802, 3651, 8607, 4120, 1915, 4657, 9032, 8416, 7016, 2890, 8121, 3314, 8456, 8463, 3153, 7461, 7012, 1523, 3716, 9030, 6701, 5595, 3761, 2883, 1871, 8128, 5137, 8696, 1842, 7012, 1975, 5970, 10000, 8254, 6488, 8952, 6113, 8962, 4640, 9718, 7544, 2588, 4404, 9106, 9010, 9593, 7653, 5193, 5092, 4153, 8618, 6224, 2450, 1034, 9120, 1235, 9237, 1492, 6334, 9749, 6685, 7967, 5115, 4413, 7441, 7057, 2803, 3486, 1781, 8377, 4469, 8804, 2546, 7849, 7258, 2610, 6745, 3422, 9129, 7795, 2303, 2739, 5187, 7639, 4356, 7242, 6361, 9227, 5979, 6719, 3003, 3234, 3647, 6834, 4357, 8801, 8065, 3672, 7061, 8221, 8307, 1942, 7166, 8879, 8239, 1130, 7193, 7824, 9197, 5484, 3046, 2601, 5965, 2849, 3185, 4330, 6693, 6125, 9560, 5937, 1091, 5416, 1353, 3079, 6696, 1337, 3840, 1122, 1998, 1344, 4899, 3210, 6789, 7279, 2013, 2760, 9202, 1610, 7475, 3865, 7003, 4602, 2445, 7947, 9600, 6436, 3425, 5776, 1463, 7570, 2492, 2437, 1620, 4681, 1474, 3410, 4991, 4079, 6735, 1482, 4100, 2170, 8753, 4141, 1070, 1031, 6600, 5325, 3066, 5173, 1923, 1544, 9497, 3334, 9486, 3335, 6918, 4339, 3424, 4596, 2760, 7717, 2665, 1036, 3910, 8601, 7826, 6350, 9490, 7367, 2798, 5080, 5634, 2502, 2840, 3645, 9736, 7048, 1995, 3749, 9745, 5144, 8842, 1874, 4692, 5789, 8889, 2311, 2731, 4821, 2670, 9755, 2267, 2489, 6850, 1244, 5953, 5043, 2350, 4510, 5758, 7953, 4292, 8274, 4197, 7604, 8554, 1580, 4539, 7634, 3422, 7471, 7748, 3606, 8036, 2657, 3513, 7720, 3461, 3657, 7083, 5948, 8136, 9568, 5479, 7497, 2874, 4557, 5486, 6092, 6259, 9792, 4979, 4055, 7793, 2422, 8134, 3147, 4141, 2514, 9874, 4264, 1314, 3107, 6323, 3982, 8473, 1048, 7287, 3000, 3216, 7100, 2413, 7494, 2116, 2552, 7122, 2226, 2318, 6061, 1472, 8641, 8978, 4025, 2864, 7647, 9478, 5256, 7498, 3082, 3284, 1036, 6102, 2239, 1050, 5662, 3818, 7911, 2080, 8815, 2663, 6517, 3274, 3942, 7235, 9393, 4001, 4578, 3158, 2044, 4068, 9196, 7463, 3758, 6054, 5170, 6334, 9821, 7579, 5085, 7787, 9647, 7485, 7008, 5339, 1691, 4341, 4866, 5041, 4006, 4162, 5596, 3074, 7537, 5408, 5739, 1658, 1528, 9282, 2392, 1628, 3107, 7026, 8404, 4547, 1903, 8500, 4672, 4884, 3667, 7894, 5808, 2158, 8974, 1726, 7373, 4515, 1060, 6552, 7660, 6115, 8777, 5265, 8599, 5219, 3587, 9810, 3456, 9508, 7737, 4132, 3951, 9727, 7423, 4700, 6450, 4452, 7200, 8296, 9258, 1510, 5533, 2017, 6778, 9216, 3116, 8426, 4884, 2010, 4531, 7832, 6423, 6701, 4691, 5919, 3423, 3335, 9939, 8006, 6470, 2373, 1127, 2307, 4054, 3862, 1844, 3184, 9856, 3246, 1964, 8490, 9038, 5988, 9885, 5040, 1250, 4864, 6588, 1940, 1878, 7012, 5063, 7101, 1606], 961])
    testcases = [tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10]
    for i, tc in enumerate(testcases):
        print(f"testcase {i + 1}")
        combinations = chemical_combination(*tc)
        if len(combinations) == 0:
            print("    조합이 존재하지 않습니다.")
        else:
            print(f"    모든 조합의 수 : {len(combinations)}")
            print(f"    첫 10개의 조합 : {combinations[:10]}")
        print()


if __name__ == "__main__":
    main()
