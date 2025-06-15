# קלט מהמשתמש - מספר תלת ספרתי
number = input("הכנס מספר תלת ספרתי: ")

# חילוץ הספרות
first = int(number[0])
second = int(number[1])
third = int(number[2])

# חישובים
total_bricks = first + second + third
bricks_per_pig = total_bricks // 3
remainder = total_bricks % 3
divisible = remainder == 0

# פלט
print(total_bricks)
print(bricks_per_pig)
print(remainder)
print(divisible)
