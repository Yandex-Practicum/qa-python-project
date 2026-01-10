from burger import Burger
from unittest.mock import Mock, mock_open
import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_init(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns('white')
        assert burger.bun == 'white'

# проверяем не просто, что ингридиент добавлен в список, но и то, что он верно добавляет его в конец списка
    @pytest.mark.parametrize('ingredient1, ingredient2', [[INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING], [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]])
    def test_add_ingredient(self, ingredient1, ingredient2):
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.ingredients.index(ingredient2) == len(burger.ingredients) - 1

    def test_remove_ingredient(self):
        burger = Burger()
        burger.ingredients = [INGREDIENT_TYPE_SAUCE]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
        assert_index = burger.ingredients[1]
        burger.move_ingredient(1, 0)
        assert assert_index == burger.ingredients[0]

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 2.1

        mock_ingridient_1 = Mock()
        mock_ingridient_1.get_price.return_value = 3.1
        mock_ingridient_2 = Mock()
        mock_ingridient_2.get_price.return_value = 4.1

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingridient_1, mock_ingridient_2]

        assert burger.get_price() == 2.1*2 + 3.1 + 4.1

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "bun bun"
        mock_bun.get_price.return_value = 2.5

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = "sauce1"
        mock_ingredient_1.get_type.return_value = "filling"

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_name.return_value = "sauce2"
        mock_ingredient_2.get_type.return_value = "filling"

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]

        burger.get_price = Mock(return_value=5.0)

        receipt = burger.get_receipt()

        expected_receipt = "(==== bun bun ====)\n= filling sauce1 =\n= filling sauce2 =\n(==== bun bun ====)\n\nPrice: 5.0"

        assert receipt == expected_receipt