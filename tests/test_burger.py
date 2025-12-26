import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    #1 тест на проверку что bun инициализируется как None
    def test_burger_init_bun_initialization_is_none(self):
        burger = Burger()
        assert burger.bun is None

    #2 тест на проверку что ingredients инициализируется как пустой список
    def test_burger_init_ingredients_initialization_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    #3 тест на проверку что метод set_buns определяет булочку в бургере
    def test_burger_set_buns_has_correct_name(self):
        burger = Burger()
        bun = Bun('spicy bun', 150)
        burger.set_buns(bun)
        assert burger.bun == bun

    #4 тест на проверку что метод add_ingredient добавляет ингредиент в бургер
    def test_burger_add_ingredient_in_burger_is_successful(self):
        burger = Burger()
        ingredient = Ingredient('sauce', 'spicy sauce', 55)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    #5 тест на проверку что метод revome_ingredient удаляет ингредиент из бургера
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_burger_remove_ingredient_in_burger_is_successful(self, index):
        burger = Burger()
        ingredient_1 = Ingredient('sauce', 'spicy sauce', 55)
        ingredient_2 = Ingredient('filling', 'meat filling', 105)
        ingredient_3 = Ingredient('sauce', 'cheese sauce', 65)
        burger.ingredients = [ingredient_1, ingredient_2, ingredient_3]
        removed_ingredient = burger.ingredients[index]
        burger.remove_ingredient(index)
        assert removed_ingredient not in burger.ingredients

    #6 тест на проверку что метод move_ingredient изменяет позицию ингредиента в бургере
    def test_burger_move_ingredient_in_burger_is_successful(self):
        burger = Burger()
        ingredient_1 = Ingredient('sauce', 'spicy sauce', 55)
        ingredient_2 = Ingredient('filling', 'meat filling', 105)
        ingredient_3 = Ingredient('sauce', 'cheese sauce', 65)
        burger.ingredients = [ingredient_1, ingredient_2, ingredient_3]
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [ingredient_3, ingredient_1, ingredient_2]

    #7 тест на проверку что корректно работает метод get_price бургера
    def test_burger_get_price_is_successful(self, bun_mock, ingredients_mock):
        expected_price = 0
        burger = Burger()
        burger.bun = bun_mock
        expected_price += 2 * burger.bun.get_price()
        burger.ingredients = ingredients_mock
        for ingredient in burger.ingredients:
            expected_price += ingredient.get_price()
        assert burger.get_price() == expected_price

    #8 тест на проверку что корректно работает метод get_receipt бургера
    def test_burger_get_receipt_is_successful(self, bun_mock, ingredients_mock):
        expected_receipt = ''
        burger = Burger()
        burger.bun = bun_mock
        expected_receipt += f'(==== {burger.bun.get_name()} ====)\n'
        burger.ingredients = ingredients_mock
        for ingredient in burger.ingredients:
            expected_receipt += f'= {(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
        expected_receipt += f'(==== {burger.bun.get_name()} ====)\n\n'
        expected_receipt += f'Price: {burger.get_price()}'
        assert burger.get_receipt() == expected_receipt
