from data import BurgerIngredients


class TestIngredient:

    def test_get_price_ingredient(self, create_ingredient):
        assert create_ingredient.get_price() == BurgerIngredients.TEST_INGREDIENT_PRICE

    def test_get_name_ingredient(self, create_ingredient):
        assert create_ingredient.get_name() == BurgerIngredients.TEST_INGREDIENT_NAME

    def test_get_type_ingredient(self, create_ingredient):
        assert create_ingredient.get_type() == BurgerIngredients.TEST_INGREDIENT_TYPE
