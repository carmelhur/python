# קולט מחרוזת מהמשתמש
user_input = input("Please enter a string: ")

# מחשב את אמצע המחרוזת (חצי ראשון קטן אם אורך אי זוגי)
half = len(user_input) // 2

# חותך וממיר בהתאם
result = user_input[:half].lower() + user_input[half:].upper()

# מדפיס את התוצאה
print(result)
