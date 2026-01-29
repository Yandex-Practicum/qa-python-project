import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.feature("Тестирование класса TestIngredient")
class TestIngredient:

    @allure.title("Проверка создания объектра класса Ingredient")
    def test_create_object_for_ingredient(self):
        ingredient_tst = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный', 1.4)
        ingredient_tst_type = ingredient_tst.type
        ingredient_tst_name = ingredient_tst.name
        ingredient_tst_price = ingredient_tst.price
        assert ingredient_tst_type == INGREDIENT_TYPE_SAUCE and ingredient_tst_name == 'Сырный' and ingredient_tst_price == 1.4, \
            f'Object values are: {ingredient_tst_type}, {ingredient_tst_name}, {ingredient_tst_price}'

    @allure.title("Проверка метода возврата стоимости")
    def test_get_ingredient_price(self):
        ingredient_tst = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный', 1.4)
        ingredient_tst_price = ingredient_tst.get_price()
        assert ingredient_tst_price == 1.4, f'ingredient_tst_price is: {ingredient_tst_price}'

    @allure.title("Проверка метода возврата имени")
    def test_get_ingredient_name(self):
        ingredient_tst = Ingredient(INGREDIENT_TYPE_FILLING, 'Куриная котлета', 2)
        ingredient_tst_name = ingredient_tst.get_name()
        assert ingredient_tst_name == 'Куриная котлета', f'ingredient_tst_name is: {ingredient_tst_name}'

    @allure.title("Проверка метода возврата типа наполнителя")
    def test_get_ingredient_type(self):
        ingredient_tst = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сырный', 500)
        ingredient_tst_type = ingredient_tst.get_type()
        assert ingredient_tst_type == INGREDIENT_TYPE_SAUCE, f'ingredient_tst_type is: {ingredient_tst_type}'
