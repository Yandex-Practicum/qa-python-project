from unittest.mock import patch, Mock

import allure

from burger import Burger
from data import BUN_NAME, BUN_PRICE, BUN2_NAME, BUN2_PRICE, SAUCE_PRICE, FILLING_PRICE, BurgerGetPrice


class TestBurger:

    @allure.title('check bun set: add 1 bun')
    def test_set_buns(self, setup_bun):
        burger = Burger()
        mock_bun = setup_bun
        burger.set_buns(mock_bun)

        assert (burger.bun is not None and
                burger.bun.name == BUN_NAME and
                burger.bun.price == BUN_PRICE)

    @allure.title('check bun set: add 2 buns')
    def test_set_buns2(self, setup_bun, setup_bun2):
        burger = Burger()
        mock_bun = setup_bun
        burger.set_buns(mock_bun)
        mock_bun2 = setup_bun2
        burger.set_buns(mock_bun2)

        assert (burger.bun is not None and
                burger.bun.name == BUN2_NAME and
                burger.bun.price == BUN2_PRICE)

    @allure.title('get_price() - buns and two ingredients')
    @allure.description('check correct price is returned')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 1:    [True, True, True, 400]  # булки и 2 ингредиента
    def test_get_price_with_buns_sauce_filling(self,
                       mock_ingredient_class,
                       mock_bun_class):

        mock_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()
        mock_bun.get_price.return_value = BUN_PRICE
        mock_sauce.get_price.return_value = SAUCE_PRICE
        mock_filling.get_price.return_value = FILLING_PRICE
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)


        assert burger.get_price() == BurgerGetPrice.BUNS_SAUCE_FILLING_PRICE      # = 400

