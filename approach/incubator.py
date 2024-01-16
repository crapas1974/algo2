

def filter_placement(n):
    # 길이 n인 리스트를 만든다.
    arr = [0] * n
    # 가장 작은 초기 조건은 값이 주어진다.
    arr[0] = 1
    arr[1] = 2
    # 그 이후로는 계산해서 올라가되, 이전에 계산한 결과를 활용한다.
    for i in range(2, n):
        arr[i] = arr[i - 2] + arr[i - 1]
    # 목표한 일반항의 값을 반환한다.
    return arr[n - 1]


def main():
    print(f"100 X 2 크기의 배양기에서 필터를 배치하는 방법의 수 : {filter_placement(100)}")

if __name__ == '__main__':
    main()