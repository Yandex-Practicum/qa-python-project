import pytest
from praktikum.bun import Bun


# класс TestBun содержит в себе набор тестов, которыми покрываем класс Bun
class TestBun:

    #1 тест на проверку что корректно инициализируется имя булочки
    def test_bun_init_name_initialization_name_bun_is_successful(self):
        bun = Bun('my tasty bun', 150)
        assert bun.name == 'my tasty bun'

    #2 тест на проверку что корректно инициализируется цена булочки
    def test_bun_init_price_initialization_price_bun_is_successful(self):
        bun = Bun('my tasty bun', 150)
        assert bun.price == 150

    #3 тест на проверку что корректно работает метод get_name булочки
    @pytest.mark.parametrize('name', ['my tasty bun', 'my lovely bun', 'spicy bun', ''])
    def test_bun_get_name_show_name_successful(self, name):
        bun = Bun(name, 150)
        assert bun.get_name() == name

    #4 тест на проверку что корректно работает метод get_price булочки
    @pytest.mark.parametrize('price', [150, 155.55, 165.99])
    def test_bun_get_price_show_price_successful(self, price):
        bun = Bun('spicy bun', price)
        assert bun.get_price() == price
