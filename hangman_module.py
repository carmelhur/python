HANGMAN_PHOTOS = {
    0: "x-------x",
    1: """x-------x
|
|
|
|
|""",
    2: """x-------x
|       |
|       0
|
|
|""",
    3: """x-------x
|       |
|       0
|       |
|
|""",
    4: """x-------x
|       |
|       0
|      /|\\
|
|""",
    5: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
    6: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS.get(num_of_tries, "Invalid number of tries"))
