import pytest
from praktikum.burger import Burger
from helpers.helpers import BurgerTestData as TestData
from helpers.helpers import BurgerTestInitData as TestInitData


class TestBurger:
    @pytest.mark.parametrize('test_param', [
        'bun',
        'ingredients'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        burger = Burger()
        assert getattr(burger, test_param) == getattr(TestInitData, test_param)

    def test_setter_buns(self):
        burger = Burger()
        burger.set_buns(TestData.exempl_bun)
        assert getattr(burger, 'bun') == TestData.exempl_bun

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        assert getattr(burger, 'ingredients') == [TestData.exempl_ingred]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        burger.remove_ingredient(0)
        assert getattr(burger, 'ingredients') == []

    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        burger.add_ingredient(TestData.exempl_ingred_sec)
        burger.move_ingredient(1, 0)
        assert getattr(burger, 'ingredients')[0] == TestData.exempl_ingred_sec

    def test_get_price_bun_x_2(self):
        burger = Burger()
        burger.set_buns(TestData.exempl_bun)
        assert burger.get_price() == TestData.exempl_bun.get_price()*2

    def test_get_prise_sum_ingrdients_n_bun(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        burger.add_ingredient(TestData.exempl_ingred_sec)
        burger.set_buns(TestData.exempl_bun)
        assert burger.get_price() == TestData.exempl_ingred.get_price()+TestData.exempl_ingred_sec.get_price()+TestData.exempl_bun.get_price()*2

    def test_get_receipt(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        burger.add_ingredient(TestData.exempl_ingred_sec)
        burger.set_buns(TestData.exempl_bun)
        assert burger.get_receipt() == TestData.gen_receipt(TestData.exempl_bun, [TestData.exempl_ingred, TestData.exempl_ingred_sec])
