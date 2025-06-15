def show_hidden_word(secret_word, old_letters_guessed):
    return " ".join([letter if letter in old_letters_guessed else "_" for letter in secret_word])
