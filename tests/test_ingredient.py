import pytest
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_ingredient_get_price_return_correct_price(self):
        """Проверяет, что метод get_price возвращает корректную стоимость ингредиента"""

        ingredient = Ingredient(
            ingredient_type=INGREDIENT_TYPE_SAUCE,
            name="Соус Spice-X",
            price=90
        )

        assert ingredient.get_price() == 90

    def test_ingredient_get_name_return_correct_name(self):
        """Проверяет, что метод get_name возвращает корректное название ингредиента"""

        ingredient = Ingredient(
            ingredient_type=INGREDIENT_TYPE_SAUCE,
            name="Соус Spice-X",
            price=90
        )

        assert ingredient.get_name() == "Соус Spice-X"

    @pytest.mark.parametrize(
        "ingredient_type,name,price,expected_ingredient_type",
        [
            (INGREDIENT_TYPE_SAUCE, "Соус Spice-X", 90, 'SAUCE'),
            (INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000, 'FILLING')
        ],
        ids=[
            "sauce_type_return_SAUCE", 
            "filling_type_return_FILLING"
        ]
    )
    def test_ingredient_get_type_return_correct_type(self, ingredient_type, name, price, expected_ingredient_type):
        """Проверяет, что метод get_type возвращает корректный тип ингредиента"""

        ingredient = Ingredient(
            ingredient_type=ingredient_type,
            name=name,
            price=price
        )

        assert ingredient.get_type() == expected_ingredient_type
