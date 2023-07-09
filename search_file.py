def search_entry():
    keyword = input("Введите ключевое слово для поиска: ")
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        found_entries = []
        for line in lines[1:]:
            if keyword.lower() in line.lower():
                found_entries.append(line.strip())
        if found_entries:
            print("Найденные записи:")
            for entry in found_entries:
                print(entry)
        else:
            print("Записи не найдены.")