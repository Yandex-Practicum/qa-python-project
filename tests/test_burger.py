import pytest
from praktikum.burger import Burger
import data
import logging
logging.basicConfig(level=logging.INFO)


class TestBurger:

    def test_set_buns_burger_true(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == mock_bun.name

    def test_add_ingredient_one_true(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        logging.info(f'\nКоличество ингридиентов в бургере: {len(burger.ingredients)}')

    def test_add_ingredient_two_true(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 2
        logging.info(f'\nКоличество ингридиентов в бургере: {len(burger.ingredients)}')

    def test_remove_ingredient_from_list_true(self, burger):
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        logging.info(f'\nКоличество ингридиентов в бургере: {len(burger.ingredients)}')

    def test_remove_ingredient_from_clear_list_error(self, burger):
        burger.remove_ingredient(1)
        burger.remove_ingredient(0)
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
        logging.info(f'\nКоличество ингредиентов в бургере: {len(burger.ingredients)}')
        assert len(burger.ingredients) == 0

    def test_move_ingredient_two_ingredient_true(self, burger):
        logging.info(f'\nИнгридиент до перемещения: {burger.ingredients[1].name}')
        burger.move_ingredient(0, 1)
        logging.info(f'\nИнгридиент после перемещения:{burger.ingredients[1].name}')
        assert burger.ingredients[1].name == data.INGREDIENT_NAME_FILLING

    def test_move_ingredient_index_const_true(self, burger):
        logging.info(f'\nИнгридиент до перемещения: {burger.ingredients[1].name}')
        burger.move_ingredient(1, 1)
        logging.info(f'\nИнгридиент после перемещения:{burger.ingredients[1].name}')
        assert burger.ingredients[1].name == data.INGREDIENT_NAME_SAUCE

    def test_move_ingredient_not_ingredients_error(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)
        assert len(burger.ingredients) == 0

    def test_get_price_full_burger_true(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 360
        logging.info(f'\nСтоимость нашего бургера = {burger.get_price()}')

    def test_get_price_burger_is_not_bun_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()
        assert len(burger.ingredients) == 2

    def test_get_price_burger_is_not_ingredients_true(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == 100
        logging.info(f'\nСтоимость бургера состоящего только из булок = {burger.get_price()}')

    def test_get_receipt_full_burger_true(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert (data.BUN_NAME and data.INGREDIENT_NAME_SAUCE and
                data.INGREDIENT_NAME_FILLING and "Price" in burger.get_receipt())
        logging.info(f'\nРецепт нашего бургера:\n{burger.get_receipt()}')

    def test_get_receipt_burger_is_empty_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
        assert len(burger.ingredients) == 0
        logging.info(f'\nБургер без булки - это не бургер!')

    def test_get_receipt_burger_is_not_ingredients_true(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert (data.BUN_NAME and "Price" in burger.get_receipt())
        logging.info(f'\nРецепт нашего бургера:\n{burger.get_receipt()}'
                     f'\nВы уверены, что Вам этого достаточно?')
