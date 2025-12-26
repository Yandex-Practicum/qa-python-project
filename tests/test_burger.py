import random
import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    mock_available_buns = Mock()
    mock_available_buns.return_value = [Bun("black bun", 100),
                                        Bun("white bun", 200),
                                        Bun("red bun", 300)]

    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                                               Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                               Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

    #Тест проверяет, что в чеке правильное название булочки и типы ингредиентов без обращения к реальной булочке
    def test_get_receipt_correct_bun_and_ingredients(self):
        bun_name = 'Краторная булка N-200i'
        bun = Bun(name=bun_name, price=1255)
        first_ingridient = random.choice(TestBurger.mock_available_ingredients())
        second_ingridient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingridient)
        burger.add_ingredient(second_ingridient)
        receipt = burger.get_receipt()
        assert (
                   '(==== Краторная булка N-200i ====)') in receipt and first_ingridient.get_type().lower() in receipt and second_ingridient.get_type().lower() in receipt

    #тест проверяет, что имя булочки присутствует в чеке, если нет, то выводит сообщение, какая не найдена в чеке
    @pytest.mark.parametrize("bun", [Bun("black bun", 100),
                                     Bun("white bun", 200),
                                     Bun("red bun", 300)])
    def test_set_bun_in_receipt(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert bun.name in receipt, f"Булка {bun.name} не отображена в чеке"

    #Тест проверяет, что ингредиенты поменялись местами в списке и что булочка осталась на месте
    def test_move_ingredient(self):
        bun_name = 'Вкусная булка'
        bun = Bun(name=bun_name, price=264)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, first_ingredient]
        assert burger.bun == bun

    #Проверяем, что первый ингредиент был удален из чека
    def test_remove_ingredient(self):
        bun_name = 'Сюрприз'
        bun = Bun(name=bun_name, price=404)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.remove_ingredient(0)
        new_receipt = burger.get_receipt()
        assert first_ingredient.get_name() not in new_receipt

    #Тест проверяет корректность вычисления цены бургера на основе булки и ингредиентов
    def test_get_price(self):
        bun = random.choice(TestBurger.mock_available_buns())
        ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        # Рассчитываем начальную цену бургера: цена булки удваивается, так как булок две (верхняя и нижняя часть)
        burger_price = 2 * bun.get_price()
        # Проверяем начальную цену бургера (без ингредиентов)
        assert burger.get_price() == burger_price
        # Добавляем ингредиент и обновляем ожидаемую цену
        burger.add_ingredient(ingredient)
        burger_price += ingredient.get_price()
        # Получаем итоговую цену бургера
        receipt_price = burger.get_price()
        assert receipt_price == burger_price
