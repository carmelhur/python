
def sequence_del(my_str):
    if not my_str:
        return ""
    result = my_str[0]
    for char in my_str[1:]:
        if char != result[-1]:
            result += char
    return result
