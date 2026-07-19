import pytest
from unittest.mock import patch
import bun
from bun import Bun
from testdata.data_bun import BUN_VALID_DATA, BUN_BOUNDARY_PRICES, BUN_BOUNDARY_NAMES


class TestBunValid:
    """Тесты корректного создания и работы булочки."""

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price, expected_name, expected_price", BUN_VALID_DATA)
    def test_constructor_valid_data_stores_correctly(self, name, price, expected_name, expected_price):
        """
        Given: имя и цена булочки
        When: создаем объект Bun
        Then: атрибуты name и price сохраняются корректно
        """
        bun = Bun(name, price)

        assert bun.name == expected_name
        assert bun.price == expected_price

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price, expected_name, expected_price", BUN_VALID_DATA)
    def test_get_name_valid_name_returns_name(self, name, price, expected_name, expected_price):
        """
        Given: булочка с заданными значениями
        When: вызываем get_name
        Then: геттер возвращает корректное значение
        """
        bun = Bun(name, price)

        assert bun.get_name() == expected_name

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price, expected_name, expected_price", BUN_VALID_DATA)
    def test_get_price_valid_price_returns_price(self, name, price, expected_name, expected_price):
        """
        Given: булочка с заданными значениями
        When: вызываем get_price
        Then: геттер возвращает корректное значение
        """
        bun = Bun(name, price)

        assert bun.get_price() == expected_price

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price", [(d[0], d[1]) for d in BUN_VALID_DATA])
    def test_get_name_valid_name_returns_str(self, name, price):
        """
        Given: булочка
        When: вызываем get_name
        Then: геттер возвращает str
        """
        bun = Bun(name, price)

        assert isinstance(bun.get_name(), str)

    @pytest.mark.unit
    @pytest.mark.parametrize("name, price", [(d[0], d[1]) for d in BUN_VALID_DATA])
    def test_get_price_valid_price_returns_number(self, name, price):
        """
        Given: булочка
        When: вызываем get_price
        Then: геттер возвращает число
        """
        bun = Bun(name, price)

        assert isinstance(bun.get_price(), (int, float))


class TestBunBoundary:
    """Тесты граничных значений и нестандартных входных данных."""

    @pytest.mark.unit
    @pytest.mark.parametrize("price", BUN_BOUNDARY_PRICES)
    def test_get_price_boundary_value_stores_correctly(self, price):
        """
        Given: граничное значение цены
        When: создаем булочку
        Then: цена сохраняется без изменений
        """
        bun = Bun("Test", price)

        assert bun.get_price() == price

    @pytest.mark.unit
    @pytest.mark.parametrize("name", BUN_BOUNDARY_NAMES)
    def test_get_name_boundary_value_stores_correctly(self, name):
        """
        Given: граничное значение имени
        When: создаем булочку
        Then: имя сохраняется без изменений
        """
        bun = Bun(name, 10.0)

        assert bun.get_name() == name


class TestBunMock:
    """Тесты с использованием mock-объектов."""

    @pytest.mark.unit
    @patch('bun.Bun')
    def test_constructor_called_with_correct_args(self, mock_bun_class):
        """
        Given: имя и цена булочки
        When: создаем объект Bun через замоканный класс
        Then: конструктор вызывается с правильными аргументами
        """
        bun.Bun("black bun", 100)

        mock_bun_class.assert_called_once_with("black bun", 100)
