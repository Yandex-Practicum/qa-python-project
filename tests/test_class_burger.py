import unittest
from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger(unittest.TestCase):
    """Тесты для класса Burger. Один тест — одна проверка."""

    def setUp(self):
        """Подготовка данных для каждого теста."""
        self.burger = Burger()

        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "black bun"
        self.mock_bun.get_price.return_value = 100.0

        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_name.return_value = "cutlet"
        self.mock_ingredient1.get_price.return_value = 100.0
        self.mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING

        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_name.return_value = "hot sauce"
        self.mock_ingredient2.get_price.return_value = 50.0
        self.mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        self.mock_ingredient3 = Mock(spec=Ingredient)
        self.mock_ingredient3.get_name.return_value = "dinosaur"
        self.mock_ingredient3.get_price.return_value = 200.0
        self.mock_ingredient3.get_type.return_value = INGREDIENT_TYPE_FILLING

    # ============ __init__ ============

    def test_initialization_bun_is_none(self):
        """Проверка, что при инициализации булочка не задана."""
        self.assertIsNone(self.burger.bun)

    def test_initialization_ingredients_is_empty(self):
        """Проверка, что при инициализации список ингредиентов пуст."""
        self.assertEqual(self.burger.ingredients, [])

    def test_initialization_ingredients_is_list(self):
        """Проверка, что список ингредиентов — это list."""
        self.assertIsInstance(self.burger.ingredients, list)

    # ============ set_buns ============

    def test_set_buns_sets_bun_correctly(self):
        """Проверка установки булочки."""
        self.burger.set_buns(self.mock_bun)
        self.assertEqual(self.burger.bun, self.mock_bun)

    def test_set_buns_updates_bun(self):
        """Проверка обновления булочки."""
        self.burger.set_buns(self.mock_bun)
        new_bun = Mock(spec=Bun)
        new_bun.get_name.return_value = "white bun"
        self.burger.set_buns(new_bun)
        self.assertEqual(self.burger.bun, new_bun)

    def test_set_buns_none(self):
        """Проверка установки булочки в None."""
        self.burger.set_buns(None)
        self.assertIsNone(self.burger.bun)

    # ============ add_ingredient ============

    def test_add_ingredient_appends_to_list(self):
        """Проверка добавления ингредиента в конец списка."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.assertEqual(len(self.burger.ingredients), 1)

    def test_add_ingredient_stores_correct_object(self):
        """Проверка, что добавленный ингредиент сохранён по индексу 0."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_add_ingredient_multiple_count(self):
        """Проверка количества после добавления нескольких ингредиентов."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(len(self.burger.ingredients), 3)

    def test_add_ingredient_multiple_first(self):
        """Проверка первого элемента после добавления нескольких ингредиентов."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_add_ingredient_multiple_second(self):
        """Проверка второго элемента после добавления нескольких ингредиентов."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)

    def test_add_ingredient_multiple_third(self):
        """Проверка третьего элемента после добавления нескольких ингредиентов."""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    # ============ remove_ingredient ============

    def test_remove_ingredient_by_index_count(self):
        """Проверка количества после удаления ингредиента по индексу."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 2)

    def test_remove_ingredient_by_index_first(self):
        """Проверка первого элемента после удаления по индексу."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_remove_ingredient_by_index_second(self):
        """Проверка второго элемента после удаления по индексу."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.remove_ingredient(1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)

    def test_remove_ingredient_first_element_count(self):
        """Проверка количества после удаления первого ингредиента."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        self.assertEqual(len(self.burger.ingredients), 1)

    def test_remove_ingredient_first_element_value(self):
        """Проверка значения оставшегося элемента после удаления первого."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)

    def test_remove_ingredient_last_element_count(self):
        """Проверка количества после удаления последнего ингредиента."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        self.assertEqual(len(self.burger.ingredients), 1)

    def test_remove_ingredient_last_element_value(self):
        """Проверка значения оставшегося элемента после удаления последнего."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_remove_ingredient_from_empty_list(self):
        """Проверка удаления ингредиента из пустого списка."""
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(0)

    def test_remove_ingredient_out_of_range(self):
        """Проверка удаления ингредиента с индексом вне диапазона."""
        self.burger.ingredients = [self.mock_ingredient1]
        with self.assertRaises(IndexError):
            self.burger.remove_ingredient(5)

    def test_remove_ingredient_negative_index_count(self):
        """Проверка количества после удаления с отрицательным индексом."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        self.assertEqual(len(self.burger.ingredients), 1)

    def test_remove_ingredient_negative_index_value(self):
        """Проверка значения оставшегося элемента после удаления с отрицательным индексом."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.remove_ingredient(-1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    # ============ move_ingredient ============

    def test_move_ingredient_forward_count(self):
        """Проверка количества после перемещения вперёд."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(len(self.burger.ingredients), 3)

    def test_move_ingredient_forward_first(self):
        """Проверка первого элемента после перемещения вперёд."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)

    def test_move_ingredient_forward_second(self):
        """Проверка второго элемента после перемещения вперёд."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)

    def test_move_ingredient_forward_third(self):
        """Проверка третьего элемента после перемещения вперёд."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(2, 0)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_backward_count(self):
        """Проверка количества после перемещения назад."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(len(self.burger.ingredients), 3)

    def test_move_ingredient_backward_first(self):
        """Проверка первого элемента после перемещения назад."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)

    def test_move_ingredient_backward_second(self):
        """Проверка второго элемента после перемещения назад."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)

    def test_move_ingredient_backward_third(self):
        """Проверка третьего элемента после перемещения назад."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(0, 2)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient1)

    def test_move_ingredient_to_same_index_count(self):
        """Проверка количества при перемещении на тот же индекс."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.move_ingredient(1, 1)
        self.assertEqual(len(self.burger.ingredients), 2)

    def test_move_ingredient_to_same_index_first(self):
        """Проверка первого элемента при перемещении на тот же индекс."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.move_ingredient(1, 1)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_move_ingredient_to_same_index_second(self):
        """Проверка второго элемента при перемещении на тот же индекс."""
        self.burger.ingredients = [self.mock_ingredient1, self.mock_ingredient2]
        self.burger.move_ingredient(1, 1)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient2)

    def test_move_ingredient_to_beginning_first(self):
        """Проверка первого элемента после перемещения в начало."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient2)

    def test_move_ingredient_to_beginning_second(self):
        """Проверка второго элемента после перемещения в начало."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 0)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)

    def test_move_ingredient_to_beginning_third(self):
        """Проверка третьего элемента после перемещения в начало."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 0)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient3)

    def test_move_ingredient_to_end_first(self):
        """Проверка первого элемента после перемещения в конец."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 2)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient1)

    def test_move_ingredient_to_end_second(self):
        """Проверка второго элемента после перемещения в конец."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 2)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient3)

    def test_move_ingredient_to_end_third(self):
        """Проверка третьего элемента после перемещения в конец."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(1, 2)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    def test_move_ingredient_from_empty_list(self):
        """Проверка перемещения ингредиента в пустом списке."""
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(0, 1)

    def test_move_ingredient_index_out_of_range(self):
        """Проверка перемещения с индексом вне диапазона."""
        self.burger.ingredients = [self.mock_ingredient1]
        with self.assertRaises(IndexError):
            self.burger.move_ingredient(5, 0)

    def test_move_ingredient_negative_index_first(self):
        """Проверка первого элемента после перемещения с отрицательным индексом."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(-1, 0)
        self.assertEqual(self.burger.ingredients[0], self.mock_ingredient3)

    def test_move_ingredient_negative_index_second(self):
        """Проверка второго элемента после перемещения с отрицательным индексом."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(-1, 0)
        self.assertEqual(self.burger.ingredients[1], self.mock_ingredient1)

    def test_move_ingredient_negative_index_third(self):
        """Проверка третьего элемента после перемещения с отрицательным индексом."""
        self.burger.ingredients = [
            self.mock_ingredient1,
            self.mock_ingredient2,
            self.mock_ingredient3,
        ]
        self.burger.move_ingredient(-1, 0)
        self.assertEqual(self.burger.ingredients[2], self.mock_ingredient2)

    # ============ get_price ============

    def test_get_price_with_bun_and_ingredients(self):
        """Проверка расчета цены с булочкой и ингредиентами."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.assertEqual(self.burger.get_price(), 350.0)

    def test_get_price_without_bun(self):
        """Проверка расчета цены без булочки (AttributeError)."""
        self.burger.add_ingredient(self.mock_ingredient1)
        with self.assertRaises(AttributeError):
            self.burger.get_price()

    def test_get_price_without_ingredients(self):
        """Проверка расчета цены только с булочкой."""
        self.burger.set_buns(self.mock_bun)
        self.assertEqual(self.burger.get_price(), 200.0)

    def test_get_price_with_real_ingredient_objects(self):
        """Проверка расчета цены с реальными объектами ингредиентов."""
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30.0)

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        self.assertEqual(self.burger.get_price(), 380.0)

    # ============ get_receipt ============

    def test_get_receipt_with_bun_and_ingredients(self):
        """Проверка формирования чека с булочкой и ингредиентами."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 350.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_without_ingredients(self):
        """Проверка формирования чека только с булочкой."""
        self.burger.set_buns(self.mock_bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)

    def test_get_receipt_calls_bun_get_name(self):
        """Проверка, что чек вызывает get_name у булочки."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_name.assert_called()

    def test_get_receipt_calls_bun_get_price(self):
        """Проверка, что чек вызывает get_price у булочки."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_bun.get_price.assert_called()

    def test_get_receipt_calls_ingredient_get_name(self):
        """Проверка, что чек вызывает get_name у ингредиента."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_ingredient1.get_name.assert_called()

    def test_get_receipt_calls_ingredient_get_type(self):
        """Проверка, что чек вызывает get_type у ингредиента."""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)

        self.burger.get_receipt()

        self.mock_ingredient1.get_type.assert_called()

    def test_get_receipt_with_real_ingredients(self):
        """Проверка формирования чека с реальными объектами."""
        real_bun = Bun("red bun", 150.0)
        real_ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)
        real_ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)

        self.burger.set_buns(real_bun)
        self.burger.add_ingredient(real_ingredient1)
        self.burger.add_ingredient(real_ingredient2)

        expected_receipt = (
            "(==== red bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== red bun ====)\n"
            "\n"
            "Price: 450.0"
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)


if __name__ == "__main__":
    unittest.main()