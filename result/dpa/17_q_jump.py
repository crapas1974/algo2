def elec_alive_probability_topdown(n, k, i, j, memo=None):
   if memo == None:
       memo = {}
      
   moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

   if i < 0 or i >= n or j < 0 or j >= n:
       return 0

   if k == 0:
       return 1

   if (i, j, k) in memo:
       return memo[(i, j, k)]

   prob = 0
   for m_i, m_j in moves:
       prob += elec_alive_probability_topdown(n, k - 1, i + m_i, j + m_j, memo) / 8.0

   memo[(i, j, k)] = prob
   return prob


def main():
    testcases = [
        (3, 1, 0, 0),
        (3, 2, 0, 0),
        (3, 2, 1, 1),
        (20, 50, 11, 13),
        (1, 10, 0, 0),
        (39, 800, 20, 20)
    ]

    for i, tc in enumerate(testcases):
        print(f'TC{i + 1} : ', end="")
        print(format(elec_alive_probability_topdown(*tc), '.10f'))

if __name__ == '__main__':
    main()