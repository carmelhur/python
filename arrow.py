def arrow(my_char, max_length):
    up = '\n'.join([f"{my_char} " * (i + 1) for i in range(max_length)])
    down = '\n'.join([f"{my_char} " * i for i in range(max_length - 1, 0, -1)])
    return f"{up}\n{down}"

print(arrow('*', 5))
