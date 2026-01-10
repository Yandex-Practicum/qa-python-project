import pytest


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient(self, burger_with_ingredients, index):
        initial_count = len(burger_with_ingredients.ingredients)
        ingredient = burger_with_ingredients.ingredients[index]
        burger_with_ingredients.remove_ingredient(index)
        assert len(burger_with_ingredients.ingredients) == initial_count - 1
        assert ingredient not in burger_with_ingredients.ingredients

    def test_move_ingredient(self, burger_with_ingredients):
        initial_ingredients = burger_with_ingredients.ingredients[:]
        burger_with_ingredients.move_ingredient(0, 2)
        assert burger_with_ingredients.ingredients[2] == initial_ingredients[0]

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_results = 2 * mock_bun.get_price() + mock_ingredient.get_price()
        assert burger.get_price() == expected_results

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient.get_type()} {mock_ingredient.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {mock_bun.get_price() * 2 + mock_ingredient.get_price()}"
        )
        assert receipt == expected_receipt

