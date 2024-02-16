def filter_placement(n):
    arr = [0] * n
    arr[0] = 1
    arr[1] = 2
    for i in range(2, n):
        arr[i] = arr[i - 2] + arr[i - 1]
    return arr[n - 1]

def main():
    testcases = [2, 3, 10, 30, 50, 100]
    for tc in testcases:
        print(f"{tc} X 2 크기의 배양기에서 필터를 배치하는 방법의 수 : {filter_placement(tc)}")

if __name__ == '__main__':
    main()