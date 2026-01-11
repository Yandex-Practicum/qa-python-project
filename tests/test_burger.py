from unittest.mock import Mock, patch

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_true(self):
        bun = Bun('black bun', 100)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize(
        'type, name, price',
        [
            [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
            [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
            [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
            [INGREDIENT_TYPE_FILLING, "cutlet", 100],
            [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
            [INGREDIENT_TYPE_FILLING, "sausage", 300]
        ]
    )
    def test_add_ingredient_true(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_true(self):
        burger = Burger()
        ingredient = [INGREDIENT_TYPE_SAUCE, "hot sauce", 100]
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient_true(self):
        burger = Burger()
        database = Database()
        list_of_ingr = database.available_ingredients()
        for i in list_of_ingr:
            burger.add_ingredient(i)
        last_index = len(burger.ingredients)-1
        last_value = burger.ingredients[last_index]
        burger.move_ingredient(last_index, 0)

        assert burger.ingredients[0] == last_value

    def test_get_price_true(self):
        burger = Burger()
        bun = Bun("white bun", 200)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == 900

    def test_get_receipt_true(self):
        burger = Burger()
        bun = Bun("red bun", 300)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert '(==== red bun ====)' in burger.get_receipt()
        assert '= sauce sour cream =' in burger.get_receipt()
        assert '= filling sausage =' in burger.get_receipt()

    def test_get_price_true_mock(self):
        mock_bun = Mock()# создаю мок объекта булки
        mock_ingredient_1 = Mock()#создаю мок объекта одного ингредиента
        mock_ingredient_2 = Mock()#создаю мок объекта другого ингредиента
        burger = Burger()#создаю объект бургера
        burger.set_buns(mock_bun)#вместо реальной булки передаю объект мока, чтобы потом для него вызвать метод гет прайс
        burger.add_ingredient(mock_ingredient_1)#вместо реального ингредиента передаю объект мока ингредиента, чтобы потом для него вызвать гет прайс
        burger.add_ingredient(mock_ingredient_2)
        mock_bun.get_price.return_value = 100
        mock_ingredient_1.get_price.return_value = 300
        mock_ingredient_2.get_price.return_value = 500
        assert burger.get_price() == 1000



    def test_get_receipt_true_mock(self):
        mock_bun = Mock()  # создаю мок объекта булки
        mock_ingredient_1 = Mock()  # создаю мок объекта одного ингредиента
        mock_ingredient_2 = Mock()  # создаю мок объекта другого ингредиента
        burger = Burger()  # создаю объект бургера
        burger.set_buns(mock_bun)  # вместо реальной булки передаю объект мока, чтобы потом для него вызвать метод гет прайс
        burger.add_ingredient(mock_ingredient_1)  # вместо реального ингредиента передаю объект мока ингредиента, чтобы потом для него вызвать гет прайс
        burger.add_ingredient(mock_ingredient_2)
        mock_bun.get_name.return_value = "red bun"
        mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_1.get_name.return_value = "sausage"
        mock_ingredient_2.get_name.return_value = "sour cream"
        mock_bun.get_price.return_value = 100
        mock_ingredient_1.get_price.return_value = 300
        mock_ingredient_2.get_price.return_value = 500
        assert '(==== red bun ====)' in burger.get_receipt()
        assert '= sauce sour cream =' in burger.get_receipt()
        assert '= filling sausage =' in burger.get_receipt()







