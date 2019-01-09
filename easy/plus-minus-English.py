def plusMinus(arr):
    size = len(arr)
    ratios = [0, 0, 0]

    for n in arr:
        if n > 0:
            ratios[0] += 1
        elif n < 0:
            ratios[1] += 1
        else:
            ratios[2] += 1

    for i, n in enumerate(ratios):
        ratios[i] = n / size

    print("{:.6f}\n{:.6f}\n{:.6f}".format(ratios[0], ratios[1], ratios[2]))

