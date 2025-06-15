
maria = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

choice = int(input("Enter a number (1-7): "))

if choice == 1:
    print(maria["last_name"])
elif choice == 2:
    print(maria["birth_date"].split(".")[1])
elif choice == 3:
    print(len(maria["hobbies"]))
elif choice == 4:
    print(maria["hobbies"][-1])
elif choice == 5:
    maria["hobbies"].append("Cooking")
    print(maria["hobbies"])
elif choice == 6:
    day, month, year = map(int, maria["birth_date"].split("."))
    birth_tuple = (day, month, year)
    print(birth_tuple)
elif choice == 7:
    current_year = 2025
    birth_year = int(maria["birth_date"].split(".")[2])
    maria["age"] = current_year - birth_year
    print(maria["age"])
