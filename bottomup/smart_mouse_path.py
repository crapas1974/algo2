
def sm_min_time_path_bu(n, t):
    # 각 지점까지의 최소 시간을 저장하는 배열
    min_time = [float('inf')] * (n + 1)

    # 각 지점까지의 최소 시간 경로에서 이전 지점을 저장하는 배열
    # 각 값은 0로 초기화하며, 이 값이 0이라는 의미는 시작 지점에서 곧장 도착했다는 의미이다.
    previous = [0] * (n + 1)

    min_time[0] = 0
    # 1번 지점부터 n번 지점까지의 최소 시간을 차례로 계산한다.
    for i in range(1, n + 1):
        for j in range(i):
            # i번 지점 까지의 최적 경로가 j번 지점을 지나는 경우 
            # min_time[i]를 갱신한다.
            if min_time[i] > min_time[j] + t[j][i]:
                min_time[i] = min_time[j] + t[j][i]
                # 이 경우 i까지의 최소시간 경로는 i 앞에서 j 지점을 지난다.
                previous[i] = j
    # 경로를 저장할 배열
    path = []
    # 도착 지점으로부터 경로를 역추적한다.
    current = n
    # 역추적하다 0 - 시작 지점 - 에 도착하면 추적이 종료된다.
    while current != 0:
        path.append(current)
        current = previous[current]

    # 역추적 한 결과이므로 경로를 뒤집는다.
    path.reverse()
    return min_time[n], path

