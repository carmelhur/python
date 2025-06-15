
def inverse_dict(my_dict):
    inverted = {}
    for key, value in my_dict.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    for value in inverted:
        inverted[value].sort()
    return inverted
