import pytest
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_set_buns_is_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_is_success(self, burger, mock_ingredient_1):
        burger.add_ingredient(mock_ingredient_1)

        assert mock_ingredient_1 in burger.ingredients

    def test_remove_ingredient_is_success(self, burger, mock_ingredient_1, mock_ingredient_2):
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_ingredient_2]

    @pytest.mark.parametrize(
            "index, new_index, expected_indexes",
            [
                (0, 1, [1, 0]),
                (1, 0, [1, 0]),
                (0, 0, [0, 1]),
                (1, 1, [0, 1])
            ]
    )
    def test_move_ingredient_is_success(self, burger, index, new_index, expected_indexes):

        first_ingredient = Ingredient("FILLING", "dinosaur", 200)
        second_ingredient = Ingredient("SAUCE", "hot sauce", 200)

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        ingredients_list = [first_ingredient, second_ingredient]

        burger.move_ingredient(index, new_index)
        
        expected_order = [ingredients_list[i] for i in expected_indexes]

        assert burger.ingredients == expected_order

    def test_get_price_with_bun_and_ingredients_is_success(self, burger, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        expected_cost = mock_bun.get_price.return_value * 2
        expected_cost += mock_ingredient_1.get_price.return_value + mock_ingredient_2.get_price.return_value

        assert burger.get_price() == expected_cost


    def test_get_receipt_is_success(self, burger, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        receipt = burger.get_receipt()

        expected_receipt = (
            '(==== red bun ====)\n'
            '= filling dinosaur =\n'
            '= sauce hot sauce =\n'
            '(==== red bun ====)\n'
            '\n'
            'Price: 1000'
        )

        assert receipt == expected_receipt
