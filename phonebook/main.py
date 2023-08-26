from phonebook import PhoneBook


def main():
    phonebook = PhoneBook('phonebook/data/phonebook.json')

    while True:
        print("\n1. Добавить запись")
        print("2. Редактировать запись")
        print("3. Поиск записей")
        print("4. Показать записи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            record = {
                "фамилия": input("Введите фамилию: "),
                "имя": input("Введите имя: "),
                "отчество": input("Введите отчество: "),
                "организация": input("Введите название организации: "),
                "телефон рабочий": input("Введите рабочий телефон: "),
                "телефон личный": input("Введите личный телефон: ")
            }
            phonebook.add(record)

        elif choice == '2':
            index = int(input("Введите номер записи для редактирования: ")) - 1
            record = {
                "фамилия": input("Введите новую фамилию: "),
                "имя": input("Введите новое имя: "),
                "отчество": input("Введите новое отчество: "),
                "организация": input("Введите новое название организации: "),
                "телефон рабочий": input("Введите новый рабочий телефон: "),
                "телефон личный": input("Введите новый личный телефон: ")
            }
            phonebook.edit(index, record)

        elif choice == '3':
            print("\nВведите один или несколько параметров для поиска.")
            kwargs = {
                "фамилия": input("Введите фамилию для поиска: "),
                "имя": input("Введите имя для поиска: "),
                "отчество": input("Введите отчество для поиска: "),
                "организация": input(
                    "Введите название организации для поиска: "
                ),
                "телефон рабочий": input(
                    "Введите рабочий телефон для поиска: "
                ),
                "телефон личный": input("Введите личный телефон для поиска: ")
            }
            results = phonebook.search(**kwargs)
            for result in results:
                print(f"\nРезультат поиска:\n{result}")

        elif choice == '4':
            page = int(input(
                "Введите номер страницы (на странице 15 записей): "
            ))
            page_size = int(15)
            records = phonebook.display(page, page_size)
            for record in records:
                print(record)

        elif choice == '5':
            break


if __name__ == "__main__":
    main()
