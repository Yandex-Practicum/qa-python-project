import pytest
from praktikum.praktikum import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['SAUCE', 'chili sauce', 300],
            ['FILLING', 'dinosaur', 200]
        ]
    )
    def test_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_price() == price
