from delete_file import delete_entry
from entry_file import add_entry
from view_file import view_phonebook
from edit_file import edit_entry
from search_file import search_entry

def run_phonebook():
    print("Доступные операции:")
    print("1. Просмотр справочника")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Редактировать контакт")
    print("5. Поиск контакта")
    print("0. Выйти из приложения")
    while True:    
        choice = input("Введите номер операции (0-5): ")

        if choice == "1":
            view_phonebook()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            search_entry()
        elif choice == "0":
            print("Давай, До свидания!")
            break
        else:
            print("Неправильный выбор операций.")
            print()
            continue

run_phonebook()

