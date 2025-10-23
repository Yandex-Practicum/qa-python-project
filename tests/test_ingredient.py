from data.test_data import INGREDIENT_PRICE_VALID, INGREDIENT_NAME_VALID, \
    INGREDIENT_TYPE_VALID


class TestIngredient:

    def test_get_ingredient_price(self, ingredient):
        assert ingredient.get_price() == INGREDIENT_PRICE_VALID, f'Цена ингредиента не соответствует ожидаемой'

    def test_get_ingredient_name(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME_VALID, f'Название ингредиента не соответствует ожидаемой'

    def test_get_ingredient_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_VALID, f'Тип ингредиента не соответствует ожидаемой'

    def test_get_ingredient_name_str(self, ingredient):
        assert isinstance(ingredient.get_name(), str), 'Метод get_name вернул не строку'

    def test_get_ingredient_type_str(self, ingredient):
        assert isinstance(ingredient.get_type(), str), 'Метод get_type вернул не строку'

    def test_get_ingredient_price_float(self, ingredient):
        assert isinstance(ingredient.get_price(), float), 'Метод get_price вернул не число с плавающей точкой'

