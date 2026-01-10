from unittest.mock import MagicMock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_get_price(self, empty_burger):
        # цена бургера только с булкой = цена булки * 2
        assert empty_burger.get_price() == 200

    def test_add_ingredient(self, empty_burger):
        ing = MagicMock()
        ing.get_type.return_value = INGREDIENT_TYPE_FILLING
        ing.get_name.return_value = "cutlet"
        ing.get_price.return_value = 100

        empty_burger.add_ingredient(ing)

        # проверяем только, что добавился ингредиент
        assert empty_burger.ingredients[0].get_name() == "cutlet"

    def test_remove_ingredient(self, empty_burger):
        ing = MagicMock()
        ing.get_name.return_value = "cutlet"
        ing.get_price.return_value = 100
        empty_burger.add_ingredient(ing)

        empty_burger.remove_ingredient(0)

        # проверяем только, что список пуст (ингредиент удалён)
        assert len(empty_burger.ingredients) == 0

    def test_move_ingredient(self, empty_burger):
        ing1 = MagicMock()
        ing1.get_name.return_value = "ketchup"
        ing2 = MagicMock()
        ing2.get_name.return_value = "cutlet"
        ing3 = MagicMock()
        ing3.get_name.return_value = "mayo"

        empty_burger.add_ingredient(ing1)
        empty_burger.add_ingredient(ing2)
        empty_burger.add_ingredient(ing3)

        empty_burger.move_ingredient(2, 0)

        # проверяем только порядок
        assert [i.get_name() for i in empty_burger.ingredients] == ["mayo", "ketchup", "cutlet"]

    def test_get_receipt(self, empty_burger):
        ing1 = MagicMock()
        ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ing1.get_name.return_value = "ketchup"
        ing1.get_price.return_value = 10
        empty_burger.add_ingredient(ing1)

        receipt = empty_burger.get_receipt()

        expected_receipt = (
            "(==== white bun ====)\n"
            "= sauce ketchup =\n"
            "(==== white bun ====)\n"
            "Price: 110"
        )

        assert receipt == expected_receipt
