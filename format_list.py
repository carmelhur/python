def format_list(my_list):
    return ', '.join(my_list[::2][:-1]) + ', and ' + my_list[-1]
