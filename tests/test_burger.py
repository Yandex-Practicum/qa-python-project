from praktikum.burger import Burger
from conftest import *
import pytest


class TestBurger:
    def test_set_buns_success(self, mock_for_the_first_bun):
        burger = Burger()
        burger.set_buns(mock_for_the_first_bun)
        assert burger.bun == mock_for_the_first_bun

    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Data.SAUCES_NAME, Data.SAUCES_NAME],
        [Data.FILLING_NAME, Data.FILLING_NAME],
        [Data_1.FILLING_NAME, Data_1.FILLING_NAME]
    ]
                             )
    def test_add_ingredient_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Data.SAUCES_NAME, Data.SAUCES_NAME],
        [Data_1.FILLING_NAME, Data_1.FILLING_NAME]
    ]
                             )
    def test_remove_ingredient_success(self, ingredients, removed_ingredient, mock_filling_for_the_first_bun):
        burger = Burger()
        burger.add_ingredient(mock_filling_for_the_first_bun)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling_for_the_first_bun in burger.ingredients

    def test_move_ingredient_success(self, mock_sauce_for_the_first_bun, mock_filling_for_the_first_bun):
        burger = Burger()
        burger.add_ingredient(mock_sauce_for_the_first_bun)
        burger.add_ingredient(mock_filling_for_the_first_bun)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling_for_the_first_bun and burger.ingredients[
            1] == mock_sauce_for_the_first_bun

    def test_get_price_burger_success(self, mock_for_the_second_bun, mock_sauce_for_second_bun,
                                      mock_filling_for_the_second_bun):
        burger = Burger()
        mock_for_the_second_bun.get_price.return_value = Data_1.PRICE_BUNS
        mock_sauce_for_second_bun.get_price.return_value = Data_1.SAUCES_PRICE
        mock_filling_for_the_second_bun.get_price.return_value = Data_1.FILLING_PRICE
        burger.set_buns(mock_for_the_second_bun)
        burger.add_ingredient(mock_sauce_for_second_bun)
        burger.add_ingredient(mock_filling_for_the_second_bun)
        expected_price = 2 * Data_1.PRICE_BUNS + Data_1.SAUCES_PRICE + Data_1.FILLING_PRICE
        assert burger.get_price() == expected_price

    def test_get_receipt_with_first_set_of_ingredients(self, mock_for_the_first_bun, mock_sauce_for_the_first_bun,
                                                       mock_filling_for_the_first_bun, mock_filling_for_the_second_bun):
        burger = Burger()
        burger.set_buns(mock_for_the_first_bun)
        burger.add_ingredient(mock_sauce_for_the_first_bun)
        burger.add_ingredient(mock_filling_for_the_first_bun)
        burger.add_ingredient(mock_filling_for_the_second_bun)

        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус фирменный Space Sauce =\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
