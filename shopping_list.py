def print_menu():
    print("\nבחר פעולה:")
    print("1. הדפסת רשימת המוצרים")
    print("2. הדפסת מספר המוצרים ברשימה")
    print("3. בדיקה האם מוצר קיים ברשימה")
    print("4. כמה פעמים מוצר מופיע ברשימה")
    print("5. מחיקת מוצר")
    print("6. הוספת מוצר")
    print("7. הדפסת מוצרים לא חוקיים")
    print("8. הסרת כפילויות")
    print("9. יציאה")

def is_valid_product(product):
    return len(product) >= 3 and product.isalpha()

# התחלת התוכנית
raw_input = input("הכנס רשימת מוצרים מופרדת בפסיקים (ללא רווחים): ")
products = raw_input.split(",")

while True:
    print_menu()
    choice = input("הקש מספר בין 1 ל-9: ")

    if choice == "1":
        print("רשימת מוצרים:", products)

    elif choice == "2":
        print("מספר מוצרים ברשימה:", len(products))

    elif choice == "3":
        product = input("הכנס שם מוצר לחיפוש: ")
        print(product in products)

    elif choice == "4":
        product = input("הכנס שם מוצר לספירה: ")
        print(products.count(product))

    elif choice == "5":
        product = input("הכנס שם מוצר למחיקה: ")
        if product in products:
            products.remove(product)
            print(product, "נמחק מהרשימה.")
        else:
            print("המוצר לא נמצא.")

    elif choice == "6":
        product = input("הכנס שם מוצר להוספה: ")
        products.append(product)
        print(product, "נוסף לרשימה.")

    elif choice == "7":
        invalids = [p for p in products if not is_valid_product(p)]
        print("מוצרים לא חוקיים:", invalids)

    elif choice == "8":
        products = list(dict.fromkeys(products))
        print("הכפילויות הוסרו.")

    elif choice == "9":
        print("להתראות!")
        break

    else:
        print("בחירה לא חוקית. נסה שוב.")
