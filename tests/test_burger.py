import pytest
import allure
from praktikum.burger import Burger

class TestBurger:

    def test_buns_set(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredients):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        assert burger.ingredients == mock_ingredients

    def test_remove_ingredient(self, mock_ingredients):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        burger.remove_ingredient(2)
        assert burger.ingredients == [mock_ingredients[0], mock_ingredients[1], mock_ingredients[3]]

    @pytest.mark.parametrize("index, index_2, index_3, index_4", [
        (0, 1, 2, 3),
        (3, 1, 2, 0),
    ])
    def test_move_ingredient(self, index, index_2, index_3, index_4, mock_ingredients):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        moved_ingredient = burger.ingredients[index]
        burger.move_ingredient(index, index_4)
        assert burger.ingredients[index_4] == moved_ingredient

    def test_get_price(self, mock_bun, mock_ingredients):
        mock_bun.get_price.return_value = 988
        mock_ingredients[0].get_price.return_value = 3000
        mock_ingredients[1].get_price.return_value = 15
        mock_ingredients[2].get_price.return_value = 4400
        mock_ingredients[3].get_price.return_value = 4142

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        burger.add_ingredient(mock_ingredients[2])
        burger.add_ingredient(mock_ingredients[3])

        price = 988 * 2 + 3000 + 15 + 4400 + 4142
        assert burger.get_price() == price

    def test_get_receipt(self, mock_bun, mock_ingredients):
        mock_bun.get_name.return_value = "Флюоресцентная булка"
        mock_ingredients[0].get_type.return_value = "FILLING"
        mock_ingredients[0].get_name.return_value = "Говяжий метеорит"
        mock_ingredients[1].get_type.return_value = "SAUCE"
        mock_ingredients[1].get_name.return_value = "Соус традиционный галактический"
        mock_ingredients[2].get_type.return_value = "FILLING"
        mock_ingredients[2].get_name.return_value = "Мини-салат Экзо-Плантаго"
        mock_ingredients[3].get_type.return_value = "FILLING"
        mock_ingredients[3].get_name.return_value = "Сыр с астероидной плесенью"

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        burger.add_ingredient(mock_ingredients[2])
        burger.add_ingredient(mock_ingredients[3])

        receipt = burger.get_receipt()
        final_recept = (
            '(==== Флюоресцентная булка ====)\n'
            '= filling Говяжий метеорит =\n'
            '= sauce Соус традиционный галактический =\n'
            '= filling Мини-салат Экзо-Плантаго =\n'
            '= filling Сыр с астероидной плесенью =\n'
            '(==== Флюоресцентная булка ====)\n\n'
            'Price: 13533'
        )
        assert receipt == final_recept
