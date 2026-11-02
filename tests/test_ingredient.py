import pytest
from ingredient import Ingredient


class TestIngredient:
    def test_init(self):
        ingredient_type = 'vegetable'
        name = 'tomato'
        price = 5
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price 

    @pytest.mark.parametrize(
        "ing_type, name, price",
        [
            ('sauce', "hot sauce", 100),
            ('filling', "cutlet", 200),
        ],
    )
    def test_ingredient_getters(self, ing_type, name, price):
        i = Ingredient(ing_type, name, price)
        
        assert i.get_type() == ing_type
        assert i.get_name() == name
        assert i.get_price() == price
