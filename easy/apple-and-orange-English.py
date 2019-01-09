def find_overlapping_fruit(s, t, a, fruits):
    count = 0
    for fruit in fruits:
        if (fruit + a) >= s and (fruit + a) <= t:
            count += 1
    return count


def countApplesAndOranges(s, t, a, b, apples, oranges):

    print(find_overlapping_fruit(s, t, a, apples))
    print(find_overlapping_fruit(s, t, b, oranges))

