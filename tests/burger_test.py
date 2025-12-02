pytest_plugins = ['conftest']
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from conftest import create_mock_ingredient, create_mock_bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    # Проверка булочек
    def test_set_bun_success(self, burger, white_bun):
        burger.set_buns(white_bun)
        assert burger.bun == white_bun

    # Проверка замены булочки
    def test_set_bun_replace_existing(self, burger, white_bun, black_bun):
        burger.set_buns(white_bun)
        burger.set_buns(black_bun)
        assert burger.bun == black_bun

    # Проверка добавления одного ингредиента
    def test_add_ingredient_one(self, burger, sauce_ingredient):
        burger.add_ingredient(sauce_ingredient)
        assert len(burger.ingredients) == 1

    # Проверка добавления ингредиента в начало списка
    def test_add_ingredient_first_element(self, burger, sauce_ingredient):
        burger.add_ingredient(sauce_ingredient)
        assert burger.ingredients[0] == sauce_ingredient

    # Проверка добавления нескольких ингредиентов
    def test_add_ingredient_multiple(self, burger, ingredient_count):
        for i in range(ingredient_count):
            ingredient = create_mock_ingredient(f"Ingredient_{i}", INGREDIENT_TYPE_SAUCE, 50.0)
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == ingredient_count

    # Проверка сохранения порядка при добавлении (первый элемент)
    def test_add_ingredient_keeps_order_first(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.ingredients[0] == sauce_ingredient

    # Проверка сохранения порядка при добавлении (второй элемент)
    def test_add_ingredient_keeps_order_second(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.ingredients[1] == filling_ingredient

    # Проверка уменьшения количества при удалении
    def test_remove_ingredient_decreases_count(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    # Проверка удаления первого ингредиента оставляет второй
    def test_remove_ingredient_first_leaves_second(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ing2

    # Проверка удаления среднего ингредиента
    def test_remove_ingredient_middle(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Middle", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Last", INGREDIENT_TYPE_SAUCE, 75.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.remove_ingredient(1)
        assert burger.ingredients[1] == ing3

    # Проверка удаления ингредиента по индексу
    def test_remove_ingredient_at_index(self, burger, move_positions):
        from_pos, to_pos = move_positions
        for i in range(3):
            ing = create_mock_ingredient(f"Ing_{i}", INGREDIENT_TYPE_SAUCE, 50.0)
            burger.add_ingredient(ing)
        burger.remove_ingredient(from_pos)
        assert len(burger.ingredients) == 2

    # Проверка перемещения ингредиента вперёд
    def test_move_ingredient_forward(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == ing1

    # Проверка изменения первой позиции при перемещении
    def test_move_ingredient_changes_first_position(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ing2

    # Проверка перемещения ингредиента назад
    def test_move_ingredient_backward(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == ing3

    # Проверка сохранения количества при перемещении
    def test_move_ingredient_preserves_count(self, burger, move_positions):
        from_pos, to_pos = move_positions
        for i in range(3):
            ing = create_mock_ingredient(f"Ing_{i}", INGREDIENT_TYPE_SAUCE, 50.0)
            burger.add_ingredient(ing)
        burger.move_ingredient(from_pos, to_pos)
        assert len(burger.ingredients) == 3

    # Проверка цены только булки
    def test_price_only_bun(self, burger, white_bun):
        burger.set_buns(white_bun)
        assert burger.get_price() == 200.0

    # Проверка цены булки и одного ингредиента
    def test_price_bun_and_one_ingredient(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        assert burger.get_price() == 290.0

    # Проверка цены булки и двух ингредиентов
    def test_price_bun_and_two_ingredients(self, burger, white_bun, sauce_ingredient, filling_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.get_price() == 390.0

    # Проверка цены различных комбинаций
    def test_price_various_combinations(self, burger, price_combinations):
        bun_price, ing_prices, expected_price = price_combinations
        bun = create_mock_bun("Test Bun", bun_price)
        burger.set_buns(bun)
        for price in ing_prices:
            ing = create_mock_ingredient("Test Ing", INGREDIENT_TYPE_SAUCE, price)
            burger.add_ingredient(ing)
        assert burger.get_price() == expected_price

    # Проверка уменьшения цены при удалении ингредиента
    def test_remove_ingredient_decreases_price(self, burger, white_bun):
        burger.set_buns(white_bun)
        ing1 = create_mock_ingredient("Item1", INGREDIENT_TYPE_SAUCE, 100.0)
        ing2 = create_mock_ingredient("Item2", INGREDIENT_TYPE_FILLING, 150.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        price_before = burger.get_price()
        burger.remove_ingredient(0)
        price_after = burger.get_price()
        assert price_after == price_before - 100.0

    # Проверка цены после перемещения ингредиента
    def test_burger_move_and_get_price(self, burger, white_bun):
        burger.set_buns(white_bun)
        ing1 = create_mock_ingredient("Item1", INGREDIENT_TYPE_SAUCE, 100.0)
        ing2 = create_mock_ingredient("Item2", INGREDIENT_TYPE_FILLING, 150.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        price = burger.get_price()
        assert price == 450.0

    # Проверка наличия булки в чеке
    def test_receipt_contains_bun(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        receipt = burger.get_receipt()
        assert "(==== White Bun ====)" in receipt

    # Проверка наличия ингредиента в чеке
    def test_receipt_contains_ingredient(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        receipt = burger.get_receipt()
        assert "spicy sauce" in receipt

    # Проверка наличия цены в чеке
    def test_receipt_contains_price(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        receipt = burger.get_receipt()
        assert "Price:" in receipt

    # Проверка отображения всех ингредиентов в чеке
    def test_receipt_shows_all_ingredients(self, burger, white_bun):
        burger.set_buns(white_bun)
        ing1 = create_mock_ingredient("Item_0", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Item_1", INGREDIENT_TYPE_SAUCE, 50.0)
        ing3 = create_mock_ingredient("Item_2", INGREDIENT_TYPE_SAUCE, 50.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        receipt = burger.get_receipt()
        assert "Item_0" in receipt

    # Проверка соответствия цены в чеке и методе get_price
    def test_receipt_price_matches_get_price(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        receipt = burger.get_receipt()
        expected_price = burger.get_price()
        assert f"Price: {expected_price}" in receipt

    # Проверка чека без ингредиентов
    def test_receipt_zero_ingredients(self, burger, white_bun):
        burger.set_buns(white_bun)
        receipt = burger.get_receipt()
        assert "(==== White Bun ====)" in receipt

    # Проверка чека с одним ингредиентом
    def test_receipt_one_ingredient(self, burger, white_bun):
        burger.set_buns(white_bun)
        ing = create_mock_ingredient("Ing_0", INGREDIENT_TYPE_SAUCE, 25.0)
        burger.add_ingredient(ing)
        receipt = burger.get_receipt()
        assert "Price:" in receipt

    # Проверка чека с тремя ингредиентами
    def test_receipt_three_ingredients(self, burger, white_bun):
        burger.set_buns(white_bun)
        for i in range(3):
            ing = create_mock_ingredient(f"Ing_{i}", INGREDIENT_TYPE_SAUCE, 25.0)
            burger.add_ingredient(ing)
        receipt = burger.get_receipt()
        assert "Price:" in receipt

    # Проверка чека с пятью ингредиентами
    def test_receipt_five_ingredients(self, burger, white_bun):
        burger.set_buns(white_bun)
        for i in range(5):
            ing = create_mock_ingredient(f"Ing_{i}", INGREDIENT_TYPE_SAUCE, 25.0)
            burger.add_ingredient(ing)
        receipt = burger.get_receipt()
        assert "Price:" in receipt

    # Проверка добавления и удаления ингредиента
    def test_burger_add_and_remove_ingredient(self, burger, white_bun, sauce_ingredient):
        burger.set_buns(white_bun)
        burger.add_ingredient(sauce_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0