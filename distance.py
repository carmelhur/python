def distance(num1, num2, num3):
    is_close = abs(num1 - num2) == 1 or abs(num1 - num3) == 1
    is_far = (abs(num2 - num3) >= 2 and abs(num1 - num2) >= 2) or (abs(num1 - num3) >= 2 and abs(num2 - num3) >= 2)
    return is_close and is_far
