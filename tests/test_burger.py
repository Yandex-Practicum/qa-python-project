from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self):
        # Создаём экземпляр булочки с мокированными методами
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 5.0
        bun.get_name.return_value = "Classic"

        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 2.0
        ingredient.get_name.return_value = "Lettuce"
        ingredient.get_type.return_value = "filling"

        burger = Burger()
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient = Mock(spec=Ingredient)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)

        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 5.0

        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 2.0

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 12.0  # цена булочки * 2 + цена ингредиента

    def test_get_receipt(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 5.0
        bun.get_name.return_value = "Classic"

        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "Lettuce"
        ingredient.get_type.return_value = "filling"
        ingredient.get_price.return_value = 2.0

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt().strip()

        receipt_lines = [line for line in receipt.split('\n') if line.strip()]  # Убираем пустые строки

        # Проверяем каждую строку чека отдельно
        assert receipt_lines[0] == "(==== Classic ====)"
        assert receipt_lines[1] == "= filling Lettuce ="
        assert receipt_lines[2] == "(==== Classic ====)"
        assert receipt_lines[3] == "Price: 12.0"