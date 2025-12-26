import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun


class TestBun:
    #тест проверяет, что булочка правильно установлена и отображается в чеке
    def test_set_bun(self):
        burger = Burger()
        bun = Bun(" Новая булочка", 123)
        burger.set_buns(bun)
        assert burger.bun == bun
        receipt = burger.get_receipt()
        assert "Новая булочка" in receipt

    #тест проверяет, что метод корректно возвращает имя булочки. которое хранится в name
    def test_bun_return_name(self, bun_option):
        bun_name = bun_option.name
        bun_get_name = bun_option.get_name()
        assert bun_get_name == bun_name

    #тест проверяет, что метод корректно возвращает цену булочки. которая хранится в price
    def test_bun_return_price(self, bun_option):
        bun_price = bun_option.price
        bun_get_price = bun_option.get_price()
        assert bun_get_price == bun_price

    # тест проверяет, что методы возвращают правильные значения без обращения к реальной булочке
    def test_bun_return_mock_name_and_price(self):
        bun_option = Mock()
        bun_option.name = "Флюоресцентная булка R2-D3"
        bun_option.get_name.return_value = "Флюоресцентная булка R2-D3"
        bun_name = bun_option.name
        bun_get_name = bun_option.get_name()
        bun_option.price = "988"
        bun_option.get_price.return_value = "988"
        bun_price = bun_option.price
        bun_get_price = bun_option.get_price()
        assert bun_get_name == bun_name
        assert bun_get_price == bun_price

