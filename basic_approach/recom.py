def find_recombination_regions(sequence, pattern, window_size, threshold):
    recombination_regions = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        pattern_count = window.count(pattern)
        if pattern_count > threshold:
            recombination_regions.append((i, i + window_size, window))
    return recombination_regions

# 예제 데이터
sequence = "ATCGTTAGGCTTAACGTTAGGCTTAACGTTAGGC"
pattern = "TTA"
window_size = 10
threshold = 2

# 재조합 지역 탐지
regions = find_recombination_regions(sequence, pattern, window_size, threshold)
print(regions)
for start, end, region in regions:
    print(f"재조합 지역: 시작 {start}, 끝 {end}, 서열: {region}")
