from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_for_ingredient_successful(self):
        ingredient = Ingredient('SAUCE', "hot sauce", 125)
        assert ingredient.get_price() == 125, 'Неправильная цена соуса'

    def test_get_name_for_one_ingredient_successful(self):
        ingredient = Ingredient('SAUCE', "Начинка", 200)
        assert ingredient.get_name() == 'Начинка', 'Направильное название начинки'

    def test_get_type_for_one_ingredient_successful(self):
        ingredient = Ingredient('SAUCE', "hot sauce", 250)
        assert ingredient.get_type() == 'SAUCE', 'Неверный тип ингредиента'
