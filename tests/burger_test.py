from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import constants

class TestBurger:

    # создает булочку и проверяет, что булочка создалась
    def test_set_buns_create_one_bun(self, bun, burger):
        burger.set_buns(bun=bun)
        assert burger.bun == bun

    # создает соус и проверяет, что первый элемент в списке ингредиентов это созданный соус
    def test_add_ingredient_one_ingredient(self, ingredient, burger):
        burger.add_ingredient(ingredient=ingredient)
        assert burger.ingredients[0] == ingredient

    # создает соус, добавляет его в список ингредиентов, удаляет его, проверяет, что список пуст
    def test_remove_ingredient(self, ingredient, burger):
        burger.add_ingredient(ingredient=ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # добавляет 2 ингредиента в список, меняет местами первый элемент со вторым и проверяет это
    def test_move_ingredient_move_first_to_second(self, burger):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1,0)
        assert burger.ingredients[0] == mock_ingredient_2

    # создает бургер, проверяет цену бургера
    def test_get_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 400

    # создает бургер, проверяет текст рецепта бургера
    def test_get_receipt(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = constants.PUDGE_BUN

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = constants.MEAT_SAUCE

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_receipt() == constants.RECEIPT_TEXT



