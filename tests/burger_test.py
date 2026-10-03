from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    # 1. Тест установки булочки
    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # 2. Тест добавления ингредиента — проверка наличия
    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    # 3. Тест добавления ингредиента — проверка длины списка
    def test_add_ingredient_increases_list_length(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    # 4. Тест удаления ингредиента — проверка отсутствия
    def test_remove_ingredient_removes_from_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    # 5. Тест удаления ингредиента — проверка длины
    def test_remove_ingredient_decreases_list_length(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # 6. Тест перемещения ингредиентов — проверка первого элемента
    def test_move_ingredient_first_position(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ing_2

    # 7. Тест перемещения ингредиентов — проверка второго элемента
    def test_move_ingredient_second_position(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ing_1

    # 8. Тест расчета стоимости
    def test_get_price_calculates_total_cost(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250.0

    # 9. Тест печати чека
    def test_get_receipt_returns_formatted_string(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "Марсианская булка"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Chili"
        mock_ingredient.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== Марсианская булка ====)\n"
            "= sauce Chili =\n"
            "(==== Марсианская булка ====)\n"
            "\n"
            "Price: 250.0"
        )

        assert burger.get_receipt() == expected_receipt