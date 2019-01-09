def diagonalDifference(arr):
    a = 0
    b = 0
    if arr:
        limit = len(arr) - 1
        for n in range(limit + 1):
            a += arr[n][n]
            b += arr[n][limit - n]
    return abs(a - b)

