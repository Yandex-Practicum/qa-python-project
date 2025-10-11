import pytest

from data.burger_data import RECEIPT_TEST_DATA, BUN_PRICE, INGREDIENT_PRICE, PRICE_TEST_DATA
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Белая булка", 100)

        burger.set_buns(bun)

        assert burger.bun == bun
        assert burger.bun.get_name() == "Белая булка"
        assert burger.bun.get_price() == 100

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("SAUCE", "Сырный соус", 50.0)

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient
        assert burger.ingredients[0].get_name() == "Сырный соус"
        assert burger.ingredients[0].get_price() == 50.0
        assert burger.ingredients[0].get_type() == "SAUCE"

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "Сырный соус", 50.0)
        ingredient2 = Ingredient("FILLING", "Говядина", 150.0)
        ingredient3 = Ingredient("SAUCE", "Острый соус", 60.0)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ingredient1, ingredient3]
        assert burger.ingredients[0].get_name() == "Сырный соус"
        assert burger.ingredients[1].get_name() == "Острый соус"

    def test_move_ingredient(self):
        burger = Burger()
        cheese = Ingredient("SAUCE", "Сырный", 50)
        beef = Ingredient("FILLING", "Говядина", 150)
        chili = Ingredient("SAUCE", "Острый", 60)

        burger.add_ingredient(cheese)
        burger.add_ingredient(beef)
        burger.add_ingredient(chili)

        # перемещаем ингредиент с индексом 0 (Сырный) на позицию 2
        burger.move_ingredient(0, 2)

        assert len(burger.ingredients) == 3
        assert burger.ingredients[0].get_name() == "Говядина"
        assert burger.ingredients[1].get_name() == "Острый"
        assert burger.ingredients[2].get_name() == "Сырный"

    @pytest.mark.parametrize("bun_price,ingredients_data,expected_price", PRICE_TEST_DATA)
    def test_get_price(self, bun_price, ingredients_data, expected_price):
        burger = Burger()
        burger.set_buns(Bun("Тестовая булка", bun_price))

        for ingredient_type, name, price in ingredients_data:
            burger.add_ingredient(Ingredient(ingredient_type, name, price))

        actual_price = burger.get_price()

        assert actual_price == expected_price

    @pytest.mark.parametrize(
        "bun_name,ingredients_data,expected_receipt",
        RECEIPT_TEST_DATA
    )
    def test_get_receipt(self, bun_name, ingredients_data, expected_receipt):
        # Подготовка
        burger = Burger()
        burger.set_buns(Bun(bun_name, BUN_PRICE))

        for ingredient_type, name in ingredients_data:
            burger.add_ingredient(Ingredient(ingredient_type, name, INGREDIENT_PRICE))

        # Действие
        receipt = burger.get_receipt()

        # Проверка
        assert receipt == expected_receipt
