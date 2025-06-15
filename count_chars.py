def count_chars(my_str):
    my_str = my_str.replace(" ", "")  # הסרת רווחים
    result = {}
    for char in my_str:
        result[char] = result.get(char, 0) + 1
    return result
