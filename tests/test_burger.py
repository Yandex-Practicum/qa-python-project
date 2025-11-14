import allure

from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:

    @allure.title('Проверка установки булок')
    def test_set_buns(self):

        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = 'Большая космо булка'
        burger.set_buns(mock_bun.name)

        assert burger.bun == 'Большая космо булка'


    @allure.title('Проверка добавления ингредиента')
    def test_add_ingredient(self):

        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = 'Соус'
        burger.add_ingredient(mock_ingredient.name)

        assert burger.ingredients == ['Соус']


    @allure.title('Проверка удаления ингредиента')
    def test_remove_ingredient(self):

        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name_1 = 'Его добавили первым'
        mock_ingredient.name_2 = 'Его добавили вторым'

        burger.add_ingredient(mock_ingredient.name_1)
        burger.add_ingredient(mock_ingredient.name_2)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1 and burger.ingredients == ['Его добавили первым']


    @allure.title('Проверка перемещения ингредиента')
    def test_move_ingredient(self):

        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name_1 = 'Его добавили первым'
        mock_ingredient.name_2 = 'Его добавили вторым'

        burger.add_ingredient(mock_ingredient.name_1)
        burger.add_ingredient(mock_ingredient.name_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == ['Его добавили вторым', 'Его добавили первым']


    @allure.title('Проверка получения стоимости')
    def test_get_price(self):

        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 2.0

        burger.add_ingredient(mock_ingredient)
        result_price = 4.0

        assert result_price == burger.get_price()


    @allure.title('Проверка печати чека')
    def test_get_receipt(self):

        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Большая космо булка'
        mock_bun.get_price.return_value = 1.0

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Сырный'
        mock_ingredient.get_type.return_value = 'Соус'
        mock_ingredient.get_price.return_value = 2.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        result = (
            "(==== Большая космо булка ====)\n"
            "= соус Сырный =\n"
            "(==== Большая космо булка ====)\n"
            "\nPrice: 4.0"
        )
        assert result == burger.get_receipt()
