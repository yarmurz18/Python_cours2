import uuid


class Book:
    def __init__(self, name_of_the_author: str, title: str):
        self.name_of_the_author = name_of_the_author
        self.title: str = title
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f"<Book {self.title} - {self.name_of_the_author} - {self.inn}>"


class Library:
    def __init__(self, name: str):
        self.name: str = name
        self.book_list: list[Book] = []

    def book_list(self) -> list[str]:
        local_book_list = []
        for book in self.book_list:
            local_book_list.append(str(book))
        return local_book_list

    def add_book(self, book: Book):
        self.book_list.append(book)

    def remove_book(self, inn: uuid.UUID):
        self.book_list = [book for book in self.book_list if book.inn != inn]
