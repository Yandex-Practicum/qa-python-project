from unittest.mock import Mock

import pytest

from praktikum.bun import Bun


class TestBun:
    # тест проверяет, что при запросе названия булки в ответе приходит корректное значение
    @pytest.mark.parametrize(
        'name, expected_name',
        [
            ('Флюоресцентная булка', 'Флюоресцентная булка'),
            ('Космическая булка', 'Космическая булка'),
            ('Краторная булка', 'Краторная булка')
        ],
        ids=['Bun name 1',
             'Bun name 2',
             'Bun name 3'
             ]
    )
    def test_get_name(self, name, expected_name):
        bun = Bun(name, 0.0)
        actual_name = bun.get_name()
        assert actual_name == expected_name

    # тест проверяет, что при запросе цены булки в ответе приходит корректное значение
    @pytest.mark.parametrize(
        'price, expected_price',
        [
            (10.0, 10.0),
            (15.5, 15.5),
            (20.75, 20.75)
        ],
        ids=['Bun price 1',
             'Bun price 2',
             'Bun price 3'
             ]
    )
    def test_get_price(self, price, expected_price):
        bun = Bun('Test bun', price)
        actual_price = bun.get_price()
        assert actual_price == expected_price

    # тест проверяет, что при использовании мока названия булки в ответе приходит корректное значение
    def test_get_name_mock(self):
        bun = Mock()
        bun.get_name.return_value = 'Mocked Bun'
        result = bun.get_name()
        assert result == 'Mocked Bun'

    # тест проверяет, что при использовании мока цены булки в ответе приходит корректное значение
    def test_get_price_mock(self):
        bun = Mock()
        bun.get_price.return_value = 0.99
        result = bun.get_price()
        assert result == 0.99
