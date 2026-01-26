from praktikum.ingredient_types import *

class TestIngredient:
    def test_get_price_success(self,ingredient1):
        result_price = ingredient1.get_price()
        assert result_price == 300

    def test_get_name_success(self, ingredient1):
        result_name = ingredient1.get_name()
        assert result_name == "chili sauce"

    def test_get_type_success(self, ingredient1):
        result_type = ingredient1.get_type()
        assert result_type == INGREDIENT_TYPE_SAUCE


