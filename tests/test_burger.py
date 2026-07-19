import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    # === set_buns ===
    def test_set_buns(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        assert burger.bun == bun

    # === add_ingredient ===
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "cutlet"
        ingredient.get_price.return_value = 100
        ingredient.get_type.return_value = "FILLING"

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    # === remove_ingredient ===
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    # === move_ingredient ===
    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        ing3 = Mock(spec=Ingredient)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing3
        assert burger.ingredients[2] == ing1

    # === get_price (с моками) ===
    def test_get_price(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 100 * 2 + 50 + 50 == 300

    # === get_price с параметризацией ===
    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [50, 50], 300),
        (200, [100], 500),
        (150, [30, 40, 50], 420),
    ])
    def test_get_price_parametrized(self, bun_price, ing_prices, expected):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ing_prices:
            ing = Mock(spec=Ingredient)
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    # === get_receipt ===
    def test_get_receipt(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = "FILLING"
        ingredient.get_name.return_value = "cutlet"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 250" in receipt  # 100*2 + 50

    # === get_receipt пустой бургер (проверка, что нет ошибок) ===
    def test_get_receipt_empty_burger(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "white bun"
        bun.get_price.return_value = 200
        burger.set_buns(bun)

        receipt = burger.get_receipt()
        assert "(==== white bun ====)" in receipt
        assert "Price: 400" in receipt

        # === get_receipt с несколькими ингредиентами ===
    def test_get_receipt_with_multiple_ingredients(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ing1 = Mock(spec=Ingredient)
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "hot sauce"
        ing1.get_price.return_value = 50

        ing2 = Mock(spec=Ingredient)
        ing2.get_type.return_value = "FILLING"
        ing2.get_name.return_value = "cutlet"
        ing2.get_price.return_value = 100

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 350" in receipt  # 100*2 + 50 + 100

    # === get_price только с булкой (без ингредиентов) ===
    def test_get_price_only_bun(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 150
        burger.set_buns(bun)

        assert burger.get_price() == 300

    # === get_receipt без ингредиентов (только булка) ===
    def test_get_receipt_no_ingredients(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "red bun"
        bun.get_price.return_value = 120
        burger.set_buns(bun)

        receipt = burger.get_receipt()
        assert "(==== red bun ====)" in receipt
        assert "Price: 240" in receipt

    # === move_ingredient на тот же индекс (граничный случай) ===
    def test_move_ingredient_same_index(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 0)

        assert burger.ingredients[0] == ing1
        assert burger.ingredients[1] == ing2


        