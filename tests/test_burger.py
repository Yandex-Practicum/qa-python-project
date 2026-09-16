import pytest
from unittest.mock import Mock
from ..burger import Burger
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
        assert burger.bun.get_name() == "Test Bun"

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_price.return_value = 50.0
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert mock_ingredient1 in burger.ingredients
        assert mock_ingredient2 not in burger.ingredients
        assert mock_ingredient3 in burger.ingredients

    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

        with pytest.raises(IndexError):
            burger.remove_ingredient(-10)

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient, name="ing1")
        mock_ingredient2 = Mock(spec=Ingredient, name="ing2")
        mock_ingredient3 = Mock(spec=Ingredient, name="ing3")

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] is mock_ingredient2
        assert burger.ingredients[1] is mock_ingredient3
        assert burger.ingredients[2] is mock_ingredient1

    def test_move_ingredient_reverse(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient, name="ing1")
        mock_ingredient2 = Mock(spec=Ingredient, name="ing2")
        mock_ingredient3 = Mock(spec=Ingredient, name="ing3")

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(2, 0)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0] is mock_ingredient3
        assert burger.ingredients[1] is mock_ingredient1
        assert burger.ingredients[2] is mock_ingredient2

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50.0

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 75.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = 100.0 * 2 + 50.0 + 75.0 
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "White Bun"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "Hot Sauce"
        mock_ingredient1.get_price.return_value = 50.0

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "Cutlet"
        mock_ingredient2.get_price.return_value = 75.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()

        assert "(==== White Bun ====)" in receipt
        assert "= sauce Hot Sauce =" in receipt
        assert "= filling Cutlet =" in receipt
        assert "Price:" in receipt
