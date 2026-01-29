import pytest
from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [['filling', 'cutlet', 100.0],
                                                              ['sauce', 'hot sauce', 100.0],
                                                              ['filling', 'sausage', 300.0]])
    def test_get_price_shows_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result_get_price = ingredient.get_price()
        assert result_get_price > 0.0 and result_get_price != None and type(result_get_price) == float

    @pytest.mark.parametrize('ingredient_type, name, price', [['sauce', 'sour cream', 200.0],
                                                              ['sauce', 'hot sauce', 100.0],
                                                              ['filling', 'dinosaur', 300.0]])
    def test_get_name_shows_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result_get_name = ingredient.get_name()
        assert len(result_get_name) != 0 and type(result_get_name) == str

    @pytest.mark.parametrize('ingredient_type, name, price', [['sauce', 'sour cream', 200.0],
                                                              ['sauce', 'hot sauce', 100.0],
                                                              ['filling', 'dinosaur', 300.0]])
    def test_get_type_shows_true(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        result_get_type = ingredient.get_type()
        assert (result_get_type == 'sauce' or result_get_type == 'filling') and type(result_get_type) == str
