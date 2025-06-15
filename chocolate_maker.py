def chocolate_maker(small, big, x):
    max_big = min(big, x // 5)
    remaining = x - (max_big * 5)
    return remaining <= small
