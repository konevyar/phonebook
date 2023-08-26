import json
from typing import List, Dict, Union


class PhoneBook:
    def __init__(self, file_path: str):
        """
        Инициализация телефонной книги.
        :param file_path: Путь к файлу JSON, в котором
        хранятся данные телефонной книги.
        """
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def save(self) -> None:
        """
        Сохраняет текущие данные телефонной книги в файл.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

    def add(self, record: Dict[str, Union[str, List[str]]]) -> None:
        """
        Добавляет новую запись в телефонную книгу.
        :param record: Словарь с информацией о записи.
        """
        self.data.append(record)
        self.save()

    def edit(self, index: int, record: Dict[str, Union[str, List[str]]]) \
            -> None:
        """
        Редактирует существующую запись в телефонной книге.
        :param index: Индекс записи для редактирования.
        :param record: Словарь с новой информацией о записи.
        """
        self.data[index] = record
        self.save()

    def search(self, **kwargs) -> List[Dict[str, Union[str, List[str]]]]:
        """
        Поиск записей по заданным критериям.
        :param kwargs: Ключи и значения для поиска.
        :return: Список найденных записей.
        """
        return [record for record in self.data if any(
            item in record.items() for item in kwargs.items()
        )]

    def display(self, page: int, page_size: int) -> \
            List[Dict[str, Union[str, List[str]]]]:
        """
        Выводит записи из телефонной книги постранично.
        :param page: Номер страницы.
        :param page_size: Количество записей на странице.
        :return: Список записей на указанной странице.
        """
        return self.data[(page - 1) * page_size: page * page_size]
