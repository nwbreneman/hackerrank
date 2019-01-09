def surfaceArea(A):
    H = len(A)
    W = len(A[0])

    cost = 2 * H * W

    for i in range(H):
        for j in range(W):
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                try:
                    # -1 in Python arrays wraps around to end element,
                    # handle manually
                    if -1 in (i + a, j + b):
                        raise IndexError
                    cost += max(0, A[i][j] - A[i + a][j + b])
                except IndexError:
                    cost += A[i][j]

    return cost

