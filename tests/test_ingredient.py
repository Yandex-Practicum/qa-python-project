import pytest
from inspect import signature
from praktikum.ingredient import Ingredient


class TestIngredient:
    """
    Тесты для класса Ingredient.
    Проверяем инициализацию и методы получения свойств ингредиента.
    """

    # Параметризованный тест для проверки инициализации с разными значениями
    @pytest.mark.parametrize(
        "ingredient_type,name,price",
        [
            ("SAUCE", "hot sauce", 100.0),  # Обычный случай
            ("FILLING", "cheese", 200.5),  # Дробная цена
            ("FILLING", "beef", 0),  # Нулевая цена
            ("SAUCE", "", 10.0),  # Пустое название
            ("FILLING", "a" * 100, 999.99),  # Длинное название
        ],
        ids=[
            "sauce_normal_case",
            "filling_float_price",
            "zero_price",
            "empty_name",
            "long_name"
        ]
    )
    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Проверяем корректность инициализации ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    # Тесты для метода get_type()
    def test_get_type_returns_correct_value(self):
        """Проверяем, что get_type() возвращает правильный тип"""
        ingredient = Ingredient("SAUCE", "chili sauce", 50.0)
        assert ingredient.get_type() == "SAUCE"

    # Тесты для метода get_name()
    def test_get_name_returns_string(self):
        """Проверяем, что get_name() всегда возвращает строку"""
        ingredient = Ingredient("FILLING", "tomato", 30.0)
        assert isinstance(ingredient.get_name(), str)

    # Тесты для метода get_price()
    def test_get_price_returns_float(self):
        """Проверяем, что get_price() всегда возвращает float"""
        ingredient = Ingredient("FILLING", "onion", 40)
        assert isinstance(ingredient.get_price(), float)

        ingredient_float = Ingredient("SAUCE", "garlic", 25.5)
        assert isinstance(ingredient_float.get_price(), float)

    def test_method_type_annotations(self):
        """Проверяем соответствие аннотаций типов"""
        assert signature(Ingredient.get_price).return_annotation is float
        assert signature(Ingredient.get_name).return_annotation is str
        assert signature(Ingredient.get_type).return_annotation is str