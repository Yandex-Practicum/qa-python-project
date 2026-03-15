import pytest
import allure

from praktikum.ingredient import Ingredient



class TestIngredient:

    # В классе Ingredient не выполняются проверки передаваемых значений, 
    # поэтому считаю достаточно проверить создание ингредиентов
    @allure.title("Создание ингредиента")
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("sauce","chipotle", 100),
            ("filling","cucumber", 400.0),
            ("filling","jalapeno", -300),
            ("filling","tail", 0),
            ("bun","white bun", -50.5),
            ("sauce","southwest", 999999.99),
        ],
    )
    def test_get_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
        assert ingredient.get_type() == ingredient_type