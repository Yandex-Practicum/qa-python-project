from unittest.mock import Mock

from practicum.bun import Bun
from practicum.ingredient import Ingredient


class TestBurger:

    def test_burger_initialize(self, burger):
        # Проверяем начальную инициализацию объекта Burger
        assert burger.bun is None, "Поле bun должно быть равно None"
        assert isinstance(burger.ingredients, list) and len(burger.ingredients) == 0, ("Поле ingredients - пустой "
                                                                                       "массив из Ingredient")
        for ingredient in burger.ingredients:
            assert isinstance(ingredient, Ingredient), "Поле ingredients - пустой массив из Ingredient"

    def test_set_buns(self, burger):
        # Проверяем выбор булки для бургера
        bun = Bun("Имя", 100)
        burger.set_buns(bun)
        assert burger.bun == bun, "Ошибка при выборе булки!"

    def test_add_ingredients(self, burger, two_indegrients):
        # Проверяем добавление ингредиентов для бургера
        ingredient_one, ingredient_two = two_indegrients
        burger.add_ingredient(ingredient_one)
        assert burger.ingredients == [ingredient_one] and len(burger.ingredients) == 1, "Ошибка добавления ингридиента!"
        burger.add_ingredient(ingredient_two)
        assert burger.ingredients == [ingredient_one, ingredient_two] and len(
            burger.ingredients) == 2, "Ошибка добавления ингридиента!"

    def test_remove_ingredients(self, burger, two_indegrients):
        # Проверяем удаление ингредиентов для бургера
        ingredient_one, ingredient_two = two_indegrients
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_two] and len(
            burger.ingredients) == 1, "Ошибка при удалении ингридиента!"

    def test_move_ingredients(self, burger, two_indegrients):
        ingredient_one, ingredient_two = two_indegrients
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_two, ingredient_one], "Ошибка при замене места ингридиента!"

    def test_get_price(self, burger, two_indegrients):
        bun = Bun("Имя", 100)
        burger.set_buns(bun)
        ingredient_one, ingredient_two = two_indegrients
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        assert burger.get_price() == 400

    def test_get_reciept(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "Тестовая булка"
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "TEST"
        mock_ingredient.get_name.return_value = "Тестовый ингредиент"
        mock_ingredient.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_receipt() == ('(==== Тестовая булка ====)\n'
                                        '= test Тестовый ингредиент =\n'
                                        '(==== Тестовая булка ====)\n'
                                        '\n'
                                        'Price: 300'), "В рецепте содержатся ошибки!"
