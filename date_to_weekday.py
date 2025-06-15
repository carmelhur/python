date_input = input("Enter a date (dd/mm/yyyy): ")
try:
    date_object = datetime.strptime(date_input, "%d/%m/%Y")
    day_of_week = date_object.strftime("%A")
    print(day_of_week)
except ValueError:
    print("Invalid date format. Please use dd/mm/yyyy.")
