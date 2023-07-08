def create_phonebook():
    with open("phonebook.txt", "w", encoding="utf-8") as file:
        file.write("ФИО,Номер телефона\n")
    print("Телефонный справочник создан.")

create_phonebook()
