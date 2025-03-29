class TestLibrary:
    def test_new_library(self, library):
        assert library.name
        assert not library.book_list

    def test_name_in_library(self, library, another_library):
        assert library.name != another_library.name
