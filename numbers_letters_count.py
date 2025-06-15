def numbers_letters_count(my_str):
    num_digits = sum(char.isdigit() for char in my_str)
    num_non_digits = len(my_str) - num_digits
    return [num_digits, num_non_digits]
