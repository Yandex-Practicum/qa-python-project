from data.ingredient_data import IngredientData


class TestIngredient:

    def test_get_price_return_price(self, ibgredient):
        assert ibgredient.get_price() == IngredientData.price

    def test_get_name_return_name(self, ibgredient):
        assert ibgredient.get_name() == IngredientData.name

    def test_get_type_return_type(self, ibgredient):
        assert ibgredient.get_type() == IngredientData.type
