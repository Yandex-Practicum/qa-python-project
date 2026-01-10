from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBun:
    def ingredient(self):
        ingredient = Ingredient()
        return ingredient

    def ingredient_types_one(self):
        ingredient_types_one = INGREDIENT_TYPE_SAUCE()
        return ingredient_types_one

    def ingredient_types_two(self):
        ingredient_types_two = INGREDIENT_TYPE_FILLING()
        return ingredient_types_two

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
