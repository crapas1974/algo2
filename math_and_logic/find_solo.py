
def find_solo(arr):
    xor_result = 0
    for i in arr:
        xor_result ^= i
    return xor_result


def main():
    arr = [1, 2, 3, 2, 1, 4, 5, 6, 7, 8]
    print(find_solo(arr))

    print("---")
    xr = 2 ** 16 - 1
    before = -1
    for i in range(1, 100):
        xr ^= i
        print(i, xr)
        # if xr == 0:
        #     if i - before != 4:
        #         print(i, xr)
        #     before = i

if __name__ == "__main__":
    main()



