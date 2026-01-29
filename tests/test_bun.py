import pytest
from praktikum.bun import Bun


class TestBun:
    # Общие тестовые данные
    VALID_CASES = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("булочка с кунжутом", 150.50),
        ("b", 0.01),
        ("очень длинное название булочки с множеством слов и символов", 999.99)
    ]

    EDGE_CASES = [
        ("", 100),
        (" ", 100),
        ("123", 100),
        ("!@#$%^&*()", 100),
        ("black bun", 0),
        ("black bun", 0.001),
        ("black bun", 999999.99)
    ]

    PRICE_TYPE_CASES = [
        ("bun", 100, True),
        ("bun", "100", False),
        ("bun", None, False),
        ("bun", [100], False),
        ("bun", {"price": 100}, False)
    ]

    NEGATIVE_PRICE_CASES = [
        ("negative bun", -1),
        ("negative bun", -0.01),
        ("negative bun", -1000000)
    ]

    # Тесты для валидных случаев
    @pytest.mark.parametrize("name, price", VALID_CASES)
    def test_valid_bun_name(self, name, price):
        """Тестирование корректности имени булочки"""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", VALID_CASES)
    def test_valid_bun_price(self, name, price):
        """Тестирование корректности цены булочки"""
        bun = Bun(name, price)
        assert bun.get_price() == price

    # Тесты граничных случаев для имени
    @pytest.mark.parametrize("name, price", EDGE_CASES)
    def test_edge_cases_name(self, name, price):
        """Тестирование граничных случаев имени"""
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тесты граничных случаев для цены
    @pytest.mark.parametrize("name, price", EDGE_CASES)
    def test_edge_cases_price(self, name, price):
        """Тестирование граничных случаев цены"""
        bun = Bun(name, price)
        assert bun.get_price() == price

    # Тесты типа цены
    @pytest.mark.parametrize("name, price, is_valid", PRICE_TYPE_CASES)
    def test_price_type_validation(self, name, price, is_valid):
        """Проверка типа данных для цены"""
        bun = Bun(name, price)
        assert isinstance(bun.get_price(), (int, float)) == is_valid

    # Тесты отрицательных цен
    @pytest.mark.parametrize("name, price", NEGATIVE_PRICE_CASES)
    def test_negative_price_value(self, name, price):
        """Проверка сохранения отрицательных значений цены"""
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", NEGATIVE_PRICE_CASES)
    def test_negative_price_type(self, name, price):
        """Проверка типа данных при отрицательной цене"""
        bun = Bun(name, price)
        assert isinstance(bun.get_price(), (int, float))
