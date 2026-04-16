import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
   
    def test_set_buns(self, mocker):
        #Проверяем, что set_buns корректно устанавливает булочку
        burger = Burger()
        mock_bun = mocker.Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_appends(self, mocker):
        #Проверяем, что add_ingredient добавляет ингредиент в список
        burger = Burger()
        mock_ingredient = mocker.Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_by_index(self, mocker):
        #Проверяем, что remove_ingredient удаляет ингредиент по индексу
        burger = Burger()
        ing1 = mocker.Mock(spec=Ingredient)
        ing2 = mocker.Mock(spec=Ingredient)
        burger.ingredients = [ing1, ing2]
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_move_ingredient_changes_order(self, mocker):
        #Проверяем, что move_ingredient перемещает ингредиент
        burger = Burger()
        ing1 = mocker.Mock(spec=Ingredient)
        ing2 = mocker.Mock(spec=Ingredient)
        ing3 = mocker.Mock(spec=Ingredient)
        burger.ingredients = [ing1, ing2, ing3]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1]

    def test_get_price_calculates_correct_total(self, mocker):
        #Проверяем, что get_price правильно считает цену булочки (x2) и ингредиентов
        burger = Burger()

        # Мокаем булочку
        mock_bun = mocker.Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        # Мокаем два ингредиента
        ing1 = mocker.Mock(spec=Ingredient)
        ing1.get_price.return_value = 50.0
        ing2 = mocker.Mock(spec=Ingredient)
        ing2.get_price.return_value = 75.5
        burger.ingredients = [ing1, ing2]

        expected_price = 100.0 * 2 + 50.0 + 75.5  #325.5
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_correct(self, mocker):
        #Проверяем, что get_receipt формирует правильный чек
        burger = Burger()

        mock_bun = mocker.Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        ing1 = mocker.Mock(spec=Ingredient)
        ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ing1.get_name.return_value = "hot sauce"
        ing1.get_price.return_value = 50.0

        ing2 = mocker.Mock(spec=Ingredient)
        ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ing2.get_name.return_value = "cutlet"
        ing2.get_price.return_value = 100.0

        burger.ingredients = [ing1, ing2]

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 350.0"
        )

        assert burger.get_receipt() == expected_receipt