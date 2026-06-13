from data import *

class TestBurger:

    def test_burger_initially_empty(self, burger):
        """Бургер создаётся без булочки и ингредиентов."""
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_stores_bun(self, burger):
        """Бургер сохраняет переданную булочку."""
        bun = Bun(*TEST_BUN)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_buns_overwrites_previous_bun(self, burger):
        """Повторный вызов заменяет булочку."""
        bun1 = Bun(*TEST_BUN)
        bun2 = Bun(*TEST_BUN_2)
        burger.set_buns(bun1)
        burger.set_buns(bun2)
        assert burger.bun == bun2

    def test_add_ingredient_appends_to_list(self, burger):
        """Ингредиент добавляется в конец списка."""
        ingredient1 = Ingredient(*TEST_SAUCE)
        ingredient2 = Ingredient(*TEST_FILLING_1)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.ingredients == [ingredient1, ingredient2]

    def test_can_add_same_ingredient_multiple_times(self, burger):
        """Можно добавить один и тот же ингридиент несколько раз."""
        ingredient = Ingredient(*TEST_FILLING_1)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient, ingredient] and len(burger.ingredients) == 2

    def test_remove_ingredient_by_index(self, burger):
        """Удаление ингредиента по индексу."""
        ing1 = Ingredient(*TEST_SAUCE)
        ing2 = Ingredient(*TEST_FILLING_1)
        burger.ingredients = [ing1, ing2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_move_ingredient_changes_order(self, burger):
        """Перемещение меняет порядок ингредиентов."""
        ing1 = Ingredient(*TEST_SAUCE)
        ing2 = Ingredient(*TEST_FILLING_1)
        ing3 = Ingredient(*TEST_FILLING_2)
        burger.ingredients = [ing1, ing2, ing3]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1]

    def test_get_price(self, full_burger):
        """Проверка расчёта цены."""
        price = full_burger.get_price()
        assert price == 270.0

    def test_get_receipt_format(self, full_burger):
        """Проверка формата чека."""
        receipt = full_burger.get_receipt()
        expected_price = (TEST_BUN["price"] * 2 + TEST_SAUCE["price"] + TEST_FILLING_1["price"])
        expected = RECEIPT_TEMPLATE.format(
            bun=TEST_BUN["name"],
            sauce=TEST_SAUCE["name"],
            filling=TEST_FILLING_1["name"],
            price=expected_price
        )
        assert receipt == expected