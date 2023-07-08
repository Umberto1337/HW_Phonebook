# Телефонный справочник

## Create файл создает файл txt для записи.
Можно создать с новым именем.
Можно затереть старый, удалив все данные.

## Main файл - основной для работы со справочником.
В нём импортированы 3 файла: добавить, удалить и просмотр контактов.

## Entry файл - добавляет контакты
Добавляет новый контакт по ФИО без проверки, поэтому можно написать что угодно.
Затем добавляется номер телефона с проверкой на наличие "+7" или "8" в начале и размером в 11 элементов включительно.
Затем следует проверка: если номер был записан с "8", то он изменяется и сохраняется в формате "+7XXXXXXXXXX".

## Delete файл - удаляет запись по введённому ФИО
Здесь есть мысли о том, что можно добавить, но это будет сделано позже.

## View файл - запускает просмотр справочника на наличие контактов.
-------

### .gitignore файл
Используется для указания файлов и папок, которые не будут отслеживаться и коммититься в репозитории.
Например, Phonebook.txt