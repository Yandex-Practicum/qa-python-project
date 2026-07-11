import pytest
import numbers
from bun import Bun
from testdata.data_bun import BunData

# ============================================================
# ОСНОВНЫЕ ТЕСТЫ
# ============================================================
class TestBunValid:
    """Тесты корректного создания и работы булочки."""
    
    @pytest.mark.unit
    @pytest.mark.parametrize("name, price, expected_name, expected_price", BunData.BUN_VALID_DATA)
    def test_bun_should_store_and_return_correct_values(self, name, price, expected_name, expected_price):
        """
        Given: имя и цена булочки
        When: создаем объект Bun
        Then: значения сохраняются в атрибутах и возвращаются через геттеры
        """
        bun = Bun(name, price)
        
        # Проверка конструктора
        assert bun.name == expected_name, f"Expected name '{expected_name}', got '{bun.name}'"
        assert bun.price == expected_price, f"Expected price {expected_price}, got {bun.price}"
        
        # Проверка геттеров
        assert bun.get_name() == expected_name, f"get_name() returned '{bun.get_name()}'"
        assert bun.get_price() == expected_price, f"get_price() returned {bun.get_price()}"
        
        # Проверка типов
        assert isinstance(bun.get_name(), str), "get_name() should return str"
        assert isinstance(bun.get_price(), numbers.Number), "get_price() should return a number"


# ============================================================
# 3. ГРАНИЧНЫЕ ТЕСТЫ
# ============================================================
class TestBunBoundary:
    """Тесты граничных значений и нестандартных входных данных."""
    
    @pytest.mark.unit
    @pytest.mark.parametrize("price", BunData.BUN_BOUNDARY_PRICES)
    def test_bun_should_handle_boundary_prices(self, price):
        """
        Given: граничное значение цены (0, отрицательное, очень большое)
        When: создаем булочку
        Then: цена сохраняется без изменений (валидация отсутствует)
        """
        bun = Bun("Test", price)
        assert bun.get_price() == price, f"Expected {price}, got {bun.get_price()}"
    
    @pytest.mark.unit
    @pytest.mark.parametrize("name", BunData.BUN_BOUNDARY_NAMES)
    def test_bun_should_handle_boundary_names(self, name):
        """
        Given: граничное значение имени (пустое, пробелы, длинное, спецсимволы)
        When: создаем булочку
        Then: имя сохраняется без изменений
        """
        bun = Bun(name, 10.0)
        assert bun.get_name() == name, f"Expected '{name}', got '{bun.get_name()}'"
