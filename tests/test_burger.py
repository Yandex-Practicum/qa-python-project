from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from helpers import Helpers


class TestBurger:

    # Проверка выбора булочки
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка добавления ингредиента
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Проверка удаления ингредиента
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == Data.LEN_REMOVE_INGREDIENT

    # Проверка перемещения ингредиента
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_two = Mock()
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one

    # Проверка итоговой цены бургера
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = Data.MOCK_BUN_PRICE_VALUE
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = Data.MOCK_INGREDIENT_PRICE_VALUE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = Helpers()
        price_receipt = price.price_receipt()
        assert burger.get_price() == price_receipt

    # Проверка получения чека
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = Data.MOCK_BUN_NAME_VALUE
        mock_bun.get_price.return_value = Data.MOCK_BUN_PRICE_VALUE
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = Data.MOCK_INGREDIENT_NAME_VALUE
        mock_ingredient.get_type.return_value = Data.MOCK_INGREDIENT_TYPE_VALUE
        mock_ingredient.get_price.return_value = Data.MOCK_INGREDIENT_PRICE_VALUE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result_receipt = (
            "(==== white bun ====)\n"
            "= sauce chili sauce =\n"
            "(==== white bun ====)\n"
            "\nPrice: 700")
        assert burger.get_receipt() == expected_result_receipt
