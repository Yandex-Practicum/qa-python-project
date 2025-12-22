from data import BurgerIngredients


class TestBun:
    def test_bun_get_name(self, create_bun):
        assert create_bun.get_name() == BurgerIngredients.TEST_BUN_NAME

    def test_bun_get_price(self, create_bun):
        assert create_bun.get_price() == BurgerIngredients.TEST_BUN_PRICE
