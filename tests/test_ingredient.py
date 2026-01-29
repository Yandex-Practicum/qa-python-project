from data import BurgerData
from ingredient import Ingredient


class TestIngredient:
    def test_get_price(self, mock_filling):
        filling = Ingredient(mock_filling.type, mock_filling.name, mock_filling.price)
        assert filling.get_price() == BurgerData.FILLING_PRICE

    def test_get_name(self, mock_sauce):
        sauce = Ingredient(mock_sauce.type, mock_sauce.name, mock_sauce.price)
        assert sauce.get_name() == BurgerData.SAUCE_NAME

    def test_get_type(self, mock_sauce):
        sauce = Ingredient(mock_sauce.type, mock_sauce.name, mock_sauce.price)
        assert sauce.get_type() == BurgerData.INGREDIENT_TYPE_SAUCE
