def plus_two(n):
    if n <= 0:
        return None
    if n == 1:
        return 2
    return 2 + plus_two(n - 1)

def main():
    print(plus_two(10))

if __name__ == "__main__":
    main()
    