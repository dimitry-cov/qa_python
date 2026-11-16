import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    #покрываем проверку длины названия (использована параметризация) (проверка добавления книг)
    @pytest.mark.parametrize('book_name', ['A' * 40, 'A' * 41])
    def test_add_new_book_name_lenght(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        if len(book_name) <= 40:
            assert book_name in collector.get_books_genre()
        else:
            assert book_name not in collector.get_books_genre()

    
    #покрываем проверку отсутствиия жанра в списке доступных (негативная)
    def test_set_book_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фэнтези')
        assert collector.get_book_genre('Гарри Поттер') == ''


    #покрываем проверку получения жанра существующей книги (позитивная)
    def test_get_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'


    #покрываем проверку получения списка книг с определенным жанром (позитивная)
    def test_get_books_with_specific_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Мизери')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Оно','Ужасы')
        collector.set_book_genre('Мизери','Ужасы')
        collector.set_book_genre('Гарри Поттер','Фэнтези')
        expected_result = ['Оно', 'Мизери']
        assert collector.get_books_with_specific_genre('Ужасы') == expected_result


    #покрываем проверку вывода словаря (позитивная)
    def test_get_books_genre_valid(self):
       collector = BooksCollector() 
       collector.add_new_book('Дюна')
       collector.set_book_genre('Дюна','Фантастика')
       assert collector.get_books_genre() == {'Дюна': 'Фантастика'}


    #покрываем проверку отсутствия подходящих книг (в детских), если добавляем ужасы (негативная)
    def test_get_books_for_children_empty_result(self):
         collector = BooksCollector()
         collector.add_new_book('Оно')
         collector.set_book_genre('Оно','Ужасы')
         assert collector.get_books_for_children() == []


    #покрываем проверку добавления существующей книги в избранное (позитивная)
    def test_add_book_in_favorites_valid(self):
        collector = BooksCollector() 
        collector.add_new_book('Властелин Колец')
        collector.add_book_in_favorites('Властелин Колец')
        assert collector.get_list_of_favorites_books() == ['Властелин Колец']


    #покрываем проверку удаления книги, которая есть в избранном (позитивная)
    def test_delete_book_from_favorites_valid(self):
        collector = BooksCollector() 
        collector.add_new_book('Властелин Колец')
        collector.add_book_in_favorites('Властелин Колец')
        collector.delete_book_from_favorites('Властелин Колец')
        assert collector.get_list_of_favorites_books() == []


    #покрываем проверку получения списка избранных книг (позитивная)
    def test_get_list_of_favorites_books_valid(self):
        collector = BooksCollector() 
        collector.add_new_book('Властелин Колец')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Властелин Колец')
        collector.add_book_in_favorites('Гарри Поттер')
        expected_result = ['Властелин Колец', 'Гарри Поттер']
        assert collector.get_list_of_favorites_books() == expected_result
        