class TestBookList:
    def test_add_book_to_library(self, library, book):
        library.add_book(book)
        assert len(library.book_list) == 1
        assert str(library.book_list[0]) == str(book)

    def test_remove_book_from_library(self, library, book):
        library.add_book(book)
        book_inn = book.inn
        library.remove_book(book_inn)
        assert len(library.book_list) == 0