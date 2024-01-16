def remove_rival_list(n, k):
    virus = [True] * n
    count = n
    cur = 0
    while count > 1:
        i = 0
        while i < k:
            if virus[cur]:
                i += 1
            cur = (cur + 1) % n
        virus[(cur - 1) % n] = False
        count -= 1
    for i in range(n):
        if virus[i]:
            return i + 1
        
#if __name__ == '__main__':
#    print(josep(100000, 1000))
import time

def main():
    testcases = [(7, 3), (15, 5), (1, 10), (10, 1), (15, 5), (5, 15), (30, 30), (1000, 1), (1000, 39), (100000, 100), (100000, 333), (100000, 1000)]
    for i, (n, k) in enumerate(testcases):
        start = time.time()
        last_person = remove_rival_list(n, k)
        print(f"testcase {i + 1}: {last_person}")
        print(f"  execution time : {time.time() - start}")

if __name__ == "__main__":
    main()