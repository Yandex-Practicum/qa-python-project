import pytest
from praktikum.burger import Burger

class TestBurger:

    # Тесты для инициализации
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Тесты для set_buns
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты для add_ingredient
    def test_add_ingredient(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients['sauce'])
        burger.add_ingredient(mock_ingredients['veggie'])
        burger.add_ingredient(mock_ingredients['meat'])
        assert len(burger.ingredients) == 3
        assert burger.ingredients == mock_ingredients['all']

    # Тесты для remove_ingredient
    def test_remove_ingredient(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = [mock_ingredients['veggie'], mock_ingredients['sauce']]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients['sauce']

    # # Тесты для move_ingredient
    def test_move_ingredient(self, mock_ingredients):
        burger = Burger()
        ingredients = mock_ingredients['all']
        burger.ingredients = ingredients.copy()
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock_ingredients['veggie'], mock_ingredients['meat'], mock_ingredients['sauce']]

    # Тесты для get_price
    @pytest.mark.parametrize("ingredients, price", [
    (['veggie', 'meat'], 100*2 + 30 + 100),
    (['meat', 'meat'], 100*2 + 100*2),
    ])
    def test_get_price_with_bun_and_ingredients(self, mock_bun, mock_ingredients, ingredients, price):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredients[ingredients[0]], mock_ingredients[ingredients[1]]]
        assert burger.get_price() == price

    # Тесты для get_receipt
    def test_get_receipt_full(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredients['sauce']]
        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )
        assert burger.get_receipt() == expected