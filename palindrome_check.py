
user_input = input("Enter a string: ")
normalized = user_input.replace(" ", "").lower()
if normalized == normalized[::-1]:
    print("OK")
else:
    print("NOT")
