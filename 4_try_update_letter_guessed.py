from check_valid_input import check_valid_input

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted_list = sorted([char.lower() for char in old_letters_guessed])
        print(" -> ".join(sorted_list))
        return False
