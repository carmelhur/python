user_input = input("Please enter a string: ")
first_char = user_input[0]
modified = first_char + user_input[1:].replace(first_char, 'e')
print(modified)
