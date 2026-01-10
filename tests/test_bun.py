from praktikum.bun import Bun
from data import IngredientData

class TestBun:

    def test_get_name(self):
        bun = Bun(name=IngredientData.BUN_NAME, price=IngredientData.BUN_PRICE)
        assert bun.get_name() == IngredientData.BUN_NAME, f"Название булки должно быть '{IngredientData.BUN_NAME}'."

    def test_get_price(self):
        bun = Bun(name=IngredientData.BUN_NAME, price=IngredientData.BUN_PRICE)
        assert bun.get_price() == IngredientData.BUN_PRICE, f"Цена булки должна быть '{IngredientData.BUN_PRICE}'."