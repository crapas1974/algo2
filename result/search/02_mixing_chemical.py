from element_x import testcases


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


def main():
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
