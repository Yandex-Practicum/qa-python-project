import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_init_success(self, burger):
        assert burger.bun == None and len(burger.ingredients) == 0

    def test_set_buns_bun_is_set(self, burger):
        bun = Bun(name = "Бриошь", price = 95.0)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_ingredient_appended(self, burger):
        ingredient = Ingredient(ingredient_type='SAUCE', name = "Шрирача", price = 30.0)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) > 0

    def test_remove_ingredient_deletes_ingredient(self, burger):
        cheese = Ingredient(ingredient_type='FILLING', name="Чеддер", price=15.0)
        greens = Ingredient(ingredient_type='FILLING', name="Салат Айсберг", price=10.0)
        bacon = Ingredient(ingredient_type='FILLING', name="Бекон", price=45.0)
        burger.add_ingredient(cheese)
        burger.add_ingredient(greens)
        burger.add_ingredient(bacon)
        burger.remove_ingredient(1)
        assert greens not in burger.ingredients and len(burger.ingredients) == 2

    def test_move_ingredient_position_changed(self, burger):
        cheese = Ingredient(ingredient_type='FILLING', name="Чеддер", price=15.0)
        greens = Ingredient(ingredient_type='FILLING', name="Салат Айсберг", price=10.0)
        bacon = Ingredient(ingredient_type='FILLING', name="Бекон", price=45.0)
        burger.add_ingredient(cheese)
        burger.add_ingredient(greens)
        burger.add_ingredient(bacon)
        burger.move_ingredient(1,2)
        assert burger.ingredients[2] == greens

    def test_get_price_returns_sum(self, burger):
        burger.bun = Bun(name = "С кунжутом", price = 40.0)
        cheese = Ingredient(ingredient_type='FILLING', name="Чеддер", price=15.0)
        bacon = Ingredient(ingredient_type='FILLING', name="Бекон", price=45.0)
        burger.add_ingredient(cheese)
        burger.add_ingredient(bacon)
        final_sum = burger.get_price()
        expected_sum = 40.0 * 2 + 15.0 + 45.0
        assert final_sum == expected_sum

    def test_get_receipt_returns_names(self, burger):
        burger.bun = Bun(name = "Бриошь", price = 90.0)
        cheese = Ingredient(ingredient_type='FILLING', name="Чеддер", price=15.0)
        burger.add_ingredient(cheese)
        final_sum = burger.get_price()
        receipt = burger.get_receipt()
        assert burger.bun.name and cheese.name and str(final_sum) in receipt



