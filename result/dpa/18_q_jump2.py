def elec_alive_probability_buttomup(n, m, k, i, j):
    directions = {}
    directions[4] = [(2, 1), (1, 2)]
    directions[2] = [(2, -1), (-2, 1), (1, -2), (-1, 2)]
    directions[1] = [(-2, -1), (-1, -2)]
    weight_sum = sum([weight * len(direction) for weight, direction in directions.items()])

    prob = [[0 for _ in range(m)] for _ in range(n)]
    prob[i][j] = 1

    for _ in range(k):
        prob_next = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                for weight, directions_for_weight in directions.items():
                    for m_i, m_j in directions_for_weight:
                        next_i, next_j = i + m_i, j + m_j
                        if 0 <= next_i < n and 0 <= next_j < m:
                            prob_next[next_i][next_j] += prob[i][j] * weight / weight_sum

        out_grid_prob = 1 - sum(sum(row) for row in prob)
        prob_next[i][j] += out_grid_prob * 0.1
        prob = prob_next

    return sum(sum(row) for row in prob)

def main():
    testcases = [
        (3, 3, 1, 0, 0),
        (3, 3, 2, 0, 0),
        (3, 3, 2, 1, 1),
        (20, 25, 50, 11, 13),
        (1, 1, 10, 0, 0),
        (21, 31, 10, 0, 0),
        (21, 31, 10, 11, 16),
        (21, 31, 10, 20, 30),
        (21, 31, 3000, 0, 0),
        (21, 31, 3000, 11, 16),
        (21, 31, 3000, 20, 30)
    ]
    for i, tc in enumerate(testcases):
        print(f'TC{i + 1} : ', end="")
        print(format(elec_alive_probability_buttomup(*tc), '.10f'))

if __name__ == '__main__':
    main()