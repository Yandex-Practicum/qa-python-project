from data import EXPECTED_RECEIPT
from praktikum.burger import Burger

class TestBurger:

    # Тест инициализации бургера
    def test_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Тест добавления булочки
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тест добавления ингредиента
    def test_add_ingredient(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    # Тест удаления ингредиента
    def test_remove_ingredient(self, prepared_burger):
        initial_count = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_count - 1

    # Тест перемещения ингредиента
    def test_move_ingredient(self, prepared_burger):
        first_ingredient = prepared_burger.ingredients[0]
        prepared_burger.move_ingredient(0, 1)
        assert prepared_burger.ingredients[1] == first_ingredient

    # Тест расчёта цены
    def test_get_price(self, prepared_burger):
        # 100 (булка) * 2 + 50 (соус) + 30 (начинка) = 280
        assert prepared_burger.get_price() == 280

    # Тест генерации чека
    def test_get_receipt(self, prepared_burger):
        assert prepared_burger.get_receipt() == EXPECTED_RECEIPT
