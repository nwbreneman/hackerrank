# the apparent trick to this is that there's only one 3x3 magic square,
# the "Lo Shu" square, and all other magic squares are rotations/reflections
# of it. we could compute each rotation/reflection each time but faster to
# just store them in a constant.
ALL_3x3_SQUARES = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]


def formingMagicSquare(s):
    min_cost = float("inf")

    for square in ALL_3x3_SQUARES:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(square[i][j] - s[i][j])

        min_cost = min(min_cost, cost)

    return min_cost

