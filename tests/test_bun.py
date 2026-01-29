import pytest
from praktikum.bun import Bun
from data import DataBurgerIngredients


class TestBun:

    # Проверяем "имя" выбираемой булочки с корректными данными на входе
    @pytest.mark.parametrize("bun_name, bun_price", DataBurgerIngredients.data_buns)
    def test_get_name_bun_correct_name(self, bun_name, bun_price):
        expected_bun_name = bun_name
        bun = Bun(bun_name, bun_price)
        actual_bun_name = bun.get_name()

        assert actual_bun_name == expected_bun_name

    # Проверяем цену булочки с корректными данными на входе
    @pytest.mark.parametrize("bun_name, bun_price", DataBurgerIngredients.data_buns)
    def test_get_price_correct_price(self, bun_name, bun_price):
        expected_bun_price = bun_price
        bun = Bun(bun_name, bun_price)
        actual_bun_price = bun.get_price()

        assert actual_bun_price == expected_bun_price
