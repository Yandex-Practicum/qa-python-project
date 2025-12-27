import sys
sys.path.insert(0,"C:/Users/alekberovalf/PycharmProjects/Diplom_1/")

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
class TestIngredient:

    # Тест на получение цены соуса
    def test_get_price(self):
        price_sauces = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90.0)
        assert price_sauces.get_price() == 90

    # Тест на получение соуса
    def test_get_name(self):
        name_sauces = Ingredient(INGREDIENT_TYPE_SAUCE,'Соус Spicy-X', 90.0)
        assert name_sauces.get_name() == 'Соус Spicy-X'

    # Тест на получение типа ингредиента (соус или начинка)

    def test_get_type(self):
        type_ingredient = Ingredient('Начинка', 'Мясо бессмертных моллюсков Protostomia', 1337.0)
        assert type_ingredient.get_type() == 'Начинка'
