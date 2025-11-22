import pytest
from practikum.burger import Burger
from practikum.bun import Bun
from practikum.constants import TB_NAME_BUN, TB_ING_CHEESE_NAME, TB_ING_CHEESE_PRICE, TB_ING_SAUSE_NAME, \
    TB_ING_SAUSE_PEICE, \
    TB_PRICE_BUN, TB_ING_CUTLET_NAME, TB_ING_CUTLET_PRICE, EXPECTED_RECEIPT
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurder:
    # Создаем фикстуру для тестовых объектов булочек и ингредиентов
    @pytest.fixture
    def setup_burger(self):
        bun = Bun(TB_NAME_BUN, TB_PRICE_BUN)
        cheese = Ingredient(INGREDIENT_TYPE_FILLING, TB_ING_CHEESE_NAME, TB_ING_CHEESE_PRICE)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, TB_ING_SAUSE_NAME, TB_ING_SAUSE_PEICE)
        cutlet = Ingredient(INGREDIENT_TYPE_FILLING, TB_ING_CUTLET_NAME, TB_ING_CUTLET_PRICE)

        burger = Burger()
        burger.set_buns(bun)
        return burger, bun, cheese, cutlet, sauce

    #тест метода set_buns() для установки булочек
    def test_set_buns(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        assert burger.bun.get_name() == TB_NAME_BUN, "Метод get_buns() возвращает неверное имя."
        assert burger.bun.get_price() == TB_PRICE_BUN, "Метод get_buns() возвращает неверную цену."

    #тест метода add_ingredient() для добавления ингредиентов
    def test_add_ingredient(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        burger.add_ingredient(cheese)
        burger.add_ingredient(cutlet)
        assert len(burger.ingredients) == 2 , "Количество ингредиентов не соответствует проверяемому значению."
        assert burger.ingredients[0].get_name() == TB_ING_CHEESE_NAME, "Метод add_ingredient() не добавил элемент."
        assert burger.ingredients[1].get_name() == TB_ING_CUTLET_NAME, "Метод add_ingredient() не добавил элемент."

    #тест для метода  remove_ingredient()
    def test_remove_ingredient(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        burger.add_ingredient(cheese)
        burger.add_ingredient(cutlet)
        burger.remove_ingredient(0)  # Удаляем первый ингредиент (сheese)
        assert len(burger.ingredients) == 1 , "Количество ингредиентов не соответствует проверяемому значению."
        assert burger.ingredients[0].get_name() == TB_ING_CUTLET_NAME, "На позиции [0], нет проверяемого элемента."


    #тест метода move_ingredient(), который меняет порядок позиций в списке ингредиентов
    def test_move_ingredient_reposition_ing_at_new_position(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        burger.add_ingredient(cheese)
        burger.add_ingredient(cutlet)
        burger.move_ingredient(0, 1)  # Перемещаем Cheese на вторую позицию
        assert burger.ingredients[0].get_name() == TB_ING_CUTLET_NAME, "На позиции [0], нет проверяемого элемента."
        assert burger.ingredients[1].get_name() == TB_ING_CHEESE_NAME, "На позиции [1], нет проверяемого элемента."

    #тест метода get_price(), который считает цену бургера
    def test_get_price_fill_burger_expected_price_is_valid(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        burger.add_ingredient(cheese)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(sauce)
        expected_price = bun.get_price() * 2 + cheese.get_price() + cutlet.get_price() + sauce.get_price()
        assert burger.get_price() == expected_price, "Результат не соответствует ожидаемому."

     #тест метода get_receipt(), который выводит состав бургера и его цену
    def test_get_receipt_fill_burger_expected_result_is_valid(self, setup_burger):
        burger, bun, cheese, cutlet, sauce = setup_burger
        burger.add_ingredient(cheese)
        burger.add_ingredient(cutlet)
        burger.add_ingredient(sauce)
        assert burger.get_receipt() == EXPECTED_RECEIPT, "Результат не соответствует ожидаемому."
