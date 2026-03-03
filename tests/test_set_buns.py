from unittest.mock import Mock 
from unittest.mock import patch
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import Credentials

class TestSetBuns:

    '''
    Проверяется метод добавления булочек
    def set_buns(self, bun: Bun):
        self.bun = bun
    '''
    @pytest.mark.parametrize("bun_name, bun_price", zip(Credentials.bun_names, Credentials.bun_prices))
       
    def test_set_buns(self, bun_name, bun_price, create_mock_bun):
        
        bun_mock = create_mock_bun(bun_name, bun_price)
        burger = Burger()
        burger.set_buns(bun_mock)

        assert burger.bun is not None, "Булка не установлена"
        assert burger.bun.get_name() == bun_name, \
            f"Ожидалось имя булки '{bun_name}', получено '{burger.bun.get_name()}'"
        assert burger.bun.get_price() == bun_price,\
            f"Ожидалась цена булки '{bun_price}', получено '{burger.bun.get_price()}'"


