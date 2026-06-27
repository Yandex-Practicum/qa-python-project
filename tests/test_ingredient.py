import data


class TestIngredient:
    def test_get_type(self, ingredient):
        result = ingredient.get_type()
        assert isinstance(result, str) and result == data.INGR_TYPE

    def test_get_name(self, ingredient):
        result = ingredient.get_name()
        assert isinstance(result, str) and result == data.INGR_NAME
    
    def test_get_price(self, ingredient):
        result = ingredient.get_price()
        assert isinstance(result, float) and result == data.INGR_PRICE