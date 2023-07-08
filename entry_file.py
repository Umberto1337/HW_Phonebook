import re

def add_entry():
    name = input("Введите ФИО: ")
    while True:
        phone_number = input("Введите номер телефона: ")
        if re.match(r'^(\+7|8)[\d]{10}$', phone_number):
            if phone_number.startswith('8'):
                phone_number = '+7' + phone_number[1:]
            break
        else:
            print("Неправильный формат номера. Введите номер телефона в формате +7XXXXXXXXXX или 8XXXXXXXXXX.")
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{phone_number}\n")
    print("Запись добавлена.")

add_entry()

