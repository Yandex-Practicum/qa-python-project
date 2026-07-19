from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:
    def test_create_burger_success(self):
        burger = Burger()
        assert burger.bun is None
        assert isinstance(burger.ingredients, list)
        assert len(burger.ingredients) == 0

    def test_set_bun_success(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_success(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient1
        assert burger.ingredients[1] == ingredient3

    def test_move_ingredient_forward(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(2, 1)

        expected = [ingredient1, ingredient3, ingredient2]
        assert burger.ingredients == expected

    def test_get_price_success(self):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 30

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.get_price() == 280.0

    def test_get_receipt_success(self):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = "SAUCE"
        mock_ingredient1.get_name.return_value = "ketchup"
        mock_ingredient1.get_price.return_value = 50

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = "FILLING"
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 150

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce ketchup =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 400" in receipt
        assert receipt.count("(==== black bun ====)") == 2