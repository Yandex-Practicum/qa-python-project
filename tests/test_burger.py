import pytest
from praktikum.burger import Burger
from data import Burger_Info
from unittest.mock import Mock


class TestBurger:
    @pytest.mark.parametrize('bun_name, bun_price', [
        (Burger_Info.Bun_1, Burger_Info.Price_Bun),
        (Burger_Info.Bun_2, Burger_Info.Price_Bun),
])
    def test_set_buns(self, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == bun_name and burger.bun.get_price() == bun_price, "Булка установлена неправильно"

    @pytest.mark.parametrize('ingredient_name, ingredient_price', [
        (Burger_Info.Sauce, Burger_Info.Price_Sauce),
        (Burger_Info.Filling, Burger_Info.Price_Filling),
])
    def test_add_ingredient(self, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_name() == ingredient_name and burger.ingredients[
            0].get_price() == ingredient_price, "Ингредиент добавлен неправильно"

    @pytest.mark.parametrize('bun_price, ingredient_price, expected_price', [
        (Burger_Info.Price_Bun, Burger_Info.Price_Sauce, Burger_Info.Price_Bun * 2 + Burger_Info.Price_Sauce),
        (Burger_Info.Price_Bun, Burger_Info.Price_Filling, Burger_Info.Price_Bun * 2 + Burger_Info.Price_Filling),
])
    def test_get_price(self, bun_price, ingredient_price, expected_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price, "Цена бургера рассчитана неверно"

    def test_remove_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = Burger_Info.Sauce
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_name.return_value = Burger_Info.Filling

        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.remove_ingredient(0)

        assert burger.ingredients[0].get_name() == Burger_Info.Filling, "Ингредиент не был удален правильно"

    def test_move_ingredient(self):

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_name.return_value = Burger_Info.Sauce
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_name.return_value = Burger_Info.Filling

        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0].get_name() == Burger_Info.Filling and burger.ingredients[
            1].get_name() == Burger_Info.Sauce, "Ингредиенты не были перемещены правильно"

    def test_bun_name_ingredient_name_and_price_in_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = Burger_Info.Bun_1
        mock_bun.get_price.return_value = Burger_Info.Price_Bun

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = Burger_Info.Sauce
        mock_ingredient.get_type.return_value = "sauce"
        mock_ingredient.get_price.return_value = Burger_Info.Price_Sauce

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        bun_in_receipt = Burger_Info.Bun_1 in receipt
        ingredient_in_receipt = f"= sauce {Burger_Info.Sauce} =" in receipt
        expected_price = Burger_Info.Price_Bun * 2 + Burger_Info.Price_Sauce
        price_in_receipt = f"Price: {expected_price}" in receipt

        assert bun_in_receipt and ingredient_in_receipt and price_in_receipt, f"Чек сформирован неверно: {receipt}"

