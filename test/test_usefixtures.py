import pytest


@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURES] Удаляем все данные из БД")


@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURES] Создаем новые данные в БД")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Read books")


@pytest.mark.usefixtures(
    'fill_books_database',
    'clear_books_database'
)
class TestLibrary:
    def test_book_from(self):
        ...

    def test_delete_book(self):
        ...
