from data import INGREDIENT_NAME, INGREDIENT_PRICE


class TestIngredient:

    def test_get_name(self, ingredient_fixture):
        ingredient_name = ingredient_fixture.get_name()
        assert ingredient_name == INGREDIENT_NAME

    def test_get_price(self, ingredient_fixture):
        ingredient_price = ingredient_fixture.get_price()
        assert ingredient_price == INGREDIENT_PRICE

    def test_get_type(self, ingredient_fixture):
        type_name = ingredient_fixture.get_type()
        assert type_name == ingredient_fixture.type