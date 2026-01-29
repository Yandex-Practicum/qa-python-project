from praktikum.ingredient import Ingredient
from constsnts import Constants


class TestIngredient:

    def test_ingredient_attribute_ingredient_type_true(self):

        ingredient = Ingredient(ingredient_type="SAUCE", name=Constants.INGREDIENT_NAME,
                                price=Constants.INGREDIENT_PRICE)
        assert ingredient.type == "SAUCE"

    def test_ingredient_attribute_name_true(self):

        ingredient = Ingredient(ingredient_type=Constants.INGREDIENT_TYPE, name="hot sauce",
                                price=Constants.INGREDIENT_PRICE)
        assert ingredient.name == "hot sauce"

    def test_ingredient_attribute_price_true(self):

        ingredient = Ingredient(ingredient_type=Constants.INGREDIENT_TYPE,
                                name=Constants.INGREDIENT_NAME, price=100)
        assert ingredient.price == 100

    def test_ingredient_get_price_successful(self, ingredient_fix):

        assert ingredient_fix.get_price() == Constants.INGREDIENT_PRICE

    def test_ingredient_get_name_successful(self, ingredient_fix):

        assert ingredient_fix.get_name() == Constants.INGREDIENT_NAME

    def test_ingredient_get_type_successful(self, ingredient_fix):

        assert ingredient_fix.get_type() == Constants.INGREDIENT_TYPE
