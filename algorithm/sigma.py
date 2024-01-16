def sigma(n):
    result = 0
    if n < 1:
        return 0
    for i in range(1, n+1):
        result += i
    return result

def main():
    testcases = [10, 100, 1000, 10000, 100000, 1000000]
    for i, n in enumerate(testcases):
        result = sigma(n)
        print(f"testcase {i + 1}: {result}")

if __name__ == "__main__":
    main()