def max_sales(n, prices, memo_max_sales=None, memo_sales_unit=None):
    if memo_max_sales == None:
        memo_max_sales = {}
    if memo_sales_unit == None:
        memo_sales_unit = {}
    if n == 0:
        return 0, memo_sales_unit
    max_price = 0
    for i in range(1, n + 1):
        # n - 1이 메모에 없으면 재귀호출로 값을 구한다.
        if n - i not in memo_max_sales:
            memo_max_sales[n - i], _ = max_sales(n - i, prices, memo_max_sales, memo_sales_unit)
        # 조건에 등호를 넣어서, 같은 값이라도 더 큰 주문을 선택하도록 한다.
        if max_price <= prices[i - 1] + memo_max_sales[n - i]:
            memo_sales_unit[n] = i 
            max_price = prices[i - 1] + memo_max_sales[n - i]
    # 계산된 값을 메모에 저장한다.
    memo_max_sales[n] = max_price
    return max_price, memo_sales_unit

def sales_unit_limit(n, memo_sales_unit):
    if n == 0:
        return [], 0
    # 메모에 저장되어 있지 않다는 의미는, 더 이상 구하지 않았다는 의미이다.
    if n not in memo_sales_unit:
        return [], 0
    result, _ = sales_unit_limit(n - memo_sales_unit[n], memo_sales_unit)
    result = [memo_sales_unit[n]] + result
    # 잔여 용량을 계산한다.
    rest = n - sum(result)
    return result, rest

def max_sales_limit(n, prices, memo_max_sales=None, memo_sales_unit=None):
    if memo_max_sales == None:
        memo_max_sales = {}
    if memo_sales_unit == None:
        memo_sales_unit = {}
    if n == 0:
        return 0, memo_sales_unit
    max_price = 0
    for i in range(1, n + 1):
        # 가격이 0, 즉 처리하지 않는 용량 단위인 경우 건너뛴다.
        if prices[i - 1] == 0:
            continue
        if n - i not in memo_max_sales:
            memo_max_sales[n - i], _ = max_sales_limit(n - i, prices, memo_max_sales, memo_sales_unit)
        if max_price <= prices[i - 1] + memo_max_sales[n - i]:
            memo_sales_unit[n] = i 
            max_price = prices[i - 1] + memo_max_sales[n - i]
    memo_max_sales[n] = max_price
    return max_price, memo_sales_unit


def sales_unit(n, memo_sales_unit):
    # 더 이상 처리할 수 없으면 
    if n == 0:
        return []
    # n단위 일때의 최적의 판매 방법을 메모에서 가지고 오고, 
    # 남은 조각의 판매 방법을 재귀 호출로 덧붙인다.
    return [memo_sales_unit[n]] + sales_unit(n - memo_sales_unit[n], memo_sales_unit)

def main():

    prices = []
    prices.append([0, 5, 0, 9])
    prices.append([0, 0, 8, 0, 0, 0, 14, 0])
    prices.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    prices.append([0, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    prices.append([0, 0, 7, 8, 10, 14, 16, 17, 20, 24, 27, 29, 32, 33, 37, 38, 41, 43, 47, 49, 51, 54, 56, 60, 64, 68, 71, 75, 78, 80, 0, 0, 0, 0, 0, 94, 95, 99, 100, 104, 106, 107, 109, 111, 115, 118, 120, 124, 126, 130, 133, 136, 138, 140, 142, 145, 149, 153, 155, 158, 162, 163, 165, 166, 168, 172, 174, 175, 179, 182, 183, 186, 188, 189, 193, 196, 200, 203, 204, 207, 211, 214, 218, 220, 223, 227, 228, 230, 231, 232, 233, 236, 239, 240, 242, 244, 246, 248, 251, 253])
    # for i in range(len(prices)):
    #     print(f"TC {i + 1}: ")
    #     max_price, memo_sales_unit = max_sales(len(prices[i]), prices[i])
    #     print(f"  최대 매출 : {max_price}억원")
    #     sales_way = sales_unit(len(prices[i]), memo_sales_unit)
    #     sales_per_unit = {}
    #     for unit in sales_way:
    #         if unit not in sales_per_unit:
    #             sales_per_unit[unit] = 1
    #         else:
    #             sales_per_unit[unit] += 1
    #     print("  판매 방법 : ")
    #     for unit, order in sales_per_unit.items():
    #         print(f"     {unit}단위 주문 : {order}회")
    #     print()

    for i in range(len(prices)):
        print(f"TC {i + 1}: ")
        max_price, memo_sales_unit = max_sales_limit(len(prices[i]), prices[i])
        print(f"  최대 매출 : {max_price}억원")
        sales_way, remainer_unit = sales_unit_limit(len(prices[i]), memo_sales_unit)
        sales_per_unit = {}
        for unit in sales_way:
            if unit not in sales_per_unit:
                sales_per_unit[unit] = 1
            else:
                sales_per_unit[unit] += 1
        print("  판매 방법 : ")
        for unit, order in sales_per_unit.items():
            print(f"     {unit}단위 주문 : {order}회")
        print(f"  잔여 처리 용량 : {remainer_unit}단위")
        print()
if __name__ == '__main__':
    main()
