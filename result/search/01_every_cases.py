def every_combinations(letters):    
    if len(letters) == 0:
        return []
    if len(letters) == 1:
        return [[], [letters[0]]]
    result = []
    following_result = every_combinations(letters[1:])
    for combination in following_result:
        result.append(combination)
        result.append([letters[0]] + combination)
    return result
    
def every_permutations(letters):
    if len(letters) == 0:
        return []
    if len(letters) == 1:
        return [letters[0]]
    result = []
    for i in range(len(letters)):
        head = letters[i]
        rest = letters[:i] + letters[i + 1:]
        following_result = every_permutations(rest)
        for combination in following_result:
            result.append(head + combination)
    return result

def every_words(letters):    
    if len(letters) == 1:
        return [letters[0]]
    result = []
    for i in range(len(letters)):
        following_result = every_words(letters[:i] + letters[i + 1:])
        for combination in following_result:
            if letters[i] + combination not in result:
                result.append(letters[i] + combination)
            if combination not in result:
                result.append(combination)
    return result

def every_words_with_max_count_per_letter(letters, max_count):
    letters_extended = letters * max_count
    return every_words(letters_extended)


def main():
    letters = ['C', 'T', 'A', 'G']    
    every_combinations_result = every_combinations(letters)
    every_combinations_result.sort()
    print(f"모든 조합 목록의 길이는 {len(every_combinations_result)}입니다.")
    print(f"    모든 조합의 목록 : {every_combinations_result}\n")
    every_permutations_result = every_permutations(letters)
    every_permutations_result.sort()
    print(f"한 번씩 사용해 만든 모든 단어의 수는 {len(every_permutations_result)}입니다.")
    print(f"    모든 단어의 목록 : {every_permutations_result}\n")
    every_words_result = every_words(letters)
    every_words_result.sort()
    print(f"최대 한 번씩 사용해 만든 모든 단어의 수는 {len(every_words_result)}입니다.")
    print(f"    모든 단어의 목록 : {every_words_result}\n")
    every_words_result_with_max_2 = every_words_with_max_count_per_letter(letters, 2)
    every_words_result_with_max_2.sort()
    print(f"최대 두 번씩 사용해 만든 모든 단어의 수는 {len(every_words_result_with_max_2)}입니다.")
    print(f"    모든 단어의 목록 : {every_words_result_with_max_2}")

if __name__ == "__main__":
    main()

