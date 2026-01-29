import allure
import pytest
from unittest.mock import Mock, patch

from burger import Burger
from data import BurgerGetPrice as p, BurgerInfo as b

class TestBurger:
    """
    Тесты методов класса Burger.
    """

    #
    # Тесты метода set_buns() - добавление булок
    #
    @allure.title('set_buns() - добавление булок: 1 булка')
    @allure.description('Проверяем, что булка добавлена')
    def test_set_buns(self, mock_bun):
        """
        Params: mock_bun - фикстура, которая возвращает мок булки
        """
        burger = Burger()
        burger.set_buns(mock_bun)

        # проверяем, что булка добавлена
        assert (burger.bun is not None and
                burger.bun.name == b.BUN_NAME and
                burger.bun.price == b.BUN_PRICE)


    @allure.title('set_buns() - добавление булок: 2 булки')
    @allure.description('Проверяем, что добавлена вторая булка')
    def test_set_buns_2_buns(self, mock_bun, mock_bun2):
        """
        Params: mock_bun, mock_bun2 - фикстуры, которые возвращают мок булок
        """
        burger = Burger()
        # создаем и добавляем булку 1
        burger.set_buns(mock_bun)
        # создаем и добавляем булку 2
        burger.set_buns(mock_bun2)

        # проверяем, что добавлена булка 2
        assert (burger.bun is not None and
                burger.bun.name == b.BUN2_NAME and
                burger.bun.price == b.BUN2_PRICE)


    #
    # Тесты метода add_ingredient() - добавление ингредиента
    #
    @allure.title('add_ingredient() - добавление ингредиентов: 1 ингредиент')
    @allure.description('Проверяем, что в бургер добавлен 1 ингредиент - соус')
    def test_add_ingredient_one_ingredient(self, mock_sauce):
        """
        Params: mock_sauce - фикстура, которая возвращает мок ингредиента (соуса)
        """
        burger = Burger()
        # создаем и добавляем 1 ингредиент - соус
        burger.add_ingredient(mock_sauce)

        # проверяем, что в списке 1 ингредиент
        assert len(burger.ingredients) == 1


    @allure.title('add_ingredient() - добавление ингредиентов: 2 соуса')
    @allure.description('Проверяем, что в бургер можно добавить 2 соуса')
    def test_add_ingredient_two_sauces(self, mock_sauce):
        burger = Burger()
        # Добавляем 1-й ингредиент
        burger.add_ingredient(mock_sauce)
        # Добавляем 2-й ингредиент
        burger.add_ingredient(mock_sauce)

        # проверяем, что в списке 2 соуса
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == b.SAUCE_TYPE
        assert burger.ingredients[1].type == b.SAUCE_TYPE


    @allure.title('add_ingredient() - добавление ингредиентов: 2 начинки')
    @allure.description('Проверяем, что в бургер можно добавить 2 начинки')
    def test_add_ingredient_two_fillings(self, mock_filling):
        burger = Burger()
        # Добавляем 1-й ингредиент
        burger.add_ingredient(mock_filling)
        # Добавляем 2-й ингредиент
        burger.add_ingredient(mock_filling)

        # проверяем, что в списке 2 соуса
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == b.FILLING_TYPE
        assert burger.ingredients[1].type == b.FILLING_TYPE


    @allure.title('add_ingredient() - добавление ингредиентов: соус и начинка')
    @allure.description('Проверяем, что в бургер можно добавить соус и начинку')
    def test_add_ingredient_sauce_and_filling(self, mock_sauce, mock_filling):
        burger = Burger()
        # Добавляем 1-й ингредиент
        burger.add_ingredient(mock_sauce)
        # Добавляем 2-й ингредиент
        burger.add_ingredient(mock_filling)

        # проверяем, что в списке 2 соуса
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == b.SAUCE_TYPE and burger.ingredients[1].type == b.FILLING_TYPE


    @allure.title('add_ingredient() - добавление 6 ингредиентов: 3 соуса и 3 начинки')
    @allure.description('Проверяем, что все ингредиенты добавлены')
    def test_add_ingredient_6_ingredients(self, mock_sauce, mock_filling, get_burger_with_6_ingredients):
        burger = get_burger_with_6_ingredients
        # проверяем, что в списке 6 ингредиентов

        assert len(burger.ingredients) == 6


    #
    # Тесты метода remove_ingredient() - удаление ингредиента
    #
    @allure.title('remove_ingredient() - удаление ингредиента: 1 ингредиент в списке')
    @allure.description('Проверяем, что после удаления ингредиента список пустой')
    def test_remove_ingredient_one_ingredient_in_list(self, mock_sauce):
        # создаем бургер и добавляем 1 ингредиент - соус
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        # удаляем ингредиент
        burger.remove_ingredient(0)

        # проверяем, что список пустой
        assert len(burger.ingredients) == 0


    @allure.title('remove_ingredient() - удаление ингредиента: 2 ингредиента в списке, удаляем 1-й')
    @allure.description('Проверяем, что остался 2-й ингредиент')
    #@pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredient_two_ingredients_remove_first(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем 2 ингредиента - соус и начинка
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # удаляем ингредиент с индексом index (0 или 1)
        burger.remove_ingredient(0)

        # проверяем, что в списке остался один ингредиент - не тот, который был удален
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == b.FILLING_TYPE


    @allure.title('remove_ingredient() - удаление ингредиента: 2 ингредиента в списке, удаляем 2-й')
    @allure.description('Проверяем, что остался 1-й ингредиент')
    def test_remove_ingredient_two_ingredients_remove_last(self, mock_sauce, mock_filling):
        burger = Burger()
        # добавляем 2 ингредиента - соус и начинка
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # удаляем ингредиент с индексом index (0 или 1)
        burger.remove_ingredient(1)

        # проверяем, что в списке остался один ингредиент - не тот, который был удален
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == b.SAUCE_TYPE


    @allure.title('remove_ingredient() - удаление ингредиента: пустой список')
    @allure.description('Проверяем, что список остался пустым')
    def test_remove_ingredient_empty_list_no_changes(self):
        burger = Burger()
        burger.remove_ingredient(0)

        # проверяем что программа не сломалась и список остался пустым
        assert len(burger.ingredients) == 0


    @allure.title('remove_ingredient() - удаление ингредиента: неправильный индекс')
    @allure.description('Проверяем, что программа не сломалась и в списке осталось 2 ингредиента')
    def test_remove_ingredient_invalid_index_no_changes(self, mock_sauce, mock_filling):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # пытаемся удалить ингредиент с индексом 2
        burger.remove_ingredient(2)

        # проверяем что программа не сломалась и в списке осталось 2 ингредиента
        assert len(burger.ingredients) == 2


    #
    # Тесты метода move_ingredient() - перемещение ингредиента
    #
    @allure.title('move_ingredient() - перемещение ингредиента: 2 ингредиента в списке, поменять местами')
    @allure.description('Проверяем, что')
    @pytest.mark.parametrize('index_before, index_after', [[0, 1], [1, 0]])
    def test_move_ingredient_move_1_and_2(self, mock_sauce, mock_filling, index_before, index_after):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # перемещаем ингредиент с индексом index_before на место index_after
        burger.move_ingredient(index_before, index_after)

        # проверяем что в списке осталось 2 элемента и они поменялись местами
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == b.FILLING_TYPE
        assert burger.ingredients[1].type == b.SAUCE_TYPE


    @allure.title('move_ingredient() - перемещение ингредиента: 2 ингредиента, тот же индекс')
    @allure.description('Проверяем, что ингредиенты остались на тех же местах')
    @pytest.mark.parametrize('index', [0, 1])
    def test_move_ingredient_the_same_index(self, mock_sauce, mock_filling, index):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # перемещаем ингредиент с индексом index на то же место
        burger.move_ingredient(index, index)

        # проверяем что в списке остались 2 элемента на тех же местах
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == b.SAUCE_TYPE
        assert burger.ingredients[1].type == b.FILLING_TYPE


    @allure.title('move_ingredient() -  перемещение ингредиента: пустой список')
    @allure.description('Проверяем, что программа не сломалась и список остался пустым')
    def test_move_ingredient_empty_list(self):
        # создаем бургер с пустым списком ингредиентов
        burger = Burger()
        burger.move_ingredient(0, 1)

        # проверяем что программа не сломалась и список остался пустым
        assert len(burger.ingredients) == 0


    @allure.title('move_ingredient() -  перемещение ингредиента: неправильный индекс')
    @allure.description('Проверяем, что программа не сломалась и в списке остались 2 ингредиента')
    @pytest.mark.parametrize('index_before, index_after', [[0, 2], [2, 1], [3, 5]])
    def test_move_ingredient_invalid_index(self, mock_sauce, mock_filling, index_before, index_after):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # перемещаем ингредиент с индексом index_before на место index_after
        burger.move_ingredient(index_before, index_after)

        # проверяем что программа не сломалась и в списке остались 2 ингредиента
        assert len(burger.ingredients) == 2


    #
    # Тесты метода get_price() - получение стоимости бургера
    #
    @allure.title('get_price() - получение стоимости бургера: булки и 2 ингредиента')
    @allure.description('Проверяем, что метод возвращает правильную стоимость')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 1:    [True, True, True, 400]  # булки и 2 ингредиента
    def test_get_price_with_buns_sauce_filling(self,
                       mock_ingredient_class,
                       mock_bun_class):
        # создаем моки для булок и ингредиентов
        mock_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()
        # назначаем мокам возвращаемое значение для метода get_price()
        mock_bun.get_price.return_value = b.BUN_PRICE
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        mock_filling.get_price.return_value = b.FILLING_PRICE
        # создаем бургер и добавляем в него булки и ингредиенты
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == p.BUNS_SAUCE_FILLING_PRICE      # = 400


    @allure.title('get_price() - получение стоимости бургера: только булки')
    @allure.description('Проверяем, что программа не ломается и метод возвращает правильную стоимость')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 2:    [True, False, False, 100],  # только булки
    def test_get_price_with_buns(self,
                       mock_ingredient_class,
                       mock_bun_class):
        # создаем мок для булок
        mock_bun = Mock()
        # назначаем моку возвращаемое значение для метода get_price()
        mock_bun.get_price.return_value = b.BUN_PRICE
        # создаем бургер и добавляем в него булки
        burger = Burger()
        burger.set_buns(mock_bun)

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == p.BUNS_PRICE      # = 100


    @allure.title('get_price() - получение стоимости бургера: булки и соус')
    @allure.description('Проверяем, что программа не ломается и метод возвращает правильную стоимость')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 3:    [True, True, False, 200],  # булки и соус
    def test_get_price_with_buns_and_sauce(self,
                       mock_ingredient_class,
                       mock_bun_class):
        # создаем моки для булок и ингредиентов
        mock_bun = Mock()
        mock_sauce = Mock()
        # назначаем мокам возвращаемое значение для метода get_price()
        mock_bun.get_price.return_value = b.BUN_PRICE
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        # создаем бургер и добавляем в него булки и ингредиенты
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == p.BUNS_SAUCE_PRICE      # = 200


    @allure.title('get_price() - получение стоимости бургера: только соус без булок')
    @allure.description('Проверяем, что программа не ломается и метод возвращает правильную стоимость')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 4:    [False, True, False, 100],  # только соус без булок
    def test_get_price_with_sauce(self,
                       mock_ingredient_class,
                       mock_bun_class):
        # создаем моки для булок и ингредиентов
        mock_sauce = Mock()
        # назначаем мокам возвращаемое значение для метода get_price()
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        # создаем бургер и добавляем в него булки и ингредиенты
        burger = Burger()
        burger.add_ingredient(mock_sauce)

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == p.SAUCE_PRICE      # = 100


    @allure.title('get_price() - получение стоимости бургера: "пустой" бургер - без булок и ингредиентов')
    @allure.description('Проверяем, что программа не ломается и метод возвращает правильную стоимость')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    # 5:    [False, False, False, 0]  # "пустой" бургер - без булок и ингредиентов
    def test_get_price_empty_burger(self,
                       mock_ingredient_class,
                       mock_bun_class):
       # создаем бургер и добавляем в него булки и ингредиенты
        burger = Burger()

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == p.EMPTY_BURGER_PRICE      # = 0


    #
    # Тесты метода get_receipt() - получение рецепта бургера
    #
    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера: булки и 2 ингредиента')
    @allure.description('Проверяем, что программа не ломается и рецепт содержит все ингредиенты')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=b.BURGER_PRICE)
    # 1:    [True, True, True],        # булки и 2 ингредиента
    def test_get_receipt_with_buns_sauce_filling(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class):
        # создаем моки для ингредиентов
        # назначаем возвращаемое значение для методов get_name(), get_type() и get_price()
        mock_bun = Mock()
        mock_bun.get_name.return_value = b.BUN_NAME
        mock_bun.get_price.return_value = b.BUN_PRICE
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = b.SAUCE_TYPE
        mock_sauce.get_name.return_value = b.SAUCE_NAME
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        mock_filling = Mock()
        mock_filling.get_type.return_value = b.FILLING_TYPE
        mock_filling.get_name.return_value = b.FILLING_NAME
        mock_filling.get_price.return_value = b.FILLING_PRICE
        # создаем бургер
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # получаем рецепт
        receipt = burger.get_receipt()

        # проверяем что рецепт получен
        assert type(receipt) is str
        assert len(receipt) > 0
        # проверяем что рецепт полный - указаны названия всех ингредиентов
        assert b.BUN_NAME.lower() in receipt.lower()
        assert b.SAUCE_NAME.lower() in receipt.lower()
        assert b.FILLING_NAME.lower() in receipt.lower()
        assert 'price' in receipt.lower()
        assert f'{b.BURGER_PRICE}' in receipt.lower()


    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера: только булки')
    @allure.description('Проверяем, что программа не ломается и рецепт содержит все ингредиенты')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=500)
    # 2:    [True, False, False],      # только булки
    def test_get_receipt_with_buns(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class):
        # создаем моки для ингредиентов
        # назначаем возвращаемое значение для методов get_name(), get_type() и get_price()
        mock_bun = Mock()
        mock_bun.get_name.return_value = b.BUN_NAME
        mock_bun.get_price.return_value = b.BUN_PRICE
        # создаем бургер
        burger = Burger()
        burger.set_buns(mock_bun)
        # получаем рецепт
        receipt = burger.get_receipt()

        # проверяем что рецепт получен
        assert type(receipt) is str
        assert len(receipt) > 0
        # проверяем что рецепт полный - указаны названия всех ингредиентов
        assert b.BUN_NAME.lower() in receipt.lower()
        assert 'price' in receipt.lower()
        assert f'{b.BURGER_PRICE}' in receipt.lower()


    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера: булки и соус')
    @allure.description('Проверяем, что программа не ломается и рецепт содержит все ингредиенты')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=500)
    # 3:    [True, True, False],       # булки и соус
    def test_get_receipt_with_buns_and_sauce(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class):
        # создаем моки для ингредиентов
        # назначаем возвращаемое значение для методов get_name(), get_type() и get_price()
        mock_bun = Mock()
        mock_bun.get_name.return_value = b.BUN_NAME
        mock_bun.get_price.return_value = b.BUN_PRICE
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = b.SAUCE_TYPE
        mock_sauce.get_name.return_value = b.SAUCE_NAME
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        # создаем бургер
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        # получаем рецепт
        receipt = burger.get_receipt()

        # проверяем что рецепт получен
        assert type(receipt) is str
        assert len(receipt) > 0
        # проверяем что рецепт полный - указаны названия всех ингредиентов
        assert b.BUN_NAME.lower() in receipt.lower()
        assert b.SAUCE_NAME.lower() in receipt.lower()
        assert 'price' in receipt.lower()
        assert f'{b.BURGER_PRICE}' in receipt.lower()


    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера: только соус без булок')
    @allure.description('Проверяем, что программа не ломается и рецепт содержит все ингредиенты')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=500)
    # 4:    [False, True, False],      # только соус без булок
    def test_get_receipt_with_sauce(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class):
        # создаем моки для ингредиентов
        # назначаем возвращаемое значение для методов get_name(), get_type() и get_price()
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = b.SAUCE_TYPE
        mock_sauce.get_name.return_value = b.SAUCE_NAME
        mock_sauce.get_price.return_value = b.SAUCE_PRICE
        # создаем бургер
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        # получаем рецепт
        receipt = burger.get_receipt()

        # проверяем что рецепт получен
        assert type(receipt) is str
        assert len(receipt) > 0
        # проверяем что рецепт полный - указаны названия всех ингредиентов
        assert b.SAUCE_NAME.lower() in receipt.lower()
        assert 'price' in receipt.lower()
        assert '500' in receipt.lower()
        assert 'price' in receipt.lower()
        assert f'{b.BURGER_PRICE}' in receipt.lower()


    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера^ "пустой" бургер - без булок и ингредиентов')
    @allure.description('Проверяем, что программа не ломается и рецепт содержит все ингредиенты')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=500)
    # 5:    [False, False, False]     # "пустой" бургер - без булок и ингредиентов
    def test_get_receipt_empty_burger(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class):
        # создаем "пустой" бургер
        burger = Burger()
        # получаем рецепт
        receipt = burger.get_receipt()

        # проверяем что рецепт получен
        assert type(receipt) is str
        assert len(receipt) > 0
        assert 'price' in receipt.lower()
        assert f'{b.BURGER_PRICE}' in receipt.lower()

