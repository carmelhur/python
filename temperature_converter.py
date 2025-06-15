
temp_input = input("Insert the temperature you would like to convert: ").strip()

# Separate the numeric part and the unit
number = float(temp_input[:-1])
unit = temp_input[-1].lower()

if unit == 'f':
    celsius = (number - 32) * 5 / 9
    print(f"{round(celsius, 2)}C")
elif unit == 'c':
    fahrenheit = number * 9 / 5 + 32
    print(f"{round(fahrenheit, 2)}F")
else:
    print("Invalid input. Please provide a temperature ending with 'C' or 'F'.")
