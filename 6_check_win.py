def check_win(secret_word, old_letters_guessed):
    return all(letter in old_letters_guessed for letter in secret_word)
