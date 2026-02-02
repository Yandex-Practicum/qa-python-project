from data import SAUCE_DATA


class TestIngredient:

    def test_get_name(self, ingredient_fixture):
        ingredient_name = ingredient_fixture.get_name()
        assert ingredient_name == next(iter(SAUCE_DATA))

    def test_get_price(self, ingredient_fixture):
        ingredient_price = ingredient_fixture.get_price()
        assert ingredient_price == SAUCE_DATA[next(iter(SAUCE_DATA))]

    def test_get_type(self, ingredient_fixture):
        type_name = ingredient_fixture.get_type()
        assert type_name == ingredient_fixture.type