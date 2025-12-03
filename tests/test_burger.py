import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
import constants


class TestBurger:
    """
    Тесты для класса Burger с использованием данных из Stellar Burgers.
    Класс Burger отвечает за сборку бургера, расчет стоимости и формирование чека.
    """

    def test_burger_initialization_bun_is_none(self):
        """
        Тест инициализации бургера - проверка что булка изначально None.
        Проверяет, что при создании нового бургера атрибут bun установлен в None.
        Это важно для корректной работы set_buns().
        """
        burger = Burger()
        # Проверяем что булка изначально None
        assert burger.bun is None


    def test_burger_initialization_ingredients_empty_list(self):
        """
        Тест инициализации бургера - проверка что список ингредиентов пуст.
        Проверяет, что при создании нового бургера список ingredients является пустым списком.
        Это гарантирует что мы начинаем сборку бургера "с чистого листа".
        """
        burger = Burger()
        # Проверяем что список ингредиентов изначально пуст
        assert burger.ingredients == []
        # Также проверяем что это именно список и он пустой
        assert isinstance(burger.ingredients, list)
        assert len(burger.ingredients) == 0


    def test_burger_initialization_state(self):
        """
        Комплексный тест начального состояния бургера после инициализации.
        Проверяет что все атрибуты класса Burger находятся в корректном начальном состоянии.
        """
        burger = Burger()
        
        # Проверяем что булка не установлена
        assert burger.bun is None, "Булка должна быть None при инициализации"
        
        # Проверяем что список ингредиентов пуст
        assert burger.ingredients == [], "Список ингредиентов должен быть пустым при инициализации"
        
        # Проверяем тип списка ингредиентов
        assert isinstance(burger.ingredients, list), "Ingredients должен быть списком"


    def test_set_buns(self, new_bun):
        """
        Тест установки булки в бургер.
        Проверяет, что булка корректно сохраняется в атрибуте бургера.
        """
        burger = Burger()
        burger.set_buns(new_bun)
        assert burger.bun == new_bun


    def test_add_ingredient(self, new_ingredient):
        """
        Тест добавления ингредиента в бургер.
        Проверяет, что ингредиент добавляется в список ингредиентов бургера.
        """
        burger = Burger()
        burger.add_ingredient(new_ingredient)
        assert new_ingredient in burger.ingredients


    def test_remove_ingredient(self, new_ingredient):
        """
        Тест удаления ингредиента из бургера.
        Проверяет, что ингредиент корректно удаляется из списка по индексу.
        """
        burger = Burger()
        burger.add_ingredient(new_ingredient)
        ingredient_index = burger.ingredients.index(new_ingredient)
        burger.remove_ingredient(ingredient_index)
        assert new_ingredient not in burger.ingredients


    def test_move_ingredient(self, new_burger, new_ingredient):
        """
        Тест перемещения ингредиента в списке.
        Проверяет, что ингредиент корректно перемещается на новую позицию.
        """
        new_burger.add_ingredient(new_ingredient)
        ingredient_index = new_burger.ingredients.index(new_ingredient)
        new_index = ingredient_index - 1
        new_burger.move_ingredient(ingredient_index, new_index)
        assert new_burger.ingredients.index(new_ingredient) == new_index


    def test_get_price(self):
        """
        Тест расчета стоимости бургера.
        Проверяет правильность формулы: цена_булки * 2 + сумма_цен_ингредиентов.
        Использует моки для изоляции теста от реальных объектов.
        """
        bun_price = 1000
        ingredient_price = 500
        
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        ingredient_mock.get_price.return_value = ingredient_price
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == bun_price * 2 + ingredient_price


    @pytest.mark.parametrize("bun_index, sauce_index, filling_index", [
        (0, 0, 0),  # Краторная булка + Spicy-X + Мясо моллюсков
        (1, 1, 1),  # Флюоресцентная булка + Space Sauce + Говяжий метеорит
        (0, 2, 2),  # Краторная булка + Традиционный + Биокотлета
        (1, 3, 3),  # Флюоресцентная булка + Антарианский + Филе тетраодонтимформа
    ])
    def test_get_price_real_combinations(self, bun_index, sauce_index, filling_index):
        """
        Параметризованный тест расчета стоимости с реальными комбинациями из Stellar Burgers.
        Проверяет правильность расчета на реальных данных меню.
        """
        # Создаем моки с реальными данными
        bun_mock = Mock()
        bun_mock.get_price.return_value = constants.bun_prices[bun_index]
        
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = constants.sauces[sauce_index][1]
        
        filling_mock = Mock()
        filling_mock.get_price.return_value = constants.fillings[filling_index][1]
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        
        # Рассчитываем ожидаемую стоимость
        expected_price = (constants.bun_prices[bun_index] * 2 + 
                         constants.sauces[sauce_index][1] + 
                         constants.fillings[filling_index][1])
        
        assert burger.get_price() == expected_price


    def test_get_receipt_right_bun_in_result(self, new_burger):
        """
        Тест что булка присутствует в чеке в правильном формате ДВАЖДЫ.
        """
        receipt = new_burger.get_receipt()
        bun_line = f'(==== {new_burger.bun.get_name()} ====)'
        # Проверяем что строка с булкой есть ДВАЖДЫ (в начале и в конце)
        assert receipt.count(bun_line) == 2

    @pytest.mark.parametrize("index", [0, 1])
    def test_get_receipt_right_ingredients_in_result(self, new_burger, index):
        """
        Параметризованный тест формирования чека - проверка отображения ингредиентов.
        Проверяет, что названия всех ингредиентов присутствуют в чеке в правильном формате.
        """
        receipt = new_burger.get_receipt()
       # Проверяем ингредиент в правильном формате: = {type} {name} =
        ingredient = new_burger.ingredients[index]
        ingredient_line = f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} ='
        assert ingredient_line in receipt


    def test_get_receipt_right_price_in_result(self, new_burger):
        """
        Тест формирования чека - проверка отображения общей стоимости.
        Проверяет, что рассчитанная стоимость присутствует в чеке в правильном формате.
        """
        receipt = new_burger.get_receipt()
        burger_price = new_burger.get_price()
        # Проверяем цену в правильном формате: Price: {price}
        price_line = f'Price: {burger_price}'
        assert price_line in receipt

    def test_move_ingredient_to_same_position(self):
        """
        Тест перемещения ингредиента на ту же позицию.
        Проверяет, что порядок не меняется при перемещении на текущую позицию.
        """
        burger = Burger()
        
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        original_order = burger.ingredients.copy()
        burger.move_ingredient(1, 1)
        assert burger.ingredients == original_order
        

    def test_remove_ingredient_from_empty_burger(self):
        """
        Тест удаления ингредиента из пустого бургера.
        Проверяет что при удалении из пустого списка возникает IndexError.
        """
        burger = Burger()
        
        # Проверяем что изначально пусто
        assert burger.ingredients == []
        
        # Ожидаем IndexError при попытке удалить из пустого списка
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
        
        # Убеждаемся что список остался пустым
        assert burger.ingredients == []
