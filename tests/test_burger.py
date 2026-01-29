import pytest
from praktikum.burger import Burger
from data import Data

class TestBurger:
    def test_burger_set_buns(mock_bun):
        """Проверяем set_buns: устанавливает bun."""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, mock_ingredient_factory):
        """Проверяем add_ingredient: добавляет ингредиент."""
        ingredient = mock_ingredient_factory(Data.sauces[0], Data.sauces[1], Data.sauces[2])
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    @pytest.mark.parametrize("initial_names, index, expected_names", [
        (["A", "B", "C"], 1, ["A", "C"]),
        (["A"], 0, []),
    ])
    def test_burger_remove_ingredient(self, mock_ingredient_factory, initial_names, index, expected_names):
        """Проверяем remove_ingredient: удаляет ингредиент по индексу."""
        burger = Burger()
        for name in initial_names:
            burger.add_ingredient(mock_ingredient_factory(Data.fillings[0], name, Data.fillings[2]))
        burger.remove_ingredient(index)
        result_names = [ing.get_name() for ing in burger.ingredients]
        assert result_names == expected_names

    @pytest.mark.parametrize("initial_names, index, new_index, expected_names", [
        (["A", "B", "C"], 0, 2, ["B", "C", "A"]),
        (["A", "B"], 1, 0, ["B", "A"]),
    ])
    def test_burger_move_ingredient(self, mock_ingredient_factory, initial_names, index, new_index, expected_names):
        """Проверяем move_ingredient: перемещает ингредиент."""
        burger = Burger()
        for name in initial_names:
            burger.add_ingredient(mock_ingredient_factory(Data.fillings[0], name, Data.fillings[2]))
        burger.move_ingredient(index, new_index)
        result_names = [ing.get_name() for ing in burger.ingredients]
        assert result_names == expected_names

    @pytest.mark.parametrize("ingredients_data, expected_price", [
        ([], 1976.0),
        ([(Data.sauces[0], "hot sauce", 100.0)], 2076.0),
        ([(Data.fillings, "cutlet", 100.0), (Data.sauces, "chili sauce", 300.0)], 2376.0),
    ])
    def test_burger_get_price(self, mock_ingredient_factory, mock_bun, ingredients_data, expected_price):
        """Проверяем get_price: считает цену (bun * 2 + ингредиенты)."""
        burger = Burger()
        burger.set_buns(mock_bun)
        for create_ingredient in ingredients_data:
            burger.add_ingredient(mock_ingredient_factory(create_ingredient[0],create_ingredient[1],create_ingredient[2]))
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ingredients_data, expected_receipt", [
        ([], "(==== Test Bun ====)\n(==== Test Bun ====)\n\nPrice: 1976"),
        ([(Data.sauces[0], "hot sauce", 100.0)], "(==== Test Bun ====)\n= sauce hot sauce =\n(==== Test Bun ====)\n\nPrice: 2076.0"),
    ])
    def test_burger_get_receipt(self, mock_ingredient_factory,mock_bun, ingredients_data, expected_receipt):
        """Проверяем get_receipt: формирует чек."""
        burger = Burger()
        burger.set_buns(mock_bun)
        for ingredient_type, name, price in ingredients_data:
            burger.add_ingredient(mock_ingredient_factory(ingredient_type, name, price))
        assert burger.get_receipt() == expected_receipt