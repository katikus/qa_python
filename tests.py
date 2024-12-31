import pytest

from main import BooksCollector

class TestBooksCollector:
    @pytest.fixture
    def collector(self):
        from main import BooksCollector
        return BooksCollector()

    def test_add_new_book_add_one_book_positive_result(self, collector):
        collector.add_new_book("Человеческая многоножка")
        assert "Человеческая многоножка" in collector.get_books_genre()

    def test_add_new_book_add_book_without_name_positive_result(self, collector):
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_add_new_book_add_book_with_long_name_positive_result(self, collector):
        long_name = "A" * 42
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_book_genre_set_correct_genre_positive_result(self, collector):
        collector.add_new_book("Человеческая многоножка")
        collector.set_book_genre("Человеческая многоножка", "Ужасы")
        assert collector.get_book_genre("Человеческая многоножка") == "Ужасы"

    def test_set_book_genre_add_wrong_genre_positive_result(self, collector):
        collector.add_new_book("Человеческая многоножка")
        collector.set_book_genre("Человеческая многоножка", "Боди-хоррор")
        assert collector.get_book_genre("Человеческая многоножка") != "Боди-хоррор"

    def test_get_books_with_specific_genre_positive_result(self):
        booksbollector = BooksCollector()

        booksbollector.add_new_book("Автостопом по Галактике")
        booksbollector.set_book_genre("Автостопом по Галактике", "Фантастика")
        booksbollector.add_new_book("Война миров")
        booksbollector.set_book_genre("Война миров", "Фантастика")
        booksbollector.add_new_book("Оно")
        booksbollector.set_book_genre("Оно", "Ужасы")

        books = booksbollector.get_books_with_specific_genre("Фантастика")
        assert books == ["Автостопом по Галактике", "Война миров"]

    def test_get_books_for_children_add_three_books_one_returned(self):
        booksbollector = BooksCollector()

        booksbollector.add_new_book("Автостопом по Галактике")
        booksbollector.set_book_genre("Автостопом по Галактике", "Фантастика")
        booksbollector.add_new_book("Оно")
        booksbollector.set_book_genre("Оно", "Ужасы")
        booksbollector.add_new_book("Десять негритят")
        booksbollector.set_book_genre("Десять негритят", "Детективы")

        children_books = booksbollector.get_books_for_children()
        assert children_books == ["Автостопом по Галактике"]

    def test_add_book_in_favorites_add_one_one_in_favorite(self):
        booksbollector = BooksCollector()

        booksbollector.add_new_book("Автостопом по Галактике")
        booksbollector.add_book_in_favorites("Автостопом по Галактике")
        assert "Автостопом по Галактике" in booksbollector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_uncollected_not_in_favorite(self):
        booksbollector = BooksCollector()

        booksbollector.add_book_in_favorites("Десять негритят")
        assert "Десять негритят" not in booksbollector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_favorite(self,):
        booksbollector = BooksCollector()

        booksbollector.add_new_book("Автостопом по Галактике")
        booksbollector.add_book_in_favorites("Автостопом по Галактике")
        booksbollector.delete_book_from_favorites("Автостопом по Галактике")
        assert "Автостопом по Галактике" not in booksbollector.get_list_of_favorites_books()

