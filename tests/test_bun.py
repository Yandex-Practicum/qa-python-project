from praktikum.bun import Bun


class TestBun:

    #  Тест на метод-конструктор класса Булка
    def test_name_of_bun_is_equals_the_assigned(self):

        bun = Bun('bulichka', 1.5)

        assert bun.name == 'bulichka'

    #  Тест на метод-конструктор класса Булка
    def test_price_of_bun_is_equals_the_assigned(self):

        bun = Bun('bulichka', 1.5)

        assert bun.price == 1.5

    #  Тест, проверяющий метод get_name класса Bun
    def test_get_name_of_bun_return_assigned_name(self):

        bun = Bun('bulichka', 1.5)

        assert bun.get_name() == 'bulichka'

    #  Тест, проверяющий метод get_price класса Bun
    def test_get_price_of_bun_return_assigned_price(self):

        bun = Bun('bulichka', 1.5)

        assert bun.get_price() == 1.5
