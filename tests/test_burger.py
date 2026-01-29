import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    #Тест добавление ингредиента
    def test_add_ingredient(self):
        #Создаем объект Burger
        burger = Burger()
        #Создаем моки для ингредиентов разных типов
        sauce_mock = Mock()
        filling_mock = Mock()
        #Добавляем ингредиенты разных типов в бургер
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        #Проверяем, что ингредиенты были добавлены
        assert sauce_mock in burger.ingredients
        assert filling_mock in burger.ingredients

    #Тест удаление ингредиента
    def test_remove_ingredient(self):
        #Создаем объект Burger
        burger = Burger()
        #Создаем моки для ингредиентов указав их тип
        first_ingredient_mock = Mock()
        first_ingredient_mock.get_type.return_value = 'SAUCE'
        second_ingredient_mock = Mock()
        second_ingredient_mock.get_type.return_value = 'FILLING'
        #Добавляем ингредиенты в бургер
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        #Удаляем первый ингредиент
        burger.remove_ingredient(0)
        #Проверяем, что первый ингредиент был удален, и второй ингредиент занял его место
        assert (burger.ingredients[0].get_type()) == 'FILLING'

    #Тест смена положения ингредиента
    def test_move_ingredient(self):
        #Создаем объект Burger
        burger = Burger()
        #Создаем моки для ингредиентов
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        #Добавляем ингредиенты в бургер
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        #Перемещаем первый ингредиент на новую позицию
        burger.move_ingredient(0, 1)
        #Проверяем, что ингредиенты были перемещены и поменялись местами
        assert burger.ingredients == [second_ingredient_mock, first_ingredient_mock]

    #Тест получение цены бургера
    def test_get_price(self):
        #Создаем объект Burger
        burger = Burger()
        #Создаем мок для булочки
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100.1
        #Создаем моки для ингредиентов и устанавливаем цену
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        first_ingredient_mock.get_price.return_value = 200.2
        second_ingredient_mock.get_price.return_value = 300.3
        #Устанавливаем булочку и добавляем ингредиенты в бургер
        burger.set_buns(bun_mock)
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        #Проверяем правильность расчета цены(не забыть,что цена булки удваивается)
        assert burger.get_price() == 700.7


    #при расчете цены не забыть, что цену булки надо удвоить
    @pytest.mark.parametrize("ingredient_data, expected_result", [
        ([("sauce", "hot sauce", 200.2), ("filling", "cutlet", 300.3)],
         "(==== Wheat Bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== Wheat Bun ====)\n\nPrice: 700.7"),
    ])
    #
    def test_get_receipt(self, ingredient_data, expected_result):
        #Создаем объект Burger
        burger = Burger()
        #Устанавливаем булочку, задаем ей наименование и цену
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Wheat Bun"
        bun_mock.get_price.return_value = 100.1
        burger.set_buns(bun_mock)

        #Добавляем ингредиенты в бургер на основе ingredient_data
        for ingredient_type, ingredient_name, ingredient_price in ingredient_data:
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = ingredient_name
            ingredient_mock.get_price.return_value = ingredient_price
            #Добавляем созданный мок ингредиента в бургер
            burger.add_ingredient(ingredient_mock)

        #Проверяем правильность формирования чека
        assert burger.get_receipt() == expected_result