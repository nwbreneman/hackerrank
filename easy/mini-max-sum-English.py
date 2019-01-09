def miniMaxSum(arr):

    min_n = float("inf")
    max_n = float("-inf")
    total = 0

    for n in arr:
        total += n

    for n in arr:
        min_n = min(min_n, total - n)
        max_n = max(max_n, total - n)

    print("{} {}".format(min_n, max_n))