def main():
    TC1 = [[0, 314, 604, 927, 1257, 1704, 1976, 2325, 2432, 2596, 2835, 3267, 3893, 3932, 4178, 4462, 4781, 5344, 5504, 5430, 5760], [-1, 0, 398, 625, 938, 1263, 1442, 1660, 2103, 2404, 2663, 2877, 3164, 3748, 3999, 3987, 4210, 4849, 5202, 5348, 5300], [-1, -1, 0, 304, 590, 790, 1299, 1600, 1783, 1961, 2759, 2738, 3074, 3410, 3631, 4034, 4298, 4586, 4820, 5131, 5076], [-1, -1, -1, 0, 343, 427, 779, 1136, 1685, 1756, 2095, 2324, 2852, 3043, 3642, 3524, 3729, 4602, 4206, 4670, 5175], [-1, -1, -1, -1, 0, 252, 633, 884, 1189, 1549, 2010, 2229, 2493, 2764, 2731, 3131, 3668, 4134, 4467, 4418, 4437], [-1, -1, -1, -1, -1, 0, 232, 707, 858, 1193, 1356, 1728, 2199, 1915, 2682, 3088, 3801, 3975, 3598, 4031, 3941], [-1, -1, -1, -1, -1, -1, 0, 348, 693, 926, 1028, 1752, 1857, 2032, 2250, 2555, 2639, 3349, 3241, 3950, 4448], [-1, -1, -1, -1, -1, -1, -1, 0, 346, 546, 878, 1093, 1679, 1708, 2095, 2430, 2359, 3013, 3216, 3380, 3658], [-1, -1, -1, -1, -1, -1, -1, -1, 0, 360, 601, 861, 1241, 1578, 1588, 2069, 2479, 2742, 3158, 3234, 3235], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 369, 498, 1078, 1207, 1377, 1700, 2113, 2273, 2729, 2808, 3197], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 215, 502, 948, 1166, 1423, 1719, 1824, 2580, 2484, 3033], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 321, 751, 949, 1236, 1376, 1635, 2035, 2441, 2772], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 394, 578, 954, 1111, 1545, 1592, 2162, 2347], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 247, 425, 965, 1079, 1616, 1948, 2236], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 365, 569, 1038, 1205, 1539, 1617], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 329, 704, 983, 1173, 1407], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 227, 697, 912, 1196], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 383, 647, 981], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 220, 749], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 375], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
    TC2 = [[0, 379, 706, 980, 1295, 1501, 1825, 2244, 2153, 2981, 2923, 3643, 3549, 3696, 4179, 4368, 4918, 4862, 5458, 6133, 5844, 6036, 6447, 6705, 7457, 7374, 8208, 7718, 8373, 9017, 8955, 8823, 9801, 9646, 10245, 9734, 10348, 11052, 11657, 11939, 11849], [-1, 0, 356, 719, 764, 1086, 1377, 1818, 2281, 2615, 2870, 3080, 3304, 3186, 3796, 4331, 4204, 4723, 4783, 5456, 5451, 5650, 6605, 5931, 7343, 7113, 7354, 7150, 7712, 8292, 8760, 9069, 9314, 9256, 9813, 10013, 10195, 10423, 11305, 11495, 11397], [-1, -1, 0, 305, 587, 713, 1279, 1464, 1729, 2013, 2463, 3286, 3073, 3205, 3710, 4478, 3956, 4117, 4657, 4829, 5482, 5376, 6156, 6423, 6392, 6855, 7343, 7347, 7466, 7894, 7861, 8503, 8609, 8892, 9180, 10052, 10261, 10040, 10129, 10935, 11076], [-1, -1, -1, 0, 311, 606, 864, 1171, 1438, 1935, 2083, 2554, 2499, 3406, 3348, 3664, 3690, 3544, 4700, 4944, 5358, 5250, 5785, 6086, 6754, 6696, 6505, 6771, 7718, 7276, 7998, 8723, 8254, 9295, 9174, 9679, 9389, 10384, 10975, 10592, 10912], [-1, -1, -1, -1, 0, 215, 591, 917, 1291, 1560, 1772, 1929, 2346, 2518, 2918, 3394, 3315, 3387, 3903, 4256, 4860, 5092, 5523, 5698, 6239, 6307, 6469, 6833, 6908, 7673, 7700, 8073, 8339, 8707, 9081, 8916, 9381, 9639, 9932, 10746, 10312], [-1, -1, -1, -1, -1, 0, 376, 620, 1052, 1238, 1469, 1805, 1978, 2214, 2877, 3136, 3246, 4050, 4184, 3799, 4555, 4576, 5283, 5414, 5866, 6069, 6176, 6752, 7022, 6997, 7743, 8100, 8229, 8316, 8127, 9802, 9527, 9723, 10278, 9455, 10116], [-1, -1, -1, -1, -1, -1, 0, 260, 593, 898, 1331, 1527, 1745, 2034, 2754, 2703, 3020, 3215, 3596, 3899, 4252, 4238, 4986, 5242, 5391, 5934, 6194, 5592, 6728, 7088, 7143, 7824, 7565, 7392, 8631, 8558, 9407, 8981, 9407, 10117, 9693], [-1, -1, -1, -1, -1, -1, -1, 0, 231, 441, 863, 1242, 1581, 1571, 2253, 2515, 2717, 3178, 3605, 3696, 3977, 4135, 4422, 5008, 4419, 5477, 5224, 5896, 6287, 6691, 6896, 7211, 7352, 7880, 8630, 8765, 8534, 8967, 9094, 9696, 9731], [-1, -1, -1, -1, -1, -1, -1, -1, 0, 341, 559, 804, 1459, 1459, 1801, 2081, 2283, 2492, 3036, 3199, 3621, 4006, 4207, 4503, 4744, 5188, 5048, 5850, 6106, 6442, 6115, 7131, 7447, 7523, 8203, 8353, 8442, 9607, 9053, 8927, 9553], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 304, 528, 1055, 1235, 1642, 1871, 2120, 2539, 2671, 2844, 3297, 3859, 3915, 4330, 4560, 4581, 5409, 5238, 6205, 6180, 6564, 6730, 6833, 7340, 7317, 8481, 8244, 7861, 8838, 9208, 9112], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 325, 746, 878, 855, 1798, 1812, 1951, 2404, 2599, 2713, 3579, 3740, 3704, 4212, 4752, 4729, 5146, 5086, 5651, 6240, 6205, 6873, 6976, 7180, 7725, 7454, 7919, 8557, 8482, 9478], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 398, 709, 1087, 1156, 1534, 1829, 2225, 2190, 2766, 3350, 3419, 3644, 4213, 4107, 4534, 4532, 5111, 5516, 5844, 5813, 6104, 6531, 6698, 7018, 7540, 7669, 8548, 8236, 8694], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 379, 653, 941, 1237, 1399, 1845, 2058, 2697, 2722, 2982, 3534, 3360, 3874, 4462, 5030, 5142, 5039, 5085, 5632, 5741, 6076, 6799, 7007, 6528, 6896, 7676, 7771, 8322], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 314, 659, 685, 1350, 1504, 1741, 2170, 2258, 2658, 2838, 3566, 3790, 3985, 3948, 4645, 4380, 5069, 5406, 5385, 6236, 6476, 6871, 6609, 6854, 7709, 8248, 7740], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 205, 514, 944, 1305, 1536, 1788, 2377, 2002, 2642, 2969, 3292, 3820, 3715, 4191, 4386, 4599, 5296, 5363, 6252, 6219, 6656, 6416, 7247, 7164, 7663, 7622], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 213, 459, 774, 935, 1561, 1878, 1973, 2365, 2717, 2997, 3365, 3656, 4062, 4282, 4746, 4599, 4830, 5665, 5838, 6235, 6402, 6751, 6726, 7065, 7798], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 292, 594, 887, 1410, 1490, 1945, 2154, 2391, 2604, 3010, 3136, 3437, 3852, 3972, 4535, 4642, 5225, 5351, 5179, 6313, 6124, 6581, 7138, 7522], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 390, 627, 713, 1129, 1610, 1826, 2064, 2479, 2553, 2830, 3157, 3715, 3752, 3951, 4575, 5087, 5171, 5092, 5318, 5721, 6418, 6756, 7111], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 259, 567, 807, 990, 1541, 1761, 2109, 2540, 2657, 3032, 3511, 3526, 4391, 4564, 3827, 4745, 5131, 5704, 5746, 5696, 6407, 6451], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 348, 564, 742, 1161, 1573, 1840, 2156, 2637, 2799, 2868, 3078, 3437, 3546, 4280, 4071, 5052, 5254, 5331, 5884, 5940, 6231], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 302, 558, 811, 1461, 1326, 1727, 2071, 2485, 2530, 3219, 3087, 3909, 4084, 4318, 4350, 5016, 4778, 5828, 5725, 5925], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 352, 450, 857, 1107, 1455, 1914, 1988, 2491, 2743, 2802, 3640, 3693, 3720, 4177, 4792, 4494, 4876, 5489, 5750], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 227, 509, 799, 1065, 1435, 1819, 2164, 2402, 2754, 2679, 3342, 3271, 3744, 4289, 4566, 4717, 5051, 5514], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 398, 588, 889, 1134, 1389, 1859, 1901, 2473, 2893, 2847, 3636, 3655, 4086, 3840, 4622, 4970, 5255], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 338, 726, 940, 1299, 1500, 1882, 2165, 2444, 2673, 3098, 3531, 3642, 3831, 4015, 4199, 4913], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 240, 520, 961, 1362, 1357, 2213, 2203, 2480, 2586, 3207, 3005, 3773, 3785, 4385, 4085], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 204, 541, 979, 1027, 1370, 2028, 1728, 2369, 2465, 3094, 3158, 3594, 4057, 4314], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 396, 778, 942, 968, 1494, 1772, 2093, 2435, 2540, 2645, 3128, 3553, 3895], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 298, 494, 791, 1163, 1339, 1842, 2060, 2182, 2767, 2960, 3335, 3611], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 272, 701, 800, 1175, 1669, 1758, 2126, 2516, 2702, 3340, 3406], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 286, 612, 838, 1118, 1827, 1575, 2067, 2438, 2480, 2849], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 319, 565, 891, 1060, 1502, 2168, 2561, 2248, 2830], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 302, 712, 925, 1148, 1491, 1845, 2288, 2124], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 235, 525, 910, 1117, 1566, 1903, 2339], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 354, 645, 966, 1124, 1421, 1799], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 256, 532, 837, 1207, 1258], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 256, 767, 856, 1192], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 368, 559, 934], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 293, 494], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 212], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]

    testcases = [TC1, TC2]
    for i, tc in enumerate(testcases):
        print(f"TC {i+1} :")
        n = len(tc) - 1
        min_time, min_path = sm_min_time_path_bu(n, tc)
        min_path = [0] + min_path        
        print(f"최소 이동 비용 : {min_time}")
        print(f"최소 이동 경로 : {min_path}")




if __name__ == '__main__':
    main()