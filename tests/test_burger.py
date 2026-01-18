import unittest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger(unittest.TestCase):
    def setUp(self):
        self.burger = Burger()
        self.bun = Mock(spec=Bun)
        self.ingredient = Mock(spec=Ingredient)

    def test_set_buns(self):
        # Проверяем, что булочка устанавливается корректно
        self.burger.set_buns(self.bun)
        self.assertEqual(self.burger.bun, self.bun)

    def test_add_ingredient(self):
        # Проверяем добавление ингредиента
        self.burger.add_ingredient(self.ingredient)
        self.assertIn(self.ingredient, self.burger.ingredients)

    def test_remove_ingredient(self):
        # Добавляем ингредиент и затем удаляем его
        self.burger.add_ingredient(self.ingredient)
        index = self.burger.ingredients.index(self.ingredient)
        self.burger.remove_ingredient(index)
        self.assertNotIn(self.ingredient, self.burger.ingredients)

    def test_move_ingredient(self):
        # Добавляем два ингредиента и перемещаем их
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.burger.move_ingredient(0, 1)
        self.assertEqual(self.burger.ingredients, [ingredient2, ingredient1])

    def test_get_price(self):
        # Проверяем расчёт цены
        self.bun.get_price.return_value = 10.0
        self.ingredient.get_price.return_value = 5.0
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient)
        price = self.burger.get_price()
        self.assertEqual(price, 25.0)

    def test_get_receipt(self):
        # Проверяем генерацию чека
        self.bun.get_name.return_value = "Classic Bun"
        self.ingredient.get_type.return_value = "Meat"
        self.ingredient.get_name.return_value = "Beef"

        # Устанавливаем булочку перед генерацией чека
        self.burger.set_buns(self.bun)

        # Добавляем ингредиент в бургер
        self.burger.add_ingredient(self.ingredient)

        # Добавляем настройку для метода get_price
        self.bun.get_price.return_value = 10.0  # Пример значения цены булочки
        self.ingredient.get_price.return_value = 5.0  # Добавляем настройку цены для ингредиента

        receipt = self.burger.get_receipt()
        expected_receipt = "(==== Classic Bun ====)\n= meat Beef =\n(==== Classic Bun ====)\n\nPrice: 25.0"
        self.assertEqual(receipt, expected_receipt)

if __name__ == '__main__':
    unittest.main()




    
