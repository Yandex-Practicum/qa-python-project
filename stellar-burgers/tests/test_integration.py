import pytest
from praktikum.burger import Burger
from praktikum.database import Database
from data import (
    BLACK_BUN_NAME, SAUCE_NAME, FILLING_NAME,
)


class TestBurgerAssembly:
    """Интеграционные тесты сборки бургера."""

    def test_complete_burger_creation_flow(self):
        """Тест полного процесса создания бургера."""
        db = Database()
        burger = Burger()

        # Получаем объекты из базы данных по имени
        selected_bun = next(b for b in db.available_buns() if b.get_name() == BLACK_BUN_NAME)
        selected_sauce = next(i for i in db.available_ingredients() if i.get_name() == SAUCE_NAME)
        selected_filling = next(i for i in db.available_ingredients() if i.get_name() == FILLING_NAME)

        burger.set_buns(selected_bun)
        burger.add_ingredient(selected_sauce)
        burger.add_ingredient(selected_filling)

        expected_price = selected_bun.get_price() * 2 + selected_sauce.get_price() + selected_filling.get_price()
        actual_price = burger.get_price()

        assert actual_price == expected_price

        receipt = burger.get_receipt()
        assert selected_bun.get_name() in receipt
        assert selected_sauce.get_name() in receipt
        assert selected_filling.get_name() in receipt
        assert str(expected_price) in receipt

    def test_burger_manipulation_operations(self):
        """Тест операций манипуляции с бургером."""
        db = Database()
        burger = Burger()

        white_bun = next(b for b in db.available_buns() if b.get_name() == "white bun")
        burger.set_buns(white_bun)

        sauce = next(i for i in db.available_ingredients() if i.get_name() == SAUCE_NAME)
        filling1 = next(i for i in db.available_ingredients() if i.get_name() == FILLING_NAME)
        filling2 = next(i for i in db.available_ingredients() if i.get_name() == "dinosaur")

        burger.add_ingredient(sauce)
        burger.add_ingredient(filling1)
        burger.add_ingredient(filling2)

        initial_price = burger.get_price()

        burger.move_ingredient(0, 2)
        assert burger.get_price() == initial_price

        burger.remove_ingredient(1)
        assert burger.get_price() < initial_price
