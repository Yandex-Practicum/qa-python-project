from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:
    """
    Тесты для класса Burger, который представляет бургер.
    """

    def test_set_buns(self) -> None:
        """
        Тестирует метод set_buns(), который задаёт булочку для бургера.
        """
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun, "Булочка не была правильно установлена"

    def test_add_ingredients(self) -> None:
        """
        Тестирует метод add_ingredient(), добавляющий ингредиент в бургер.
        """
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1, "Ингредиент не был добавлен"
        assert burger.ingredients[0].get_name() == 'cutlet'
        assert burger.ingredients[0].get_price() == 100
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self) -> None:
        """
        Тестирует метод remove_ingredient(), удаляющий ингредиент из бургера.
        """
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0, "Ингредиент не был удалён"

    def test_get_price(self) -> None:
        """
        Тестирует метод get_price(), рассчитывающий общую стоимость бургера.
        """
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        expected_price = 800
        assert burger.get_price() == expected_price, f"Цена бургера должна быть {expected_price}"

    def test_get_receipt(self) -> None:
        """
        Тестирует метод get_receipt(), который возвращает описание бургера.
        """
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[2])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        expected_result = (
            "(==== red bun ====)\n"
            "= sauce hot sauce =\n"
            "= sauce sour cream =\n"
            "= sauce chili sauce =\n"
            "(==== red bun ====)\n\n"
            "Price: 1200"
        )
        assert burger.get_receipt() == expected_result, "Квитанция не совпадает с ожидаемой"

    def test_move_ingredient(self) -> None:
        """
        Тестирует метод move_ingredient(), который перемещает ингредиенты в списке.
        """
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_price.return_value = 100
        mock_ingredient_one.get_name.return_value = 'cutlet'
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING

        mock_ingredient_second = Mock()
        mock_ingredient_second.get_price.return_value = 300
        mock_ingredient_second.get_name.return_value = 'sausage'
        mock_ingredient_second.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_second)

        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2, "Ингредиенты потеряны после перемещения"
        assert burger.ingredients[0] == mock_ingredient_second, "Ингредиенты не поменялись местами"
        assert burger.ingredients[1] == mock_ingredient_one

    def test_move_ingredient_out_of_bounds(self) -> None:
        """
        Проверяет обработку выхода за пределы списка в методе move_ingredient().
        """
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError, match="list index out of range"):
            burger.move_ingredient(0, 2)
