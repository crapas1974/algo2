def max_sales_type1(n, prices, memo_max_sales=None, counter=0):
    if memo_max_sales == None:
        memo_max_sales = {}
    if n == 0:
        return 0, counter
    max_price = 0
    for i in range(1, n + 1):
        if n - i not in memo_max_sales:
            counter += 1
            memo_max_sales[n - i], counter = max_sales_type1(n - i, prices, memo_max_sales, counter)
        if max_price <= prices[i - 1] + memo_max_sales[n - i]:
            max_price = prices[i - 1] + memo_max_sales[n - i]
    memo_max_sales[n] = max_price
    return max_price, counter

def max_sales_type2(n, prices, memo_max_sales=None, counter= 0):
    if memo_max_sales == None:
        memo_max_sales = {}
    if n == 0:
        return 0, counter
    if n in memo_max_sales:
        return memo_max_sales[n], counter
    max_price = 0
    for i in range(1, n + 1):
        counter += 1
        max_sale, counter = max_sales_type2(n - i, prices, memo_max_sales, counter)
        if max_price <= prices[i - 1] + max_sale:
            max_price = prices[i - 1] + max_sale
    memo_max_sales[n] = max_price
    return max_price, counter


def main():
    tc = [2, 5, 7, 8, 10, 14, 16, 17, 20, 24, 27, 29, 32, 33, 37, 38, 41, 43, 47, 49, 51, 54, 56, 60, 64, 68, 71, 75, 78, 80, 82, 84, 87, 91, 93, 94, 95, 99, 100, 104, 106, 107, 109, 111, 115, 118, 120, 124, 126, 130, 133, 136, 138, 140, 142, 145, 149, 153, 155, 158, 162, 163, 165, 166, 168, 172, 174, 175, 179, 182, 183, 186, 188, 189, 193, 196, 200, 203, 204, 207, 211, 214, 218, 220, 223, 227, 228, 230, 231, 232, 233, 236, 239, 240, 242, 244, 246, 248, 251, 253]
    print(max_sales_type1(100, tc))
    print(max_sales_type2(100, tc))

if __name__ == '__main__':
    main()