import json
import os
from phonebook.phonebook import PhoneBook


def test_add():
    phonebook = PhoneBook('phonebook/data/test_phonebook.json')

    record = {
        "фамилия": "Иванов",
        "имя": "Иван",
        "отчество": "Иванович",
        "организация": "ООО Рога и копыта",
        "телефон рабочий": "+7 999 999 99 99",
        "телефон личный": "+7 888 888 88 88"
    }

    phonebook.add(record)

    with open('phonebook/data/test_phonebook.json', 'r') as file:
        data = json.load(file)
        assert data == [record]

    os.remove('phonebook/data/test_phonebook.json')


def test_edit():
    phonebook = PhoneBook('phonebook/data/test_phonebook.json')

    record = {
        "фамилия": "Иванов",
        "имя": "Иван",
        "отчество": "Иванович",
        "организация": "ООО Рога и копыта",
        "телефон рабочий": "+7 999 999 99 99",
        "телефон личный": "+7 888 888 88 88"
    }

    phonebook.add(record)

    new_record = {
        "фамилия": "Петров",
        "имя": "Петр",
        "отчество": "Петрович",
        "организация": "ООО Инфо",
        "телефон рабочий": "+7 777 777 77 77",
        "телефон личный": "+7 666 666 66 66"
    }

    phonebook.edit(0, new_record)

    with open('phonebook/data/test_phonebook.json', 'r') as file:
        data = json.load(file)
        assert data == [new_record]

    os.remove('phonebook/data/test_phonebook.json')
