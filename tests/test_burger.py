import pytest
from practikum.burger import Burger
from practikum.bun import Bun
from practikum.ingredient import Ingredient


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Sesame", 1.5)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("Cheese", "Беконайзер", 2.0)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат", 0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Удаляем первый ингредиент
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат",0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Перемещаем второй ингредиент на первое место
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Sesame", 1.5)
        ingredient1 = Ingredient("Cheese", "Сыр", 2.0)
        ingredient2 = Ingredient("Lettuce", "Салат", 0.5)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Проверяем общую цену (булочка * 2 + ингредиенты)
        assert burger.get_price() == 1.5 * 2 + 2.0 + 0.5
