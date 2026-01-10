import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



class TestIngredient:

    @pytest.mark.parametrize("name", [
        "Чесночный соус",
        "Chili sauce",
        "1-й в мире соус с чесноком!!!",
        "ЧЕСНОЧНЫЙ СОУС"
    ])
    def test_get_name_returns_correct_name(self, name, simple_ingredient):
        ingredient = simple_ingredient(name = name)
        new_name = ingredient.get_name()
        assert new_name == name, \
            f"Ошибка: ожидали имя '{name}', получили '{new_name}'."


    @pytest.mark.parametrize("price", [
        10,
        50.5,
        0,
        999.99
    ])
    def test_get_price_returns_correct_price(self, price, simple_ingredient):
        ingredient = simple_ingredient(price=price)
        new_price = ingredient.get_price()
        assert new_price == price, \
                f"Ошибка: ожидали имя '{price}', получили '{new_price}'."


    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    )
    def test_type_returns_correct_type(self, ingredient_type, simple_ingredient):
        ingredient = simple_ingredient(ingredient_type=ingredient_type)
        actual_type = ingredient.get_type()
        assert actual_type == ingredient_type, \
            f"Ошибка: ожидали тип '{ingredient_type}', получили '{actual_type}'."





