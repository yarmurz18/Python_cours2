class TestBook:
    def test_new_book(self, book):
        assert book.inn
        assert book.title
        assert book.name_of_the_author

    def test_inn_in_book(self, book, another_book):
        assert book.inn != another_book.inn

    def test_title_in_book(self, book, another_book):
        assert book.title != another_book.title
