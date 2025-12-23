from ingredient_types import INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_type(self, ingredient_filling):
        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_ingredient_name(self, ingredient_sauce):
        sauce_name, _ = ingredient_sauce.get_name(), ingredient_sauce.get_price()
        assert ingredient_sauce.get_name() == sauce_name

    def test_ingredient_price(self, ingredient_filling):
        _, filling_price = ingredient_filling.get_name(), ingredient_filling.get_price()
        assert ingredient_filling.get_price() == filling_price
