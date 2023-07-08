def add_entry():
    name = input("Введите ФИО: ")
    phone_number = input("Введите номер телефона: ")
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{phone_number}\n")
    print("Запись добавлена.")

add_entry()
