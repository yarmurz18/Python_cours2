import pytest

from models import Book, Library


@pytest.fixture()
def book() -> Book:
    book2 = Book("Joan Kathleen Rowling", "Harry Potter")
    return book2


@pytest.fixture()
def another_book() -> Book:
    book1 = Book("Mikhail Bulgakov", "The Master and Margarita")
    return book1


@pytest.fixture()
def library() -> Library:
    a = Library("World of books")
    return a


@pytest.fixture()
def another_library() -> Library:
    a = Library("World of book")
    return a


@pytest.fixture()
def add_books_to_library(library, book, another_book):
    library.add_book(book)
    library.add_book(another_book)
    return library
