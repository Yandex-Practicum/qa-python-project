# tests/test_ingredient.py
import pytest
import numbers
from ingredient import Ingredient
from testdata.data_ingredient import (
    INGREDIENT_VALID_DATA,
    INGREDIENT_BOUNDARY_TYPES,
    INGREDIENT_BOUNDARY_NAMES,
    INGREDIENT_BOUNDARY_PRICES,
    INGREDIENT_COMBINED_DATA,
)


# ============================================================
# ОСНОВНЫЕ ТЕСТЫ
# ============================================================
class TestIngredientValid:
    """Тесты корректного создания и работы ингредиента."""
    
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        INGREDIENT_VALID_DATA
    )
    def test_ingredient_should_store_and_return_correct_values(
        self, ingredient_type, name, price, 
        expected_type, expected_name, expected_price
    ):
        """
        Given: тип, имя и цена ингредиента
        When: создаем объект Ingredient
        Then: значения сохраняются в атрибутах и возвращаются через геттеры
        """
        ingredient = Ingredient(ingredient_type, name, price)
        
        # Проверка конструктора (прямой доступ к атрибутам)
        assert ingredient.type == expected_type, \
            f"Expected type '{expected_type}', got '{ingredient.type}'"
        assert ingredient.name == expected_name, \
            f"Expected name '{expected_name}', got '{ingredient.name}'"
        assert ingredient.price == expected_price, \
            f"Expected price {expected_price}, got {ingredient.price}"
        
        # Проверка геттеров
        assert ingredient.get_type() == expected_type, \
            f"get_type() returned '{ingredient.get_type()}'"
        assert ingredient.get_name() == expected_name, \
            f"get_name() returned '{ingredient.get_name()}'"
        assert ingredient.get_price() == expected_price, \
            f"get_price() returned {ingredient.get_price()}"
        
        # Проверка типов возвращаемых значений
        assert isinstance(ingredient.get_type(), str), \
            "get_type() should return str"
        assert isinstance(ingredient.get_name(), str), \
            "get_name() should return str"
        assert isinstance(ingredient.get_price(), numbers.Number), \
            "get_price() should return a number"


# ============================================================
# ТЕСТЫ НА ГРАНИЧНЫЕ ЗНАЧЕНИЯ
# ============================================================
class TestIngredientBoundary:
    """Тесты граничных значений и нестандартных входных данных."""
    
    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type", INGREDIENT_BOUNDARY_TYPES)
    def test_ingredient_should_handle_boundary_types(self, ingredient_type):
        """
        Given: граничное значение типа (пустое, пробелы, спецсимволы, регистр)
        When: создаем ингредиент
        Then: тип сохраняется без изменений (валидация отсутствует)
        """
        ingredient = Ingredient(ingredient_type, "Test", 1.0)
        assert ingredient.get_type() == ingredient_type, \
            f"Expected type '{ingredient_type}', got '{ingredient.get_type()}'"
    
    @pytest.mark.unit
    @pytest.mark.parametrize("name", INGREDIENT_BOUNDARY_NAMES)
    def test_ingredient_should_handle_boundary_names(self, name):
        """
        Given: граничное значение имени (пустое, пробелы, длинное, спецсимволы)
        When: создаем ингредиент
        Then: имя сохраняется без изменений
        """
        ingredient = Ingredient("sauce", name, 1.0)
        assert ingredient.get_name() == name, \
            f"Expected name '{name}', got '{ingredient.get_name()}'"
    
    @pytest.mark.unit
    @pytest.mark.parametrize("price", INGREDIENT_BOUNDARY_PRICES)
    def test_ingredient_should_handle_boundary_prices(self, price):
        """
        Given: граничное значение цены (0, отрицательное, очень большое)
        When: создаем ингредиент
        Then: цена сохраняется без изменений (валидация отсутствует)
        """
        ingredient = Ingredient("sauce", "Test", price)
        assert ingredient.get_price() == price, \
            f"Expected price {price}, got {ingredient.get_price()}"
    
    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_COMBINED_DATA)
    def test_ingredient_should_handle_combined_boundary_values(
        self, ingredient_type, name, price
    ):
        """
        Given: комбинация граничных/валидных значений
        When: создаем ингредиент
        Then: все значения сохраняются корректно
        """
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
        
        # Проверяем, что все геттеры возвращают согласованные данные
        assert ingredient.get_type() == ingredient.type
        assert ingredient.get_name() == ingredient.name
        assert ingredient.get_price() == ingredient.price



# ============================================================
# ТЕСТЫ НА ВЗАИМОДЕЙСТВИЕ МЕЖДУ МЕТОДАМИ
# ============================================================
class TestIngredientConsistency:
    """Тесты на согласованность данных между разными методами."""
    
    @pytest.mark.unit
    def test_ingredient_all_getters_return_consistent_data(self):
        """
        Given: ингредиент с конкретными значениями
        When: вызываем все геттеры
        Then: они возвращают те же значения, что были переданы в конструктор
        """
        test_type = "filling"
        test_name = "Cheese"
        test_price = 1.5
        
        ingredient = Ingredient(test_type, test_name, test_price)
        
        assert ingredient.get_type() == test_type
        assert ingredient.get_name() == test_name
        assert ingredient.get_price() == test_price
        
        # Проверяем согласованность между геттерами и прямыми атрибутами
        assert ingredient.get_type() == ingredient.type
        assert ingredient.get_name() == ingredient.name
        assert ingredient.get_price() == ingredient.price
    
    @pytest.mark.unit
    def test_ingredient_objects_are_independent(self):
        """
        Given: два разных ингредиента
        When: создаем их с разными значениями
        Then: они независимы и не влияют друг на друга
        """
        ingredient1 = Ingredient("sauce", "Ketchup", 0.5)
        ingredient2 = Ingredient("filling", "Bacon", 2.0)
        
        # Проверяем, что это разные объекты
        assert ingredient1 is not ingredient2
        
        # Проверяем независимость данных
        assert ingredient1.get_type() == "sauce"
        assert ingredient2.get_type() == "filling"
        
        assert ingredient1.get_name() == "Ketchup"
        assert ingredient2.get_name() == "Bacon"
        
        assert ingredient1.get_price() == 0.5
        assert ingredient2.get_price() == 2.0
        
        # Изменяем один объект (если это возможно)
        ingredient1.name = "Changed"
        
        # Второй объект не изменился
        assert ingredient2.get_name() == "Bacon"
