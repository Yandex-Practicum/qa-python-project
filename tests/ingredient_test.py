from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBun:

    @classmethod
    def setup_class(cls):
        cls.buns = Ingredient(INGREDIENT_TYPE_FILLING, 'Соус Spicy-X', 90)

    def test_get_ingredient_name_success_result(self):
        result = self.buns.get_name()
        assert 'Соус Spicy-X' == result, 'Вернулось неправильное имя'

    def test_get_ingredient_price_success_result(self):
        result = self.buns.get_price()
        assert 90 == result, 'Вернулась неправильная цена'

    def test_get_ingredient_type_success_result(self):
        result = self.buns.get_type()
        assert INGREDIENT_TYPE_FILLING == result, 'Вернулся неправильный ингредиент'
