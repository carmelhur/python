def extend_list_x(list_x, list_y):
    for i in reversed(list_y):
        list_x.insert(0, i)
    return list_x


# דוגמה להרצה
x = [4, 5, 6]
y = [1, 2, 3]
print(extend_list_x(x, y))  # Output: [1, 2, 3, 4, 5, 6]
