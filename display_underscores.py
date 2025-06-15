
# קלט מחרוזת מהמשתמש
secret_word = input("Please enter a secret word: ")

# יצירת מחרוזת של קווים תחתונים באורך המילה
underscores = ' '.join(['_' for _ in secret_word])

# הדפסת התוצאה
print(underscores)
