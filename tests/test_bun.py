from praktikum.bun import Bun
import ingredient_types


class TestBun:

    bun = Bun(ingredient_types.BUN_NAME, ingredient_types.BUN_PRICE)

    def test_get_name_bun(self):

        assert self.bun.get_name() == ingredient_types.BUN_NAME

    def test_get_price_bun(self):

        assert self.bun.get_price() == ingredient_types.BUN_PRICE

    def test_name_of_bun_true(self):

        assert self.bun.name == ingredient_types.BUN_NAME
