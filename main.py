from delete_file import delete_entry
from entry_file import add_entry
from view_file import view_phonebook


def run_phonebook():
    print("Доступные операции:")
    print("1. Просмотр справочника")
    print("2. Добавить запись")
    print("3. Удалить запись")

    choice = input("Введите номер операции (1-3): ")

    if choice == "1":
        view_phonebook()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        delete_entry()
    else:
        print("Неправильный выбор операции.")

run_phonebook()

